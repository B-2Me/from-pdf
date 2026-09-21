# Serverless PDF to Markdown Pipeline

An automated, zero-server pipeline that converts PDF documents into pristine, Obsidian-ready Markdown using a flexible suite of OCR and AI engines.

## How to use
1. Navigate to the **Issues** tab.
2. Click **New Issue**.
3. Drag and drop your `.pdf` file into the issue description box.
4. (Optional) Add slash commands to the issue description to customize the extraction.
5. Click **Submit new issue**.

Within a few minutes, a GitHub Action bot will comment on your issue containing direct download links for the raw `.md` file and a `.zip` archive containing the Markdown and any extracted images.

---

## Advanced Configuration (Slash Commands)

You can completely customize how the pipeline processes your PDF by dropping these slash commands anywhere in your issue body.

### Engine Selection
The pipeline supports three distinct architectural paths. If no engine is specified, the system defaults to `marker`.
* **/engine=marker (Default):** Lightning-fast extraction using the PDF's native digital text layer. Zero LLM calls. Best for clean, natively digital PDFs.
* **/engine=marker-llm:** Extracts text rapidly using Marker, but routes the output through a cloud LLM to perfectly format complex tables, fix math, and clean up the structural Markdown.
* **/engine=vision:** Bypasses Marker entirely. Converts PDF pages into images and uses a multimodal Vision AI to holistically read and transcribe the page. Best for heavily corrupted PDFs, scanned documents, or complex visual math.

### Modifiers & Overrides
* **/force-ocr:** Tells Marker to ignore the PDF's digital text layer and boot up its neural network to visually read every character. **Use only for image-only scans.** *(Warning: Runs locally on GitHub Actions CPU and takes ~6 minutes per page. Do not use with `/engine=vision`.)*
* **/page-range=X-Y:** Processes only a specific chunk of the document (e.g., `/page-range=1-20`). The outputs are dynamically named (e.g., `document_vision_pages_1-20.md`) so you can process large books in safe increments without overwriting previous chunks.
* **/timeout=X:** Sets the maximum execution time in minutes before the engine gracefully stops and packages whatever pages it has finished (e.g., `/timeout=30`). **Default:** `15`.
* **/model=X:** Overrides the OpenRouter LLM used by the `vision` or `marker-llm` engines (e.g., `/model=qwen/qwen-2.5-72b-instruct:free`).

---

## Example Workflows

**1. The Fast Default (Clean Digital PDFs)**
Just drop the PDF in the issue. No commands needed. Runs standard Marker text extraction in seconds.

**2. The "Bad Scan" Fixer**
```text
/engine=marker-llm
/force-ocr
/page-range=1-5
```
*Forces Marker to visually read a scanned document, then uses an LLM to clean up the messy OCR formatting. Limited to 5 pages to avoid the 15-minute CPU timeout.*

**3. The Complex Math & Layout Reader**
```text
/engine=vision
/page-range=10-25
/timeout=30
```
*Takes pictures of pages 10 through 25 and lets the default Vision AI perfectly transcribe the LaTeX math and tables, giving it an extended 30-minute window to finish the job.*

---

## Maintenance
Processed files are stored in the `conversions/` directory and are automatically purged after 30 days to optimize repository storage.
