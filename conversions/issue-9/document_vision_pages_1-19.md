nature physics

Supplementary information

https://doi.org/10.1038/s41567-026-03382-5

# Time-domain identification of distinct mechanisms for competing charge density waves in a rare-earth tritelluride

In the format provided by the authors and unedited

---

3

![FIG. S2. Comparison of CDW recovery dynamics with different incident photon polarization. Four panels: (a) c-CDW in-gap intensity (norm.) vs Delay time (ps), LV; (b) a-CDW in-gap intensity (norm.) vs Delay time (ps), LV; (c) c-CDW, LH; (d) a-CDW, LH. Fluence legend (mJ/cm²): 0.07, 0.14, 0.28, 0.42, 0.56, 0.70.](fig_s2)

**FIG. S2. Comparison of CDW recovery dynamics with different incident photon polarization.** **a,b** Time evolution of normalized in-gap intensity of $c$-CDW (a) and $a$-CDW (b) measured with LV polarization, reproduced from Fig.3 (**c,d**). **c,d** Same measurement performed with probe photons with LH polarization. Same recovery dynamics of CDWs are observed with different incident probe photon polarizations, thus excluding the possibility of artifacts caused by the matrix element effect.

In Fig. S3, we demonstrate the EDC analysis on the snapshots presented in Fig. 2 of the main text. From the raw EDC curves, we can clearly observe the rightward shifts of leading edges after timezero. This is a typical signature of CDW suppression. While in Fig. S4, we demonstrate the timescan counter part of the same analysis.In both sets of plots, we overlapped the data points with the fitting curves of corresponding pump fluences in Fig. 3**c** and **d**, with only vertical scaling due to the different units. We can clearly see that the temporal evolution of leading edges extracted from EDCs in both sets of data agrees well with the temporal evolution of spectral weight in the CDW gaps. This is a strong evidence showcasing the consistency between the in-gap spectral weight dynamics and CDW gap dynamics.

Having established the equivalence between gap and in-gap spectral weight dynamics, we further analyze the fluence dependence of the EDCs. The EDCs at a delay time with maximum CDW suppression signal (0.5 ps) at $c$- and $a$-CDW gap positions in reciprocal space are plotted in Fig. S5 **a** and **b**. Compared to the spectra in equilibrium (grey curves), the leading edges of the EDCs demonstrate a clear shift towards the Fermi level. This shift in energy scales with fluence, signifying a typical suppression of CDW amplitude upon photoexcitation.

We note that in all analysis demonstrated above, no other signals of in-gap states are observed from EDCs. Thus, the in-gap spectral weight increase observed in our trARPES measurement is dominantly contributed by the CDW suppression, justifying the in-gap spectral weight as a proper measure of the CDW amplitude dynamics. It is also noteworthy that the EDC analysis for both CDW gaps under different fluences indicates that $c$-CDW has not reached the full CDW suppression within our fluence range while $a$-CDW is close to full suppression, given the saturation behaviour under different fluences, as shown in **c–d**. This is also consistent with previous ultrafast measurements on similar materials$^{11-14}$.

---

4

**FIG. S3. EDCs analysis of *snapshot* data.** **a,b** EDCs at different timesteps for *c*-CDW (**a**) and *a*-CDW (**c**) extracted from the same dataset as demonstrated in Fig. 2 in the main text. **c-d** Leading edge of *c*-CDW (**c**) and *a*-CDW (**d**) bands extracted from EDCs of each delay time, overlapped with the fitting curve for $0.42 \text{ mJ/cm}^2$ data from Fig. 3, with only vertical scaling. The error bars represent the energy resolution of our trARPES instrument.

*2. Quantitative understanding of EDCs in trARPES*

We would like to note that though extracting gap dynamics from EDCs can be qualitatively useful and consistent with in-gap spectral weight analysis, one needs to be extra cautious before citing the extracted gap value as the exact gap size. Here we provide a systematic study on how the shifts in EDC leading edge can underestimate the actually gap size change in trARPES measurements

We start from revisiting the gap closure dynamics of *c*-CDW. Besides in-gap spectral weight and transient EDCs of valence band, one can extract the CDW gap dynamics, in a limited time interval, also from the conduction band bottom above the CDW gap.

In Fig. S6, we demonstrate the transient EDCs for *c*-CDW gap plotted in log-scale. we note that this analysis is only practical for *c*-CDW, where the gap is large enough and is thus de-convolved from the thermal broadening near the Fermi level. For *a*-CDW, due to particle-hole asymmetry$^{15}$ and small gap amplitude, it is not practical to identify the transient gap closure process from transient EDC.

We can clearly observe the closure of CDW gap. After photoexcitation, the leading edge of the conduction band is barely distinguishable. A careful tracing of the conduction band peak position gives an estimation of 40% of gap closure, as indicated by the black triangular labels in Fig. S6. This is consistent with the observation in previous trARPES studies on $R$Te$_3$$^{16}$. We note that compared to the values extracted from valence band EDC fitting presented in Fig. S5, the percentage of change extracted from conduction band shifting is much larger, indicating a severe underestimation in valence band EDC fitting.

To further demonstrate the underestimation effect of transient valence EDC analysis, we perform a simulation of ARPES spectra for electronic bands gapped by long range orders. From the simulation, we find that the number extracted from the leading edge in EDC, is usually a severe underestimation. We note that part of this underestimation

---

5

**Figure S4.** Six panels (**a**–**f**). Top row (**a**–**c**): *c-CDW* band leading edge (eV) plotted against Delaytime (ps), with panel titles $0.14~\mathrm{mJ/cm^2}$, $0.42~\mathrm{mJ/cm^2}$, and $0.70~\mathrm{mJ/cm^2}$ respectively; vertical axis spans roughly $-0.21$ to $-0.19$ eV. Bottom row (**d**–**f**): *a-CDW* band leading edge (eV) plotted against Delaytime (ps) for the same fluences; vertical axis spans roughly $-0.06$ to $-0.04$ eV, horizontal axis $-0.5$ to $2.0$ ps.

**FIG. S4. EDCs analysis of *timescan* data.** **a-c** (**d-f**) Leading edge of *c-CDW* (*a-CDW*) band extracted from EDCs acquired from binning the continuous time scans with a 250 fs step size, at $0.14$, $0.42$, $0.70~\mathrm{mJ/cm^2}$, respectively. All data are overlapped with corresponding fitting curves from Fig. 3 in the main text, with only vertical scaling. The error bars represent the energy resolution of our trARPES instrument.

is a result of Fermi-Dirac function. Unlike equilibrium-state ARPES measurement, where Fermi-Dirac function can be removed in order to extract precise gap size, transient electronic states measured in trARPES do not strictly follow Fermi-Dirac distribution before thermalization and thus it would not be fully justified to extract the precise gap size in trARPES by removing the Fermi-Dirac distribution at a very short delay time after the time zero.

As demonstrated in Fig. S7, we first generate the single-electron spectral function for an electronic system gapped by a long range order from the eigenvalues of Fröhlich Hamiltonian. As an example, we compare the two cases where the CDW gap $\Delta = 100$ meV (**a**) and 200 meV (**b**) respectively. In order to simulate real ARPES spectrum, we multiply the spectral function by the Fermi-Dirac function (**c,d**) convoluted with the instrument resolution, and superposed with a background noise function (**e,f**). By making cut along the window labeled in Fig. S7e, we acquired the EDCs for $\Delta = 100$ meV and 200 meV case respectively. By either directly fitting the EDCs or fitting the peak position after the taking the first derivative with respect to energy, we extracted a gap difference between 10 meV and 40 meV, which are 2.5 to 10 times smaller than the real gap difference of 100 meV. We thus conclude that EDC analysis returns a severely underestimated gap size, possibly due to the existence of Fermi-Dirac function. However, the qualitative change and recovery dynamics, which we previously showed to be consistent with the in-gap spectral weight, is still meaningful and trustworthy.

## C. Effect of energy integration window

The data we presented in Fig. 3 of the main text is acquired by integrating over a window of 50 meV energy window centered at Fermi energy for the best signal-to-noise ratio. In order to exclude the possibility of contributions from other parts of the electronic structure, we hereby show the robustness against the selection of an integration window.

Comparing the results acquired with a 50 meV integration window to the ones acquired with a 20 meV integration window (Fig. S8), we clearly observe that the time traces, after normalization from 0 to 1, agree almost perfectly. We can thus exclude the possibility of any artifacts created by the selection of the integration window, solidifying the analysis and conclusions presented in the main text.

---

8

**FIG. S8.**

**(a)** c-CDW in-gap intensity (norm.) vs. Delay time (ps) [range: -0.5 to 2.0]

- 20 meV window, 0.70 mJ/cm$^2$
- 50 meV window, 0.70 mJ/cm$^2$
- 20 meV window, 0.07 mJ/cm$^2$
- 50 meV window, 0.07 mJ/cm$^2$

**(b)** a-CDW in-gap intensity (norm.) vs. Delay time (ps) [range: -0.5 to 2.0]

- 20 meV window, 0.70 mJ/cm$^2$
- 50 meV window, 0.70 mJ/cm$^2$
- 20 meV window, 0.07 mJ/cm$^2$
- 50 meV window, 0.07 mJ/cm$^2$

**FIG. S8.** **Comparison of time traces acquired from different energy integration windows** a,b In-gap photoemission intensities of $c$-CDW (a) and $a$-CDW (b) under 0.07 mJ/cm$^2$ (light) and 0.70 mJ/cm$^2$ (dark) fluences, acquired with a 50 meV integration window (hollow) and a 20 meV integration window (solid).

---

**Left panel:** SW at c-CDW gap momentum (norm.) vs. Delay time (ps) [range: -0.5 to 2.0]
Constant-energy contours: 0 meV, 100 meV, 200 meV, 300 meV, 400 meV

**Right panel:** SW at a-CDW gap momentum (norm.) vs. Delay time (ps) [range: -0.5 to 2.0]
Constant-energy contours: 0 meV, 100 meV, 200 meV, 300 meV, 400 meV

**FIG. S9.** **Distinct behaviours of CDW gap dynamics and carrier population dynamics.** Time evolution of the spectral weight at the $c$-CDW (left) and $a$-CDW (right) gap momentum-space position across various constant-energy contours. The clearly different dynamics at Fermi level ($E - E_F = 0$ meV) showcases the CDW order parameter dynamics as opposed to electron population dynamics.

---

10

## A. The scenario of coupled order parameters

The approximate symmetry of the CDW in $\mathrm{ErTe_3}$ is $U(1) \times U(1) \times \mathbb{Z}_2$ as we are dealing with two orthogonal incommensurate CDWs$^{17}$. However, due to a slight orthorhombicity, the $\mathbb{Z}_2$ symmetry is explicitly broken (the space group is $Cmcm$)$^{18}$. Thus, at zero applied stress, the dominant order is, in reality, always along the $c$-axis. Up to fourth order, the free energy potential compatible with this symmetry is

$$f[\mathbf{\Phi}] = \frac{r}{2} \left( |\Phi^a|^2 + |\Phi^c|^2 \right) + \frac{b}{2} \left( |\Phi^a|^2 - |\Phi^c|^2 \right) + \frac{\tilde{g}}{2} |\Phi^a|^2 |\Phi^c|^2 + \frac{u}{4} \left( |\Phi^a|^2 + |\Phi^c|^2 \right)^2 \ . \tag{S5}$$

For $g = \tilde{g} + u > 0$ and $b > 0$ it leads to two second-order phase transitions at different temperatures $T \sim r$: First into a striped CDW along the $c$-axis and second into a checkerboard state. Neglecting fluctuations the critical temperatures for the two phase transitions are given by $T_{c1} = \tilde{T}_c (b/r_0 + 1)$ and $T_{c2} = \tilde{T}_c b (g + u) / (r_0 (g - u)) + \tilde{T}_c$. In practice, the second phase is actually a bidirectional CDW as the strengths of the two CDWs are different. Furthermore, this model also lacks a first-order phase transition if the strain $\epsilon \sim b$ is tuned. These shortcomings can be cured by including higher order expansion terms, which was done in previous works$^{19,20}$. However, these higher-order terms do not change the nature of the temperature-driven second-order phase transitions.

In the absence of slow hydrodynamics modes, the dynamics close to a phase transition exhibit a clear separation of scales: All physical quantities fluctuate much faster than the order parameter, i.e., they merely constitute a stochastic force on the order parameter. Since the CDW order parameter is not conserved, the equation of motion describing the post-quench evolution is of model-A type$^{21}$:

$$\frac{\mathrm{d}}{\mathrm{d}t} \phi_\alpha(\mathbf{r}, t) = - \Gamma_\alpha \frac{\delta \mathcal{F}}{\delta \phi_\alpha(\mathbf{r}, t)} + \eta_\alpha(\mathbf{r}, t) \tag{S6}$$

with a Gaussian noise $\langle \eta_\alpha(\mathbf{r}, t) \rangle = 0$ and $\langle \eta^\alpha_\alpha(\mathbf{r}, t) \eta^\beta_\beta(\mathbf{r}', t') \rangle = 2 \Gamma_\alpha T_{\mathrm{ph}} \delta(\mathbf{r} - \mathbf{r}') \delta(t - t') \delta_{\alpha \beta}$. In what follows, we simplify the stochastic nonlinear dynamics by employing the Gaussian approximation, which gives a non-perturbative framework to study post-quench evolution and competition of the two CDWs – this closely follows Refs.$^{13,22}$. To this end, we split the complex fields into real and imaginary parts: $\Phi^a = \phi_1^a + i \phi_2^a$ and $\Phi^c = \phi_1^c + i \phi_2^c$ and rewrite the free energy

$$\mathcal{F}[\phi] = \int \mathrm{d}^d \mathbf{r} \left[ \frac{K}{2} \sum_\alpha \left[ (\nabla \phi^a_\alpha(\mathbf{r}, t))^2 + (\nabla \phi^c_\alpha(\mathbf{r}, t))^2 \right] + f[\phi(\mathbf{r}, t)] \right] \ , \tag{S7}$$

$$f[\phi(\mathbf{r})] = \frac{r + b}{2} \sum_\alpha (\phi^a_\alpha)^2 + \frac{r - b}{2} \sum_\alpha (\phi^c_\alpha)^2 + \frac{g}{2} \sum_{\alpha, \beta} (\phi^a_\alpha)^2 (\phi^c_\beta)^2 + \frac{u}{4} \sum_{\alpha, \beta} \left( (\phi^a_\alpha)^2 (\phi^a_\beta)^2 + (\phi^c_\alpha)^2 (\phi^c_\beta)^2 \right). \tag{S8}$$

We split each field into its mean field part $\bar{\phi}$ and fluctuations $\delta \phi$ around it:

$$\phi^o_\alpha(\mathbf{r}, t) = \bar{\phi}^o_\alpha(t) + \delta \phi^o_\alpha(\mathbf{r}, t) = \bar{\phi}^{o, \alpha}(t) + \frac{1}{\sqrt{N}} \sum_{\mathbf{k} \neq \mathbf{0}} e^{i \mathbf{k} \cdot \mathbf{r}} \phi^{o, \alpha}_{\mathbf{k}}(t) = \frac{1}{\sqrt{N}} \sum_{\mathbf{k}} e^{i \mathbf{k} \cdot \mathbf{r}} \phi^{o, \alpha}_{\mathbf{k}}(t), \qquad \phi^{o, \alpha}_{\mathbf{k} = \mathbf{0}} = \sqrt{N} \bar{\phi}^{o, \alpha} \ . \tag{S9}$$

We introduce the equal-time correlation functions as

$$D^{o, \alpha \alpha}_{\mathbf{k}}(t) = \langle \delta \phi^{o, \alpha}_{\mathbf{k}}(t) \delta \phi^{o, \alpha}_{-\mathbf{k}}(t) \rangle \ , \qquad n^{o \alpha \alpha}(t) = \frac{1}{N} \sum_{\mathbf{k}} D^{o, \alpha \alpha}_{\mathbf{k}}(t) \tag{S10}$$

where $o = a, c$, and all other correlators are assumed to be zero. Without loss of generality, we can set $\bar{\phi}^{\alpha \neq 1} = 0$, as by symmetry, always picking $\alpha = 1$ to be the direction of symmetry breaking/condensation. The mean-field equations of motion in the $1/\mathcal{N}$ expansion (here $\mathcal{N} = 4$) read

$$\frac{\mathrm{d}}{\mathrm{d}t} \bar{\phi}^o = - \Gamma_o r^o_{\mathrm{eff}} \bar{\phi}^o \qquad \text{with} \qquad r^a_{\mathrm{eff}} = r + b + u \left( (\bar{\phi}^a)^2 + \sum_\beta n^a_{\beta \beta} \right) + g \left( (\bar{\phi}^c)^2 + \sum_\beta n^c_{\beta \beta} \right) \tag{S11}$$

$$r^c_{\mathrm{eff}} = r - b + u \left( (\bar{\phi}^c)^2 + \sum_\beta n^c_{\beta \beta} \right) + g \left( (\bar{\phi}^a)^2 + \sum_\beta n^a_{\beta \beta} \right) \tag{S12}$$

where $\bar{\phi}^o \equiv \bar{\phi}_{o, \alpha = 1}$ and we used Wick's theorem which holds for the Gaussian approximation we employ. Within the same approximation, the dynamics of correlators is then governed by:

$$\frac{\mathrm{d}}{\mathrm{d}t} D^{o, \parallel}_{\mathbf{k}}(t) = 2 \Gamma_o T_{\mathrm{ph}} - 2 \Gamma_o \left[ r^o_{\mathrm{eff}} + K k^2 + 2 u (\bar{\phi}^o)^2 \right] D^{o, \parallel}_{\mathbf{k}}(t) \tag{S13}$$

$$\frac{\mathrm{d}}{\mathrm{d}t} D^{o, \perp}_{\mathbf{k}}(t) = 2 \Gamma_o T_{\mathrm{ph}} - 2 \Gamma_o \left[ r^o_{\mathrm{eff}} + K k^2 \right] D^{o, \perp}_{\mathbf{k}}(t) \tag{S14}$$

---

11

# Free Energy Landscapes for $\Delta_T = 1.5$

| $\Phi^c$| Landscape for minimal $|\Phi^a|$ | $\Phi^a$| Landscape for minimal $|\Phi^c|$ |
|---|---|
| $t=0.0$ | $t=0.0$ |
| $t=0.5$ | $t=0.5$ |
| $t=1.0$ | $t=1.0$ |
| $t=1.5$ | $t=1.5$ |
| $t=2.0$ | $t=2.0$ |

**FIG. S10.** Free energy landscape for $T_{\text{eq}} = 0.4$, $\tilde{T}_c = 0.9$, $r_0 = 2$, $u = 1$, $\tilde{g} = -1$, $b = 0.23$, $\tau_{\text{eq}} = 0.3$

where $D_k^{a,\|}(t) = D_k^{a,11}(t)$ and $D_k^{a,\perp}(t) = D_k^{a,22}(t)$. To numerically solve Eqs. (S11)–(S14), we must define a momentum grid. Given that $\text{ErTe}_3$ is a layered material and ARPES typically probes only a few layers, we set the dimensionality to $d = 2$. In our simulations, we fix a UV cutoff, $\Lambda$, and the number of radial momentum points, $N_k$, which introduces an effective IR cutoff. This is physically meaningful, as quenched disorder in the real material also imposes a natural IR cutoff.

## 1. Results

| $\Phi^c / \Phi_0^c$ | $\Delta_T = 1.5$ | $\Delta_T = 2.7$ | $\Delta_T = 3.9$ | $\Delta_T = 5.1$ | $\Delta_T = 6.3$ | $\Delta_T = 7.5$ | exp. fit |
|---|---|---|---|---|---|
| $\Phi^a / \Phi_0^a$ | $\Delta_T = 1.5$ | $\Delta_T = 2.7$ | $\Delta_T = 3.9$ | $\Delta_T = 5.1$ | $\Delta_T = 6.3$ | $\Delta_T = 7.5$ | exp. fit |
| Recovery time $\tau$ | c-CDW | a-CDW | | | | | |

**FIG. S11.** Order parameter dynamics after a quench in the coupled orders scenario, cf. Eq. (S8). Exponential fits were done only to extract the characteristic recovery times. We use a numerical time step of $\Delta t = 0.0005$ and a fourth order Runge–Kutta. Numerical parameters are $\Lambda = \pi$, $\Gamma_a = \Gamma_c = 0.5$ , $K = 1$, $\tau_{\text{eq}} = 0.3$, dimension $d = 2$ and #momenta $N_k = 1000$.

Figure S11 (left) shows the resulting post-pulse $a$- and $c$-CDWs dynamics, as described by Eqs. (S11)–(S14). Following the experiment, we are primarily interested in extracting the recovery times of each CDW. To this end, we fit an exponential decay to each curve shown in Fig. S11 (left), starting at the time the corresponding minimum is reached. Strictly speaking, the recovery of the order parameters in this modeling follows a power-law$^{22}$; however, the exponential fits are employed to extract the characteristic recovery times, which we then compare with experimental data. Figure S11 (right) shows these recovery times as functions of fluence: both quantities strongly depend on the

---

12

![](images/image_001.png)

FIG. S12. Photoexcitation dynamics of CDW mean fields and two-point correlation functions in the scenario of coupled order parameters, cf. Eq. (S8). We use a numerical time step of $\Delta t = 0.0005$ and a fourth-order Runge–Kutta.Numerical parameters are $\Lambda = \pi$, $\Gamma_a = \Gamma_c = 0.5$ , $K = 1$, $\tau_{\text{eq}} = 0.3$, dimension $d = 2$ and #momenta $N_k = 1000$.

pulse strength, characteristic of second-order phase transitions$^{22}$. We remark that while we set $\Gamma_a = \Gamma_c$, we still observe distinct recovery times of the two order parameters. Crucially, the $a$-CDW exhibits an even stronger fluence dependence, which clearly disagrees with the experimental findings and necessitates further analysis, as we detail below.

## B. Nucleation scenario

Free Energy Landscapes for $\Delta_T = 1.5$

![](images/image_002.png)

FIG. S13. Free energy for numerical parameters $T_{\text{eq}} = 0.4$, $T_{c1} = 1.0$, $T_{c2} = 0.6$, $r_c^0 = 2$, $r_a^0 = 1$, $u_c = 1$, $u_a = -25$, $u_a' = 20$

The assumption for Eq. (S5) is that the order parameters are small close to the phase transition. This assumption is valid for the phase transition at $T_{c1}$, but for the subdominant phase transition, it may be problematic, especially if it

---

is first order. Indeed, it is not clear whether the phase transition is driven by competition between the different CDW order parameters. For example,$^{23}$ proposes a competition between a band anticrossing and the $a$-CDW instability instead, which leads to a hysteresis behavior of the Hall coefficient.

A second-order phase transition is driven by fluctuations, which naturally give rise to a fluence-dependent recovery rate, as shown in Sec. **II A**—this might not be the case for a first-order phase transition. Within cooling the electronic temperature, a new minimum with lower energy can form. Fluctuations determine the probability of nucleating into the new minima, cf. the canonical Kramer's problem – see Fig. **S14**. Once this local nucleation happens the mean field value is suddenly large and fluctuations become negligible. Guided by this, we propose in this section a decoupled free energy

$$
f[\mathbf{\Phi}] = \frac{1}{2} \left( r_c |\Phi^c|^2 + r_a |\Phi^a|^2 \right) + \frac{1}{4} \left( u_a |\Phi^a|^4 + u_c |\Phi^c|^4 \right) + \frac{u_a'}{6} |\Phi^a|^6 \tag{S15}
$$

where for $r_a > 0$, $u_a < 0$, and $u_a' > 0$, we get a first-order phase transition in the $a$-CDW. Neglecting fluctuations the critical temperatures are given by $T_{c1} = \tilde{T}_{c1}$ and $T_{c2} = \tilde{T}_{c2} (1 + 3 u_a^2 / (16 r_a u_a'))$.

Nucleation of a bubble gains (local) free energy but costs surface energy. Within the thin-wall approximation the energy of a bubble of size $R$ is given by

$$
E(R) = 2 \pi R \sigma - \pi R^2 \Delta f, \tag{S16}
$$

where $\sigma$ is a surface tension that quantifies the cost of a domain wall between the disordered phase ($\bar{\phi}^a = 0$) and the ordered phase ($\bar{\phi}^a = \phi_0^a$) and $\Delta f = f(\bar{\phi}_0^a) - f(0)$, the free energy density benefit of being in the ordered phase. This schematic estimate of the free energy of a bubble is instructive in the following sense. Small bubbles are energetically costly due to the surface tension overpowering the free energy benefit. In the opposite regime, $R \to \infty$, the free energy gain dominates the surface tension cost, and the bubble size runs away. The maximum free energy occurs at $R_c = \frac{\sigma}{\Delta f}$, the critical bubble size, which accompanies a barrier $\Delta F$. Bubbles are formed by nucleation of ordered domains of radius $R_c$, which occurs at a rate $\Gamma_{\mathrm{ nuc}} \simeq \exp(-\Delta F / T)$. In the Sec. **II B 2** we pedagogically articulate how we calculate the instantaneous nucleation rate $\Gamma_{\mathrm{ nuc}}(t) \simeq \exp(-\Delta F(r_a(t)) / T)$, as a function of $r_a(t)$.

Once a bubble has nucleated, it grows spherically, due to the pressure difference building up inside and outside of the bubble, with a rate $\Gamma_g$ until it impinges upon another bubble. Growth occurs in nucleated regions, nucleation can only occur in un nucleated regions. Accordingly, we subtract off an excluded volume arising from the regions in which nucleation has already occurred. Assuming a homogeneous and isotropic nucleation and growth we end up with

$$
\frac{\mathrm{d}}{\mathrm{d} t} \bar{\phi}^a(t) = \left( \bar{\phi}_0^a - \bar{\phi}^a(t) \right) \Gamma_g \, \Gamma_{\mathrm{ nuc}}(t), \tag{S17}
$$

where $\bar{\phi}_0$ is the global minimum. Eq. (**S17**) is similar to the Avrami equation but assumes a transformation that is dominated by nucleation. It is, however, only valid for $T < T_{c2}$, i.e. after a new minima in the free energy has formed. For $T > T_{c2}$ there is only a single minimum and thus we can adopt the model developed in Sec. **II A** to model the dynamics instantaneously after the quench. For a free energy up to 6th order they read

$$
\frac{\mathrm{d}}{\mathrm{d} t} \bar{\phi}^a = - \Gamma_{\parallel} r_{\mathrm{ eff}} \bar{\phi}^a \tag{S18}
$$

$$
\frac{\mathrm{d}}{\mathrm{d} t} D_{\boldsymbol{k}}^{\parallel}(t) = 2 \Gamma_{\parallel} T_{\mathrm{ ph}} - 2 \Gamma_{\parallel} \left[ r_{\mathrm{ eff}} + K k^2 + 2 u (\bar{\phi}^a)^2 + 4 {u'} (\bar{\phi}^a)^4 \right] D_{\boldsymbol{k}}^{\parallel}(t) \tag{S19}
$$

$$
\frac{\mathrm{d}}{\mathrm{d} t} D_{\boldsymbol{k}}^{\perp}(t) = 2 \Gamma_{\perp} T_{\mathrm{ ph}} - 2 \Gamma_{\perp} [r_{\mathrm{ eff}} + K k^2] D_{\boldsymbol{k}}^{\perp}(t) \tag{S20}
$$

$$
r_{\mathrm{ eff}} = r + u \left( (\bar{\phi}^a)^2 + \sum_{\beta} n_{\beta \beta} \right) + {u'} \left( (\bar{\phi}^a)^4 + 2 (\bar{\phi}^a)^2 \sum_{\beta} n_{\beta \beta} + \sum_{\beta, \gamma} n_{\beta \beta} n_{\gamma \gamma} \right) \tag{S21}
$$

where we have defined $D_{\boldsymbol{k}}^{\parallel}(t) = D_{\boldsymbol{k}}^{11}(t)$ and $D_{\boldsymbol{k}}^{\perp}(t) = D_{\boldsymbol{k}}^{22}(t)$. Similarly to the previous section we model the pump as $r_c(t) = r_c^0 (T_{\mathrm{e}}(t) / \tilde{T}_{c1} - 1)$ and $r_a(t) = r_a^0 (T_{\mathrm{e}}(t) / \tilde{T}_{c2} - 1)$ where the electronic temperature behavior follows Eq. (**S4**). The dynamics for the $c$-CDW is given by Eq. (**S11**) - (**S14**).

A sketch of the dynamics is given in Fig. **S14**.

### 1. *Results*

In Fig. **S15** a) and b) we plot the $a$- and $c$-CDW dynamics dynamics for a decoupled free energy given by Eq. (**S15**). The results for the dominant order a) are similar to the one obtained in Fig. **S11** and the recovery time exhibits a

---

