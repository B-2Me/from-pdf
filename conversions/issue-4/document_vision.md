Check for updates

Advanced Materials

ADVANCED MATERIALS

www.advmat.de

RESEARCH ARTICLE OPEN ACCESS

# Sub-Nanometer Curvature Unlocks Quantum Orbital Flexoelectricity in Graphene

Sathvik Ajay Iyengar^1,2 | James G. McHugh^3 | Jonathan P. Salvage^4 | Robert Vajtai^1,2 | Venkataramana Gadhamshetty^5 | Alan B. Dalton^6 | Manoj Tripathi^5,6 | Pulickel M. Ajayan^1,2 | Vincent Meunier^7

^1 Department of Materials Science and NanoEngineering, Rice University, Houston, Texas, USA | ^2 Rice Advanced Materials Institute, Rice University, Houston, Texas, USA | ^3 National Graphene Institute, University of Manchester, Manchester, UK | ^4 School of Pharmacy and Biomolecular Science, University of Brighton, Brighton, UK | ^5 2D-Materials for Biofilm Engineering, Science, and Technology Department of Civil and Environmental Engineering, South Dakota School of Mines and Technology, Rapid City, South Dakota, USA | ^6 Department of Physics and Astronomy, School of Mathematical and Physical Sciences, University of Sussex, Brighton, UK | ^7 Department of Engineering Science and Mechanics, Pennsylvania State University, Pennsylvania, USA

**Correspondence:** Alan B. Dalton (A.B.Dalton@sussex.ac.uk) | Manoj Tripathi (M.Tripathi@sussex.ac.uk) | Pulickel M. Ajayan (ajayan@rice.edu) | Vincent Meunier (vincent.meunier@psu.edu)

**Received:** 16 September 2025 | **Revised:** 17 June 2026 | **Accepted:** 6 July 2026

**Keywords:** DFT calculations | flexoelectricity | graphene | probe microscopy | quantum

**ABSTRACT**

Flexoelectricity, defined as polarization induced by strain gradients, is especially pronounced in two-dimensional (2D) materials due to their mechanical flexibility and sensitivity to deformation. In nanostructures with nanometer-scale curvature, bending can perturb out-of-plane π orbitals and generate quantum-mechanical polarization and electrostatic modulation beyond classical lattice distortion alone. Here, we combine scanning probe measurements and first-principles calculations to provide experimental and theoretical evidence for large intrinsic quantum orbital flexoelectricity in graphene nanowrinkles (GNWrs) with estimated polarization densities of P_th ~ 4 C m^-2 and P_exp ~ 1 C m^-2, exceeding those of mesoscale systems by 5 to 7 orders of magnitude. These GNWrs exhibit high apex curvature, undergo atomic-level buckling, and produce localized strain fields, as supported by atomic force microscopy analysis and Raman spectroscopy. Kelvin probe force microscopy reveals curvature-dependent work-function shifts, while conductive atomic force microscopy detects reproducible GNWr-associated currents with a threshold voltage (Φ_th ~ 1 V) comparable to the band offset predicted by ab initio calculations (~ 1.2 V). These results support an interpretation in which curvature-induced flexoelectric dipoles reshape the local electronic potential. GNWrs therefore provide a structurally simple carbon-based platform for probing quantum-mechanical flexoelectricity.

## 1 | Introduction

Flexoelectricity, the coupling between strain gradients and polarization, can occur in all materials, including those with centrosymmetry and has long been recognized as a universal electromechanical phenomenon [1, 2]. In low-dimensional nanomaterials, where extreme compliance allows for localized curvature and large strain gradients, the magnitude and consequences of flexoelectricity are predicted to be particularly pronounced [3, 4].

Classical flexoelectricity occurs when charges are separated across a deformed membrane, leading to a net polarization. It can also arise from the asymmetric redistribution of dipoles upon bending. In contrast, quantum flexoelectricity results from changes in electronic orbital overlap and is thus predicted even in structures without pre-existing dipoles or charge separation. Kalinin and Meunier [5] first theorized that quantum polarization could be induced in otherwise nonpolar van der Waals (vdW) atomically-thin 2D crystals such as graphene. Since then,

---

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

© 2026 The Author(s). Advanced Materials published by Wiley-VCH GmbH

Advanced Materials, 2026; 0:e18224
https://doi.org/10.1002/adma.202518224
1 of 11

---

theoretical studies have expanded on these predictions in other xenes, 2D boron nitride, and transition metal dichalcogenides (TMDs) [6–8], yet direct experimental confirmation remains limited.

In contrast to bulk materials, where competing electromechanical phenomena obscure flexoelectricity [9] and flexo-photovoltaic effects [10], 2D systems offer a clean platform for directly investigating strain gradient-induced polarization at the nanoscale. Although recent experimental efforts have begun to probe this research space, isolating intrinsic flexoelectric behavior remains challenging. For instance, flexo-photovoltaic responses have been reported in MoS₂-based hybrid heterostructures incorporating VO₂ phase-change layers [11], where strain gradients generate polarization-driven currents. However, the involvement of thermally activated transitions and structural complexity can pose challenges for reproducibility and scalability.

Accessing flexoelectricity in 2D materials through large-area thin-film bending, such as graphene bubbles [12], does not necessarily imply a quantum manifestation of the effect. The prerequisite is that the buckling, deformation, or strain must be set by the spatial extent of the out-of-plane orbitals (such as π-orbitals in graphene), representing the thinnest possible quantum mechanical separation over which flexoelectric polarization can manifest. To that effect, most prior studies have accessed strain gradients corresponding to ~ 10⁶ m⁻¹ curvature [13, 14], several orders of magnitude below atomically sharp curvatures (~ 10⁹ m⁻¹ achieved in this work). Further, in most cases, strong mechanical inputs, such as atomic force microscopy (AFM) tip indentation, are used to drive localized deformation, limiting the ability to probe spontaneous or stable response [15–19]. Lastly, features such as crack tips have provided critical insight into nanoscale polarization confined to a few atomic layers [20–22]. Such systems present a high strain-gradient induced local curvature and, due to their strong electronic screening, ionic nature, and lack of a freestanding membrane to support flexure, these systems may obscure the intrinsic quantum mechanical origins of flexoelectricity.

Here, we explore quantum orbital flexoelectricity in self-assembled GNWrs, a spontaneously formed and electronically clean platform that provides access to large strain gradients while minimizing extrinsic effects from defects, dopants, or external forces.

## 2 | Results and Discussion

### 2.1 | A Platform for Quantum Orbital Flexoelectricity

Unlike piezoelectricity (Figure 1A (i)), which arises from strain in noncentrosymmetric crystals, flexoelectricity (Figure 1A (ii)) also occurs in centrosymmetric materials under strain gradients. In GNWrs, the quantum flexoelectric response (Figure 1A (iii)) is described by curvature-driven strain gradients at subnanometer length scales, which induce intralayer hybridization of π-orbitals in a carbon-based system. We generate these GNWrs by the mechanical mismatch between two 2D materials, graphene and MoS₂, with MoS₂ promoting wrinkle formation more effectively than silica due to its distinct elastic properties (Figure 1B). The incommensurate graphene-MoS₂ interface, resulting from their differing lattice constants (0.31 nm for MoS₂ and 0.24 nm for graphene), along with differences in Poisson's ratios, drives spontaneous buckling under compressive/slip strain. Additionally, the mismatched Young's moduli facilitates interfacial shear-sliding, further enhancing wrinkle formation. This morphology is consistent with previously reported transmission electron microscopy (TEM) and density functional theory (DFT) analysis on standing-collapsed graphene loops under extreme strain fields [23], and also confirmed experimentally by AFM measurements in this study (Figure S1).

A key factor in this morphology is the difference in in-plane elastic modulus: graphene, with a modulus (1.0 ± 0.1 TPa) [24] nearly four times higher than MoS₂ (~ 270 ± 100 GPa) [25], can form wrinkles under compressive/slip strain while maintaining favorable substrate interactions. The energy cost of bending is further offset by vdW interaction between the vertical walls of the GNWr. The lower interfacial shear force between graphene and MoS₂ compared to graphene and silica enables graphene to slide and form pronounced wrinkles, as revealed by friction force mapping (Figure S2), which shows a threefold difference in friction between Gr/MoS₂ and Gr/silica. AFM and scanning electron microscopy (SEM) measurements indicate that GNWrs on MoS₂ reach heights of 6–8 nm, with a roughness (Rq = 2.78 nm, Ra = 1.73 nm) nearly six times higher than on silica (Rq = 0.48 nm, Ra = 0.28 nm) (extracted from data in Figure 3A).

Unlike traditional wrinkle formation in CVD graphene due to thermal expansion mismatch, the MoS₂ substrate enhances wrinkle height and density in physically deposited graphene (further details in Figure S3). Molecular dynamics simulations, using DFT-parameterized Lennard-Jones potentials for the graphene-MoS₂ interfacial interactions summarized in Table S1, indicate this assembly is extremely rapid: small wrinkles spontaneously nucleate for local uniaxial strains εx > 0.02 and subsequently coalesce by sliding across the MoS₂ within 0.16 ns (Figure 1C). Furthermore, GNWrs provide a well-defined platform for evaluating quantum flexoelectricity. Their tips exhibit longitudinally uniform curvature governed by the interplay of covalent bonding, local strain, and van der Waals-stabilized lips. Similar morphologies have been observed in graphene loops at multilayer edges. Raman spectroscopic data also show little to no D-band signal (Figure S4), indicating that Raman-active defect-related contributions are unlikely to dominate the observed response.

Figure 1D directly illustrates the central role of symmetry breaking in enabling quantum flexoelectricity through the visualization of computed maximally localized Wannier [26] functions of pz orbitals at the top of the wrinkle. By contrasting a symmetric, closed curved graphene geometry with an asymmetric, substrate-supported GNWr, the calculations reveal a qualitative difference in electronic response despite comparable local curvature. In the symmetric configuration, charge redistribution remains balanced due to preserved inversion symmetry, resulting in no net polarization. In contrast, the asymmetric geometry of an open nanowrinkle breaks inversion symmetry and produces a pronounced displacement of Wannier centers, indicating curvature-induced redistribution of π-electron density. This visualization

2 of 11
Advanced Materials, 2026
15214095, 2026, Downloaded from https://advances.advancement.wiley.com/doi/10.1002/adma.202501824, Wiley Online Library on [18/09/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions/) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

---

15214095, 2025, 10. Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/adma.202501224, Wiley Online Library on [18/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

| Panel | Labels |
|---|---|
| **A (i)** | Compression<br>Non-centrosymmetric crystal<br>Piezoelectricity |
| **A (ii)** | Ions, polar molecules, etc.<br>Strain gradient<br>Centrosymmetric crystal / membrane<br>Classical flexoelectricity |
| **A (iii)** | Intra-layer orbital overlap<br>Confined π e⁻ flexion<br>0.07 e/Å³<br>0.00<br>Self-assembled shear slide<br>Quantum flexoelectricity |
| **B** | Before graphene<br>Graphene on MoS₂<br>After graphene |
| **C** | 1 ps<br>10 ps<br>100 ps<br>160 ps<br>Time<br>Standing-collapsed GNWr (most stable state) |
| **D** | 0.30<br>0.24<br>0.18<br>0.12<br>0.06<br>0.00<br>\|Ψp̂(x,y,z)\| |
| **E** | ~2–3 nm<br>120 130 140<br>Standing-collapsed GNWr<br>Height (nm)<br>Line profile (nm)<br>Folded GNWr<br>~0.5 nm |

**FIGURE 1** | A platform for quantum orbital flexoelectricity. (A) Schematic illustration comparing **(i)** piezoelectricity, **(ii)** flexoelectricity, and **(iii)** quantum orbital flexoelectricity based on crystal centrosymmetry, methods of compression/strain, mechanisms of relaxation, and curvature. The charge density in (iii) is obtained by DFT and shows the density in a 2 eV window below the Fermi energy. (B) Scanning electron microscopy (SEM) micrographs of a flat MoS₂ substrate before and after the transfer of monolayer graphene and subsequent GNWr self-assembly. (C) Molecular dynamics simulations depicting the time evolution of GNWr self-assembly at T = 100 K. Smaller wrinkles spontaneously nucleate under compressive strains ε_xx > 0.02, and rapidly combine into large, standing collapsed wrinkles within a 0.16 ns time scale. (D) Maximally localized Wannier function visualizations contrasting asymmetric (open GNWrs) and symmetric (closed nanotube, side view). (E) AFM image of a standing-collapsed GNWr (the focus of this study), and a folded GNWr (the other, less stable counterpart). All scale bars are 1 μm.

provides direct orbital-level evidence that extreme curvature alone is insufficient to generate polarization, and that asymmetry is a necessary condition for the emergence of a net flexoelectric dipole.

Figure 1E distinguishes the standing-collapsed GNWrs studied here from folded GNWrs, which are related but less stable configurations [27, 28]. Unlike folded geometries, substrate-supported GNWrs impose open, asymmetric boundary conditions. The AFM measurements therefore provide experimental constraints on the relevant wrinkle geometry and curvature regime used to interpret the electronic and electromechanical responses.

Figure 2A (i–iii) further benchmarks the geometry of GNWrs against other ripple-like carbon nanostructures across length scales while also establishing the limits of AFM-based curvature extraction. Multilayer graphene, Figure 2A (i), exhibits extended ripple networks with lateral dimensions on the order of ~200 nm, reflecting mesoscale, in-plane deformation rather than localized curvature. Carbon nanotubes in Figure 2A (ii) represent a well-defined nanoscale limit, with diameters of ~6 nm and near-ideal cylindrical symmetry that provides a reference for curvature [29]. GNWrs, Figure 2A (iii), occupy a distinct regime, with lateral dimensions of ~4–5 nm and a standing-collapsed morphology characterized by sharp apex curvature and broken symmetry; importantly, they can also exhibit in-plane twisting (Figure 2A (iii), yellow arrows), which distorts the apparent profile and must be excluded when extracting intrinsic curvature.

To quantify GNWr geometry, we analyze high-resolution AFM line profiles using an elliptical representation of the wrinkle cross-section (Equation 1), combined with a geometrical correction for tip convolution. For features with height h comparable to or smaller than the tip radius r_tip, the lateral

*Advanced Materials, 2026*

3 of 11

---

**A**

| Multilayer graphene ripples | Carbon nanotubes | Standing-collapsed graphene nanowrinkles (GNWrs) |
|---|---|---|
| (i) | (ii) | (iii) |
| | | Standing-collapsed GNWrs<br>In-plane Twisted GNWrs |

Profile plots (Height (nm) vs Position (nm)):

| (i) | (ii) | (iii) |
|---|---|---|
| Ripple width ~200 nm | CNT diameter ~6 nm | Tip deconvolved elliptical fit (4.65 nm)<br>Raw data ~17 nm |
| Y-axis: 100, 80, 60, 40, 20, 0 | Y-axis: 6, 4, 2, 0, -2 | Y-axis: 4, 2, 0, -2 |
| X-axis (Position (nm)): 0, 300, 600, 900, 1200, 1500 | X-axis: 0, 50, 100, 150, 200 | X-axis: 0, 10, 20, 30, 40, 50, 60 |

**B**

Tensile ↑

| 0.0 0.1 0.2 0.3 0.4 0.5 | 0.0 0.1 0.2 0.3 0.4 0.5 |
|---|---|
| strain (%) | strain (%) |

← Compressive &nbsp;&nbsp;&nbsp;&nbsp; Compressive →

**C**

11.2 nm<br>-11.7 nm

**D**

0.007%<br>-0.009%

FIGURE 2 | Structure and strain gradients in GNWrs. (A) Comparison of various ripple-like nanostructures in (i) multilayer graphene [~ 200 nm features, scale bar 1 µm], (ii) carbon nanotubes [~ 6 nm features, scale bar 100 nm] to (iii) GNWrs [4.65 nm features, scale bar 100 nm]. Note that in-plane twisting of GNWrs is a possible phenomenon, and can distort the apparent profile and affect curvature extraction. (B) Histogram of calculated lattice strain across a GNWr. (C) AFM topology and corresponding (D) strain map obtained from Raman spectroscopic mapping. The scale bar is 200 nm. *Note*: White pixels are regions where graphene is absent (and therefore no measurable 2D/G bands (cm⁻¹) from which to extract strain).

broadening is given by:

Δ = r_tip cos { arcsin ( (r_tip − h) / r_tip ) } (1)

where Δ is the lateral convolution error introduced by the finite probe size, r_tip is the radius of curvature of the AFM tip apex (as obtained from Figure S13, a scanning electron micrograph of the tip), and h is the true height of the nanowrinkle feature. Physically, Δ represents the horizontal offset between the true edge of the structure and the first point of tip–sample contact, arising because the tip engages the feature away from its apex. The measured width is therefore broadened as w_exp = w_true + 2Δ,

where w_true is the intrinsic width of the wrinkle. This treatment follows standard geometrical models of AFM tip convolution [30].

By fitting the measured AFM profiles to the elliptical form and incorporating this convolution correction, we estimate intrinsic widths below ~5 nm and apex radii of curvature on the order of ~1–2 nm. Because GNWr dimensions approach the instrumental resolution limit, these values should be interpreted as AFM-deconvolved geometric estimates rather than exact local atomic curvatures.

Graphene nanostructures exhibit a range of morphologies, including wrinkles, folds, and bubbles, all of which fall within

---

4 of 11 | Advanced Materials, 2026

15214095, 2025, 3. Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202501234. Wiley Online Library on [18/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are powered by the applicable Creative Commons License

---

a similar strain range. Previous work reports strain values of 0.03 ± 0.01 % for graphene bubbles and 0.04 ± 0.01 % for folded wrinkles [27, 31]. More broadly, curvature-induced strain in 2D materials typically falls within the 0.01 % range [32–35]. Despite these comparable strain values, GNWrs occupy the upper limit of this range and exhibit a unique structural character. Unlike bubbles or folds, GNWrs possess extremely high curvature yet break symmetry in a way that induces polarization. Strain field calculations based on bond-length fluctuations reveal significant buckling under flexion near the curved GNWr apex associated with c₂. To further investigate variations based on GNWr height, we performed DFT calculations for three different cases, now referred to as GNWr1 (h = 15.64 Å), GNWr2 (h = 27.54 Å), and GNWr3 (h = 39.99 Å) (see **SI methods**, Figure S5). Figure 2B presents lattice-strain values for a DFT-relaxed GNWr, mapping bond-length variations in the vicinity and away from the GNWr (GNWr1 and GNWr2 in Figure S6).

Crucially, while the absolute strain values remain within a narrow and commonly reported range, the spatial variation of strain in GNWrs is exceptionally sharp. In our system, compressive stress originates in the flat basal graphene regions due to elastic and thermal expansion mismatch with the underlying MoS₂ substrate. This interpretation is consistent with the Raman-extracted strain gradient data shown in Figure 2D (AFM image in Figure 2C), which reveal pronounced compressive strain in flat graphene prior to wrinkle formation. As graphene transitions from compressive basal regions into the curved GNWr apex, strain changes over nanometer-scale distances, producing localized gradients governed by curvature and symmetry breaking rather than by strain magnitude alone. Correspondingly, the strain associated with this transition is predominantly tensile. Still, these values likely underestimate the actual local strain due to the averaging effect of Raman mapping, which has a spot size of approximately 300 nm [36]. Accordingly, the curvature and strain-gradient values reported here should be viewed as approximate experimental constraints on the relevant nanoscale geometry, rather than exact point-by-point measurements of atomic curvature.

### 2.2 | Submicroscopic Manifestations of Subnanometer Flexoelectricity

The resulting GNWrs form a curvature-driven ripple, exhibiting a net polarization leading to the relationship:

P = f(c₁ + c₂) (2)

where P is the induced polarization, f is the material-dependent flexoelectric constant, and c₁ and c₂ are the principal curvatures on the surface. Here, the first principal curvature in the plane of the graphene sheet (along the ripple), c₁, is ~ 0, and the second principal curvature, transverse to the wrinkle axis, c₂ = 1/R, where R is the radius of curvature. Approximating the GNWr tip as roughly circular, as depicted in Figure 3A, gives:

P = f/R (3)

showing that the polarization effect is strongest in materials with a large flexoelectric constant and a small local radius of curvature. In bulk perovskites, for example, f is typically on the order of 1–10 nC m⁻¹ [37], whereas in 2D systems, values can vary widely depending on material properties and strain conditions. For graphene, DFT predicts f ~ 2 nC m⁻¹ [5]. Although direct measurements of f in graphene are challenging, our experimental response is consistent with the DFT-predicted scale. Direct extraction of an intrinsic flexoelectric coefficient, however, remains limited by uncertainty in the local curvature and strain gradient.

What distinguishes nanomaterials is not necessarily an unusually large flexoelectric constant, which can be comparable to values reported for biological membranes [38], but rather their ability to achieve nanometer-scale radii of curvature. In carbon nanostructures, a reasonable lower limit for the radius of curvature is R ~ 3.4 Å, as observed in C₆₀ fullerenes and small-diameter nanotubes such as (5,5) and (9,0) carbon nanotubes. Curvature-induced charge separation across carbon nanotube walls has been predicted by DFT [39], but these closed structures do not exhibit a net polarization because of their symmetric assembly: each local curvature-induced dipole, while potentially large [40], is canceled by an opposing antiparallel dipole. In contrast, the atomistic GNWr models considered here contain local apex radii approaching ~ 5 Å, while AFM-deconvolved experimental profiles support nanometer-scale apex curvature. Although the exact experimental apex radius cannot be uniquely determined by AFM, both experiment and theory place GNWrs in a high-curvature regime without the symmetry cancellation present in closed nanotubes or fullerenes.

It follows that the emerging polarization can lead to measurable effects on the electronic properties. The pronounced work-function shift observed by Kelvin probe force microscopy (KPFM) is consistent with a strong curvature-associated electrostatic response (Figure 3B,C).

To compare work-function variations across flat and wrinkled graphene, we segmented KPFM maps into class-specific regions and extracted contact potential difference (CPD) distributions for each class. Because CPD is an intensive local quantity, direct normalization by area would be physically misleading. However, GNWrs occupy only a small fraction of the imaged area, so raw pixel counts alone underrepresent the spatial localization of their electrostatic response. We therefore report Gaussian statistics for each CPD distribution and introduce an area-aware figure of merit (FoM) to compare extended flat regions with highly localized curved features:

FoM_i = |Δψ_i| log₁₀(1/f_i) (4)

where Δψ_i is the class-averaged CPD shift relative to a reference and f_i is the areal fraction of that class within the KPFM map. This formulation preserves the intensive nature of CPD while explicitly accounting for spatial localization. The logarithmic factor is small for extended flat regions and large for GNWrs, which occupy on the order of 10⁻⁴ of the surface. Even when intrinsic CPD shifts are comparable, the FoM highlights the strong concentration of electronic response within nanoscale curved regions, as shown in Figure 3D. The deviation of GNWr work-function values from those of unflexed graphene is challenging

---

Advanced Materials, 2026

5 of 11

15214095, 0. Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202501824, Wiley Online Library on [18/09/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

---

**A**

Graphene nanowrinkle

C1 = 0

h

C2 = 1/R

Graphene

MoS2 (2D substrate)

Silica (3D substrate)

**B**

Topography

SiO2

Phase contrast

Gr/SiO2

Gr/MoS2

Surface potential

SiO2

Gr/SiO2

Gr/MoS2

**C**

Normalized counts

- Overall work function profile
- Flat graphene on MoS2
- Flat graphene on SiO2
- SiO2
- GNWrs on MoS2

1.5, 1.0, 0.5, 0.0

4.6, 4.8, 5.0, 5.2, 5.4

Work Function (eV)

**D**

Figure of Merit |Δφf| log10(1/fr)

4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0

GNWr (5.234 eV)

Graphene -SiO2 (5.171 eV)

Graphene -MoS2 (5.259 eV)

SiO2 (4.978 eV)

Charge Potential Difference (CPD) Material Class

**FIGURE 3** | Flexoelectric effect-driven work function shifts. (A) Schematic representation showing the carbon GNWr (blue) on MoS2 (yellow/grey), on top of SiO2 substrate (red and dark blue). The schematics show the principal curvatures in the GNWr, used in the flexoelectric scale analysis. (B) Atomic force microscopy (AFM) is used for topography and phase contrast, with corresponding Kelvin probe force microscopy (KPFM) measuring surface potential across different substrate regimes. (C) Work function distribution across surfaces. (D) Area-aware figure of merit (FoM) derived for localized electrostatic response from Equation (4). The FoM combines the class-averaged contact potential difference shift with a logarithmic factor accounting for areal localization, enabling comparison between extended flat graphene and highly localized GNWrs. The enhanced FoM highlights the strong concentration of curvature-induced electrostatic response despite their small spatial footprint. All scale bars are 1 μm.

to explain by substrate effects alone. Instead, the observed shift supports the interpretation that curvature-induced polarization contributes substantially to the local surface-potential contrast.

The combined experimental and theoretical trends indicate that the electrical response is weakly dependent on GNWr height and more closely correlated with localized apex curvature. To probe this response, we performed conductive atomic force microscopy (c-AFM) on dense GNWr networks containing features of varying heights (Figure 4A). Under a fixed 2 V bias (Figure 4B), GNWrs with different heights exhibit comparable current values of ~ 67 pA (Figure 4C), supporting the interpretation that the c-AFM contrast is associated with curvature-driven electrostatic modulation rather than simple topographic height.

15214095, © Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202505224, Wiley Online Library on [18/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

6 of 11

Advanced Materials, 2026

---

**A**

Gr/SiO₂

Gr/MoS₂

**B**

6.0 nm | 712.8 pA

-6.6 nm | -149.5 pA

**C**

Nanowrinkle height (nm): 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

Current (pA): 0, 30, 60, 90, 120

Height (nm): 16, 11, 6, 1 | Position (nm): 0, 200, 400, 600, 800

Current (pA): 120, 80, 40, 0 | Position (nm): 0, 200, 400, 600, 800, 1000

**FIGURE 4** | Large-area, uniform, quantum orbital flexoelectricity. (A) Atomic force microscopy (AFM) and (B) corresponding conductive AFM characterization of the topography and current distribution of GNWr. Only the GNWrs exhibit a higher baseline current, which is independent of GNWr height (i.e., independent of height *h*), as shown in (C). All scale bars are 1 μm.

This interpretation is further supported by the absence of a calculated bandgap opening (Figure S7), the height-independent potential trends (Figure S8), the apex-localized depolarization response (Figure S9), and the comparison between curved GNWrs and noncurved topographic features (Figure S10).

**2.3 | Tuning Quantum Orbital Flexoelectricity Near Fundamental Curvature Limits**

To further investigate the flexoelectric response, we performed c-AFM measurements, now, under varying bias conditions and looping the spatial coordinates (Figure 5A). As observed previously and supported by our DFT calculations, the effect depends on the applied bias and remains uniform for a given bias, regardless of GNWr height, resulting in large-area coverage and reproducibility, as seen in Figure 5B. Dipole moments calculated for these systems were found to be 0.0261 e Å (0.125 D), 0.0223 e Å (0.107 D), and 0.0297 e Å (0.143 D), respectively (see Figure S11 for fitting details). This shows minimal variation across various sizes of GNWrs. Figure 5C analyzes four specific GNWrs, looping the same spatial resolution across different voltages, and reveals a clear asymmetry in response when probing low and negative biases. In this bias regime, a threshold voltage (Φth) of ~ 1.01 V is observed (Figure 5D), corresponding to a barrier-like potential that must be overcome, consistent with the flexoelectric dipole induced in the GNWr. The calculated polarization results in a significant local work function shift in the vicinity of the wrinkles compared to flat graphene, corroborating with DFT (Figure 5E). This work function difference leads to a band offset at the interface between wrinkled and flat graphene, forming a local electrostatic junction, with the calculated offset (~ 1.2 V) shown

---

*15214095, 2024. Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202501234. Wiley Online Library on [18/09/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are powered by the applicable Creative Commons License*

Advanced Materials, 2026 | 7 of 11

---

**A**

Looped spatial coordinates
c-AFM tip
Sample-wide varying potential bias
Graphene nanowrinkles
+ / −

**B**

6.0 nm / -6.6 nm
+2 V / 361.1 pA
-2 V / -72.7 pA

**C**

1 2 3 4
40.0 pA (scale) / -40.0 pA
2, 1.75, 1.5, 1.25, 1, 0.75, 0.5, 0.25, 0 V, -0.25, -0.5, -0.75, -1, -1.25, -1.5, -1.75, -2
GNWrs
Flat graphene
Varying bias

**D**

GNWrs
Flat graphene
Flexoelectroic current (pA): 50, 0, -50
ON / OFF
Φ_th ~ 1.02 V
Bias voltage (V): -2.4, -1.8, -1.2, -0.6, 0.0, 0.6, 1.2, 1.8, 2.4

**E**

Basal plane / Tip
eV: 0, -25, -50, -75, -100, -125, -150, -175, -200
y (Å): 80, 70, 60, 50, 40, 30, 20, 10
x (Å): 0, 10, 20, 30, 40, 50, 60

**F**

Potential (eV): 0.0, -2.5, -5.0, -7.5
1.2 V
x (Å)

**G**

ρ_E=-0.1 + ρ_E=+0.1 - 2 ρ_E=0
Charge difference (e/nm²): 0.4, 0.2, 0, -0.2, -0.4, -0.6
y (Å): 70, 60, 50, 40, 30, 20, 10
x (Å): 0, 10, 20, 30, 40, 50, 60

FIGURE 5 | Bias-dependent electrostatic response of GNWrs. (A) c-AFM measurement setup to study flexoelectric response in GNWr. (B) Spatially-resolved c-AFM data under equal-magnitude biases of opposite polarity show asymmetry in current response. (C) Bias voltage-dependent data where each 'strip' consists of a repeated area over the sample under a different potential. Numbers indicate the positions of four GNWrs. At zero bias, the GNWr-associated current contrast is weak, whereas bias application produces clear asymmetric current signatures. (D) GNWr-associated current measurements were collected specifically on GNWrs and flat graphene and averaged across a bias range. (E) Electrostatic potential map of a GNWr with potential extracted at the tip and basal plane, as shown in (F). (F) also shows the macroscopic average potential (blue), showing that the flexoelectric polarization yields a reduction of the work function at the wrinkle tip and the ensuing band alignment. (G) Asymmetry in electrostatic response obtained by computing charge density difference between opposite and equal magnitude potential fields. The calculated flexoelectric polarization is consistent with the asymmetry in charge redistribution under opposite electric fields. All scale bars are 1 μm.

in Figure 5F. Together, with the fact that there is no bandgap opening (Figure S7) these results support the influence of strain gradients on electron distribution and electrostatic properties within confined 2D volumes.

Such an asymmetric response under bias is consistent with net flexoelectric-induced polarization (Figure 5G). The estimated response is among the strongest reported for flexoelectric systems and is enabled by the large local curvature of GNWrs, approaching bond-length-scale radii in the atomistic model as shown in Figure 6A. As discussed previously in Equation 2, there is a strong inverse relationship between the radius of curvature and the flexoelectric effect. Using Φ_th ~ 1 V from Figure 5D, we can describe it as the potential of a first-order point-dipole at the probe position as follows:

Φ_th = (1 / 4πε₀) · (p / r²) cos θ (5)

where p is the dipole moment, r is the effective distance between the dipole center and the conductive probe apex (~ 2.52 ± 0.27 nm, as determined in a separate experiment; see Figure S12), and θ ~ 0, assuming that the dipole axis is aligned with the surface normal and the tip-sample separation vector during measurement. Equation (5) provides an order-of-magnitude estimate within a vacuum point-dipole approximation. Extracting the polarization density from Equations (3) and (5) for theory and experiment yield P_th ~ 4 C m⁻², P_exp ~ 1 C m⁻². Given our curvature of ~ 10⁹ m⁻¹, we move towards fundamental limits for these values, as shown in Figure 6B.

These results show that self-assembled GNWrs provide a scalable platform for studying curvature-mediated electromechanical effects in 2D materials. The transition from flat graphene to high-curvature wrinkle termini offers a geometry-controlled route for probing how strain gradients modify local electronic response, with implications for future device design [48]. Future work should integrate GNWrs into controlled device architectures compatible with scalable 2D-material processing [49] and examine coupling with other 2D materials, particularly with wide-bandgap systems [50, 51, 52], to potentially engineer flexoelectric responses in 2D hybrids [53].

---

8 of 11
Advanced Materials, 2026

15214055, 2025, 3. Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/adma.202510224. Wiley Online Library on [18/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are powered by the applicable Creative Commons License

---

**A**

Band offset [ΔE_g] (eV)

★ This work (GNWrs)

fundamental limit: length of C–C bond

| Theoretical reports: |
|---|
| TMDs |
| NTs |
| Carbon 1D/2D |
| hBN |
| Janus TMD |

10^0
10^-1
10^-2

10^-1
10^0
10^1
10^2

Radius of curvature [R] (nm)

**B**

| Experimental reports: | |
|---|---|
| intrinsic | |
| extrinsic | |

theory
SrTiO3
This work
experiment
h-YbFeO3

YAIO3
TiO2
KTaO3
DyScO3

Polarization density [P] (C.m^-2)

10^1
10^-1
10^-3
10^-5
10^-7
10^-9
10^-11

fundamental limit: length of C–C bond

10^-2
10^0
10^2
10^4
10^6
10^8
10^10
10^12

Curvature [κ] (m^-1)

FIGURE 6 | Quantum orbital flexoelectricity approaches fundamental limits of polarization densities. (A) Comparison of band offsets in different 2D material systems as a function of flexoelectric radius of curvature. *Note:* all literature reports, except for this work, are only theoretical reports [40–45]. (B) Comparison of polarization density as a function of flexoelectric curvature. *Note:* all literature reports, except for this work, are only experimental reports on bulk materials [17, 37, 46, 47]. Trend lines are linear on a log-log plot, indicating power-law scaling with curvature.

### Author Contributions

S.A.I., V.M., and M.T. conceived the project and designed the research. S.A.I., V.M., and M.T. collected, analyzed, and presented the data and co-wrote the manuscript with input from all authors. J.G.M. performed the MD simulations. V.M. performed the DFT calculations. J.P.S. collected scanning electron micrographs. M.T., V.G., A.B.D., R.V., V.M., and P.M.A. acquired funding for the project. V.M., P.M.A., A.B.D., and M.T. supervised the entire project.

### Acknowledgements

We thank the Rice Shared Equipment Authority (SEA) for its support.

### Funding

S.A.I. and P.M.A. acknowledge and thank the Quad Fellowship. A.B.D. acknowledges the Sussex Strategy Development Fund. J.G.M. is supported by the University of Manchester Dame Kathleen Ollerenshaw Fellowship. M.T. and V.G. acknowledge the National Science Foundation under awards OIA-2418752, OIA-1849206, and DGE-2510643.

### Conflicts of Interest

The authors declare no conflicts of interest.

### Data Availability Statement

The data that support the findings of this study are available from the corresponding author upon reasonable request.

### References

1. A. K. Tagantsev, V. Meunier, and P. Sharma, "Novel Electromechanical Phenomena at the Nanoscale: Phenomenological Theory and Atomistic Modeling," *MRS Bulletin* 34 (2009): 643–647, https://doi.org/10.1557/mrs2009.175.

2. S. Krichen and P. Sharma, "Flexoelectricity: A Perspective on an Unusual Electromechanical Coupling," *Journal of Applied Mechanics* 83 (2016): 030801, https://doi.org/10.1115/1.4032378.

3. T. D. Nguyen, S. Mao, Y. Yeh, P. K. Purohit, and M. C. McAlpine, "Nanoscale Flexoelectricity," *Advanced Materials* 25 (2013): 946–974, https://doi.org/10.1002/adma.201203852.

4. P. Zubko, G. Catalan, and A. K. Tagantsev, "Flexoelectric Effect in Solids," *Annual Review of Materials Research* 43 (2013): 387–421, https://doi.org/10.1146/annurev-matsci-071312-121634.

5. S. V. Kalinin and V. Meunier, "Electronic Flexoelectricity in Low-dimensional Systems," *Physical Review B* 77 (2008): 033403, https://doi.org/10.1103/PhysRevB.77.033403.

6. A. N. Morozovska, E. A. Eliseev, G. I. Dovbeshko, M. D. Glinchuk, Y. Kim, and S. V. Kalinin, "Flexoinduced Ferroelectricity in Low-dimensional Transition Metal Dichalcogenides," *Physical Review B* 102 (2020): 075417, https://doi.org/10.1103/PhysRevB.102.075417.

7. M. Springolo, M. Royo, and M. Stengel, "Direct and Converse Flexoelectricity in Two-Dimensional Materials," *Physical Review Letters* 127 (2021): 216801, https://doi.org/10.1103/PhysRevLett.127.216801.

8. K. Zheng, T. Vegge, and I. E. Castelli, "Giant in-Plane Flexoelectricity and Radial Polarization in Janus IV–VI Monolayers and Nanotubes," *ACS Applied Materials & Interfaces* 16 (2024): 19369–19378, https://doi.org/10.1021/acsami.4c01527.

9. B. Wang, Y. Gu, S. Zhang, and L.-Q. Chen, "Flexoelectricity in Solids: Progress, Challenges, and Perspectives," *Progress in Materials Science* 106 (2019): 100570, https://doi.org/10.1016/j.pmatsci.2019.05.003.

10. M.-M. Yang, D. J. Kim, and M. Alexe, "Flexo-photovoltaic Effect," *Science* 360 (2018): 904–907, https://doi.org/10.1126/science.aan3256.

11. J. Jiang, Z. Chen, Y. Hu, et al., "Flexo-photovoltaic Effect in MoS2," *Nature Nanotechnology* 16 (2021): 894–901, https://doi.org/10.1038/s41565-021-00919-y.

12. R. Roy, D. Nečas, and L. Zajičková, "Evidence of Flexoelectricity in Graphene Nanobubbles Created by Tip Induced Electric Field," *Carbon* 179 (2021): 677–682, https://doi.org/10.1016/j.carbon.2021.04.086.

13. X. Wang, A. Cui, F. Chen, et al., "Probing Effective Out-of-Plane Piezoelectricity in van der Waals Layered Materials Induced by Flexoelectricity," *Small* 15 (2019): 193106.

14. W. Peng, S. Y. Park, C. J. Roh, et al., "Flexoelectric Polarizing and Control of a Ferromagnetic Metal," *Nature Physics* 20 (2024): 450–455, https://doi.org/10.1038/s41567-023-02333-8.

---

Advanced Materials, 2026

9 of 11

e2140619-9. Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202501824, Wiley Online Library on [18/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are powered by the applicable Creative Commons License

---

15. H. Lu, C.-W. Bark, D. E. de los Ojos, et al., "Mechanical Writing of Ferroelectric Polarization," *Science* 336 (2012): 59–61, https://doi.org/10.1126/science.1218693.

16. S. Das, B. Wang, T. R. Paudel, et al., "Enhanced Flexoelectricity at Reduced Dimensions Revealed by Mechanically Tunable Quantum Tunnelling," *Nature Communications* 10 (2019): 537, https://doi.org/10.1038/s41467-019-08462-0.

17. S. M. Park, B. Wang, T. Paudel, et al., "Colossal Flexoresistance in Dielectrics," *Nature Communications* 11 (2020): 2586, https://doi.org/10.1038/s41467-020-16207-7.

18. L. Wang, S. Liu, X. Feng, et al., "Flexoelectronics of Centrosymmetric Semiconductors," *Nature Nanotechnology* 15 (2020): 661–667, https://doi.org/10.1038/s41565-020-0700-y.

19. X. Hu, G. Yu Chen, Y. Luan, et al., "Flexoelectricity Modulated Electron Transport of 2D Indium Oxide," *Advanced Science* 11 (2024): 2404272, https://doi.org/10.1021/acs.nanolett.9b03176.

20. A. Abdollahi, C. Peco, D. Millán, M. Arroyo, G. Catalan, and I. Arias, "Fracture Toughening and Toughness Asymmetry Induced by Flexoelectricity," *Physical Review B* 92 (2015): 094101, https://doi.org/10.1103/PhysRevB.92.094101.

21. H. Wang, X. Jiang, Y. Wang, et al., "Direct Observation of Huge Flexoelectric Polarization Around Crack Tips," *Nano Letters* 20 (2020): 88–94, https://doi.org/10.1021/acs.nanolett.9b03176.

22. M. Xu, X. Tian, Q. Deng, Q. Li, and S. Shen, "Directly Observing the Evolution of Flexoelectricity at the Tip of Nanocrystals," *Nano Letters* 23 (2023): 66–72, https://doi.org/10.1021/acs.nanolett.2c03614.

23. A. Lopez-Bezanilla, J. Campos-Delgado, B. G. Sumpter, et al., "Geometric and Electronic Structure of Closed Graphene Edges," *Journal of Physical Chemistry Letters* 3 (2012): 2097–2102.

24. C. Lee, X. Wei, J. W. Kysar, and J. Hone, "Measurement of the Elastic Properties and Intrinsic Strength of Monolayer Graphene," *Science* 321 (2008): 385–388, https://doi.org/10.1126/science.1157996.

25. S. Bertolazzi, J. Brivio, and A. Kis, "Stretching and Breaking of Ultrathin MoS2," *ACS Nano* 5 (2011): 9703–9709, https://doi.org/10.1021/nn203879f.

26. N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, and D. Vanderbilt, "Maximally Localized Wannier Functions: Theory and Applications," *Reviews of Modern Physics* 84 (2012): 1419–1475, https://doi.org/10.1103/RevModPhys.84.1419.

27. W. Zhu, T. Low, V. Perebeinos, et al., "Structure and Electronic Transport in Graphene Wrinkles," *Nano Letters* 12 (2012): 3431–3436, https://doi.org/10.1021/nl300563h.

28. J. Aljedani, M. J. Chen, and B. J. Cox, "Variational Model for Collapsed Graphene Wrinkles," *Applied Physics A* 127 (2021): 886, https://doi.org/10.1007/s00339-021-05000-y.

29. M. Tripathi, L. Valentini, Y. Rong, et al., "Free-Standing Graphene Oxide and Carbon Nanotube Hybrid Papers With Enhanced Electrical and Mechanical Performance and Their Synergy in Polymer Laminates," *International Journal of Molecular Sciences* 21 (2020): 8585, https://doi.org/10.3390/ijms21228585.

30. J. Canet-Ferrer, E. Coronado, A. Forment-Aliaga, and E. Pinilla-Cienfuegos, "Correction of the Tip Convolution Effects in the Imaging of Nanostructures Studied Through Scanning Force Microscopy," *Nanotechnology* 25 (2014): 395703, https://doi.org/10.1088/0957-4484/25/39/395703.

31. M. Tripathi, F. Lee, A. Michail, et al., "Structural Defects Modulate Electronic and Nanomechanical Properties of 2D Materials," *ACS Nano* 15 (2021): 2520–2531, https://doi.org/10.1021/acsnano.0c06701.

32. Z. Li, I. A. Kinloch, R. J. Young, et al., "Deformation of Wrinkled Graphene," *ACS Nano* 9 (2015): 3917–3925, https://doi.org/10.1021/nn507202c.

33. E. Khestanova, F. Guinea, L. Fumagalli, A. K. Geim, and I. V. Grigorieva, "Universal Shape and Pressure Inside Bubbles Appearing in van der Waals Heterostructures," *Nature Communications* 7 (2016): 12587, https://doi.org/10.1038/ncomms12587.

34. S. Deng, D. Rhee, W.-K. Lee, et al., "Graphene Wrinkles Enable Spatially Defined Chemistry," *Nano Letters* 19 (2019): 5640–5646, https://doi.org/10.1021/acs.nanolett.9b02178.

35. M. V. Balois-Oguchi, N. Hayazawa, S. Yasuda, et al., "Probing Strain and Doping along a Graphene Wrinkle Using Tip-Enhanced Raman Spectroscopy," *The Journal of Physical Chemistry C* 127 (2023): 5982–5990, https://doi.org/10.1021/acs.jpcc.2c08529.

36. A. A. Graf, S. P. Ogilvie, H. J. Wood, et al., "Raman Metrics for Molybdenum Disulfide and Graphene Enable Statistical Mapping of Nanosheet Populations," *Chemistry of Materials* 32 (2020): 6213–6221, https://doi.org/10.1021/acs.chemmater.0c02109.

37. P. Koirala, C. A. Mizzi, and L. D. Marks, "Direct Observation of Large Flexoelectric Bending at the Nanoscale in Lanthanide Scandates," *Nano Letters* 18 (2018): 3850–3856, https://doi.org/10.1021/acs.nanolett.8b01126.

38. A. G. Petrov, "Flexoelectricity of Model and Living Membranes," *Biochimica et Biophysica Acta (BBA)—Biomembranes* 1561 (2002): 1–25, https://doi.org/10.1016/S0304-4157(01)00007-7.

39. T. Dumitrică, C. M. Landis, and B. I. Yakobson, "Curvature-induced Polarization in Carbon Nanoshells," *Chemical Physics Letters* 360 (2002): 182–188, https://doi.org/10.1016/S0009-2614(02)00820-5.

40. V. I. Artyukhov, S. Gupta, A. Kutana, and B. I. Yakobson, "Flexoelectricity and Charge Separation in Carbon Nanotubes," *Nano Letters* 20 (2020): 3240–3246, https://doi.org/10.1021/acs.nanolett.9b05345.

41. J.-D. Zheng, Y.-F. Zhao, Z.-Q. Bao, et al., "Flexoelectric Effect Induced p–n Homojunction in Monolayer GeSe," *2D Materials* 9 (2022): 035005, https://doi.org/10.1088/2053-1583/ac6677.

42. H. Chen, C. Hu, L. Chen, et al., "Flexoelectric Effects in a Bent α–In2Se3 Ferroelectric Monolayer," *Physical Review B* 110 (2024): 014102, https://doi.org/10.1103/PhysRevB.110.014102.

43. J. Dong, B. Cai, and G. Ouyang, "Controllable Photoelectric Properties in Double-Wall MoS2 Nanotubes by the Flexoelectric Effect," *The Journal of Physical Chemistry C* 125 (2021): 11318–11324, https://doi.org/10.1021/acs.jpcc.1c02008.

44. H. Guo, T. Yang, X. Xuan, Z. Zhang, and W. Guo, "Flexoelectricity in Hexagonal Boron Nitride Monolayers," *Extreme Mechanics Letters* 52 (2022): 101669, https://doi.org/10.1016/j.eml.2022.101669.

45. K. P. Dou, H. H. Hu, X. Wang, et al., "Asymmetrically Flexoelectric Gating Effect of Janus Transition-metal Dichalcogenides and Their Sensor Applications," *Journal of Materials Chemistry C* 8 (2020): 11457–11467, https://doi.org/10.1039/D0TC02610G.

46. C. A. Mizzi, B. Guo, and L. D. Marks, "Experimental Determination of Flexoelectric Coefficients in SrTiO3, KTaO3, TiO2, and YAlO3 Single Crystals," *Physical Review Materials* 6 (2022): 055005, https://doi.org/10.1103/PhysRevMaterials.6.055005.

47. X. Li, G. Ren, Y. Yun, et al., (2024), *arXiv preprint arXiv:2409.17022*.

48. S. A. Iyengar, A. B. Puthirath, and V. Swaminathan, "Realizing Quantum Technologies in Nanomaterials and Nanoscience," *Advanced Materials* 35 (2023): 2107839, https://doi.org/10.1002/adma.202107839.

49. S. A. Iyengar, S. Bhattacharyya, S. Roy, N. R. Glavin, A. K. Roy, and P. M. Ajayan, "A Researcher's Perspective on Unconventional Lab-to-Fab for 2D Semiconductor Devices," *ACS Nano* 17 (2023): 12955–12970, https://doi.org/10.1021/acsnano.3c01927.

50. S. Roy, X. Zhang, A. B. Puthirath, et al., "Structure, Properties and Applications of Two-Dimensional Hexagonal Boron Nitride," *Advanced Materials* 33 (2021): 2101589, https://doi.org/10.1002/adma.202101589.

51. S. A. Iyengar, M. Tripathi, A. Srivastava, et al., "Graphene: A Hybridization of 2D Silica Glass and Graphene," *Advanced Materials* 37 (2025): 2419136, https://doi.org/10.1002/adma.202419136.

---

10 of 11

*Advanced Materials*, 2026

e1214095-10 Downloaded from https://advmat.onlinelibrary.wiley.com/doi/10.1002/adma.202419136 by the The New York Public Library on 18/09/2025. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

---

52. G. S. L. Fabris, R. B. de Oliveira, M. L. Jr. Pereira, R. Vajtai, P. M. Ajayan, and D. S. Galvão, "From Glaphene to Glaphynes: A Hybridization of Two-Dimensional Silica Glass and Graphynes," *ACS Nano* 20 (2026): 5541–5549, https://doi.org/10.1021/acsnano.5c16085.

53. P. Kumar, G. Singh, X. Guan, et al., "The Rise of Xene Hybrids," *Advanced Materials* 36 (2024): 2403881, https://doi.org/10.1002/adma.202403881.

**Supporting Information**

Additional supporting information can be found online in the Supporting Information section.

**Supporting File 1:** adma74142-sup-0001-SuppMat.docx.

**Supporting File 2:** adma74142-sup-0002-MovieSI-S7.zip.

*Advanced Materials*, 2026 — 11 of 11

15214095. Downloaded from https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202510224 on [18/09/2025]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License