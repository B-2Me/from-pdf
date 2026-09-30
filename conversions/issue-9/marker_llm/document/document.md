1

#### CONTENTS

| I. II. | Details of data analysis in trARPES measurement A. Matrix element effect in trARPES measurement B. Observation of charge density wave gap closure 1. Energy distribution curve (EDC) analysis 2. Quantitative understanding of EDCs in trARPES C. Effect of energy integration window D. Fitting of delay time scan data Time-dependent Ginzburg-Landau theory and theory of phase nucleation A. The scenario of coupled order parameters | 1 1 2 2 4 5 6 9 10 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|        | 1. Results                                                                                                                                                                                                                                                                                                                                                                                                                                | 11                 |
|        | B. Nucleation scenario                                                                                                                                                                                                                                                                                                                                                                                                                    | 12                 |
|        | 1. Results                                                                                                                                                                                                                                                                                                                                                                                                                                | 13                 |
|        | 2. Calculating the Nucleation Barrier                                                                                                                                                                                                                                                                                                                                                                                                     | 15                 |
|        | 3. Analytical constraint of decoupled TDGL model                                                                                                                                                                                                                                                                                                                                                                                          | 16                 |
| III.   | Selection and extraction of data from previous literature                                                                                                                                                                                                                                                                                                                                                                                 | 17                 |
| IV.    | Nomenclature of CDWs in rare-earth tritellurides                                                                                                                                                                                                                                                                                                                                                                                          | 18                 |
| V.     | Supplementary references                                                                                                                                                                                                                                                                                                                                                                                                                  | 18                 |

# <span id="page-1-0"></span>I. Details of data analysis in trARPES measurement

## <span id="page-1-1"></span>A. Matrix element effect in trARPES measurement

The photoemission intensity measured in ARPES experiments can be expressed by the following formula[<sup>1</sup>](#page-18-2) :

| $I(\mathbf{k}, E) = I_0(\mathbf{k}, E, \mathbf{A})A(\mathbf{k}, E)f(E, T)$ | (S1) |
|----------------------------------------------------------------------------|------|
|----------------------------------------------------------------------------|------|

where A(k, E) is the one-electron spectral function that encodes the band structure and correlation effects, and f(E, T) is the Fermi-Dirac distribution, where T is the temperature. The first term on the right-hand side I0(k, E, A) is proportional to P f,i M<sup>k</sup> f,i 2 , where M<sup>k</sup> f,i <sup>=</sup> ⟨<sup>ϕ</sup> k f |<sup>A</sup> · <sup>p</sup>|<sup>ϕ</sup> k i ⟩ is the photoemission matrix element that describes the transition from the initial state ϕ k i to the final state ϕ k f . p and A are respectively the electron momentum operator and the vector potential of incident electromagnetic wave. The matrix element thus is dependent on the polarization of the incident XUV beam that emits the photoelectron. Different matrix elements would lead to different spectral weight distributions on the photoemission spectra. However, matrix elements do not carry intrinsic information about the CDW order parameter dynamics. We thus need to exclude the possibility of artifacts created by the matrix element effect.

For this purpose, we repeated the same set of experiments with incident XUV photon polarization rotated by 90◦ . The data presented in the main text were all collected with linear polarization perpendicular to the sample surface (LV). Here, we compare the results with the spectra and time-resolved scans measured with linear polarization parallel to the sample surface (LH).

Comparing the spectrum acquired with different polarization (Fig. [S1$](#page-2-2), we noticed that the shadow band near c-CDW gap does not have spectral weight with LV polarization. Similarly, the shadow band near a-CDW gap is not present when measured with LH polarization. Meanwhile, the measured CDW gap size for both CDWs is consistent across different probe polarizations. Thus the matrix element does not create confusion in the description of the order parameter.

We further investigate the matrix element effect on the pump-probe scans under different excitation fluences. From Fig. [S2,](#page-3-0) comparing the time-evolution of the in-gap intensity measured with different probe polarizations, the recovery dynamics of both c-CDW (a and c) and a-CDW (b and d) are consistent and thus the matrix element effect does not affect the determination of CDW dynamics from the spectral weight in the CDW gaps.

2

![](_page_2_Figure_1.jpeg)

<span id="page-2-2"></span>FIG. S1. Comparison of ARPES spectrum with different incident photon polarization a-c Fermi surface map (a) and energy-momentum dispersion cuts featuring c-CDW (b) and a-CDW (c) measured with photon polarization perpendicular to the sample surface (LV), reproduced from Fig.1 (d-f) d-f The same ARPES measurement performed with photon polarization parallel to the sample surface (LH). The same color scales are used for each pair of spectra for comparison. The same CDW gaps for both a-CDW and c-CDW are consistently measured with both photon polarization.

## <span id="page-2-0"></span>B. Observation of charge density wave gap closure

# <span id="page-2-1"></span>1. Energy distribution curve (EDC) analysis

In the main text, we used the spectral weight in the CDW gaps as the major measure of CDW suppression, as the increase of spectral weight in the CDW gaps is dominantly contributed by the closure of CDW gap. This method was commonly adopted by the trARPES community to bypass the intrinsically inferior energy resolution and signal-to-noise ratio (SNR) of trARPES compared to equilibrium-state ARPES. For this reason, previous trARPES studies on various CDW systems, including but not limited to RTe3, 1T-TiSe2, CsV3Sb5, (TaSe4)2I, and 1T-TaS2, have used the in-gap spectral weight as a measure of CDW order parameter amplitude[2–](#page-18-3)[10](#page-19-0). Here, we directly prove that the CDW gap is indeed suppressed upon photoexcitation by comparing the energy distribution curves (EDCs) after photoexcitation. Furthermore, we provide further reasoning and analysis on how to appropriately understand the CDW gap values extracted from EDCs

In our trARPES measurements, we typically have two different strategies of data-taking for different purposes. The first strategy is snapshots, exemplified as data in Fig. 2, where we park the pump-probe delay at a fixed value and integrate heavily on the electron count. This strategy is meant to optimize the signal-to-noise ratio (SNR) in energy and momentum resolution. The second strategy is timescans, exemplified as data in Fig. 3, where we repeatedly scan the pump-probe delay and record data in a stroboscopic manner. This strategy is meant to optimize the SNR in temporal evolution. Due to the finite lifetime of the sample surface, it is not realistic to measure fine-step time scans with multiple pump fluences while at the same time having optimized SNR in energy and momentum on the same sample. Here, we demonstrate EDC analysis on both the snapshot data and the timescan data binned with 250 fs windows.

3

![](_page_3_Figure_1.jpeg)

<span id="page-3-0"></span>FIG. S2. Comparison of CDW recovery dynamics with different incident photon polarization. a,b Time evolution of normalized in-gap intensity of c-CDW (a) and a-CDW (b) measured with LV polarization, reproduced from Fig.3 (c.d) c,d Same measurement performed with probe photons with LH polarization. Same recovery dynamics of CDWs are observed with different incident probe photon polarizations, thus excluding the possibility of artifacts caused by the matrix element effect.

In Fig. [S3,](#page-4-1) we demonstrate the EDC analysis on the snapshots presented in Fig. 2 of the main text. From the raw EDC curves, we can clearly observe the rightward shifts of leading edges after timezero. This is a typical signature of CDW suppression. While in Fig. [S4,](#page-5-1) we demonstrate the timescan counter part of the same analysis.In both sets of plots, we overlapped the data points with the fitting curves of corresponding pump fluences in Fig. 3c and d, with only vertical scaling due to the different units. We can clearly see that the temporal evolution of leading edges extracted from EDCs in both sets of data agrees well with the temporal evolution of spectral weight in the CDW gaps. This is a strong evidence showcasing the consistency between the in-gap spectral weight dynamics and CDW gap dynamics.

Having established the equivalence between gap and in-gap spectral weight dynamics, we further analyze the fluence dependence of the EDCs. The EDCs at a delay time with maximum CDW suppression signal (0.5 ps) at c- and a-CDW gap positions in reciprocal space are plotted in Fig. [S5](#page-6-1) a and b. Compared to the spectra in equilibrium (grey curves), the leading edges of the EDCs demonstrate a clear shift towards the Fermi level. This shift in energy scales with fluence, signifying a typical suppression of CDW amplitude upon photoexcitation.

We note that in all analysis demonstrated above, no other signals of in-gap states are observed from EDCs. Thus, the in-gap spectral weight increase observed in our trARPES measurement is dominantly contributed by the CDW suppression, justifying the in-gap spectral weight as a proper measure of the CDW amplitude dynamics. It is also noteworthy that the EDC analysis for both CDW gaps under different fluences indicates that c-CDW has not reached the full CDW suppression within our fluence range while a-CDW is close to full suppression, given the saturation behaviour under different fluences, as shown in c-d. This is also consistent with previous ultrafast measurements on similar materials[11–](#page-19-1)[14](#page-19-2) .

4

![](_page_4_Figure_1.jpeg)

<span id="page-4-1"></span>FIG. S3. EDCs analysis of snapshot data. a,b EDCs at different timesteps for c-CDW (a) and a-CDW (c) extracted from the same dataset as demonstrated in Fig. 2 in the main text. c-d Leading edge of c-CDW (c) and a-CDW (d) bands extracted from EDCs of each delay time, overlapped with the fitting curve for 0.42 mJ/cm2 data from Fig. 3, with only vertical scaling. The error bars represent the energy resolution of our trARPES instrument.

## <span id="page-4-0"></span>2. Quantitative understanding of EDCs in trARPES

We would like to note that though extracting gap dynamics from EDCs can be qualitatively useful and consistent with in-gap spectral weight analysis, one needs to be extra cautious before citing the extracted gap value as the exact gap size. Here we provide a systematic study on how the shifts in EDC leading edge can underestimate the actually gap size change in trARPES measurements

We start from revisiting the gap closure dynamics of c-CDW. Besides in-gap spectral weight and transient EDCs of valence band, one can extract the CDW gap dynamics, in a limited time interval, also from the conduction band bottom above the CDW gap.

In Fig. [S6,](#page-7-0) we demonstrate the transient EDCs for c-CDW gap plotted in log-scale. we note that this analysis is only practical for c-CDW, where the gap is large enough and is thus de-convolved from the thermal broadening near the Fermi level. For a-CDW, due to particle-hole asymmetry[<sup>15</sup>](#page-19-3) and small gap amplitude, it is not practical to identify the transient gap closure process from transient EDC.

We can clearly observe the closure of CDW gap. After photoexcitation, the leading edge of the conduction band is barely distinguishable. A careful tracing of the conduction band peak position gives an estimation of 40% of gap closure, as indicated by the black triangular labels in Fig. [S6.](#page-7-0) This is consistent with the observation in previous trARPES studies on RTe<sup>3</sup> [<sup>16</sup>](#page-19-4). We note that compared to the values extracted from valence band EDC fitting presented in Fig. [S5,](#page-6-1) the percentage of change extracted from conduction band shifting is much larger, indicating a severe underestimation in valence band EDC fitting.

To further demonstrate the underestimation effect of transient valence EDC analysis, we perform a simulation of ARPES spectra for electronic bands gapped by long range orders. From the simulation, we find that the number extracted from the leading edge in EDC, is usually a severe underestimation. We note that part of this underestimation

5

![](_page_5_Figure_1.jpeg)

<span id="page-5-1"></span>FIG. S4. EDCs analysis of timescan data. a-c (d-f) Leading edge of c-CDW (a-CDW) band extracted from EDCs acquired from binning the continuous time scans with a 250 fs step size, at 0.14, 0.42, 0.70 mJ/cm<sup>2</sup> , respectively. All data are overlapped with corresponding fitting curves from Fig. 3 in the main text, with only vertical scaling. The error bars represent the energy resolution of our trARPES instrument.

is a result of Fermi-Dirac function. Unlike equilibrium-state ARPES measurement, where Fermi-Dirac function can be removed in order to extract precise gap size, transient electronic states measured in trARPES do not strictly follow Fermi-Dirac distribution before thermalization and thus it would not be fully justified to extract the precise gap size in trARPES by removing the Fermi-Dirac distribution at a very short delay time after the time zero.

As demonstrated in Fig. [S7,](#page-7-1) we first generate the single-electron spectral function for an electronic system gapped by a long range order from the eigenvalues of Fröhlich Hamiltonian. As an example, we compare the two cases where the CDW gap ∆ = 100 meV (a) and 200 meV (b) respectively. In order to simulate real ARPES spectrum, we multiply the spectral function by the Fermi-Dirac function (c,d) convoluted with the instrument resolution, and superposed with a background noise function (e,f). By making cut along the window labeled in Fig. [S7](#page-7-1)e, we acquired the EDCs for ∆ = 100 meV and 200 meV case respectively. By either directly fitting the EDCs or fitting the peak position after the taking the first derivative with respect to energy, we extracted a gap difference between 10 meV and 40 meV, which are 2.5 to 10 times smaller than the real gap difference of 100 meV. We thus conclude that EDC analysis returns a severely underestimated gap size, possibly due to the existence of Fermi-Dirac function. However, the qualitative change and recovery dynamics, which we previously showed to be consistent with the in-gap spectral weight, is still meaningful and trustworthy.

## <span id="page-5-0"></span>C. Effect of energy integration window

The data we presented in Fig. 3 of the main text is acquired by integrating over a window of 50 meV energy window centered at Fermi energy for the best signal-to-noise ratio. In order to exclude the possibility of contributions from other parts of the electronic structure, we hereby show the robustness against the selection of an integration window.

Comparing the results acquired with a 50 meV integration window to the ones acquired with a 20 meV integration window (Fig. [S8$](#page-8-0), we clearly observe that the time traces, after normalization from 0 to 1, agree almost perfectly. We can thus exclude the possibility of any artifacts created by the selection of the integration window, solidifying the analysis and conclusions presented in the main text.

6

![](_page_6_Figure_1.jpeg)

<span id="page-6-1"></span>FIG. S5. Direct observation of CDW gaps closure through energy distribution curves (EDCs) a,b EDCs 0.5 ps after photoexcitation of various fluences, plotted in log scale for better visualization. The EDCs were acquired by integrating spectral weights over a momentum window of 0.1 Å<sup>−</sup><sup>1</sup> centered at the c-CDW (a) and a-CDW (b) gap position. The EDCs without photoexcitation are shown in grey for reference. Inset: raw data of EDCs plotted in linear scale. c-d Change of In-gap spectral weight (c) acquired by integrating the electron counts over the ROI for c-CDW and a-CDW respectively, at the delay time when CDW quenching reaches maximum and leading edge position (d) extracted from the same snapshot scans as in a and b, showing consistency.

to further prove the validity of our choice of Region of interest (ROI), we comparatively study the CDW gap dynamics and conduction band carrier population dynamics with the time evolution of spectral weight on each constant energy contours from 0 to 0.4 eV.

Fig. [S9](#page-8-1) demonstrates the integrated spectral weight at the c-CDW (left) and a-CDW (right) gap momentum-space position across various binding energies. We can clearly observe that at high binding energy, the electron population decays at a significantly higher rate compared to the SW at the Fermi level, which represents the CDW dynamics. For c-CDW, the band occupation dynamics has slight effect around 100 meV, where the ROI start to touch the edge of conduction band[<sup>15</sup>](#page-19-3). Above 200 meV, the spectral weight dynamics is dominated by electron population dynamics in the conduction bands. For a-CDW, due to the small gap, electron population dynamics in the conduction bands starts to dominate right above the Fermi level. In either case, we have proven that the SW evolution at the Fermi level, and thus in the CDW gaps, are vastly different from electron population evolution in conduction bands.

# <span id="page-6-0"></span>D. Fitting of delay time scan data

In order to quantitatively extract and compare the recovery dynamics of CDWs, we fit the time trace data in Fig. 3 to an exponential function that models relaxation dynamics multiplied by an error function that models the initial CDW quenching. The entire fitting function is convolved with a Gaussian function that models the temporal

7

![](_page_7_Figure_1.jpeg)

<span id="page-7-0"></span>FIG. S6. CDW gap dynamics through conduction band. Energy distribution curves for c-CDW gap at various delay time with 0.42 mJ/cm<sup>2</sup> excitation. Same data as in Fig. [S3](#page-4-1) but plotted in log scale to highlight the conduction band bottom dynamics. The curves are offset by a constant for clarity.

![](_page_7_Figure_3.jpeg)

<span id="page-7-1"></span>FIG. S7. Simulation of ARPES spectrum of gapped electronic system. a-b. Single-electron spectral function A(k, E) for a system gapped by long-range order. The gap sizes are respectively 100 meV and 200 meV. c-d. Single-electron spectral function multiplied by Fermi-Dirac function. e-f. Spectra in c-d superposed with a noise function that simulates real ARPES data. g. Energy distribution curves cut from spectra in e-f, showing a leading edge shift much smaller than 100 meV.

8

![](_page_8_Figure_1.jpeg)

<span id="page-8-0"></span>FIG. S8. Comparison of time traces acquired from different energy integration windows a,b In-gap photoemission intensities of c-CDW (a) and a-CDW (b) under 0.07 mJ/cm<sup>2</sup> (light) and 0.70 mJ/cm<sup>2</sup> (dark) fluences, acquired with a 50 meV integration window (hollow) and a 20 meV integration window (solid).

![](_page_8_Figure_3.jpeg)

<span id="page-8-1"></span>FIG. S9. Distinct behaviours of CDW gap dynamics and carrier population dynamics. Time evolution of the spectral weight at the c-CDW (left) and a-CDW (right) gap momentum-space position across various constant-energy contours. The clearly different dynamics at Fermi level (E − E<sup>F</sup> = 0 meV) showcases the CDW order parameter dynamics as opposed to electron population dynamics.

9

resolution of the instrument. The fitting function takes the following general form[<sup>3</sup>](#page-18-4) :

<span id="page-9-2"></span>
$$\Delta f(t) = \left[ \frac{1}{2} \left( 1 + \text{Erf} \left( \frac{2\sqrt{\ln 2}(t - t_0)}{w} \right) \right) \right. \\ \left. \cdot (I_\infty + I_0 e^{-(t-t_0)/\tau}) \right] * g(w_0, t). \quad (\text{S2})$$

In this model, w represents the intrinsic system response time due to photoexcitation, in our specific case, the Debye-Waller intensity suppression time. I<sup>0</sup> represents the maximum system response. I<sup>∞</sup> denotes the value of ∆f at long time delays when the system reaches a quasi-equilibrium thermal state. τ is the characteristic relaxation time to the quasi-equilibrium. t<sup>0</sup> is associated with the relative arrival time of pump and probe pulses.

### <span id="page-9-0"></span>II. Time-dependent Ginzburg-Landau theory and theory of phase nucleation

We begin by reviewing the putative equilibrium free energy landscape of ErTe3. This material undergoes two phase transitions: A first into a unidirectional CDW at Tc<sup>1</sup> (dominant order) and a second into a bidirectional CDW at Tc<sup>2</sup> (subdominant order). The two CDW orders can each be represented by a complex scalar field Φ <sup>c</sup> = ϕ c <sup>1</sup> + iϕ<sup>c</sup> <sup>2</sup> and Φ <sup>a</sup> = ϕ a <sup>1</sup> + iϕ<sup>a</sup> 2 , which encode both the amplitude and phase of the CDW modulation along the corresponding lattice directions.

To construct the free energy functional, we assume that it depends smoothly on the order parameters and their spatial variations. It generally consist of a "kinetic" term that penalizes spatial variations of the fields and a "potential" term f[Φ(r, t)]:

$$\mathcal{F}[\Phi(\mathbf{r}, t)] = \int d^d \mathbf{r} \left[ \frac{K}{2} (|\nabla_{\mathbf{r}} \Phi^a(\mathbf{r}, t)|^2 + |\nabla_{\mathbf{r}} \Phi^c(\mathbf{r}, t)|^2) + f[\Phi(\mathbf{r}, t)] \right] \quad (\text{S3})$$

where we truncated the "kinetic" term at second order in spatial derivatives assuming that the order parameters vary smoothly on length scales large compared to the microscopic lattice spacing. For the "potential" term f[Φ(r, t)] the conventional approach to studying phase transitions involves expanding in the order parameters, Φ <sup>c</sup> and Φ a , while ensuring that this expansion respects the symmetries of the system. This approach assumes that the order parameter is small within the vicinity of the phase transition. Whereas this is generically true for second-order phase transitions, for a first-order one, however, the order parameter can undergo a discontinuous jump to a finite value, questioning the validity of the symmetry constrained expansion. Thus in the following we consider two distinct cases for the free energy potential f[Φ(r, t)]:

- 1. A coupled scenario (cf. Sec. [II A$](#page-10-0), where the expansion of the order parameters assumes a symmetry between the a- and c-CDW. This leads to second-order phase transitions at T<sup>c</sup><sup>1</sup> and T<sup>c</sup>2.
- 2. A decoupled scenario (cf. Sec. [II B$](#page-12-0), where the expansion is not subject to lattice symmetry constraints. This results in a second-order phase transition at T<sup>c</sup><sup>1</sup> and a first-order phase transition at T<sup>c</sup>2.

In both cases, we ensure that the U(1) symmetry of the CDW order parameter remains intact by only including terms that are analytic in |<sup>Φ</sup> <sup>α</sup>(r, t)| 2 .

To model the influence of the pump pulse, we assume that the incident light is primarily absorbed by electrons, leading to an instantaneous increase in the electronic temperature Te. Following this initial jump, we assume, for simplicity, the electronic temperature to decay to equilibrium with a constant rate τeq, i.e.

<span id="page-9-1"></span>
$$T_e(t) = T_{ph} + \theta(t) \Delta T_e^{-t/\tau_{eq}}. \quad (S4)$$

In our modeling, the electronic temperature modulates the second order Landau coefficient <sup>r</sup>(t) = <sup>r</sup>0(Te(t) − <sup>T</sup>˜ <sup>c</sup>)/T˜ c (the "mass" term) of the free energy potential f[Φ(r, t)]. Here, T˜ <sup>c</sup> denotes the temperature at which r(t) changes sign; however, due to the inclusion of higher-order terms in the expansion, T˜ <sup>c</sup> does not correspond to the actual phase transition temperature. The cooling down of the electronic subsystem increases the phononic temperature Tph but given the significantly larger heat capacity of the lattice, this effect is typically negligible. Accordingly, we assume the phononic temperature, Tph, to remain constant throughout the time evolution. This modeling applies to both the coupled and decoupled scenarios. However, in the decoupled one we will have r a <sup>0</sup> and r c 0 , instead of a single r0.

10

#### <span id="page-10-4"></span><span id="page-10-0"></span>A. The scenario of coupled order parameters

The approximate symmetry of the CDW in ErTe<sup>3</sup> is <sup>U</sup>(1) × <sup>U</sup>(1) × **<sup>Z</sup>**<sup>2</sup> as we are dealing with two orthogonal incommensurate CDWs[<sup>17</sup>](#page-19-5). However, due to a slight orthorhombicity, the **Z**<sup>2</sup> symmetry is explicitly broken (the space group is Cmcm) [<sup>18</sup>](#page-19-6). Thus, at zero applied stress, the dominant order is, in reality, always along the c-axis. Up to fourth order, the free energy potential compatible with this symmetry is

$$f[\Phi] = \frac{r}{2} (|\Phi^a|^2 + |\Phi^c|^2) + \frac{b}{2} (|\Phi^a|^2 - |\Phi^c|^2) + \frac{\tilde{g}}{2} |\Phi^a|^2 |\Phi^c|^2 + \frac{u}{4} (|\Phi^a|^2 + |\Phi^c|^2)^2. \quad (\text{S5})$$

For <sup>g</sup> = ˜g+u > <sup>0</sup> and b > <sup>0</sup> it leads to two second-order phase transitions at different temperatures <sup>T</sup> ∼ <sup>r</sup>: First into a striped CDW along the c-axis and second into a checkerboard state. Neglecting fluctuations the critical temperatures for the two phase transitions are given by Tc<sup>1</sup> = T˜ <sup>c</sup>(b/r<sup>0</sup> + 1) and Tc<sup>2</sup> = T˜ <sup>c</sup>b(<sup>g</sup> <sup>+</sup> <sup>u</sup>)/(r0(<sup>g</sup> − <sup>u</sup>)) + <sup>T</sup>˜ <sup>c</sup>. In practice, the second phase is actually a bidirectional CDW as the strengths of the two CDWs are different. Furthermore, this model also lacks a first-order phase transition if the strain <sup>ϵ</sup> ∼ <sup>b</sup> is tuned. These shortcomings can be cured by including higher order expansion terms, which was done in previous works[19,](#page-19-7)[20](#page-19-8). However, these higher-order terms do not change the nature of the temperature-driven second-order phase transitions.

In the absence of slow hydrodynamics modes, the dynamics close to a phase transition exhibit a clear separation of scales: All physical quantities fluctuate much faster than the order parameter, i.e., they merely constitute a stochastic force on the order parameter. Since the CDW order parameter is not conserved, the equation of motion describing the post-quench evolution is of model-A type[<sup>21</sup>](#page-19-9):

<span id="page-10-3"></span>
$$\frac{d}{dt}\phi_\alpha(\mathbf{r},t) = -\Gamma_\alpha \frac{\delta \mathcal{F}}{\delta\phi_\alpha(\mathbf{r},t)} + \eta_\alpha(\mathbf{r},t) \quad (\text{S6})$$

with a Gaussian noise ⟨<sup>η</sup> <sup>α</sup>(r, t)⟩ = 0 and ⟨<sup>η</sup> <sup>α</sup>(r, t)η β (r ′ , t′ )⟩ = 2ΓαTphδ(<sup>r</sup> − <sup>r</sup> ′ )δ(<sup>t</sup> − <sup>t</sup> ′ )δαβ. In what follows, we simplify the stochastic nonlinear dynamics by employing the Gaussian approximation, which gives a non-perturbative framework to study post-quench evolution and competition of the two CDWs – this closely follows Refs.[13,](#page-19-10)[22](#page-19-11). To this end, we split the complex fields into real and imaginary parts: Φ <sup>a</sup> = ϕ a <sup>1</sup> + iϕ<sup>a</sup> <sup>2</sup> and Φ <sup>c</sup> = ϕ c <sup>1</sup> + iϕ<sup>c</sup> <sup>2</sup> and rewrite the free energy

$$\mathcal{F}[\phi] = \int d^d \mathbf{r} \left[ \frac{K}{2} \sum_{\alpha} \left[ (\nabla \phi_{\alpha}^{\alpha}(\mathbf{r}, t))^2 + (\nabla \phi_{\alpha}^c(\mathbf{r}, t))^2 \right] + f[\phi(\mathbf{r}, t)] \right], \quad (S7)$$

$$f[\phi(\mathbf{r})] = \frac{r+b}{2} \sum_{\alpha} (\phi_{\alpha}^{\alpha})^2 + \frac{r-b}{2} \sum_{\alpha} (\phi_{\alpha}^{\alpha})^2 + \frac{g}{2} \sum_{\alpha,\beta} (\phi_{\alpha}^{\alpha})^2 (\phi_{\beta}^{\alpha})^2 + \frac{u}{4} \sum_{\alpha,\beta} ((\phi_{\alpha}^{\alpha})^2 (\phi_{\beta}^{\alpha})^2 + (\phi_{\alpha}^{\alpha})^2 (\phi_{\beta}^{\alpha})^2). \quad (\text{S8})$$

We split each field into its mean field part ϕ¯ and fluctuations δϕ around it:

$$\phi_\alpha^o(\mathbf{r}, t) = \bar{\phi}_\alpha^o(t) + \delta\phi_\alpha^o(\mathbf{r}, t) = \bar{\phi}^{o,\alpha}(t) + \frac{1}{\sqrt{N}} \sum_{\mathbf{k}\neq 0} e^{i\mathbf{k}\cdot\mathbf{r}} \phi_{\mathbf{k}}^{o,\alpha}(t) = \frac{1}{\sqrt{N}} \sum_{\mathbf{k}} e^{i\mathbf{k}\cdot\mathbf{r}} \phi_{\mathbf{k}}^{o,\alpha}(t), \quad \phi_{\mathbf{k}=0}^{o,\alpha} = \sqrt{N}\bar{\phi}^{o,\alpha}. \quad (\text{S9})$$

We introduce the equal-time correlation functions as

| $D_{\mathbf{k}}^{o,\alpha\alpha}(t) = \langle \delta\phi_{\mathbf{k}}^{o,\alpha}(t)\delta\phi_{-\mathbf{k}}^{o,\alpha}(t) \rangle, \quad n_{\alpha\alpha}^o(t) = \frac{1}{N} \sum_{\mathbf{k}} D_{\mathbf{k}}^{o,\alpha\alpha}(t) \quad (S10)$ |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|

where o = a, c, and all other correlators are assumed to be zero. Without loss of generality, we can set ϕ¯α̸=1 = 0, as by symmetry, always picking α = 1 to be the direction of symmetry breaking/condensation. The mean-field equations of motion in the <sup>1</sup>/N expansion (here N = 4) read

| $\frac{d}{dt}\bar{\phi}^o = -\Gamma_o r_{\text{eff}}^o \bar{\phi}^o$ | with | $r_{\text{eff}}^o = r + b + u \left( (\bar{\phi}^a)^2 + \sum_{\beta} n_{\beta\beta}^a \right) + g \left( (\bar{\phi}^c)^2 + \sum_{\beta} n_{\beta\beta}^c \right)$ | (S11) |
|----------------------------------------------------------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| <hr/>                                                                |      |                                                                                                                                                                    |       |

<span id="page-10-2"></span><span id="page-10-1"></span>
$$r_{\text{eff}}^c = r - b + u \left( (\bar{\phi}^c)^2 + \sum_{\beta} n_{\beta\beta}^c \right) + g \left( (\bar{\phi}^a)^2 + \sum_{\beta} n_{\beta\beta}^a \right) \quad (S12)$$

where <sup>ϕ</sup>¯<sup>o</sup> ≡ <sup>ϕ</sup>¯o,α=1 and we used Wick's theorem which holds for the Gaussian approximation we employ. Within the same approximation, the dynamics of correlators is then governed by:

$$\frac{d}{dt} D_{\mathbf{k}}^{D, \cdot \parallel}(t) = 2\Gamma_o T_{\text{ph}} - 2\Gamma_o \left[ r_{\text{eff}}^o + Kk^2 + 2u(\bar{\phi}^o)^2 \right] D_{\mathbf{k}}^{D, \parallel}(t) \quad (\text{S13})$$

$$\frac{d}{dt} D_{\mathbf{k}}^{o,\perp}(t) = 2\Gamma_o T_{\text{ph}} - 2\Gamma_o [r_{\text{eff}}^o + Kk^2] D_{\mathbf{k}}^{o,\perp}(t) \quad (\text{S14})$$

11

![](_page_11_Figure_1.jpeg)

FIG. S10. Free energy landscape for Teq = 0.4, T˜<sup>c</sup> = 0.9, r<sup>0</sup> = 2, u = 1, g˜ = −1, b = 0.23, τeq = 0.3

where D o,∥ k (t) = D o,11 k (t) and D o,⊥ k (t) = D o,22 k (t). To numerically solve Eqs. [$S11$](#page-10-1)–[$S14$](#page-10-2), we must define a momentum grid. Given that ErTe<sup>3</sup> is a layered material and ARPES typically probes only a few layers, we set the dimensionality to d = 2. In our simulations, we fix a UV cutoff, Λ, and the number of radial momentum points, Nk, which introduces an effective IR cutoff. This is physically meaningful, as quenched disorder in the real material also imposes a natural IR cutoff.

### <span id="page-11-0"></span>1. Results

![](_page_11_Figure_5.jpeg)

<span id="page-11-1"></span>FIG. S11. Order parameter dynamics after a quench in the coupled orders scenario, cf. Eq. [$S8$](#page-10-3). Exponential fits were done only to extract the characteristic recovery times. We use a numerical time step of ∆t = 0.0005 and a fourth order Runge–Kutta. Numerical parameters are Λ = π, Γ<sup>a</sup> = Γ<sup>c</sup> = 0.5 , K = 1, τeq = 0.3, dimension d = 2 and #momenta N<sup>k</sup> = 1000.

Figure [S11](#page-11-1) (left) shows the resulting post-pulse a- and c-CDWs dynamics, as described by Eqs. [$S11$](#page-10-1)-[$S14$](#page-10-2). Following the experiment, we are primarily interested in extracting the recovery times of each CDW. To this end, we fit an exponential decay to each curve shown in Fig. [S11](#page-11-1) (left), starting at the time the corresponding minimum is reached. Strictly speaking, the recovery of the order parameters in this modeling follows a power-law[<sup>22</sup>](#page-19-11); however, the exponential fits are employed to extract the characteristic recovery times, which we then compare with experimental data. Figure [S11](#page-11-1) (right) shows these recovery times as functions of fluence: both quantities strongly depend on the

12

![](_page_12_Figure_1.jpeg)

FIG. S12. Photoexcitation dynamics of CDW mean fields and two-point correlation functions in the scenario of coupled order parameters, cf. Eq. [$S8$](#page-10-3). We use a numerical time step of ∆t = 0.0005 and a fourth-order Runge–Kutta.Numerical parameters are Λ = π, Γ<sup>a</sup> = Γ<sup>c</sup> = 0.5 , K = 1, τeq = 0.3, dimension d = 2 and #momenta N<sup>k</sup> = 1000.

pulse strength, characteristic of second-order phase transitions[<sup>22</sup>](#page-19-11). We remark that while we set Γ<sup>a</sup> = Γc, we still observe distinct recovery times of the two order parameters. Crucially, the a-CDW exhibits an even stronger fluence dependence, which clearly disagrees with the experimental findings and necessitates further analysis, as we detail below.

# <span id="page-12-0"></span>B. Nucleation scenario

![](_page_12_Figure_6.jpeg)

Free Energy Landscapes for ∆<sup>T</sup> = 1.5

FIG. S13. Free energy for numerical parameters Teq = 0.4, Tc<sup>1</sup> = 1.0, Tc<sup>2</sup> = 0.6, r 0 <sup>c</sup> = 2, r 0 <sup>a</sup> = 1, u<sup>c</sup> = 1, u<sup>a</sup> = −25, u ′ <sup>a</sup> = 20

The assumption for Eq. [$S5$](#page-10-4) is that the order parameters are small close to the phase transition. This assumption is valid for the phase transition at T<sup>c</sup>1, but for the subdominant phase transition, it may be problematic, especially if it 13

is first order. Indeed, it is not clear whether the phase transition is driven by competition between the different CDW order parameters. For example,[<sup>23</sup>](#page-19-12) proposes a competition between a band anticrossing and the a-CDW instability instead, which leads to a hysteresis behavior of the Hall coefficient.

A second-order phase transition is driven by fluctuations, which naturally give rise to a fluence-dependent recovery rate, as shown in Sec. [II A—](#page-10-0)this might not be the case for a first-order phase transition. Within cooling the electronic temperature, a new minimum with lower energy can form. Fluctuations determine the probability of nucleating into the new minima, cf. the canonical Kramer's problem – see Fig. [S14.](#page-14-0) Once this local nucleation happens the mean field value is suddenly large and fluctuations become negligible. Guided by this, we propose in this section a decoupled free energy

$$f[\Phi] = \frac{1}{2} (r_c|\Phi^c|^2 + r_a|\Phi^a|^2) + \frac{1}{4} (u_a|\Phi^a|^4 + u_c|\Phi^c|^4) + \frac{u'_a}{6}|\Phi^a|^6 \quad (S15)$$

where for r<sup>a</sup> > 0, u<sup>a</sup> < 0, and u ′ <sup>a</sup> > 0, we get a first-order phase transition in the a-CDW. Neglecting fluctuations the critical temperatures are given by Tc<sup>1</sup> = T˜ <sup>c</sup><sup>1</sup> and Tc<sup>2</sup> = T˜ <sup>c</sup>2(1 + 3u 2 <sup>a</sup>/(16r 0 au ′ a )).

Nucleation of a bubble gains (local) free energy but costs surface energy. Within the thin-wall approximation the energy of a bubble of size R is given by

<span id="page-13-2"></span>

| $E(R) = 2\pi R\sigma - \pi R^2 \Delta f$ | (S16) |
|------------------------------------------|-------|
|                                          |       |

where σ is a surface tension that quantifies the cost of a domain wall between the disordered phase (ϕ <sup>a</sup> = 0) and the ordered phase (ϕ¯<sup>a</sup> = ϕ a 0 ) and ∆f = f(ϕ¯<sup>a</sup> 0 ) − <sup>f</sup>(0), the free energy density benefit of being in the ordered phase. This schematic estimate of the free energy of a bubble is instructive in the following sense. Small bubbles are energetically costly due to the surface tension overpowering the free energy benefit. In the opposite regime, <sup>R</sup> → ∞, the free energy gain dominates the surface tension cost, and the bubble size runs away. The maximum free energy occurs at R<sup>c</sup> = σ ∆f , the critical bubble size, which accompanies a barrier ∆F. Bubbles are formed by nucleation of ordered domains of radius <sup>R</sup>c, which occurs at a rate <sup>Γ</sup>nuc ≃ exp(−∆F/T). In the Sec. [II B 2](#page-15-0) we pedagogically articulate how

we calculate the instantaneous nucleation rate <sup>Γ</sup>nuc(t) ≃ exp(−∆F(ra(t))/T), as a function of <sup>r</sup>a(t). Once a bubble has nucleated, it grows spherically, due to the pressure difference building up inside and outside of the bubble, with a rate Γ<sup>g</sup> until it impinges upon another bubble. Growth occurs in nucleated regions, nucleation can only occur in unnucleated regions. Accordingly, we subtract off an excluded volume arising from the regions in which nucleation has already occurred. Assuming a homogeneous and isotropic nucleation and growth we end up with

<span id="page-13-1"></span>
$$\frac{d}{dt}\bar{\phi}^a(t) = (\bar{\phi}_0^a - \bar{\phi}^a(t)) \Gamma_{\text{nuc}}(t), \quad (\text{S17})$$

where ϕ¯ <sup>0</sup> is the global minimum. Eq. [$S17$](#page-13-1) is similar to the Avrami equation but assumes a transformation that is dominated by nucleation. It is, however, only valid for T < T<sup>c</sup>2, i.e. after a new minima in the free energy has formed. For T > T<sup>c</sup><sup>2</sup> there is only a single minimum and thus we can adopt the model developed in Sec. [II A](#page-10-0) to model the dynamics instantaneously after the quench. For a free energy up to 6th order they read

$$\frac{d}{dt}\bar{\phi}^a = -\Gamma_{\parallel} r_{\text{eff}}\bar{\phi}^a \quad (\text{S18})$$

d D k (t) = 2Γ∥Tph − 2Γ<sup>∥</sup> reff + Kk<sup>2</sup> + 2u(ϕ¯<sup>a</sup> ) <sup>2</sup> + 4u ′ (ϕ¯<sup>a</sup> ) 4 D k (t) (S19)

| $\frac{d}{dt} D_{\mathbf{k}}(t) = 2\Gamma_{\perp} T_{\text{ph}} - 2\Gamma_{\parallel} T_{\text{eff}} + 2\Gamma_{zz} T_{\text{eff}}(p) - 2\Gamma_{zt}(p) + 2\Gamma_{zk}(p)$ | (S10) |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| $\frac{d}{dt} D_{\mathbf{k}}^{\perp}(t) = 2\Gamma_{\perp} T_{\text{ph}} - 2\Gamma_{\perp} [r_{\text{eff}} + Kk^2] D_{\mathbf{k}}^{\perp}(t)$                               | (S20) |

$$r_{\text{eff}} = r + u \left( (\bar{\phi}^a)^2 + \sum_{\beta} n_{\beta\beta} \right) + u' \left( (\bar{\phi}^a)^4 + 2(\bar{\phi}^a)^2 \sum_{\beta} n_{\beta\beta} + \sum_{\beta, \gamma} n_{\beta\beta} n_{\gamma\gamma} \right) \quad (\text{S21})$$

where we have defined D k (t) = D<sup>11</sup> k (t) and D<sup>⊥</sup> k (t) = D<sup>22</sup> k (t). Similarly to the previous section we model the pump as rc(t) = r c (Te(t)/T˜ <sup>c</sup><sup>1</sup> − 1) and <sup>r</sup>a(t) = <sup>r</sup> 0 a (Te(t)/T˜ <sup>c</sup><sup>2</sup> − 1) where the electronic temperature behavior follows Eq. [$S4$](#page-9-1). The dynamics for the c-CDW is given by Eq. [$S11$](#page-10-1) - [$S14$](#page-10-2).

A sketch of the dynamics is given in Fig. [S14.](#page-14-0)

## <span id="page-13-4"></span><span id="page-13-3"></span><span id="page-13-0"></span>1. Results

In Fig. [S15](#page-14-1) a) and b) we plot the a- and c-CDW dynamics dynamics for a decoupled free energy given by Eq. [$S15$](#page-13-2). The results for the dominant order a) are similar to the one obtained in Fig. [S11](#page-11-1) and the recovery time exhibits a

14

![](_page_14_Figure_1.jpeg)

<span id="page-14-0"></span>FIG. S14. Sketch of the time evolution of the free energy in the nucleation scenario: Before the pulse arrival, the order parameter is in the equilibrium minimum of the free energy. Shortly after photoexcitation, the free energy becomes essentially parabolic with a minimum at zero, while the minimum at finite order parameter is transiently lost. The dynamics are assumed to be overdamped and given by Eq. [$S18$](#page-13-3) - Eq. [$S21$](#page-13-4). Within the subsequent cooldown, a new free-energy minimum forms so that the order parameter can "jump" into it and spatially grow, with the probability given by the Kramers problem. Both these processes are captured by Eq. [$S17$](#page-13-1).

![](_page_14_Figure_3.jpeg)

<span id="page-14-1"></span>FIG. S15. Post-pulse order parameter dynamics for the nucleation scenario. Exponential fits were done only to extract the characteristic recovery times. We use a numerical time step of ∆t = 0.0005 and a fourth order Runge–Kutta. Numerical parameters are Λ = π, Γ<sup>a</sup> = Γ<sup>c</sup> = 0.5, K = 1, τeq = 0.3, dimension d = 2 and #momenta N<sup>k</sup> = 1000.

fluence dependence. The subdominant order, in contrast, recovers fluence independently as can be seen in the fitted recovery time c), in agreement with the experiment.

This can be explained intuitively in the following: The pump suppresses the CDW order and places it in the disordered state ϕ¯ = 0. While the free energy recovers quickly within τeq, the system stays trapped in the metastable minimum due to the nucleation bottleneck see Fig. [S17](#page-16-1) a). We see that as a function of the instantaneous ra(t), the activation barrier to nucleating domain and the size of the critical nucleating domain decrease as the system relaxes towards <sup>r</sup>a(<sup>t</sup> → ∞), see Fig. [S17](#page-16-1) b). Assuming a critical <sup>r</sup>nuc ≡ <sup>r</sup>a(τrec) at which <sup>Γ</sup>nuc is large enough to be seen in experiments, we ask, how long does it take to reach rnuc as a function of fluence? By reverting Eq. [$S4$](#page-9-1) we find for the recovery timescale

$$\tau_{\text{rec}} = \tau_{\text{eq}} \log(\Delta_T/\Delta r), \quad (\text{S22})$$

where <sup>∆</sup><sup>r</sup> <sup>=</sup> <sup>r</sup>nuc − <sup>r</sup>a(<sup>t</sup> → ∞). The logarithmic behavior already suggests that the recovery time-scale will not be as fluence dependent as for the dominant CDW, e.g. if we take <sup>τ</sup>eq ∼ 100fs, then as <sup>τ</sup>rec ∼ 1ps, the logarithm is in the regime where it is very insensitive to its argument, i.e. there should be limited fluence dependence. Note, however, that this order of magnitude discrepancy implies that <sup>∆</sup><sup>T</sup> /∆<sup>r</sup> ∼ <sup>10</sup><sup>4</sup> , i.e. <sup>r</sup>nuc ≈ <sup>r</sup>a(<sup>t</sup> → ∞). Metastability in even the equilibrium landscape lasts for over 1ps.

15

![](_page_15_Figure_1.jpeg)

FIG. S16. Photoexcitation dynamics of CDW mean fields and two-point correlation functions in the nucleation scenario. We use a numerical time step of ∆t = 0.0005 and a fourth order Runge–Kutta. Numerical parameters are Λ = π, Γ<sup>a</sup> = Γ<sup>c</sup> = 0.5, K = 1, τeq = 0.3, dimension d = 2 and #momenta N<sup>k</sup> = 1000.

By this order of magnitude difference between τeq and τrec, any influence of the initial pulse significantly dampens out and the order parameter recovers through nucleation and growth independent of the transient free energy and the initial strong fluctuations. Within this framework, the remarkable nature of the non-equilibrium measurement to resolve the details of the free-energy landscape becomes apparent.

#### <span id="page-15-0"></span>2. Calculating the Nucleation Barrier

Having outlined the traditional understanding of nucleation as a competition between domain wall formation penalized by the surface tension and the free energy benefit of ordering, we now seek to understand how the nucleation barrier changes as a function of evolving ra(t). For compactness we drop the a superscript in ϕ¯<sup>a</sup> .

Let us consider a bubble that is radially symmetric whose radial profile is given by ϕ¯(r). The boundary conditions for the bubble are ϕ¯(0) = ϕ¯ <sup>0</sup> and <sup>ϕ</sup>¯(<sup>r</sup> → ∞) = 0. We can write down the spatially dependent Ginzburg-Landau free energy

<span id="page-15-1"></span>
$$F[\bar{\phi}] = 2\pi \int_0^\infty dr r \left[ \frac{1}{2} \left( \frac{d\bar{\phi}}{dr} \right)^2 + f(\bar{\phi}) \right], \quad (\text{S23})$$

where the gradient term — penalizing spatial inhomogeneity — gives rise to the surface tension. It is possible to numerically solve for ϕ¯(r). However, in the presence of higher order non-linearities, computation of such profiles becomes stiff and thereby numerically difficult. A simpler route is to parametrize the bubble profile using a variational form. A simple form for the bubble radial profile is given by

$$\bar{\phi}(r) = c_a \left( 1 + \tanh \left( \frac{R-r}{w} \right) \right), \quad (\text{S24})$$

where c<sup>a</sup> = ϕ0/(1 + tanh(R/w)) ensures ϕ¯(0) = ϕ¯ <sup>0</sup> and <sup>ϕ</sup>¯(∞) = 0. Here <sup>R</sup> represents the bubble radius and <sup>w</sup> represents the bubble width, where the domain transitions from the ordered to the disordered phase, incurring the surface tension cost.

For each value of ra(t), we find the critical bubble size, find the nucleation barrier, and obtain the effective surface tension. We do this by computing the value of the width w which minimizes the free energy given by Eq. [$S23$](#page-15-1) for 16

each value of bubble radius R. Given these minimal free energies for each R, we maximize this minimal free energy as a function of R—by doing this we determine the critical bubble radius R<sup>c</sup> and thereby the nucleation barrier. We plot the results in Fig. [S17.](#page-16-1)

![](_page_16_Figure_2.jpeg)

<span id="page-16-1"></span>FIG. S17. (a) The bubble free energy, plotted for different values of ra. (b) The activation barrier ∆F(Rc) to nucleate a domain of radius Rc. The barrier height diverges at r c <sup>a</sup> = 5.8 (dashed grey line). Numerical parameters are u<sup>a</sup> = −25 and u ′ <sup>a</sup> = 20, but we expect this phenomenology to be generic.

## <span id="page-16-0"></span>3. Analytical constraint of decoupled TDGL model

From the analysis above, we notice that there should be a threshold of nucleation, above which the nucleation picture stands and the a-CDW recovers at a constant rate. Here we extend our TDGL modelling into small fluence regime. We derive the exact percentage of order parameter suppression needed to reach the threshold. and show that our experimental parameters lies in the same regime.

Consider again the decoupled Ginzburg-Landau ϕ 6 free energy:

$$f = \frac{1}{2}r_a|\bar{\phi}^a|^2 + \frac{1}{4}u_a|\bar{\phi}^a|^4 + \frac{u'_a}{6}|\bar{\phi}^a|^6 \quad (\text{S25})$$

For a first-order transition (u<sup>a</sup> < 0, u ′ <sup>a</sup> <sup>&</sup>gt; <sup>0</sup>), the positions of the energy barrier (ϕ¯<sup>a</sup> barrier) and the ordered minimum (ϕ¯<sup>a</sup> 0 ) are analytically linked. Their ratio is given by the roots of the potential gradient:

$$\left(\frac{\bar{\phi}_{\text{barrier}}^a}{\bar{\phi}_0^a}\right)^2 = \frac{|u_a| - \sqrt{u_a^2 - 4r_a u_a'}}{|u_a| + \sqrt{u_a^2 - 4r_a u_a'}} \quad (\text{S26})$$

To push the barrier as far outward as possible, the system must approach the coexistence limit (T = T<sup>c</sup>2), where the disordered and ordered states have equal free energy (4rau ′ <sup>a</sup> = 4 u 2 a ). Substituting this into the ratio yields a strict mathematical upper bound for the barrier position:

$$\bar{\phi}_{\text{barrier}}^a \leq \frac{1}{\sqrt{3}}\bar{\phi}_0^a \approx 0.577\bar{\phi}_0^a \quad (\text{S27})$$

This fundamental limit dictates that the system must melt by at least ∼ 42% to cross the energy barrier and become trapped in the disordered state (ϕ¯<sup>a</sup> ≈ <sup>0</sup>) as shown in our simulation in Fig. [S18](#page-17-1)

As shown in our extended low-fluence simulations (Fig. [S18$](#page-17-1), if the system fails to cross this ∼ 58% threshold, the recovery is governed by purely deterministic sliding relaxation down the steep potential well. This relaxation is extremely fast. We note that the threshold behavior is certainly expected. If we consider the limiting case where the excitation fluence is close to 0, the recovery rate should also be infinitesimally small. Thus, when the system is excited below the nucleation energy barrier, the recovery of a-CDW is much faster. However, this regime is not achievable in the experiment given the finite signal-noise ratio and temporal resolution of trARPES instruments.

17

![](_page_17_Figure_1.jpeg)

<span id="page-17-1"></span>FIG. S18. Simulated recovery dynamics demonstrating the trapping threshold. (Left) For weak quenches (∆<sup>T</sup> < 1.0), the a-CDW melts shallowly and relaxes extremely rapidly. For deep quenches (∆<sup>T</sup> ≥ 1.0), the system crosses the thermodynamic barrier (ϕ¯<sup>a</sup> ≲ 0.58ϕ¯<sup>a</sup> <sup>0</sup>), becomes trapped, and recovers via slow nucleation. (Right) The extracted recovery times confirm that failing to cross the barrier results in a relaxation timescale that is drastically faster than the second-order c-CDW, contradicting the slow experimental observation.

Now we take a closer look on the regime of excitation in our observed a-CDW dynamics. First and foremost, we notice that from both spectral weight change and EDC shifts in Fig. [S5,](#page-6-1) the light-induced quenching in a-CDW is close to saturation even low fluence. This indicates that in the fluence regime we studied, a-CDW is always excited above the nucleation barrier and close to full quenching. In addition, in the previous section, we showed that the gap size fitted from transient EDCs can be severely underestimated. For systems with even smaller gap, such as a-CDW, the underestimation is more pronounced. As we have also shown previously from conduction band EDC analysis, the suppression in c-CDW is already above 40% at intermediate fluence. Given the much smaller gap size, the a-CDW is expected to be suppressed more than c-CDW. Indeed, this is what we observed in our experiment. In Fig. [S5,](#page-6-1) we can clearly observe from EDC fitting that the a-CDW is more susceptible to optical excitation. All these factors indicate that the fluence regime we study is beyond the nucleation threshold

### <span id="page-17-0"></span>III. Selection and extraction of data from previous literature

In Fig. 4d of the main text, we compared the recovery dynamics upon light excitation in several representative firstorder and second-order CDW transitions reported previously. The first-order CDW transition systems we refer to are Indium nanowires on silicon substrate[<sup>24</sup>](#page-19-13), commensurate CDW transition in 1T-TaS<sup>2</sup> [<sup>25</sup>](#page-19-14), and IrTe<sup>2</sup> [<sup>26</sup>](#page-19-15). The secondorder transition systems we refer to are TiSe<sup>2</sup> [<sup>26</sup>](#page-19-15), LaTe<sup>3</sup> [<sup>11</sup>](#page-19-1), and K0.3MoO<sup>3</sup> [<sup>27</sup>](#page-19-16). For a meaningful comparison in CDW amplitude recovery[<sup>11</sup>](#page-19-1), we only included previous studies involving transient reflectivity measurements or trARPES measurements in a fluence range similar to that of this work.

Except for LaTe3, whose recovery time versus fluence curve was plotted in the main text[<sup>11</sup>](#page-19-1), All other recovery time data are extracted by fitting either trARPES or transient reflectivity data following the same fitting procedures introduced above (Eq. [$S2$](#page-9-2)).

The recovery time extracted from literature as a function of excitation fluence is plotted in Fig. 4d, alongside the

18

results from both a-CDW and c-CDW in ErTe<sup>3</sup> measured in this work. The data are color-coded so that first-order transitions are plotted in red colors and second-order transitions in blue colors. Though the collected data set is not meant to be exhaustive, it demonstrates agreement with the conclusion of our Ginzburg-Landau model: Upon photoexcitation, the recovery of the order parameter amplitude in a second-order phase transition slows down when a higher fluence is applied, while the recovery of a first-order transition is much less sensitive to fluence. We also note that the recovery timescales of first-order transitions cited here are consistent up to less than one order of magnitude, which can be possibly the characteristic timescale of the nucleation-like growth. This comparative study, thus, suggests the generality of our combined theoretical and experimental approach to classify phase transitions and verify the driving mechanisms in time domain.

#### <span id="page-18-0"></span>IV. Nomenclature of CDWs in rare-earth tritellurides

In the RTe<sup>3</sup> family of materials, the CDW states can be tuned with external knobs such as photoexcitations and strain. These resultant CDW states are also aligned with either a or c axes of the lattice. Here we clarify their difference and our nomenclature.

The c-CDW and a-CDW in this work always refer to the CDW states in unstrained RTe<sup>3</sup> without external perturbations or excitations, meaning a/c ≥ <sup>0</sup>.997. The transition temperatures of <sup>c</sup>-CDW and <sup>a</sup>-CDW in this case are referred to as T<sup>c</sup><sup>1</sup> and T<sup>c</sup>2, respectively. In this case, c-CDW is the dominant order while a-CDW is the subdominant order, thus we can also refer to these as dominant c-CDW and secondary a-CDW.

Under a large enough strain, the dominant order aligns with the a axis of the crystalline lattice[18](#page-19-6)[,19](#page-19-7). In this case, the CDW along a-axis behaves more similarly to the original c-CDW rotated by 90◦ rather than the equilibrium a-CDW that occurs below T<sup>c</sup>2. At lower temperatures, a subdominant CDW emerges at a lower temperature along c axis. We thus refer to these strained CDW states as dominant a-CDW and subdominant c-CDW, emerging at transition temperatures T<sup>c</sup><sup>1</sup> ′ and T<sup>c</sup><sup>2</sup> ′ , respectively. These states are not relevant in this study and are included here for clarity and completeness.

In previous ultrafast electron diffraction studies[12](#page-19-17)[,13,](#page-19-10)[28](#page-19-18), a light-induced CDW is observed along a-axis in a photoexcited pure c-CDW state. This light-induced CDW is not a long-range CDW order like any of the CDWs mentioned above. Instead, it is a populated soft phonon state similar to the state around T<sup>c</sup><sup>1</sup> (see Fig. 1b). We refer to this short-range CDW as a˜-CDW.

# <span id="page-18-1"></span>V. SUPPLEMENTARY REFERENCES

- <span id="page-18-2"></span>[1] B. Lv, T. Qian, and H. Ding, Angle-resolved photoemission spectroscopy and its application to topological materials, [Nature Reviews Physics](https://doi.org/10.1038/s42254-019-0088-5) 1, 609 (2019). [2] L. Rettig, R. Cortés, J.-H. Chu, I. R. Fisher, F. Schmitt, R. G. Moore, Z.-X. Shen, P. S. Kirchmann, M. Wolf, and
- <span id="page-18-4"></span><span id="page-18-3"></span>U. Bovensiepen, Persistent order due to transiently enhanced nesting in an electronically excited charge density wave, [Nature Communications](https://doi.org/10.1038/ncomms10459) 7, 10459 (2016). [3] A. Zong, P. E. Dolgirev, A. Kogar, E. Ergeçen, M. B. Yilmaz, Y.-Q. Bie, T. Rohwer, I.-C. Tung, J. Straquadine, X. Wang,
- Y. Yang, X. Shen, R. Li, J. Yang, S. Park, M. C. Hoffmann, B. K. Ofori-Okai, M. E. Kozina, H. Wen, X. Wang, I. R. Fisher, P. Jarillo-Herrero, and N. Gedik, Dynamical Slowing-Down in an Ultrafast Photoinduced Phase Transition, [Physical](https://doi.org/10.1103/PhysRevLett.123.097601) Review Letters 123[, 097601 $2019$.](https://doi.org/10.1103/PhysRevLett.123.097601) [4] Y. Zhong, T. Suzuki, H. Liu, K. Liu, Z. Nie, Y. Shi, S. Meng, B. Lv, H. Ding, T. Kanai, J. Itatani, S. Shin, and
- K. Okazaki, Unveiling van Hove singularity modulation and fluctuated charge order in kagome superconductor CsV3Sb5, [Physical Review Research](https://doi.org/10.1103/PhysRevResearch.6.043328) 6, 043328 (2024). [5] Dynamics of electronic states in the insulating intermediate surface phase of 1T-TaS2, [Physical Review B](https://doi.org/10.1103/PhysRevB.108.155145) 108, 2 (2023). [6] C. Monney, M. Puppin, C. W. Nicholson, M. Hoesch, R. T. Chapman, E. Springate, H. Berger, A. Magrez, C. Cacho,
- R. Ernstorfer, and M. Wolf, Revealing the role of electrons and phonons in the ultrafast recovery of charge density wave correlations in 1T-TiSe2, [Physical Review B](https://doi.org/10.1103/PhysRevB.94.165165) 94, 165165 (2016), [1609.08993.](https://arxiv.org/abs/1609.08993) [7] S. Mathias, S. Eich, J. Urbancic, S. Michael, A. V. Carr, S. Emmerich, A. Stange, T. Popmintchev, T. Rohwer, M. Wiesenmayer, A. Ruffing, S. Jakobs, S. Hellmann, P. Matyba, C. Chen, L. Kipp, M. Bauer, H. C. Kapteyn, H. C. Schneider,
- K. Rossnagel, M. M. Murnane, and M. Aeschlimann, Self-amplified photo-induced gap quenching in a correlated electron material, [Nature Communications](https://doi.org/10.1038/ncomms12902) 7, 1 (2016). [8] A. Crepaldi, M. Puppin, D. Gosálbez-Martínez, L. Moreschini, F. Cilento, H. Berger, O. V. Yazyev, M. Chergui, and
- M. Grioni, Optically induced changes in the band structure of the Weyl charge-density-wave compound (TaSe4)2I, [Journal](https://doi.org/10.1088/2515-7639/ac9647) [of Physics: Materials](https://doi.org/10.1088/2515-7639/ac9647) 5, 044006 (2022). [9] S. Duan, Y. Cheng, W. Xia, Y. Yang, C. Xu, F. Qi, C. Huang, T. Tang, Y. Guo, W. Luo, D. Qian, D. Xiang, J. Zhang, and W. Zhang, Optical manipulation of electronic dimensionality in a quantum material, Nature 595[, 239 $2021$.](https://doi.org/10.1038/s41586-021-03643-8)
19

- <span id="page-19-1"></span><span id="page-19-0"></span>[10] F. Boschini, M. Zonno, and A. Damascelli, Time-resolved ARPES studies of quantum materials, [Reviews of Modern Physics](https://doi.org/10.1103/RevModPhys.96.015003) 96[, 15003 $2024$.](https://doi.org/10.1103/RevModPhys.96.015003) [11] A. Zong, A. Kogar, Y.-Q. Bie, T. Rohwer, C. Lee, E. Baldini, E. Ergeçen, M. B. Yilmaz, B. Freelon, E. J. Sie, H. Zhou,
- J. Straquadine, P. Walmsley, P. E. Dolgirev, A. V. Rozhkov, I. R. Fisher, P. Jarillo-Herrero, B. V. Fine, and N. Gedik, Evidence for topological defects in a photoinduced phase transition, [Nature Physics](https://doi.org/10.1038/s41567-018-0311-9) 15, 27 (2019). [12] A. Kogar, A. Zong, P. E. Dolgirev, X. Shen, J. Straquadine, Y.-Q. Bie, X. Wang, T. Rohwer, I.-C. Tung, Y. Yang, R. Li,
- <span id="page-19-17"></span><span id="page-19-10"></span>J. Yang, S. Weathersby, S. Park, M. E. Kozina, E. J. Sie, H. Wen, P. Jarillo-Herrero, I. R. Fisher, X. Wang, and N. Gedik, Light-induced charge density wave in LaTe3, [Nature Physics](https://doi.org/10.1038/s41567-019-0705-3) 16, 159 (2020). [13] A. Zong, P. E. Dolgirev, A. Kogar, Y. Su, X. Shen, J. A. W. Straquadine, X. Wang, D. Luo, M. E. Kozina, A. H. Reid,
- <span id="page-19-3"></span><span id="page-19-2"></span>R. Li, J. Yang, S. P. Weathersby, S. Park, E. J. Sie, P. Jarillo-Herrero, I. R. Fisher, X. Wang, E. Demler, and N. Gedik, Role of Equilibrium Fluctuations in Light-Induced Order, [Physical Review Letters](https://doi.org/10.1103/PhysRevLett.127.227401) 127, 227401 (2021). [14] A. Zong, A. Kogar, and N. Gedik, Phase competition and light-induced ordering in charge density waves, in [Ultrafast](https://doi.org/10.1117/12.2577936) [Phenomena and Nanophotonics XXV](https://doi.org/10.1117/12.2577936) , Vol. 11684 (SPIE, 2021) p. 1168412. [15] R. G. Moore, V. Brouet, R. He, D. H. Lu, N. Ru, J.-H. Chu, I. R. Fisher, and Z.-X. Shen, Fermi surface evolution across multiple charge density wave transitions in ErTe3, [Physical Review B](https://doi.org/10.1103/PhysRevB.81.073102) 81, 073102 (2010). [16] J. Maklar, Y. W. Windsor, C. W. Nicholson, M. Puppin, P. Walmsley, V. Esposito, M. Porer, J. Rittmann, D. Leuenberger,
  - M. Kubli, M. Savoini, E. Abreu, S. L. Johnson, P. Beaud, G. Ingold, U. Staub, I. R. Fisher, R. Ernstorfer, M. Wolf, and
- <span id="page-19-9"></span><span id="page-19-8"></span><span id="page-19-7"></span><span id="page-19-6"></span><span id="page-19-5"></span><span id="page-19-4"></span>L. Rettig, Nonequilibrium charge-density-wave order beyond the thermal limit, [Nature Communications](https://doi.org/10.1038/s41467-021-22778-w) 12, 2499 (2021). [17] S. A. Kivelson, A. Pandey, A. G. Singh, A. Kapitulnik, and I. R. Fisher, Emergent **Z**<sup>2</sup> symmetry near a charge density wave multicritical point, [Physical Review B](https://doi.org/10.1103/PhysRevB.108.205141) 108, 205141 (2023). [18] A. G. Singh, M. D. Bachmann, J. J. Sanchez, A. Pandey, A. Kapitulnik, J. W. Kim, P. J. Ryan, S. A. Kivelson, and I. R. Fisher, Emergent tetragonality in a fundamentally orthorhombic material, Science Advances 10[, eadk3321 $2024$.](https://doi.org/10.1126/sciadv.adk3321) [19] J. A. W. Straquadine, M. S. Ikeda, and I. R. Fisher, Evidence for Realignment of the Charge Density Wave State in ErTe<sup>3</sup> and TmTe3, [Physical Review X](https://doi.org/10.1103/PhysRevX.12.021046) 12, 021046 (2022). [20] A. Fang, J. A. W. Straquadine, I. R. Fisher, S. A. Kivelson, and A. Kapitulnik, Disorder-induced suppression of charge density wave order: STM study of Pd-intercalated ErTe3, [Physical Review B](https://doi.org/10.1103/PhysRevB.100.235446) 100, 235446 (2019). [21] P. C. Hohenberg and B. I. Halperin, Theory of dynamic critical phenomena, [Reviews of Modern Physics](https://doi.org/10.1103/RevModPhys.49.435) 49, 435 (1977). [22] P. E. Dolgirev, M. H. Michael, A. Zong, N. Gedik, and E. Demler, Self-similar dynamics of order parameter fluctuations in pump-probe experiments, [Physical Review B](https://doi.org/10.1103/PhysRevB.101.174306) 101, 174306 (2020). [23] P. D. Grigoriev, A. A. Sinchenko, P. A. Vorobyev, A. Hadj-Azzem, P. Lejay, A. Bosak, and P. Monceau, Interplay between band crossing and charge density wave instabilities, [Physical Review B](https://doi.org/10.1103/PhysRevB.100.081109) 100, 81109 (2019). [24] J. G. Horstmann, H. Böckmann, B. Wit, F. Kurtz, G. Storeck, and C. Ropers, Coherent control of a surface structural phase transition, Nature 583[, 232 $2020$.](https://doi.org/10.1038/s41586-020-2440-4) [25] A. Mann, E. Baldini, A. Odeh, A. Magrez, H. Berger, and F. Carbone, Probing the coupling between a doublon excitation and the charge-density wave in TaS<sup>2</sup> by ultrafast optical spectroscopy, [Physical Review B](https://doi.org/10.1103/PhysRevB.94.115122) 94, 115122 (2016). [26] S.-i. Ideta, D. Zhang, A. G. Dijkstra, S. Artyukhin, S. Keskin, R. Cingolani, T. Shimojima, K. Ishizaka, H. Ishii, K. Kudo,
- <span id="page-19-18"></span><span id="page-19-16"></span><span id="page-19-15"></span><span id="page-19-14"></span><span id="page-19-13"></span><span id="page-19-12"></span><span id="page-19-11"></span>M. Nohara, and R. J. D. Miller, Ultrafast dissolution and creation of bonds in IrTe<sup>2</sup> induced by photodoping, [Science](https://doi.org/10.1126/sciadv.aar3867) Advances 4[, eaar3867 $2018$.](https://doi.org/10.1126/sciadv.aar3867) [27] A. Tomeljak, H. Schäfer, D. Städter, M. Beyer, K. Biljakovic, and J. Demsar, Dynamics of Photoinduced Charge-Density-Wave to Metal Phase Transition in K0.3MoO3, [Physical Review Letters](https://doi.org/10.1103/PhysRevLett.102.066404) 102, 066404 (2009). [28] F. Zhou, J. Williams, S. Sun, C. D. Malliakas, M. G. Kanatzidis, A. F. Kemper, and C. Y. Ruan, Nonequilibrium dynamics of spontaneous symmetry breaking into a hidden state of charge-density wave, [Nature Communications](https://doi.org/10.1038/s41467-020-20834-5) 12, 1 (2021).