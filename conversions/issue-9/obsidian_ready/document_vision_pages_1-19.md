nature physics

**Supplementary information**
https://doi.org/10.1038/s41567-026-03382-5

# Time-domain identification of distinct mechanisms for competing charge density waves in a rare-earth tritelluride

In the format provided by the authors and unedited

---

1

# CONTENTS

| | |
|---|---|
| I. Details of data analysis in trARPES measurement | 1 |
| $\quad$ A. Matrix element effect in trARPES measurement | 1 |
| $\quad$ B. Observation of charge density wave gap closure | 2 |
| $\quad\quad$ 1. Energy distribution curve (EDC) analysis | 2 |
| $\quad\quad$ 2. Quantitative understanding of EDCs in trARPES | 4 |
| $\quad$ C. Effect of energy integration window | 5 |
| $\quad$ D. Fitting of delay time scan data | 6 |
| II. Time-dependent Ginzburg-Landau theory and theory of phase nucleation | 9 |
| $\quad$ A. The scenario of coupled order parameters | 10 |
| $\quad\quad$ 1. Results | 11 |
| $\quad$ B. Nucleation scenario | 12 |
| $\quad\quad$ 1. Results | 13 |
| $\quad\quad$ 2. Calculating the Nucleation Barrier | 15 |
| $\quad\quad$ 3. Analytical constraint of decoupled TDGL model | 16 |
| III. Selection and extraction of data from previous literature | 17 |
| IV. Nomenclature of CDWs in rare-earth tritellurides | 18 |
| V. Supplementary references | 18 |

### I. Details of data analysis in trARPES measurement

#### A. Matrix element effect in trARPES measurement

The photoemission intensity measured in ARPES experiments can be expressed by the following formula$^1$:

$$I(\mathbf{k}, E) = I_0(\mathbf{k}, E, \mathbf{A})A(\mathbf{k}, E)f(E, T) \eqno{(\text{S}1)}$$

where $A(\mathbf{k}, E)$ is the one-electron spectral function that encodes the band structure and correlation effects, and $f(E, T)$ is the Fermi-Dirac distribution, where $T$ is the temperature. The first term on the right-hand side $I_0(\mathbf{k}, E, \mathbf{A})$ is proportional to $\sum_{f,i} |M_{f,i}^{\mathbf{k}}|^2$, where $M_{f,i}^{\mathbf{k}} = \langle \phi_f^{\mathbf{k}} | \mathbf{A} \cdot \mathbf{p} | \phi_i^{\mathbf{k}} \rangle$ is the photoemission matrix element that describes the transition from the initial state $\phi_i^{\mathbf{k}}$ to the final state $\phi_f^{\mathbf{k}}$. $\mathbf{p}$ and $\mathbf{A}$ are respectively the electron momentum operator and the vector potential of incident electromagnetic wave. The matrix element thus is dependent on the polarization of the incident XUV beam that emits the photoelectron. Different matrix elements would lead to different spectral weight distributions on the photoemission spectra. However, matrix elements do not carry intrinsic information about the CDW order parameter dynamics. We thus need to exclude the possibility of artifacts created by the matrix element effect.

For this purpose, we repeated the same set of experiments with incident XUV photon polarization rotated by $90^\circ$. The data presented in the main text were all collected with linear polarization perpendicular to the sample surface (LV). Here, we compare the results with the spectra and time-resolved scans measured with linear polarization parallel to the sample surface (LH).

Comparing the spectrum acquired with different polarization (Fig. S1), we noticed that the shadow band near $c$-CDW gap does not have spectral weight with LV polarization. Similarly, the shadow band near $a$-CDW gap is not present when measured with LH polarization. Meanwhile, the measured CDW gap size for both CDWs is consistent across different probe polarizations. Thus the matrix element does not create confusion in the description of the order parameter.

We further investigate the matrix element effect on the pump-probe scans under different excitation fluences. From Fig. S2, comparing the time-evolution of the in-gap intensity measured with different probe polarizations, the recovery dynamics of both $c$-CDW (a and c) and $a$-CDW (b and d) are consistent and thus the matrix element effect does not affect the determination of CDW dynamics from the spectral weight in the CDW gaps.

---

2

![ARPES spectra images](https://placeholder_for_image)

**FIG. S1. Comparison of ARPES spectrum with different incident photon polarization a-c** Fermi surface map (a) and energy-momentum dispersion cuts featuring $c$-CDW (b) and $a$-CDW (c) measured with photon polarization perpendicular to the sample surface (LV), reproduced from Fig.1 (d-f) **d-f** The same ARPES measurement performed with photon polarization parallel to the sample surface (LH). The same color scales are used for each pair of spectra for comparison. The same CDW gaps for both $a$-CDW and $c$-CDW are consistently measured with both photon polarization.

### B. Observation of charge density wave gap closure

#### 1. Energy distribution curve (EDC) analysis

In the main text, we used the spectral weight in the CDW gaps as **the major** measure of CDW suppression, as the increase of spectral weight in the CDW gaps is dominantly contributed by the closure of CDW gap. This method was commonly adopted by the trARPES community to bypass the intrinsically inferior energy resolution and signal-to-noise ratio (SNR) of trARPES compared to equilibrium-state ARPES. For this reason, previous trARPES studies on various CDW systems, including but not limited to $R\text{Te}_3$, $1\text{T-TiSe}_2$, $\text{CsV}_3\text{Sb}_5$, $(\text{TaSe}_4)_2\text{I}$, and $1\text{T-TaS}_2$, have used the in-gap spectral weight as a measure of CDW order parameter amplitude$^{2-10}$. Here, we directly prove that the CDW gap is indeed suppressed upon photoexcitation by comparing the energy distribution curves (EDCs) after photoexcitation. Furthermore, we provide further reasoning and analysis on how to appropriately understand the CDW gap values extracted from EDCs

In our trARPES measurements, we typically have two different strategies of data-taking for different purposes. The first strategy is *snapshots*, exemplified as data in Fig. 2, where we park the pump-probe delay at a fixed value and integrate heavily on the electron count. This strategy is meant to optimize the signal-to-noise ratio (SNR) in energy and momentum resolution. The second strategy is *timescans*, exemplified as data in Fig. 3, where we repeatedly scan the pump-probe delay and record data in a stroboscopic manner. This strategy is meant to optimize the SNR in temporal evolution. Due to the finite lifetime of the sample surface, it is not realistic to measure fine-step time scans with multiple pump fluences while at the same time having optimized SNR in energy and momentum on the same sample. Here, we demonstrate EDC analysis on both the snapshot data and the timescan data binned with $250\text{ fs}$ windows.

---

3

(Image containing four plots: (a) and (b) for LV polarization, (c) and (d) for LH polarization. The y-axes represent normalized in-gap intensity for $c\text{-CDW}$ and $a\text{-CDW}$ respectively, and the x-axes represent Delay time in ps. Various curves are shown for pump fluences ranging from $0.07\text{ mJ/cm}^2$ to $0.70\text{ mJ/cm}^2$.)

FIG. S2. **Comparison of CDW recovery dynamics with different incident photon polarization.** **a,b** Time evolution of normalized in-gap intensity of $c\text{-CDW}$ (a) and $a\text{-CDW}$ (b) measured with LV polarization, reproduced from Fig. 3 (c.d) **c,d** Same measurement performed with probe photons with LH polarization. Same recovery dynamics of CDWs are observed with different incident probe photon polarizations, thus excluding the possibility of artifacts caused by the matrix element effect.

In Fig. S3, we demonstrate the EDC analysis on the snapshots presented in Fig. 2 of the main text. From the raw EDC curves, we can clearly observe the rightward shifts of leading edges after timezero. This is a typical signature of CDW suppression. While in Fig. S4, we demonstrate the timescan counter part of the same analysis. In both sets of plots, we overlapped the data points with the fitting curves of corresponding pump fluences in Fig. $3\text{c}$ and $\text{d}$, with only vertical scaling due to the different units. We can clearly see that the temporal evolution of leading edges extracted from EDCs in both sets of data agrees well with the temporal evolution of spectral weight in the CDW gaps. This is a strong evidence showcasing the consistency between the in-gap spectral weight dynamics and CDW gap dynamics.

Having established the equivalence between gap and in-gap spectral weight dynamics, we further analyze the fluence dependence of the EDCs. The EDCs at a delay time with maximum CDW suppression signal ($0.5\text{ ps}$) at $c\text{-}$ and $a\text{-CDW}$ gap positions in reciprocal space are plotted in Fig. S5 **a** and **b**. Compared to the spectra in equilibrium (grey curves), the leading edges of the EDCs demonstrate a clear shift towards the Fermi level. This shift in energy scales with fluence, signifying a typical suppression of CDW amplitude upon photoexcitation.

We note that in all analysis demonstrated above, no other signals of in-gap states are observed from EDCs. Thus, the in-gap spectral weight increase observed in our trARPES measurement is dominantly contributed by the CDW suppression, justifying the in-gap spectral weight as a proper measure of the CDW amplitude dynamics. It is also noteworthy that the EDC analysis for both CDW gaps under different fluences indicates that $c\text{-CDW}$ has not reached the full CDW suppression within our fluence range while $a\text{-CDW}$ is close to full suppression, given the saturation behaviour under different fluences, as shown in **c-d**. This is also consistent with previous ultrafast measurements on similar materials$^{11-14}$.

---

4

![Figure S3: Four panels (a-d) showing EDCs and leading edge analysis for c-CDW and a-CDW.](https://example.com/image.png)

**FIG. S3. EDCs analysis of snapshot data.** **a,b** EDCs at different timesteps for $c\text{-CDW}$ (**a**) and $a\text{-CDW}$ (**c**) extracted from the same dataset as demonstrated in Fig. 2 in the main text. **c-d** Leading edge of $c\text{-CDW}$ (**c**) and $a\text{-CDW}$ (**d**) bands extracted from EDCs of each delay time, overlapped with the fitting curve for $0.42\text{ mJ/cm}^2$ data from Fig. 3, with only vertical scaling. The error bars represent the energy resolution of our trARPES instrument.

***

### 2. Quantitative understanding of EDCs in trARPES

We would like to note that though extracting gap dynamics from EDCs can be qualitatively useful and consistent with in-gap spectral weight analysis, one needs to be extra cautious before citing the extracted gap value as the exact gap size. Here we provide a systematic study on how the shifts in EDC leading edge can underestimate the actually gap size change in trARPES measurements

We start from revisiting the gap closure dynamics of $c\text{-CDW}$. Besides in-gap spectral weight and transient EDCs of valence band, one can extract the CDW gap dynamics, in a limited time interval, also from the conduction band bottom above the CDW gap.

In Fig. S6, we demonstrate the transient EDCs for $c\text{-CDW}$ gap plotted in log-scale. we note that this analysis is only practical for $c\text{-CDW}$, where the gap is large enough and is thus de-convolved from the thermal broadening near the Fermi level. For $a\text{-CDW}$, due to particle-hole asymmetry$^{15}$ and small gap amplitude, it is not practical to identify the transient gap closure process from transient EDC.

We can clearly observe the closure of CDW gap. After photoexcitation, the leading edge of the conduction band is barely distinguishable. A careful tracing of the conduction band peak position gives an estimation of 40% of gap closure, as indicated by the black triangular labels in Fig. S6. This is consistent with the observation in previous trARPES studies on $R\text{Te}_3{}^{16}$. We note that compared to the values extracted from valence band EDC fitting presented in Fig. S5, the percentage of change extracted from conduction band shifting is much larger, indicating a severe underestimation in valence band EDC fitting.

To further demonstrate the underestimation effect of transient valence EDC analysis, we perform a simulation of ARPES spectra for electronic bands gapped by long range orders. From the simulation, we find that the number extracted from the leading edge in EDC, is usually a severe underestimation. We note that part of this underestimation

---

5

![EDCs analysis plots showing c-CDW and a-CDW band leading edges across different fluences and delay times.](https://example.com/image.png)

**FIG. S4. EDCs analysis of *timescan* data.** **a-c (d-f)** Leading edge of $c$-CDW ($a$-CDW) band extracted from EDCs acquired from binning the continuous time scans with a 250 fs step size, at 0.14, 0.42, 0.70 $\text{mJ/cm}^2$, respectively. All data are overlapped with corresponding fitting curves from Fig. 3 in the main text, with only vertical scaling. The error bars represent the energy resolution of our trARPES instrument.

is a result of Fermi-Dirac function. Unlike equilibrium-state ARPES measurement, where Fermi-Dirac function can be removed in order to extract precise gap size, transient electronic states measured in trARPES do not strictly follow Fermi-Dirac distribution before thermalization and thus it would not be fully justified to extract the precise gap size in trARPES by removing the Fermi-Dirac distribution at a very short delay time after the time zero.

As demonstrated in Fig. S7, we first generate the single-electron spectral function for an electronic system gapped by a long range order from the eigenvalues of Fröhlich Hamiltonian. As an example, we compare the two cases where the CDW gap $\Delta = 100 \text{ meV}$ **(a)** and $200 \text{ meV}$ **(b)** respectively. In order to simulate real ARPES spectrum, we multiply the spectral function by the Fermi-Dirac function **(c,d)** convoluted with the instrument resolution, and superposed with a background noise function **(e,f)**. By making cut along the window labeled in Fig. S7e, we acquired the EDCs for $\Delta = 100 \text{ meV}$ and $200 \text{ meV}$ case respectively. By either fitting the EDCs or fitting the peak position after the taking the first derivative with respect to energy, we extracted a gap difference between 10 meV and 40 meV, which are 2.5 to 10 times smaller than the real gap difference of 100 meV. We thus conclude that EDC analysis returns a severely underestimated gap size, possibly due to the existence of Fermi-Dirac function. However, the qualitative change and recovery dynamics, which we previously showed to be consistent with the in-gap spectral weight, is still meaningful and trustworthy.

### C. Effect of energy integration window

The data we presented in Fig. 3 of the main text is acquired by integrating over a window of 50 meV energy window centered at Fermi energy for the best signal-to-noise ratio. In order to exclude the possibility of contributions from other parts of the electronic structure, we hereby show the robustness against the selection of an integration window.

Comparing the results acquired with a 50 meV integration window to the ones acquired with a 20 meV integration window (Fig. S8), we clearly observe that the time traces, after normalization from 0 to 1, agree almost perfectly. We can thus exclude the possibility of any artifacts created by the selection of the integration window, solidifying the analysis and conclusions presented in the main text.

---

6

[Images: Four panels (a, b, c, d) showing Energy Distribution Curves (EDCs) and spectral weight changes as a function of pump fluence.]

**FIG. S5. Direct observation of CDW gaps closure through energy distribution curves (EDCs) a,b** EDCs 0.5 ps after photoexcitation of various fluences, plotted in log scale for better visualization. The EDCs were acquired by integrating spectral weights over a momentum window of $0.1 \text{ \AA}^{-1}$ centered at the $c\text{-CDW}$ **(a)** and $a\text{-CDW}$ **(b)** gap position. The EDCs without photoexcitation are shown in grey for reference. Inset: raw data of EDCs plotted in linear scale. **c-d** Change of In-gap spectral weight **(c)** acquired by integrating the electron counts over the ROI for $c\text{-CDW}$ and $a\text{-CDW}$ respectively, at the delay time when CDW quenching reaches maximum and leading edge position **(d)** extracted from the same snapshot scans as in **a** and **b**, showing consistency.

to further prove the validity of our choice of Region of interest (ROI), we comparatively study the CDW gap dynamics and conduction band carrier population dynamics with the time evolution of spectral weight on each constant energy contours from 0 to $0.4 \text{ eV}$.

Fig. S9 demonstrates the integrated spectral weight at the $c\text{-CDW}$ (left) and $a\text{-CDW}$ (right) gap momentum-space position across various binding energies. We can clearly observe that at high binding energy, the electron population decays at a significantly higher rate compared to the SW at the Fermi level, which represents the CDW dynamics. For $c\text{-CDW}$, the band occupation dynamics has slight effect around $100 \text{ meV}$, where the ROI start to touch the edge of conduction band$^{15}$. Above $200 \text{ meV}$, the spectral weight dynamics is dominated by electron population dynamics in the conduction bands. For $a\text{-CDW}$, due to the small gap, electron population dynamics in the conduction bands starts to dominate right above the Fermi level. In either case, we have proven that the SW evolution at the Fermi level, and thus in the CDW gaps, are vastly different from electron population evolution in conduction bands.

**D. Fitting of delay time scan data**

In order to quantitatively extract and compare the recovery dynamics of CDWs, we fit the time trace data in Fig. 3 to an exponential function that models relaxation dynamics multiplied by an error function that models the initial CDW quenching. The entire fitting function is convolved with a Gaussian function that models the temporal

---

7

![Intensity vs Energy plot showing four curves for delays 0, 0.2, 0.4, and 0.6 ps. The y-axis is Intensity (arb. u.) on a log scale, and the x-axis is $E - E_F$ (eV).](image_placeholder)

FIG. S6. **CDW gap dynamics through conduction band.** Energy distribution curves for c-CDW gap at various delay time with $0.42 \text{ mJ/cm}^2$ excitation. Same data as in Fig. S3 but plotted in log scale to highlight the conduction band bottom dynamics. The curves are offset by a constant for clarity.

![Six heatmaps (a-f) and one line plot (g) simulating ARPES spectra. Heatmaps show $A(k, E)$, $A(k, E)f(E)$, and $A(k, E)f(E)$ with noise for two different gap sizes $\Delta = 100 \text{ meV}$ and $\Delta = 200 \text{ meV}$. Plot g shows the Energy Distribution Curves (EDC).](image_placeholder)

FIG. S7. **Simulation of ARPES spectrum of gapped electronic system.** **a-b.** Single-electron spectral function $A(k, E)$ for a system gapped by long-range order. The gap sizes are respectively $100 \text{ meV}$ and $200 \text{ meV}$. **c-d.** Single-electron spectral function multiplied by Fermi-Dirac function. **e-f.** Spectra in **c-d** superposed with a noise function that simulates real ARPES data. **g.** Energy distribution curves cut from spectra in **e-f**, showing a leading edge shift much smaller than $100 \text{ meV}$.

---

8

(Images showing time-resolved photoemission intensity for c-CDW and a-CDW)

FIG. S8. **Comparison of time traces acquired from different energy integration windows a,b** In-gap photoemission intensities of $c\text{-CDW}$ **(a)** and $a\text{-CDW}$ **(b)** under $0.07\text{ mJ/cm}^2$ (light) and $0.70\text{ mJ/cm}^2$ (dark) fluences, acquired with a $50\text{ meV}$ integration window (hollow) and a $20\text{ meV}$ integration window (solid).

(Images showing spectral weight evolution at various energy contours for c-CDW and a-CDW)

FIG. S9. **Distinct behaviours of CDW gap dynamics and carrier population dynamics.** Time evolution of the spectral weight at the $c\text{-CDW}$ (left) and $a\text{-CDW}$ (right) gap momentum momentum-space position across various constant-energy contours. The clearly different dynamics at Fermi level ($E - E_F = 0\text{ meV}$) showcases the CDW order parameter dynamics as opposed to electron population dynamics.

---

9

resolution of the instrument. The fitting function takes the following general form$^3$:

$$\Delta f(t) = \left[ \frac{1}{2} \left( 1 + \text{Erf} \left( \frac{2\sqrt{\ln 2}(t - t_0)}{w} \right) \right) \cdot (I_\infty + I_0 e^{-(t-t_0)/\tau}) \right] * g(w_0, t). \eqno(\text{S2})$$

In this model, $w$ represents the intrinsic system response time due to photoexcitation, in our specific case, the Debye-Waller intensity suppression time. $I_0$ represents the maximum system response. $I_\infty$ denotes the value of $\Delta f$ at long time delays when the system reaches a quasi-equilibrium thermal state. $\tau$ is the characteristic relaxation time to the quasi-equilibrium. $t_0$ is associated with the relative arrival time of pump and probe pulses.

### II. Time-dependent Ginzburg-Landau theory and theory of phase nucleation

We begin by reviewing the putative equilibrium free energy landscape of $\text{ErTe}_3$. This material undergoes two phase transitions: A first into a unidirectional CDW at $T_{c1}$ (dominant order) and a second into a bidirectional CDW at $T_{c2}$ (subdominant order). The two CDW orders can each be represented by a complex scalar field $\Phi^c = \phi_1^c + i\phi_2^c$ and $\Phi^a = \phi_1^a + i\phi_2^a$, which encode both the amplitude and phase of the CDW modulation along the corresponding lattice directions.

To construct the free energy functional, we assume that it depends smoothly on the order parameters and their spatial variations. It generally consist of a “kinetic” term that penalizes spatial variations of the fields and a “potential” term $f[\Phi(\mathbf{r}, t)]$:

$$\mathcal{F}[\Phi(\mathbf{r}, t)] = \int d^d r \left[ \frac{K}{2} \left( |\nabla_r \Phi^a(\mathbf{r}, t)|^2 + |\nabla_r \Phi^c(\mathbf{r}, t)|^2 \right) + f[\Phi(\mathbf{r}, t)] \right] \eqno(\text{S3})$$

where we truncated the “kinetic” term at second order in spatial derivatives assuming that the order parameters vary smoothly on length scales large compared to the microscopic lattice spacing. For the “potential” term $f[\Phi(\mathbf{r}, t)]$ the conventional approach to studying phase transitions involves expanding in the order parameters, $\Phi^c$ and $\Phi^a$, while ensuring that this expansion respects the symmetries of the system. This approach assumes that the order parameter is small within the vicinity of the phase transition. Whereas this is generically true for second-order phase transitions, for a first-order one, however, the order parameter can undergo a discontinuous jump to a finite value, questioning the validity of the symmetry constrained expansion. Thus in the following we consider two distinct cases for the free energy potential $f[\Phi(\mathbf{r}, t)]$:

1. A coupled scenario (cf. Sec. II A), where the expansion of the order parameters assumes a symmetry between the a- and c-CDW. This leads to second-order phase transitions at $T_{c1}$ and $T_{c2}$.
2. A decoupled scenario (cf. Sec. II B), where the expansion is not subject to lattice symmetry constraints. This results in a second-order phase transition at $T_{c1}$ and a first-order phase transition at $T_{c2}$.

In both cases, we ensure that the $\text{U}(1)$ symmetry of the CDW order parameter remains intact by only including terms that are analytic in $|\Phi^\alpha(\mathbf{r}, t)|^2$.

To model the influence of the pump pulse, we assume that the incident light is primarily absorbed by electrons, leading to an instantaneous increase in the electronic temperature $T_e$. Following this initial jump, we assume, for simplicity, the electronic temperature to decay to equilibrium with a constant rate $\tau_{\text{eq}}$, i.e.

$$T_e(t) = T_{\text{ph}} + \theta(t)\Delta T_e^{-t/\tau_{\text{eq}}} . \eqno(\text{S4})$$

In our modeling, the electronic temperature modulates the second order Landau coefficient $r(t) = r_0(T_e(t) - \tilde{T}_c)/\tilde{T}_c$ (the “mass” term) of the free energy potential $f[\Phi(\mathbf{r}, t)]$. Here, $\tilde{T}_c$ denotes the temperature at which $r(t)$ changes sign; however, due to the inclusion of higher-order terms in the expansion, $\tilde{T}_c$ does not correspond to the actual phase transition temperature. The cooling down of the electronic subsystem increases the phononic temperature $T_{\text{ph}}$ but given the significantly larger heat capacity of the lattice, this effect is typically negligible. Accordingly, we assume the phononic temperature, $T_{\text{ph}}$, to remain constant throughout the time evolution. This modeling applies to both the coupled and decoupled scenarios. However, in the decoupled one we will have $r_0^a$ and $r_0^c$, instead of a single $r_0$.

---

10

### A. The scenario of coupled order parameters

The approximate symmetry of the CDW in $\text{ErTe}_3$ is $U(1) \times U(1) \times \mathbb{Z}_2$ as we are dealing with two orthogonal incommensurate $\text{CDWs}^{17}$. However, due to a slight orthorhombicity, the $\mathbb{Z}_2$ symmetry is explicitly broken (the space group is $Cmcm)^{18}$. Thus, at zero applied stress, the dominant order is, in reality, always along the $c$-axis. Up to fourth order, the free energy potential compatible with this symmetry is

$$f[\Phi] = \frac{r}{2} (|\Phi^a|^2 + |\Phi^c|^2) + \frac{b}{2} (|\Phi^a|^2 - |\Phi^c|^2) + \frac{\tilde{g}}{2} |\Phi^a|^2 |\Phi^c|^2 + \frac{u}{4} (|\Phi^a|^2 + |\Phi^c|^2)^2 . \eqno{(\text{S5})}$$

For $g = \tilde{g} + u > 0$ and $b > 0$ it leads to two second-order phase transitions at different temperatures $T \sim r$: First into a striped CDW along the $c$-axis and second into a checkerboard state. Neglecting fluctuations the critical temperatures for the two phase transitions are given by $T_{c1} = \tilde{T}_c(b/r_0 + 1)$ and $T_{c2} = \tilde{T}_{cb}(g+u)/(r_0(g-u)) + \tilde{T}_c$. In practice, the second phase is actually a bidirectional CDW as the strengths of the two CDWs are different. Furthermore, this model also lacks a first-order phase transition if the strain $\epsilon \sim b$ is tuned. These shortcomings can be cured by including higher order expansion terms, which was done in previous works$^{19,20}$. However, these higher-order terms do not change the nature of the temperature-driven second-order phase transitions.

In the absence of slow hydrodynamics modes, the dynamics close to a phase transition exhibit a clear separation of scales: All physical quantities fluctuate much faster than the order parameter, i.e., they merely constitute a stochastic force on the order parameter. Since the CDW order parameter is not conserved, the equation of motion describing the post-quench evolution is of model-A type$^{21}$:

$$\frac{\text{d}}{\text{dt}} \phi_{\alpha}(r, t) = -\Gamma_{\alpha} \frac{\delta \mathcal{F}}{\delta \phi_{\alpha}(r, t)} + \eta_{\alpha}(r, t) \eqno{(\text{S6})}$$

with a Gaussian noise $\langle \eta^{\alpha}(r, t) \rangle = 0$ and $\langle \eta^{\alpha}(r, t) \eta^{\beta}(r', t') \rangle = 2\Gamma_{\alpha} T_{\text{ph}} \delta(r - r') \delta(t - t') \delta_{\alpha\beta}$. In what follows, we simplify the stochastic nonlinear dynamics by employing the Gaussian approximation, which gives a non-perturbative framework to study post-quench evolution and competition of the two CDWs – this closely follows Refs.$^{13,22}$. To this end, we split the complex fields into real and imaginary parts: $\Phi^a = \phi_1^a + i\phi_2^a$ and $\Phi^c = \phi_1^c + i\phi_2^c$ and rewrite the free energy

$$\mathcal{F}[\phi] = \int \text{d}^d r \left[ \frac{K}{2} \sum_{\alpha} \left[ (\nabla \phi_{\alpha}^a(r, t))^2 + (\nabla \phi_{\alpha}^c(r, t))^2 \right] + f[\phi(r, t)] \right], \eqno{(\text{S7})}$$

$$f[\phi(r)] = \frac{r+b}{2} \sum_{\alpha} (\phi_{\alpha}^a)^2 + \frac{r-b}{2} \sum_{\alpha} (\phi_{\alpha}^c)^2 + \frac{g}{2} \sum_{\alpha, \beta} (\phi_{\alpha}^a)^2 (\phi_{\beta}^c)^2 + \frac{u}{4} \sum_{\alpha, \beta} ((\phi_{\alpha}^a)^2 (\phi_{\beta}^a)^2 + (\phi_{\alpha}^c)^2 (\phi_{\beta}^c)^2). \eqno{(\text{S8})}$$

We split each field into its mean field part $\bar{\phi}$ and fluctuations $\delta\phi$ around it:

$$\phi_{\alpha}^o(r, t) = \bar{\phi}_{\alpha}^o(t) + \delta\phi_{\alpha}^o(r, t) = \bar{\phi}^{o, \alpha}(t) + \frac{1}{\sqrt{N}} \sum_{k \neq 0} e^{ik \cdot r} \phi_{k}^{o, \alpha}(t) = \frac{1}{\sqrt{N}} \sum_{k} e^{ik \cdot r} \phi_{k}^{o, \alpha}(t), \quad \phi_{k=0}^{o, \alpha} = \sqrt{N} \bar{\phi}^{o, \alpha}. \eqno{(\text{S9})}$$

We introduce the equal-time correlation functions as

$$D_k^{o, \alpha\alpha}(t) = \langle \delta\phi_k^{o, \alpha}(t) \delta\phi_{-k}^{o, \alpha}(t) \rangle, \quad n_{\alpha\alpha}^o(t) = \frac{1}{N} \sum_k D_k^{o, \alpha\alpha}(t) \eqno{(\text{S10})}$$

where $o = a, c$, and all other correlators are assumed to be zero. Without loss of generality, we can set $\bar{\phi}^{\alpha \neq 1} = 0$, as by symmetry, always picking $\alpha = 1$ to be the direction of symmetry breaking/condensation. The mean-field equations of motion in the $1/\mathcal{N}$ expansion (here $\mathcal{N} = 4$) read

$$\frac{\text{d}}{\text{dt}} \bar{\phi}^o = -\Gamma_o r_{\text{eff}}^o \bar{\phi}^o \quad \text{with} \quad r_{\text{eff}}^a = r + b + u \left( (\bar{\phi}^a)^2 + \sum_{\beta} n_{\beta\beta}^a \right) + g \left( (\bar{\phi}^c)^2 + \sum_{\beta} n_{\beta\beta}^c \right) \eqno{(\text{S11})}$$

$$r_{\text{eff}}^c = r - b + u \left( (\bar{\phi}^c)^2 + \sum_{\beta} n_{\beta\beta}^c \right) + g \left( (\bar{\phi}^a)^2 + \sum_{\beta} n_{\beta\beta}^a \right) \eqno{(\text{S12})}$$

where $\bar{\phi}^o \equiv \bar{\phi}^{o, \alpha=1}$ and we used Wick's theorem which holds for the Gaussian approximation we employ. Within the same approximation, the dynamics of correlators is then governed by:

$$\frac{\text{d}}{\text{dt}} D_k^{o, \parallel}(t) = 2\Gamma_o T_{\text{ph}} - 2\Gamma_o [r_{\text{eff}}^o + K k^2 + 2u(\bar{\phi}^o)^2] D_k^{o, \parallel}(t) \eqno{(\text{S13})}$$

$$\frac{\text{d}}{\text{dt}} D_k^{o, \perp}(t) = 2\Gamma_o T_{\text{ph}} - 2\Gamma_o [r_{\text{eff}}^o + K k^2] D_k^{o, \perp}(t) \eqno{(\text{S14})}$$

---

11

Free Energy Landscapes for $\Delta_T = 1.5$

[Two plots showing free energy landscapes: the left plot is $|\Phi^c|$ Landscape for minimal $|\Phi^a|$ and the right plot is $|\Phi^a|$ Landscape for minimal $|\Phi^c|$. Both plots show several curves for different times $t = 0.0, 0.5, 1.0, 1.5, 2.0$]

FIG. S10. Free energy landscape for $T_{eq} = 0.4, \tilde{T}_c = 0.9, r_0 = 2, u = 1, \tilde{g} = -1, b = 0.23, \tau_{eq} = 0.3$

where $D_{\mathbf{k}}^{o, \parallel}(t) = D_{\mathbf{k}}^{o, 11}(t)$ and $D_{\mathbf{k}}^{o, \perp}(t) = D_{\mathbf{k}}^{o, 22}(t)$. To numerically solve Eqs. (S11)-(S14), we must define a momentum grid. Given that $\text{ErTe}_3$ is a layered material and ARPES typically probes only a few layers, we set the dimensionality to $d = 2$. In our simulations, we fix a UV cutoff, $\Lambda$, and the number of radial momentum points, $N_k$, which introduces an effective IR cutoff. This is physically meaningful, as quenched disorder in the real material also imposes a natural IR cutoff.

### 1. Results

[Two columns of plots: the left column contains two stacked plots showing $\phi^c / \phi_0^c$ and $\phi^a / \phi_0^a$ vs Delay time $t$ for various $\Delta_T$ values (1.5, 2.7, 3.9, 5.1, 6.3, 7.5) and an experimental fit. The right plot shows Recovery time $\tau$ vs Quench strength $\Delta_T$ for c-CDW (blue diamonds) and a-CDW (red diamonds)]

FIG. S11. Order parameter dynamics after a quench in the coupled orders scenario, cf. Eq. (S8). Exponential fits were done only to extract the characteristic recovery times. We use a numerical time step of $\Delta t = 0.0005$ and a fourth order Runge-Kutta. Numerical parameters are $\Lambda = \pi, \Gamma_a = \Gamma_c = 0.5, K = 1, \tau_{eq} = 0.3$, dimension $d = 2$ and #momenta $N_k = 1000$.

Figure S11 (left) shows the resulting post-pulse $a$- and $c$-CDWs dynamics, as described by Eqs. (S11)-(S14). Following the experiment, we are primarily interested in extracting the recovery times of each CDW. To this end, we fit an exponential decay to each curve shown in Fig. S11 (left), starting at the time the corresponding minimum is reached. Strictly speaking, the recovery of the order parameters in this modeling follows a power-law$^{22}$; however, the exponential fits are employed to extract the characteristic recovery times, which we then compare with experimental data. Figure S11 (right) shows these recovery times as functions of fluence: both quantities strongly depend on the

---

12

![Figure S12: Six-panel plot showing the photoexcitation dynamics of CDW mean fields and two-point correlation functions for different $\Delta_T$ values. The left column shows $\phi^c / \phi_0$, $n^c_{||}$, and $n^c_{\perp}$ in blue tones. The right column shows $\phi^a / \phi_0$, $n^a_{||}$, and $n^a_{\perp}$ in red tones. All are plotted against delay time $t$.]

FIG. S12. Photoexcitation dynamics of CDW mean fields and two-point correlation functions in the scenario of coupled order parameters, cf. Eq. (S8). We use a numerical time step of $\Delta t = 0.0005$ and a fourth-order Runge-Kutta. Numerical parameters are $\Lambda = \pi$, $\Gamma_a = \Gamma_c = 0.5$, $K = 1$, $\tau_{\text{eq}} = 0.3$, dimension $d = 2$ and #momenta $N_k = 1000$.

pulse strength, characteristic of second-order phase transitions$^{22}$. We remark that while we set $\Gamma_a = \Gamma_c$, we still observe distinct recovery times of the two order parameters. Crucially, the $a$-CDW exhibits an even stronger fluence dependence, which clearly disagrees with the experimental findings and necessitates further analysis, as we detail below.

**B. Nucleation scenario**

Free Energy Landscapes for $\Delta_T = 1.5$

![Figure S13: Two panels showing free energy landscapes. The left panel shows $|\Phi^c|$ landscape for minimal $|\Phi^a|$ and the right panel shows $|\Phi^a|$ landscape for minimal $|\Phi^c|$, both for various times $t$ from $0.0$ to $2.0$.]

FIG. S13. Free energy for numerical parameters $T_{\text{eq}} = 0.4$, $T_{c1} = 1.0$, $T_{c2} = 0.6$, $r^0_c = 2$, $r^0_a = 1$, $u_c = 1$, $u_a = -25$, $u'_a = 20$

The assumption for Eq. (S5) is that the order parameters are small close to the phase transition. This assumption is valid for the phase transition at $T_{c1}$, but for the subdominant phase transition, it may be problematic, especially if it

---

13

is first order. Indeed, it is not clear whether the phase transition is driven by competition between the different CDW order parameters. For example,$^{23}$ proposes a competition between a band anticrossing and the $a$-CDW instability instead, which leads to a hysteresis behavior of the Hall coefficient.

A second-order phase transition is driven by fluctuations, which naturally give rise to a fluence-dependent recovery rate, as shown in Sec. II A—this might not be the case for a first-order phase transition. Within cooling the electronic temperature, a new minimum with lower energy can form. Fluctuations determine the probability of nucleating into the new minima, cf. the canonical Kramer's problem – see Fig. S14. Once this local nucleation happens the mean field value is suddenly large and fluctuations become negligible. Guided by this, we propose in this section a decoupled free energy

$$f[\Phi] = \frac{1}{2} \left( r_c |\Phi^c|^2 + r_a |\Phi^a|^2 \right) + \frac{1}{4} \left( u_a |\Phi^a|^4 + u_c |\Phi^c|^4 \right) + \frac{u'_a}{6} |\Phi^a|^6 \eqno(\text{S15})$$

where for $r_a > 0$, $u_a < 0$, and $u'_a > 0$, we get a first-order phase transition in the $a$-CDW. Neglecting fluctuations the critical temperatures are given by $T_{c1} = \tilde{T}_{c1}$ and $T_{c2} = \tilde{T}_{c2}(1 + 3u_a^2/(16r_a^0 u'_a))$.

Nucleation of a bubble gains (local) free energy but costs surface energy. Within the thin-wall approximation the energy of a bubble of size $R$ is given by

$$E(R) = 2\pi R\sigma - \pi R^2 \Delta f, \eqno(\text{S16})$$

where $\sigma$ is a surface tension that quantifies the cost of a domain wall between the disordered phase ($\phi^a = 0$) and the ordered phase ($\bar{\phi}^a = \phi^a_0$) and $\Delta f = f(\bar{\phi}^a) - f(0)$, the free energy density benefit of being in the ordered phase. This schematic estimate of the free energy of a bubble is instructive in the following sense. Small bubbles are energetically costly due to the surface tension overpowering the free energy benefit. In the opposite regime, $R \to \infty$, the free energy gain dominates the surface tension cost, and the bubble size runs away. The maximum free energy occurs at $R_c = \frac{\sigma}{\Delta f}$, the critical bubble size, which accompanies a barrier $\Delta F$. Bubbles are formed by nucleation of ordered domains of radius $R_c$, which occurs at a rate $\Gamma_{\text{nuc}} \simeq \exp(-\Delta F/T)$. In the Sec. II B 2 we pedagogically articulate how we calculate the instantaneous nucleation rate $\Gamma_{\text{nuc}}(t) \simeq \exp(-\Delta F(r_a(t))/T)$, as a function of $r_a(t)$.

Once a bubble has nucleated, it grows spherically, due to the pressure difference building up inside and outside of the bubble, with a rate $\Gamma_g$ until it impinges upon another bubble. Growth occurs in nucleated regions, nucleation can only occur in unnucleated regions. Accordingly, we subtract off an excluded volume arising from the regions in which nucleation has already occurred. Assuming a homogeneous and isotropic nucleation and growth we end up with

$$\frac{\text{d}}{\text{d}t} \bar{\phi}^a(t) = (\phi^a_0 - \bar{\phi}^a(t)) \, \Gamma_g \, \Gamma_{\text{nuc}}(t), \eqno(\text{S17})$$

where $\phi_0$ is the global minimum. Eq. (S17) is similar to the Avrami equation but assumes a transformation that is dominated by nucleation. It is, however, only valid for $T < T_{c2}$, i.e. after a new minima in the free energy has formed. For $T > T_{c2}$ there is only a single minimum and thus we can adopt the model developed in Sec. II A to model the dynamics instantaneously after the quench. For a free energy up to 6th order they read

$$\frac{\text{d}}{\text{d}t} \bar{\phi}^a = -\Gamma_{\parallel} r_{\text{eff}} \bar{\phi}^a \eqno(\text{S18})$$
$$\frac{\text{d}}{\text{d}t} D_k^{\parallel}(t) = 2\Gamma_{\parallel} T_{\text{ph}} - 2\Gamma_{\parallel} \left[ r_{\text{eff}} + Kk^2 + 2u(\bar{\phi}^a)^2 + 4u'(\bar{\phi}^a)^4 \right] D_k^{\parallel}(t) \eqno(\text{S19})$$
$$\frac{\text{d}}{\text{d}t} D_k^{\perp}(t) = 2\Gamma_{\perp} T_{\text{ph}} - 2\Gamma_{\perp} [r_{\text{eff}} + Kk^2] D_k^{\perp}(t) \eqno(\text{S20})$$
$$r_{\text{eff}} = r + u\left((\bar{\phi}^a)^2 + \sum_{\beta} n_{\beta\beta}\right) + u'\left((\bar{\phi}^a)^4 + 2(\bar{\phi}^a)^2 \sum_{\beta} n_{\beta\beta} + \sum_{\beta,\gamma} n_{\beta\beta} n_{\gamma\gamma}\right) \eqno(\text{S21})$$

where we have defined $D_k^{\parallel}(t) = D_k^{11}(t)$ and $D_k^{\perp}(t) = D_k^{22}(t)$. Similarly to the previous section we model the pump as $r_c(t) = r_c^0(T_e(t)/\tilde{T}_{c1} - 1)$ and $r_a(t) = r_a^0(T_e(t)/\tilde{T}_{c2} - 1)$ where the electronic temperature behavior follows Eq. (S4). The dynamics for the $c$-CDW is given by Eq. (S11) - (S14).

A sketch of the dynamics is given in Fig. S14.

1. Results

In Fig. S15 a) and b) we plot the $a$- and $c$-CDW dynamics dynamics for a decoupled free energy given by Eq. (S15). The results for the dominant order a) are similar to the one obtained in Fig. S11 and the recovery time exhibits a

---

14

![Sketch of the time evolution of the free energy in the nucleation scenario](image_placeholder)

FIG. S14. Sketch of the time evolution of the free energy in the nucleation scenario: Before the pulse arrival, the order parameter is in the equilibrium minimum of the free energy. Shortly after photoexcitation, the free energy becomes essentially parabolic with a minimum at zero, while the minimum at finite order parameter is transiently lost. The dynamics are assumed to be overdamped and given by Eq. (S18) - Eq. (S21). Within the subsequent cooldown, a new free-energy minimum forms so that the order parameter can "jump" into it and spatially grow, with the probability given by the Kramers problem. Both these processes are captured by Eq. (S17).

![Post-pulse order parameter dynamics for the nucleation scenario](image_placeholder)

FIG. S15. Post-pulse order parameter dynamics for the nucleation scenario. Exponential fits were done only to extract the characteristic recovery times. We use a numerical time step of $\Delta t = 0.0005$ and a fourth order Runge-Kutta. Numerical parameters are $\Lambda = \pi$, $\Gamma_a = \Gamma_c = 0.5$, $K = 1$, $\tau_{\text{eq}} = 0.3$, dimension $d = 2$ and #momenta $\mathcal{N}_k = 1000$.

fluence dependence. The subdominant order, in contrast, recovers fluence independently as can be seen in the fitted recovery time c), in agreement with the experiment.

This can be explained intuitively in the following: The pump suppresses the CDW order and places it in the disordered state $\phi = 0$. While the free energy recovers quickly within $\tau_{\text{eq}}$, the system stays trapped in the metastable minimum due to the nucleation bottleneck see Fig. S17 a). We see that as a function of the instantaneous $r_a(t)$, the activation barrier to nucleating domain and the size of the critical nucleating domain decrease as the system relaxes towards $r_a(t \rightarrow \infty)$, see Fig. S17 b). Assuming a critical $r_{\text{nuc}} \equiv r_a(\tau_{\text{rec}})$ at which $\Gamma_{\text{nuc}}$ is large enough to be seen in experiments, we ask, how long does it take to reach $r_{\text{nuc}}$ as a function of fluence? By reverting Eq. (S4) we find for the recovery timescale

$$\tau_{\text{rec}} = \tau_{\text{eq}} \log(\Delta_T / \Delta r), \eqno{(\text{S22})}$$

where $\Delta r = r_{\text{nuc}} - r_a(t \rightarrow \infty)$. The logarithmic behavior already suggests that the recovery time-scale will not be as fluence dependent as for the dominant CDW, e.g. if we take $\tau_{\text{eq}} \sim 100\text{fs}$, then as $\tau_{\text{rec}} \sim 1\text{ps}$, the logarithm is in the regime where it is very insensitive to its argument, i.e. there should be limited fluence dependence. Note, however, that this order of magnitude discrepancy implies that $\Delta_T / \Delta r \sim 10^4$, i.e. $r_{\text{nuc}} \approx r_a(t \rightarrow \infty)$. Metastability in even the equilibrium landscape lasts for over 1ps.

---

15

![Plots showing photoexcitation dynamics of CDW mean fields and correlation functions. Left column (blue curves) shows $\phi^c/\phi_0$, $n_{||}^c$, and $n_{\perp}^c$. Right column (red curves) shows $\phi^a/\phi_0$, $n_{||}^a$, and $n_{\perp}^a$ as functions of delay time $t$ for various $\Delta_T$ values.](image_placeholder)

FIG. S16. Photoexcitation dynamics of CDW mean fields and two-point correlation functions in the nucleation scenario. We use a numerical time step of $\Delta t = 0.0005$ and a fourth order Runge-Kutta. Numerical parameters are $\Lambda = \pi$, $\Gamma_a = \Gamma_c = 0.5$, $K = 1$, $\tau_{eq} = 0.3$, dimension $d = 2$ and #momenta $N_k = 1000$.

By this order of magnitude difference between $\tau_{eq}$ and $\tau_{rec}$, any influence of the initial pulse significantly dampens out and the order parameter recovers through nucleation and growth independent of the transient free energy and the initial strong fluctuations. Within this framework, the remarkable nature of the non-equilibrium measurement to resolve the details of the free-energy landscape becomes apparent.

*2. Calculating the Nucleation Barrier*

Having outlined the traditional understanding of nucleation as a competition between domain wall formation penalized by the surface tension and the free energy benefit of ordering, we now seek to understand how the nucleation barrier changes as a function of evolving $r_a(t)$. For compactness we drop the $a$ superscript in $\bar{\phi}^a$.

Let us consider a bubble that is radially symmetric whose radial profile is given by $\bar{\phi}(r)$. The boundary conditions for the bubble are $\bar{\phi}(0) = \bar{\phi}_0$ and $\bar{\phi}(r \rightarrow \infty) = 0$. We can write down the spatially dependent Ginzburg-Landau free energy

$$F[\bar{\phi}] = 2\pi \int_{0}^{\infty} \text{d}r\,r \left[ \frac{1}{2} \left( \frac{\text{d}\bar{\phi}}{\text{d}r} \right)^2 + f(\bar{\phi}) \right], \eqno(\text{S23})$$

where the gradient term — penalizing spatial inhomogeneity — gives rise to the surface tension. It is possible to numerically solve for $\bar{\phi}(r)$. However, in the presence of higher order non-linearities, computation of such profiles becomes stiff and thereby numerically difficult. A simpler route is to parametrize the bubble profile using a variational form. A simple form for the bubble radial profile is given by

$$\bar{\phi}(r) = c_a \left( 1 + \tanh \left( \frac{R - r}{w} \right) \right), \eqno(\text{S24})$$

where $c_a = \phi_0 / (1 + \tanh(R/w))$ ensures $\bar{\phi}(0) = \bar{\phi}_0$ and $\bar{\phi}(\infty) = 0$. Here $R$ represents the bubble radius and $w$ represents the bubble width, where the domain transitions from the ordered to the disordered phase, incurring the surface tension cost.

For each value of $r_a(t)$, we find the critical bubble size, find the nucleation barrier, and obtain the effective surface tension. We do this by computing the value of the width $w$ which minimizes the free energy given by Eq. (S23) for

---

16

each value of bubble radius $R$. Given these minimal free energies for each $R$, we maximize this minimal free energy as a function of $R$—by doing this we determine the critical bubble radius $R_c$ and thereby the nucleation barrier. We plot the results in Fig. S17.

[Image: Two plots. (a) shows $\mathcal{F}(R)$ vs $R$ for various $r_a$ values (3.6, 4.2, 4.9, 5.3, 5.6), showing bubble free energy curves. (b) shows $\Delta F(R_c)$ vs $r_a$ with an inset zoom, showing the activation barrier increasing as $r_a$ approaches a critical value.]

FIG. S17. (a) The bubble free energy, plotted for different values of $r_a$. (b) The activation barrier $\Delta F(R_c)$ to nucleate a domain of radius $R_c$. The barrier height diverges at $r_a^c = 5.8$ (dashed grey line). Numerical parameters are $u_a = -25$ and $u'_a = 20$, but we expect this phenomenology to be generic.

### 3. Analytical constraint of decoupled TDGL model

From the analysis above, we notice that there should be a threshold of nucleation, above which the nucleation picture stands and the $a$-CDW recovers at a constant rate. Here we extend our TDGL modelling into small fluence regime. We derive the exact percentage of order parameter suppression needed to reach the threshold, and show that our experimental parameters lies in the same regime.

Consider again the decoupled Ginzburg-Landau $\phi^6$ free energy:

$$f = \frac{1}{2}r_a|\bar{\phi}^a|^2 + \frac{1}{4}u_a|\bar{\phi}^a|^4 + \frac{u'_a}{6}|\bar{\phi}^a|^6 \eqno(\text{S25})$$

For a first-order transition ($u_a < 0$, $u'_a > 0$), the positions of the energy barrier ($\bar{\phi}_{\text{barrier}}^a$) and the ordered minimum ($\bar{\phi}_0^a$) are analytically linked. Their ratio is given by the roots of the potential gradient:

$$\left(\frac{\bar{\phi}_{\text{barrier}}^a}{\bar{\phi}_0^a}\right)^2 = \frac{|u_a| - \sqrt{u_a^2 - 4r_au'_a}}{|u_a| + \sqrt{u_a^2 - 4r_au'_a}} \eqno(\text{S26})$$

To push the barrier as far outward as possible, the system must approach the coexistence limit ($T = T_{c2}$), where the disordered and ordered states have equal free energy ($4r_au'_a = \frac{3}{4}u_a^2$). Substituting this into the ratio yields a strict mathematical upper bound for the barrier position:

$$\bar{\phi}_{\text{barrier}}^a \le \frac{1}{\sqrt{3}}\bar{\phi}_0^a \approx 0.577\bar{\phi}_0^a \eqno(\text{S27})$$

This fundamental limit dictates that the system must melt by at least $\sim 42\%$ to cross the energy barrier and become trapped in the disordered state ($\bar{\phi}^a \approx 0$) as shown in our simulation in Fig. S18.

As shown in our extended low-fluence simulations (Fig. S18), if the system fails to cross this $\sim 58\%$ threshold, the recovery is governed by purely deterministic sliding relaxation down the steep potential well. This relaxation is extremely fast. We note that the threshold behavior is certainly expected. If we consider the limiting case where the excitation fluence is close to 0, the recovery rate should also be infinitesimally small. Thus, when the system is excited below the nucleation energy barrier, the recovery of a-CDW is much faster. However, this regime is not achievable in the experiment given the finite signal-noise ratio and temporal resolution of trARPES instruments.

---

17

![Figure S18: Recovery dynamics plots showing $\phi^S/\phi^S_0$ and $\phi^a/\phi^a_0$ versus delay time $t$ on the left, and recovery time $\tau$ versus quench strength $\Delta_T$ on the right.](https://placeholder.com/image)

**FIG. S18. Simulated recovery dynamics demonstrating the trapping threshold.** (Left) For weak quenches ($\Delta_T < 1.0$), the $a$-CDW melts shallowly and relaxes extremely rapidly. For deep quenches ($\Delta_T \geq 1.0$), the system crosses the thermodynamic barrier ($\phi^a \lesssim 0.58\phi^a_0$), becomes trapped, and recovers via slow nucleation. (Right) The extracted recovery times confirm that failing to cross the barrier results in a relaxation timescale that is drastically faster than the second-order $c$-CDW, contradicting the slow experimental observation.

Now we take a closer look on the regime of excitation in our observed $a$-CDW dynamics. First and foremost, we notice that from both spectral weight change and EDC shifts in Fig. S5, the light-induced quenching in $a$-CDW is close to saturation even low fluence. This indicates that in the fluence regime we studied, $a$-CDW is always excited above the nucleation barrier and close to full quenching. In addition, in the previous section, we showed that the gap size fitted from transient EDCs can be severely underestimated. For systems with even smaller gap, such as $a$-CDW, the underestimation is more pronounced. As we have also shown previously from conduction band EDC analysis, the suppression in $c$-CDW is already above 40% at intermediate fluence. Given the much smaller gap size, the $a$-CDW is expected to be suppressed more than $c$-CDW. Indeed, this is what we observed in our experiment. In Fig. S5, we can clearly observe from EDC fitting that the $a$-CDW is more susceptible to optical excitation. All these factors indicate that the fluence regime we study is beyond the nucleation threshold

### III. Selection and extraction of data from previous literature

In Fig. 4d of the main text, we compared the recovery dynamics upon light excitation in several representative first-order and second-order CDW transitions reported previously. The first-order CDW transition systems we refer to are Indium nanowires on silicon substrate$^{24}$, commensurate CDW transition in $1T\text{-TaS}_2^{25}$, and $\text{IrTe}_2^{26}$. The second-order transition systems we refer to are $\text{TiSe}_2^{26}$, $\text{LaTe}_3^{11}$, and $\text{K}_{0.3}\text{MoO}_3^{27}$. For a meaningful comparison in CDW amplitude recovery$^{11}$, we only included previous studies involving transient reflectivity measurements or trARPES measurements in a fluence range similar to that of this work.

Except for $\text{LaTe}_3$, whose recovery time versus fluence curve was plotted in the main text$^{11}$, All other recovery time data are extracted by fitting either trARPES or transient reflectivity data following the same fitting procedures introduced above (Eq. (S2)).

The recovery time extracted from literature as a function of excitation fluence is plotted in Fig. 4d, alongside the

---

18

results from both $a\text{-CDW}$ and $c\text{-CDW}$ in $\text{ErTe}_3$ measured in this work. The data are color-coded so that first-order transitions are plotted in red colors and second-order transitions in blue colors. Though the collected data set is not meant to be exhaustive, it demonstrates agreement with the conclusion of our Ginzburg-Landau model: Upon photoexcitation, the recovery of the order parameter amplitude in a second-order phase transition slows down when a higher fluence is applied, while the recovery of a first-order transition is much less sensitive to fluence. We also note that the recovery timescales of first-order transitions cited here are consistent up to less than one order of magnitude, which can be possibly the characteristic timescale of the nucleation-like growth. This comparative study, thus, suggests the generality of our combined theoretical and experimental approach to classify phase transitions and verify the driving mechanisms in time domain.

**IV. Nomenclature of CDWs in rare-earth tritellurides**

In the $\text{RTe}_3$ family of materials, the CDW states can be tuned with external knobs such as photoexcitations and strain. These resultant CDW states are also aligned with either $a$ or $c$ axes of the lattice. Here we clarify their difference and our nomenclature.

The $c\text{-CDW}$ and $a\text{-CDW}$ in this work always refer to the CDW states in unstrained $\text{RTe}_3$ without external perturbations or excitations, meaning $a/c \ge 0.997$. The transition temperatures of $c\text{-CDW}$ and $a\text{-CDW}$ in this case are referred to as $T_{c1}$ and $T_{c2}$, respectively. In this case, $c\text{-CDW}$ is the dominant order while $a\text{-CDW}$ is the subdominant order, thus, we can also refer to these as dominant $c\text{-CDW}$ and secondary $a\text{-CDW}$.

Under a large enough strain, the dominant order aligns with the $a$ axis of the crystalline lattice$^{18,19}$. In this case, the CDW along $a\text{-axis}$ behaves more similarly to the original $c\text{-CDW}$ rotated by $90^\circ$ rather than the equilibrium $a\text{-CDW}$ that occurs below $T_{c2}$. At lower temperatures, a subdominant CDW emerges at a lower temperature along $c$ axis. We thus refer to these strained CDW states as dominant $a\text{-CDW}$ and subdominant $c\text{-CDW}$, emerging at transition temperatures $T_{c1'}$ and $T_{c2'}$, respectively. These states are not relevant in this study and are included here for clarity and completeness.

In previous ultrafast electron diffraction studies$^{12,13,28}$, a light-induced CDW is observed along $a\text{-axis}$ in a photoexcited pure $c\text{-CDW}$ state. This light-induced CDW is not a long-range CDW order like any of the CDWs mentioned above. Instead, it is a populated soft phonon state similar to the state around $T_{c1}$ (see Fig. 1b). We refer to this short-range CDW as $\tilde{a}\text{-CDW}$.

**V. SUPPLEMENTARY REFERENCES**

[1] B. Lv, T. Qian, and H. Ding, Angle-resolved photoemission spectroscopy and its application to topological materials, Nature Reviews Physics **1**, 609 (2019).
[2] L. Rettig, R. Cortés, J.-H. Chu, I. R. Fisher, F. Schmitt, R. G. Moore, Z.-X. Shen, P. S. Kirchmann, M. Wolf, and U. Bovensiepen, Persistent order due to transiently enhanced nesting in an electronically excited charge density wave, Nature Communications **7**, 10459 (2016).
[3] A. Zong, P. E. Dolgirev, A. Kogar, E. Ergeçen, M. B. Yilmaz, Y.-Q. Bie, T. Rohwer, I.-C. Tung, J. Straquadine, X. Wang, Y. Yang, X. Shen, R. Li, J. Yang, S. Park, M. C. Hoffmann, B. K. Ofori-Okai, M. E. Kozina, H. Wen, X. Wang, I. R. Fisher, P. Jarillo-Herrero, and N. Gedik, Dynamical Slowing-Down in an Ultrafast Photoinduced Phase Transition, Physical Review Letters **123**, 097601 (2019).
[4] Y. Zhong, T. Suzuki, H. Liu, K. Liu, Z. Nie, Y. Shi, S. Meng, B. Lv, H. Ding, T. Kanai, J. Itatani, S. Shin, and K. Okazaki, Unveiling van Hove singularity modulation and fluctuated charge order in kagome superconductor $\text{CsV}_3\text{Sb}_5$, Physical Review Research **6**, 043328 (2024).
[5] Dynamics of electronic states in the insulating intermediate surface phase of $1\text{T-TaS}_2$, Physical Review B **108**, 2 (2023).
[6] C. Monney, M. Puppin, C. W. Nicholson, M. Hoesch, R. T. Chapman, E. Springate, H. Berger, A. Magrez, C. Cacho, R. Ernstorfer, and M. Wolf, Revealing the role of electrons and phonons in the ultrafast recovery of charge density wave correlations in $1\text{T-TiSe}_2$, Physical Review B **94**, 165165 (2016), 1609.08993.
[7] S. Mathias, S. Eich, J. Urbancic, S. Michael, A. V. Carr, S. Emmerich, A. Stange, T. Popmintchev, T. Rohwer, M. Wiesenmayer, A. Ruffing, S. Jakobs, S. Hellmann, P. Matyba, C. Chen, L. Kipp, M. Bauer, H. C. Kapteyn, H. C. Schneider, K. Rossnagel, M. M. Murnane, and M. Aeschlimann, Self-amplified photo-induced gap quenching in a correlated electron material, Nature Communications **7**, 1 (2016).
[8] A. Crepaldi, M. Puppin, D. Gosálbez-Martínez, L. Moreschini, F. Cilento, H. Berger, O. V. Yazyev, M. Chergui, and M. Grioni, Optically induced changes in the band structure of the Weyl charge-density-wave compound $(\text{TaSe}_4)_2\text{I}$, Journal of Physics: Materials **5**, 044006 (2022).
[9] S. Duan, Y. Cheng, W. Xia, Y. Yang, C. Xu, F. Qi, C. Huang, T. Tang, Y. Guo, W. Luo, D. Qian, D. Xiang, J. Zhang, and W. Zhang, Optical manipulation of electronic dimensionality in a quantum material, Nature **595**, 239 (2021).

---

