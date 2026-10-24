import base64
import os
import sys
import glob
import re
import time
from collections import Counter
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

model_to_use = os.environ.get("CUSTOM_MODEL") or "google/gemma-4-31b-it:free"
file_suffix = os.environ.get("FILE_SUFFIX")
footer_mode = os.environ.get("FOOTER_MODE") or "remove"
start_page_num = int(os.environ.get("START_PAGE_NUM") or 1)

def get_page_num(filename):
    m = re.search(r'page.*?(\d+)\.png$', filename)
    return int(m.group(1)) if m else 0

def clean_invisible(s):
    return re.sub(r'[\u200b\u200c\u200d\uFEFF]', '', s)

def is_horizontal_rule(line):
    s = clean_invisible(line).strip()
    return bool(re.match(r'^(?:(?:\s*-\s*){3,}|(?:\s*\*\s*){3,}|(?:\s*_\s*){3,})$', s))

def is_bare_page_number(line):
    s = clean_invisible(line).strip()
    if not s:
        return False
    if re.match(r'^<center>\s*\d+\s*</center>$', s, re.IGNORECASE):
        return True
    if re.match(r'^(?:page\s*)?-?\s*\d+\s*(?:/|of|-)?\s*\d*\s*-?$', s, re.IGNORECASE):
        return True
    if re.match(r'^(?:[ivxlcdm]+)$', s, re.IGNORECASE):
        return True
    return False

def is_page_number_or_separator(line):
    s = clean_invisible(line).strip()
    if not s:
        return True
    return is_horizontal_rule(line) or is_bare_page_number(line)

def normalize_for_comparison(line):
    s = clean_invisible(line)
    return re.sub(r'[\W\d_]+', '', s.lower())

def prune_simplified_page_breaks(text):
    p1 = r'(?m)^(?:\s*-\s*){3,}\s*\n+\s*\d+\s*\n+(?:\s*-\s*){3,}\s*$'
    text = re.sub(p1, '', text)
    p2 = r'(?m)^\s*\d+\s*\n+(?:\s*-\s*){3,}\s*\n+\s*\d+\s*$'
    text = re.sub(p2, '', text)
    p3 = r'(?m)^(?:\s*-\s*){3,}\s*\n+\s*\d+\s*$'
    text = re.sub(p3, '', text)
    p4 = r'(?m)^\s*\d+\s*\n+(?:\s*-\s*){3,}\s*$'
    text = re.sub(p4, '', text)
    return text

target_dir = sys.argv[1]
image_files = sorted(glob.glob(f"{target_dir}/vision/page-*.png"), key=get_page_num)
out_file = f"{target_dir}/document_vision_{file_suffix}.md"

print(f"-> Found {len(image_files)} pages. Processing with {model_to_use}...", flush=True)

raw_pages = []
prompt = """Transcribe this document page into clean Markdown. 

CRITICAL MATH RULES:
1. ALWAYS format mathematical equations, symbols, and standalone variables using proper LaTeX enclosed in `$` for inline math and `$$` for block math.
2. NEVER use Unicode math characters (e.g., avoid 𝓕, ℒ, Σ). Use their LaTeX equivalents instead (e.g., $\mathcal{F}$, $\mathcal{L}$, $\Sigma$).
3. DO NOT escape underscores. Write `_` instead of `\_` both inside and outside of math blocks.

EXCLUSION RULES:
- DO NOT include repetitive running headers or running footers from the margins.
- DO NOT include page numbers.

FORMATTING RULES:
- Reconstruct schedules and tables using standard |---| Markdown tables with <br> for inner line breaks. 
- Do NOT use HTML tags (no <ul>, <li>, <p>). 
- Ensure main headers, body text, equations, and footnotes are fully captured."""

for img_path in image_files:
    print(f"   Transcribing {os.path.basename(img_path)}...", flush=True)
    with open(img_path, "rb") as f:
        b64_image = base64.b64encode(f.read()).decode("utf-8")

    attempt = 1
    page_content = ""
    while attempt <= 3:
        try:
            response = client.chat.completions.create(
                model=model_to_use,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_image}"}}
                        ]
                    }
                ]
            )
            content = response.choices[0].message.content
            if content is None:
                raise ValueError("API returned an empty response (NoneType)")
            page_content = content
            break
        except Exception as e:
            print(f"     ❌ Attempt {attempt} failed: {e}", flush=True)
            time.sleep(5 * attempt)
            attempt += 1

    raw_pages.append(page_content)
    time.sleep(2)

cleaned_pages = []

if footer_mode == "keep":
    cleaned_pages = raw_pages
else:
    margin_signatures = Counter()
    for content in raw_pages:
        lines = [ln.strip() for ln in content.splitlines() if ln.strip()]
        top_candidates = lines[:3]
        bottom_candidates = lines[-3:] if len(lines) > 3 else []
        
        seen_in_page = set()
        for candidate in top_candidates + bottom_candidates:
            norm = normalize_for_comparison(candidate)
            if len(norm) >= 12:
                seen_in_page.add(norm)
        margin_signatures.update(seen_in_page)

    threshold = max(2, int(len(raw_pages) * 0.35))
    recurrent_margin_patterns = {sig for sig, count in margin_signatures.items() if count >= threshold}

    for page_idx, content in enumerate(raw_pages):
        normalized_content = prune_simplified_page_breaks(content)
        lines = normalized_content.splitlines()
        non_empty_indices = [i for i, line in enumerate(lines) if line.strip()]
        
        if not non_empty_indices:
            continue
            
        header_bound_idx = non_empty_indices[min(2, len(non_empty_indices) - 1)]
        footer_bound_idx = non_empty_indices[max(0, len(non_empty_indices) - 3)]
        
        filtered_lines = []
        for idx, line in enumerate(lines):
            if is_page_number_or_separator(line):
                continue
                
            if idx <= header_bound_idx or idx >= footer_bound_idx:
                norm = normalize_for_comparison(line)
                if norm in recurrent_margin_patterns:
                    continue
                    
            filtered_lines.append(line)

        page_body = "\n".join(filtered_lines).strip()
        
        if footer_mode == "simplified":
            current_num = start_page_num + page_idx
            page_body = f"{page_body}\n\n---\n{current_num}"
            
        cleaned_pages.append(page_body)

with open(out_file, "w", encoding="utf-8") as f:
    full_doc = "\n\n".join(p.strip() for p in cleaned_pages if p.strip())
    full_doc = re.sub(r'\n\n\n+', '\n\n', full_doc)
    f.write(full_doc)

print(f"✅ Transcription complete (footer mode: {footer_mode}). Written to {out_file}", flush=True)
