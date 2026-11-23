# Introduction to flavour physics
J. Zupan
Department of Physics, University of Cincinnati, Cincinnati, Ohio, USA
**Abstract**
We give a brief introduction to flavour physics. The first part covers the flavour structure of the Standard Model, how the Kobayashi-Maskawa mechanisem is tested and provides examples of searches for new physics using flavour observables, such as meson mixing and rare decays. In the second part we give a brief overview of the recent flavour anomalies and how the Higgs can act as a new flavour probe.
**Keywords**
Flavour physics; heavy quarks; $B$ physics; meson mixing; new physics; Higgs; lectures.
## 1 Introduction
The term “flavour” was coined in 1971 by Murray Gell-Mann and his student at the time, Harald Fritzsch, while sitting at a Baskin-Robbins ice-cream store in Pasadena, CA [1]. Just as ice-cream has both colour and flavour so do quarks. “Flavour” is now used slightly more generally to denote the species of any Standard Model (SM) fermion, both quarks and leptons. “Flavour physics” thus has little to do with one’s adventures in kitchen, but rather is a research area that deals with properties of quarks and leptons.
Grouped according to their QCD and QED quantum numbers, $SU(3) \times U(1)_{\text{em}}$, the SM fermions are,
$$
\begin{aligned}
3_{2/3} : &\quad \text{up type quarks;} & u, c, t, \\
3_{-1/3} : &\quad \text{down type quarks;} & d, s, b, \\
1_{-1} : &\quad \text{charged leptons;} & e, \mu, \tau, \\
1_{0} : &\quad \text{neutrinos;} & \nu_e, \nu_\mu, \nu_\tau.
\end{aligned}
\eqno(1)
$$
Each fermion type comes in three copies, i.e., the SM fermions group into three generations.
In this brief introduction to flavour physics we will cover some of the classic topics on the subject: the flavour structure of the Standard Model (SM), how the Kobayashi-Maskawa mechanism is tested, as well as the constraints on the New Physics (NP) due to flavour observables such as the meson mixing and decays. We will also touch on the more recent developments: the $B$ physics anomalies and the Higgs as a new probe of flavour. Along the way we will address two major questions currently facing particle physics. The first question is why do the SM fermions exhibit such a hierarchical structure, shown in Fig. 1? This is commonly referred to as the SM flavour puzzle. The other question is what lies above the electroweak scale? Here flavour physics offers a way to probe well above the electroweak scale.
Other excellent introductions to flavour physics the reader may want to consult include Refs. [2–7]. Ref. [2] in particular is chock full of physics insights without too much burdensome formalism. Section 2 borrows liberally from [5], which, while slightly outdated, is still a masterful introduction to the basic topics in flavour physics. For a reader that is seeking more depth a good starting point can be Refs. [8–11].
## 2 The flavour of the Standard Model
### 2.1 The SM symmetry structure
A renormalizable particle physics model is defined by specifying (i) the gauge group and (ii) the particle field content. The next step is to write down the most general renormalizable Lagrangian. The SM gauge

![Image of particle mass distribution and energy scales]
**Fig. 1:** The distribution of masses of the elementary particles, along with some of the relevant energy scales. The absolute values of neutrino masses are not known - their placement on the graph is indicative of the upper bound.
group is
$$\mathcal{G}_{\text{SM}} = SU(3)_c \times SU(2)_L \times U(1)_Y.$$ (2)
Here $SU(3)_c$ is the gauge group of strong interactions, Quantum Chromodynamics (QCD), the $SU(2)_L$ is the gauge group of weak isospin, and $U(1)_Y$ the gauge group of hypercharge. The field content of the SM consists of a single scalar, EW doublet
$$H \sim (1, 2)_{1/2},$$ (3)
and a set of fermion fields,
$$\begin{aligned} Q_{Li} \sim (3, 2)_{+1/6}, \quad u_{Ri} \sim (3, 1)_{+2/3}, \quad d_{Ri} \sim (3, 1)_{-1/3}, \\ L_{Li} \sim (1, 2)_{-1/2}, \quad \ell_{Ri} \sim (1, 1)_{-1}. \end{aligned}$$ (4)
Each of the fields comes in three copies (three generations), $i = 1, 2, 3$. To simplify the discussion we will set neutrino masses to zero. The modifications due to nonzero neutrino masses are given in appendix A. The $\mathcal{G}_{\text{SM}}$ is spontaneously broken by the Higgs vacuum expectation value, $\langle H \rangle = (0, v/\sqrt{2})$, $v = 246$ GeV, down to
$$\mathcal{G}_{\text{SM}} \rightarrow SU(3) \times U(1)_{em}.$$ (5)
After the electroweak symmetry breaking the field content in (4) splits into up and down quarks, charged leptons and neutrinos as listed in Eq. (1).
### 2.2 The SM Lagrangian
The SM Lagrangian is the most general renormalizable Lagrangian that is consistent with the gauge group $\mathcal{G}_{\text{SM}}$ and the field content (3), (4)
$$\mathcal{L}_{\text{SM}} = \mathcal{L}_{\text{kin}} + \mathcal{L}_{\text{Yukawa}} + \mathcal{L}_{\text{Higgs}}.$$ (6)
The kinetic terms in the Lagrangian are determined by the gauge structure through the covariant derivative
$$D_\mu \psi = (\partial_\mu + ig_s G_\mu^a t^a + ig W_\mu^i \tau^i + ig' B_\mu Y)\psi.$$ (7)
The strong interaction term is a product of the strong coupling, $g_s$, the eight gluon fields, $G_\mu^a$, and the generators $t^a$ of $SU(3)_c$. For color triplet $\psi$ these are $t^a = \lambda^a/2$, with $\lambda^a$ the eight $3 \times 3$ Gell-Mann matrices, while for color singlet $\psi$, $t^a = 0$. The $SU(2)_L$ term is a product of the weak coupling, $g$, the three weak gauge bosons, $W_\mu^i$, and the generators of $SU(2)_L$, $\tau^i$ (equal to $\tau^i = \sigma^i/2$ for $\psi$ that is a doublet, with $\sigma^i$ the Pauli matrices, while for singlets $\tau^i = 0$). The last term is due to the hypercharge $U(1)_Y$.

INTRODUCTION TO FLAVOUR PHYSICS
The covariant derivatives are flavour blind, i.e., generation independent. For instance, for $Q_L^i$ the kinetic term is
$$\mathcal{L}_{\text{kin}}|_{Q_L} = i\bar{Q}_L^i(\partial_\mu + ig_s G_\mu^a \frac{1}{2} \lambda^a + ig W_\mu^i \frac{1}{2} \sigma^i + i \frac{1}{6} g' B_\mu)\delta^{ij} Q_L^j, \eqno(8)$$
for up quarks it is
$$\mathcal{L}_{\text{kin}}|_{u_R} = i\bar{u}_R^i(\partial_\mu + ig_s G_\mu^a \frac{1}{2} \lambda^a + i \frac{2}{3} g' B_\mu)\delta^{ij} u_R^j, \eqno(9)$$
and similarly for the other fields. Each of the kinetic terms is invariant under the global $U(3) = SU(3) \times U(1)$ transformations. Thus $\mathcal{L}_{\text{kin}}$ has a global flavour symmetry
$$\mathcal{G}_{\text{flavour}} = U(3)_q^3 \times U(3)_{\text{lep}}^2, \eqno(10)$$
where
$$\begin{aligned} U(3)_q^3 &= U(3)_Q \times U(3)_u \times U(3)_d, \eqno(11) \\ U(3)_{\text{lep}}^2 &= U(3)_L \times U(3)_\ell. \eqno(12) \end{aligned}$$
That is, each of the five different types of fermions in Eq. (4) can be separately rotated in flavour space, $\psi^i \to U^i_j \psi^j$, where $U^i_j$ is a unitary $3 \times 3$ matrix, without changing $\mathcal{L}_{\text{kin}}$.
However, $\mathcal{G}_{\text{flavour}}$ cannot be an exact symmetry of the whole Lagrangian. We know from observations that, e.g., the top quark differs from the up quark due to the differing masses. The part of the Lagrangian that breaks $\mathcal{G}_{\text{flavour}}$ is
$$\mathcal{L}_{\text{Yukawa}} = -Y_d^{ij} \bar{Q}_L^i H d_R^j - Y_u^{ij} \bar{Q}_L^i H^c u_R^j - Y_\ell^{ij} \bar{L}_L^i H \ell_R^j + \text{h.c.}. \eqno(13)$$
The above Yukawa interactions break
$$\mathcal{G}_{\text{flavour}} \to U(1)_B \times U(1)_e \times U(1)_\mu \times U(1)_\tau \times U(1)_Y, \eqno(14)$$
where $U(1)_B$ is the baryon number, and $U(1)_\ell$ are the separate lepton numbers. That $\mathcal{L}_{\text{Yukawa}}$ breaks the flavour symmetry is not surprising, since it is the origin of fermion masses, once the Higgs obtains the vacuum expectation value (vev), $\langle H \rangle = (0, v/\sqrt{2})$, with $v = 246$ GeV.
### 2.3 A Standard Model vs. the Standard Model
Before we proceed further in understanding the breaking pattern in Eq. (14), let us make a small detour and elaborate on the difference between *a Standard Model* and *the Standard Model*. *A Standard Model* denotes any model with the SM gauge group (2) and the SM field content (3), (4), but with some arbitrary values for the coupling constants in the most general renormalizable Lagrangian. *The Standard Model* is a Standard Model with exactly the values of coupling constants observed in nature. *A Standard Model* has the exact accidental symmetry $U(1)_B \times U(1)_e \times U(1)_\mu \times U(1)_\tau$. This accidental symmetry is present for any values of the parameters in the renormalizable SM Lagrangian (but can be broken by non-renormalizable terms). It is accidental, since we did not explicitly ask for it – it is simply present because we cannot write down renormalizable terms that break it, given the field and gauge content in Eqs. (2)-(4). For *the Standard Model*, because of the actual values of the parameters, there can be additional approximate symmetries.
Isospin is an example of such an approximate symmetry. In QCD interactions one can replace $u

### 2.4 Counting physical parameters
The next question we need to address is how one counts the physical parameters. The SM has 19 physical parameters: 3 gauge couplings, 3 lepton masses, 6 quark masses, 4 parameters in the Cabibbo-Kobayashi-Maskawa (CKM) matrix, 2 parameters in the Higgs sector (the Higgs mass and the strength of the self interaction), and the QCD $\theta$ parameter. Physical parameters are parameters that cannot be rotated away by performing phase transformations or flavour rotations.
Let us understand this on the case of charged lepton masses. The charged lepton Yukawa
$$\mathcal{L}_{\text{Yukawa}} \supset -Y_{\ell}^{ij} \bar{L}_L^i H \ell_R^j + \text{h.c.}, \eqno(16)$$
can always be made diagonal and real positive through a bi-unitary transformation, $L_L \to V_L L_L$, $\ell_R \to V_{\ell} \ell_R$, which gives
$$Y_{\ell} \to V_L^{\dagger} Y_{\ell} V_{\ell} = \text{diag}(y_e, y_{\mu}, y_{\tau}). \eqno(17)$$
How many physical parameters are there? The starting point, $Y_{\ell}$, is described by 9 real and 9 imaginary numbers. The unitary matrices $V_L, V_{\ell}$ have in total $2 \times (3 \text{ real} + 6 \text{ im.})$ numbers. When we rotate $L_L^i$ and $\ell_R^j$ by the same phase there is no change in $y_{\ell}$. That means that 3 phases (im. numbers) have no effect. Thus we have $9 - 2 \times 3 = 3$ real, and $9 - (2 \times 6 - 3) = 0$ imaginary physical parameters. The three real physical parameters are the charged lepton masses, while there are no physical phases.
Extrapolating from this exercise we can postulate the general rule on how to count the physical parameters [2]
$$\# \text{ physical parameters} = \# \text{ parameters} - \# \text{ broken symmetry generators}. \eqno(18)$$
Let us check this with a simple example: the spin $1/2$ in a magnetic field. If there is no magnetic field the system has an $SO(3)$ symmetry (3 generators), since the spin can be oriented in an arbitrary direction without changing the energy. The system also has two degenerate eigenstates corresponding to spin up and spin down. In the magnetic field the Zeeman effect splits the two states. The splitting depends on the strength of the magnetic field, $B$. There is thus one physical parameter that controls the splitting. However, the magnetic field in general has three components, and is thus described by 3 parameters, $\vec{B} = B_x \hat{x} + B_y \hat{y} + B_z \hat{z}$. One can use the rotation around $x$ and $y$ axes to align $\vec{B}$ along the $z$ axis, i.e., set $B_x = B_y = 0$. After this is done, making any further rotations around $x$ and $y$ axes would change the $\vec{B}$ component: there are 2 broken symmetry generators. Using the general rule (18) gives that there is $3 - 2 = 1$ physical parameter, as expected.
We can now apply (18) to count the physical parameters in the quark sector of the SM. Using the unitary transformations
$$Q_L \to V_Q Q_L, \quad u_R \to V_u u_R, \quad d_R \to V_d d_R, \eqno(19)$$
one can bring the Yukawa couplings to the form
$$Y_d = \text{diag}(y_d, y_s, y_b), \quad Y_u = V_{\text{CKM}}^{\dagger} \text{diag}(y_u, y_c, y_t), \eqno(20)$$
with $V_{\text{CKM}}$ a unitary $3 \times 3$ CKM matrix [12, 13]. How many entries in $V_{\text{CKM}}$ are physical? The starting point, the $Y_u, Y_d$ matrices, have $2 \times (9 \text{ real} + 9 \text{ im.})$ parameters. The three unitary matrices, $V_Q, V_u, V_d$ have in total $3 \times (3 \text{ real} + 6 \text{ im.})$ parameters. Finally, there is one global phase corresponding to common phase change $Q_L \to \exp(i\phi) Q_L, u_R \to \exp(i\phi) u_R, d_R \to \exp(i\phi) d_R$, which has no effect. That is, there is one unbroken symmetry generator – the baryon number, while all the other symmetry generators are broken. Using (18) we see that there are $2 \times 9 - 3 \times 3 = 9$ real parameters and $2 \times 9 - (3 \times 6 - 1) = 1$ imaginary physical parameter. These are the 6 quark masses, as well as the 3 mixing angles and one phase describing the CKM matrix.

INTRODUCTION TO FLAVOUR PHYSICS
![Feynman diagrams showing quark couplings to $\gamma, Z, g, h,$ and $W$ bosons.](https://placeholder_image_link)
**Fig. 2:** The Feynman diagrams for flavour conserving couplings of quarks to photon, $Z$ boson, gluon and the Higgs (the first three diagrams), and the flavour changing coupling to the $W$ (the last diagram). The $3 \times 3$ matrices are visual representations of couplings in the generation space, with couplings to $\gamma, Z, g$ flavour universal, the couplings to the Higgs flavour diagonal but not universal, and the couplings to $W$ flavour changing and hierarchical.
A conventional parametrization of the CKM matrix is [14]
$$
\begin{aligned}
V_{\text{CKM}} &= \begin{pmatrix} 1 & 0 & 0 \\ 0 & c_{23} & s_{23} \\ 0 & -s_{23} & c_{23} \end{pmatrix} \begin{pmatrix} c_{13} & 0 & s_{13}e^{-i\delta} \\ 0 & 1 & 0 \\ -s_{13}e^{i\delta} & 0 & c_{13} \end{pmatrix} \begin{pmatrix} c_{12} & s_{12} & 0 \\ -s_{12} & c_{12} & 0 \\ 0 & 0 & 1 \end{pmatrix} \\
&= \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta} \\ -s_{12}c_{23} - c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23} - s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13} \\ s_{12}s_{23} - c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23} - s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13} \end{pmatrix},
\end{aligned} \eqno(21)
$$
where $c_{ij} \equiv \cos \theta_{ij}$, $s_{ij} \equiv \sin \theta_{ij}$, so that the CKM matrix is a product of three rotations with one phase inserted in the matrix describing the $\theta_{13}$ rotation. Experimentally, we observe that $\theta_{12} \gg \theta_{23} \gg \theta_{13}$, while $\delta \sim \mathcal{O}(1)$.
As the side benefit of the counting of physical parameters we just performed, we also understand that the flavour breaking due to the Yukawa matrices is as given in Eq. (14). In more detail, if we were to take nonzero just a single Yukawa coupling matrix at the time, the breaking pattern is
- since $Y_\ell \not\approx 1$: $U(3)_L \times U(3)_\ell \rightarrow U(1)_e \times U(1)_\mu \times U(1)_\tau$, i.e., the charged lepton family numbers,
- since $Y_u \not\approx 1$: $U(3)_Q \times U(3)_u \rightarrow U(1)_u \times U(1)_c \times U(1)_t$, i.e., the up-quark family numbers,
- since $Y_d \not\approx 1$: $U(3)_Q \times U(3)_d \rightarrow U(1)_d \times U(1)_s \times U(1)_b$, i.e., the down-quark family number,
- since $[Y_d, Y_u] \neq 0$: $U(1)_q^6 \rightarrow U(1)_B$, i.e., the above quark $U(1)$'s further break to a global baryon number.
Note that the final $U(1)$'s are composed both from the $U(1)$ factors in the original $[U(3) = SU(3) \times U(1)]$'s, as well as from the $t^3$ and $t^8$ generators of the $SU(3)$'s. In particular, not all of the $U(1)$ factors in $\mathcal{G}_{\text{flavour}}$ get broken by the Yukawas. The $\mathcal{G}_{\text{flavour}}$ contains five $U(1)$ factors, which can be chosen to be $U(1)^5 = U(1)_Y \times U(1)_B \times U(1)_L \times U(1)_{\text{PQ}} \times U(1)_{\ell_R}$. The $U(1)_Y$ is the hypercharge group, which is gauged, while $B$ and $L$ are the global baryon and lepton numbers. These are not broken by $\mathcal{L}_{\text{Yukawa}}$. The remaining two global $U(1)$'s can be taken to be the Peccei-Quinn symmetry $U(1)_{\text{PQ}}$ ($H$ and $d'_R, \ell'_R$ have opposite charges, all others zero), while under $U(1)_{\ell_R}$ only $\ell'_R$ is charged. The $U(1)_{\text{PQ}}$ is broken by $Y_u \neq 0$, and $U(1)_{\ell_R}$ by $Y_\ell \neq 0$. Had we included neutrino masses in the discussion, these would furthermore break the separate lepton numbers to a common lepton number, $U(1)_L$, if the neutrino masses are Dirac, while Majorana masses also break $U(1)_L$, see appendix A.
### 2.5 The flavour violation as seen in the mass basis
The main message of the discussion so far is: in the SM the flavour structure (flavour breaking) resides in the Yukawa sector of the SM Lagrangian, Eq. (13). If the Yukawa couplings were vanishingly small, the

SM would have had a very large flavour symmetry $\mathcal{G}_{\text{flavour}}$, Eq. (10). In general, the flavor breaking can be parametrized as in Eq. (20), by 6 diagonal Yukawa couplings, and the elements of the CKM matrix, $V_{\text{CKM}}$.
After Higgs obtains the vev, the Yukawa terms give the quark and charge lepton masses,
$$M_f = Y_f \frac{(v + h)}{\sqrt{2}}. \eqno(22)$$
With a field redefinition for the left-handed up quark fields
$$Q_L \to \begin{pmatrix} V^\dagger u_L \\ d_L \end{pmatrix}, \eqno(23)$$
we can move the flavour changing interactions to the kinetic term. This gives the SM Lagrangian for the quarks in the mass basis
$$\mathcal{L}_{\text{SM}} \supset (\bar{q}_i \cancel{D}_{\text{NC}} q_i) + \frac{g}{\sqrt{2}} \bar{u}_L^i W^+ V_{\text{CKM}}^{ij} d_L^j + m_{u_i} \bar{u}_L^i u_R^i \left(1 + \frac{h}{v}\right) + m_{d_i} \bar{d}_L^i d_R^i \left(1 + \frac{h}{v}\right) + \text{h.c.}. \eqno(24)$$
The covariant derivative $D_{\text{NC}}$ contains flavour diagonal, yet non-universal, couplings of photon, gluon and the $Z$. The Higgs has flavour diagonal, yet non-universal, couplings that are proportional to quark masses, while the flavour changing transitions reside in charged currents, with the strength encoded in the CKM matrix, see Fig. 2.
### 2.6 Charged currents vs. neutral currents
In the SM there is a very important distinction between flavour changing neutral and charged currents. Flavour Changing Neutral Currents (FCNCs) are processes in which the quark flavour changes, while the quark charge stays the same. The charged currents change both the flavour and the charge of the quark. A glimpse at the PDG booklet [15] reveals that the probabilities for the two types of processes are strikingly differently. The charged currents lead to the dominant weak decays, while the FCNC induced decays are extremely suppressed. Rounding the experimental results, and not showing the errors, a few representative decays are
| charged currents: | | neutral currents: | |
|---|---|---|---|
| $s \to u \mu^- \bar{\nu}_\mu$ : | $Br(K^+ \to \mu^+ \nu) = 64\%,$ | $s \to d \mu^+ \mu^-$ : | $Br(K_L \to \mu^+ \mu^-) = 7 \times 10^{-9},$ |
| $b \to c \ell^- \bar{\nu}_\ell$ : | $Br(B^- \to D^0 \ell \bar{\nu}) = 2.3\%,$ | $b \to d \mu^+ \mu^-$ : | $Br(B^- \to K^{*-} \ell^+ \ell^-) = 5 \times 10^{-7},$ |
| $c \to s \mu^+ \nu_\mu$ : | $Br(D^\pm \to K^0 \mu^\pm \nu) = 9\%,$ | $c \to u \ell^+ \ell^-$ : | $Br(D^0 \to \pi^0 \ell^+ \ell^-) < 1.8 \times 10^{-4},$ |
The reason for such a striking difference is that in the SM the charged currents occur at tree level, while FCNCs are forbidden at tree level and only arise at one loop, see Fig. 3. Furthermore, the FCNCs come suppressed by the difference of the masses of the quarks running in the loop, $m_j^2 - m_i^2$. This so called Glashow-Iliopoulos-Maiani (GIM) mechanism [16] is a result of the fact that there is no flavour violation, if all the quark masses are the same.
### 2.7 The CKM matrix
The Cabibbo-Kobayashi-Maskawa (CKM) matrix is very hierarchical in the SM,
$$V_{\text{CKM}} = \begin{pmatrix} V_{ud} & V_{us} & V_{ub} \\ V_{cd} & V_{cs} & V_{cb} \\ V_{td} & V_{ts} & V_{tb} \end{pmatrix} \sim \begin{pmatrix} 1 & 0.2 & 0.004 \\ 0.2 & 1 & 0.04 \\ 0.008 & 0.04 & 1 \end{pmatrix}. \eqno(25)$$

INTRODUCTION TO FLAVOUR PHYSICS
![Feynman diagrams showing a tree level charged current diagram on the left and a loop induced FCNC diagram on the right.](https://via.placeholder.com/500x150)
**Fig. 3:** Representative tree level charged current diagram (left) and a loop induced FCNC diagram (right).
In fact, for processes at colliders in many cases the CKM matrix can even be approximated as
$$V_{\text{CKM}} \sim \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}, \quad \text{[collider physicist]} \eqno(26)$$
i.e., for many processes at high $p_T$ to a good enough precision the generation number is conserved.
We, on the other hand, are interested precisely in the off-diagonal entries in $V_{\text{CKM}}$. These entries roughly obey a power scaling in $\lambda \equiv |V_{us}| \simeq 0.22$, giving the Wolfenstein parametrization of the CKM matrix [17],
$$V_{\text{CKM}} = \begin{pmatrix} 1 - \lambda^2/2 & \lambda & A\lambda^3(\rho - i\eta) \\ -\lambda & 1 - \lambda^2/2 & A\lambda^2 \\ A\lambda^3(1 - \rho - i\eta) & -A\lambda^2 & 1 \end{pmatrix} + \mathcal{O}(\lambda^4). \eqno(27)$$
This parametrization also encodes that the CKM matrix is unitary, $V_{\text{CKM}}^\dagger V_{\text{CKM}} = V_{\text{CKM}} V_{\text{CKM}}^\dagger = 1$. The CKM matrix depends on 3 real parameters and 1 phase. In parametrization of Eq. (21) these were the three mixing angles and the phase $\delta$. In the Wolfenstein parametrization, Eq. (27), these are the three real parameters $\lambda, A, \rho$, and one imaginary parameter, $\eta$, all counted as being $\mathcal{O}(1)$. A global fit to the flavour observables gives [18]
$$A = 0.825(9), \quad \lambda = 0.2251(3), \quad \bar{\rho} = 0.160(7), \quad \bar{\eta} = 0.350(6), \eqno(28)$$
where the modified $\rho, \eta$ parameters were introduced as $\bar{\rho} + i\bar{\eta} = -V_{ud}V_{ub}^*/(V_{cd}V_{cb}^*)$, valid to all orders in $\lambda$. To $\mathcal{O}(\lambda^4)$ we have $\bar{\rho} = \rho(1 - \lambda^2/2)$ and $\bar{\eta} = \eta(1 - \lambda^2/2)$. Note that numerically $\bar{\rho}, \bar{\eta}$ are maybe closer to $\bar{\rho}, \bar{\eta} \sim \mathcal{O}(\lambda)$ than $\bar{\rho}, \bar{\eta} \sim \mathcal{O}(1)$, while at the time when Wolfenstein parametrization was written down this was not known. This can be incorporated in modified expansions [19], though the change in counting only matters at higher orders, not for the leading order expressions in Eq. (27).
### 2.8 Origin of CP violation in the SM
The SM Lagrangian is invariant under the discrete CP symmetry, apart from the Yukawa terms.$^1$ These transform as (writing explicitly also the hermitian conjugate terms)
$$Y_{ij} \bar{\psi}_L^i H \psi_R^j + Y_{ij}^* \bar{\psi}_R^j H^\dagger \psi_L^i \xrightarrow{\text{CP}} Y_{ij} \bar{\psi}_R^j H^\dagger \psi_L^i + Y_{ij}^* \bar{\psi}_L^i H \psi_R^j. \eqno(29)$$
The CP is conserved, if Yukawa couplings are real,
$$Y_{ij}^* = Y_{ij}. \eqno(30)$$
Since there is only one physical phase in the CKM, in the SM the CP violation (CPV) is controlled by one parameter, the "CKM phase", which in the Wolfenstein parametrization is the parameter $\eta$. CP is
$^1$ There is another CP violating parameter, the strong CP phase multiplying the QCD anomaly term, $g^2/(32\pi^2)\theta G^{a\mu\nu}\tilde{G}_{\mu\nu}^a$. It is bounded experimentally to be small, $\theta \lesssim 10^{-10}$ and, even if eventually found to be nonzero, is negligible for all the processes discussed in these lectures.

![The standard CKM unitarity triangle](https://i.imgur.com/placeholder.png)
**Fig. 4:** The standard CKM unitarity triangle (from [15]).
thus violated only, if $\eta \neq 0$. This origin of the observed CPV is called the Kobayashi-Maskawa (KM) mechanism [13]. Furthermore, CPT is conserved in any Lorentz invariant Quantum Field Theory, and therefore also in the SM. This means that CPV is equivalent to having T violation – the time reversal is also violated in the SM.
For the existence of CPV in the SM it is crucial that there are at least 3 generations of quarks. Repeating the counting of physical parameters from Sec. 2.4 we can easily

INTRODUCTION TO FLAVOUR PHYSICS
![Fig. 5: Three plots showing the evolution of constraints in the CKM unitarity triangle plane for years 1995, 2001, and 2018.](https://example.com/image5.png)
**Fig. 5:** The evolution of the constraints in the standard CKM unitarity triangle plane from 1995 (left), to just after the start of $B$ factories (middle), to the present (right). Taken from the ckmfitter website [18].
![Fig. 6: Diagrams showing main CKM constraints and respective SM diagrams.](https://example.com/image6.png)
**Fig. 6:** Some of the main CKM constrains and the respective SM diagrams.
which we can rewrite as
$$
\frac{V_{ud} V_{ub}^*}{V_{cd} V_{cb}^*} + 1 + \frac{V_{td} V_{tb}^*}{V_{cd} V_{cb}^*} = 0. \eqno(36)
$$
In terms of the Wolfenstein parameters this sum rule is is
$$
-(\bar{\rho} + i\bar{\eta}) + 1 + (-1 + \bar{\rho} + i\bar{\eta}) = 0. \eqno(37)
$$
The relation (36) can be interpreted as a sum of three complex numbers that are the sides of a triangle, shown

![Fig. 7: Evolving constraints in the $\bar{\rho} - \bar{\eta}$ plane from LHCb measurements and improvements in lattice QCD calculations, alone, with current inputs (2018), and the anticipated improvements from the data accumulated by 2035 ($300\text{ fb}^{-1}$ of integrated luminosity). More information on the fits may be found in [11, 21].](https://example.com/image.png)
**Fig. 7:** Evolving constraints in the $\bar{\rho} - \bar{\eta}$ plane from LHCb measurements and improvements in lattice QCD calculations, alone, with current inputs (2018), and the anticipated improvements from the data accumulated by 2035 ($300\text{ fb}^{-1}$ of integrated luminosity). More information on the fits may be found in [11, 21].
baryon from measurements at LHCb, and the kaon physics experiments. Different constraints in the standard CKM unitarity triangle plane are shown in Fig. 6, together with the relevant SM diagrams. The upshot of these results is that the KM mechanism is the dominant origin of CPV. The measurements point to a consistent picture of flavour violation, described by four parameters, $A, \lambda, \rho, \bar{\eta}$, with the values given in Eq. (28). Since $\rho \lesssim \bar{\eta}$ the CKM phase is large, $\mathcal{O}(1)$. It is given by
$$\gamma = \arctan(\bar{\eta}/\bar{\rho}) = \arg(V_{ub}^*), \eqno(38)$$
where in the last equality we used the common parametrization of the CKM matrix, where the weak phase is moved to the $V_{ub}$ and $V_{ts}$ CKM elements, (27). Experimentally [18],
$$\gamma = (65.4 \pm 1.1)^\circ, \eqno(39)$$
so that the weak phase is indeed $\mathcal{O}(1)$ when measured in radians.
The field is undergoing a big upgrade in available statistics. The successor to the Belle experiment, called Belle II, is ramping up right now, with the first physics run expected in early 2019 [10]. Belle II aims to collect about $\sim 8 \times 10^{10}$ $B$ mesons by about 2025, roughly $50\times$ more than Belle did. The LHCb experiment also has ambitious upgrade plans [21]. After the end of Upgrade II in 2035 it may have the statistics that corresponds to roughly $\sim 10^{11}$ or more useful $B$'s (because of hadronic environment this number fluctuates from channel to channel, as well as $B_s$ mesons and heavy baryons, which are also produced in the $pp$ collisions. The constraints on the elements of the CKM matrix are thus set to become much more precise in the future. Fig. 7 (right) shows the improvements that can be achieved by using just the LHCb measurements alone at the end of the high luminosity LHC programme. A similar projection for the improvements using Belle II measurements can be found in Ref. [22].
The constraints in the standard CKM unitarity triangle plot are of two types: the tree level transitions, which are less likely to be affected by new physics, and the loop level transitions, which are more likely to be affected by new physics. In the rest of this section we will choose an example transition for each of the two types of transitions and look at it in detail. This will then lead us to the discussion of new physics searches in Section 4. However, before we do that, we need to introduce several new concepts.
### 3.2 The meson mixing
The term *mixing* denotes that the flavour eigenstates do not equal mass eigenstates, i.e., that the eigenstates of the SM Hamiltonian are composed of states with different flavour compositions. For instance, $B^0 \sim b\bar{d}$ and $\bar{B}^0 \sim \bar{b}d$ are flavour eigenstates but are not mass eigenstates. The mass eigenstates are admixtures of $B^0$ and $\bar{B}^0$.

![Fig. 8: The SM diagrams leading to $B_d$ (left) and $B_s$ mixing (right).](https://example.com/image.png)
**Fig. 8:** The SM diagrams leading to $B_d$ (left) and $B_s$ mixing (right).
The term *oscillations* denotes that the initial flavour eigenstate time evolves to a different flavour eigenstate. The reason for this is that the flavour eigenstates are composed from two mass eigenstates, each of which evolves slightly differently. The oscillation frequency is the energy splitting, $\omega = \Delta E$. In the rest frame this equals the mass splitting, $\Delta E = \Delta m$, which means that the oscillations are an excellent way to measure small mass splittings.
What kind of mixings between states are possible? A general rule that applies here is: what is not explicitly forbidden is allowed [2]. Using this important rule let us look at two examples:
- Can $B^+ \sim \bar{b}u$ and $B^- \sim b\bar{u}$ mix? The answer is no, since the electric charge is conserved. That is, the $U(1)_{\text{em}}$ gauge symmetry forbids such mixings to all orders in perturbation theory.
- Can $B^0 \sim \bar{b}d$ and $\bar{B}^0 \sim b\bar{d}$ mix? In this case the answer is yes, since nothing forbids it. That is, there is no exact symmetry that forbids this mixing to all orders, so at some order in perturbation theory the mixing will occur. Such FCNCs are forbidden at three level in the SM, but are allowed at 1 loop.
A representative 1 loop weak interactions diagram that mixes $\bar{B}^0 \sim \bar{b}d$ and $B^0 \sim b\bar{d}$ in the SM, is shown in Fig. 8 (left). These diagrams contribute to the flavour off diagonal elements in the Hermitian $\bar{B}^0, B^0$ mass matrix, see e.g., [7],$^2$
$$\mathcal{M} = \begin{pmatrix} M_{11} & M_{12} \\ M_{21} & M_{22} \end{pmatrix}, \eqno(40)$$
written in the flavour basis
$$\begin{pmatrix} |B^0\rangle \\ |\bar{B}^0\rangle \end{pmatrix}. \eqno(41)$$
The off-diagonal elements are much smaller than the diagonal ones, so that the mass matrix has the form,
$$\mathcal{M} \propto \begin{pmatrix} 1 & \epsilon \\ \epsilon & 1 \end{pmatrix}. \eqno(42)$$
CPT guarantees $M_{11} = M_{22}$. If CP is conserved, then also $M_{12} = M_{21}$. Numerically, $M_{11} = M_{22} \simeq m_B$, while $M_{12,21} \ll M_{11}$. If CP is conserved, the mass eigenstates are
$$|B_{L,H}\rangle = \frac{1}{\sqrt{2}}(|B^0\rangle \pm |\bar{B}^0\rangle), \eqno(43)$$
where we used the phase convention
$$CP|B^0\rangle = |\bar{B}^0\rangle, \quad CP|\bar{B}^0\rangle = |B^0\rangle, \eqno(44)$$
such that
$$CP|B_{L,H}\rangle = \pm |B_{L,H}\rangle. \eqno(45)$$
$^2$Note that our phase conventions differ from [7] by a sign. The results in [7] are obtained by replacing $q \to -q, |\bar{B}^0\rangle \to -|\bar{B}^0\rangle$.

That is, the mass eigen-states are maximally mixed, exactly what we are used to for eigenstates of the matrices of the form in Eq. (42).
For $B^0 - \bar{B}^0$ meson system the discussion deviates from the above results in two important ways. The first complication is that the CP is violated (but CPT still conserved). Then $M_{12} \neq M_{21}$, while $M_{11} = M_{22}$, in which case the two mass eigenstates are
$$|B_{L,H}\rangle = p|B^0\rangle \pm q|\bar{B}^0\rangle. \eqno(46)$$
For CP conserving case $p = q = 1/\sqrt{2}$.
The other complication is that $B^0$ and $\bar{B}^0$ decay. We can describe this through a non-unitary evolution of a two-state system, given by a non-hermitian Hamiltonian
$$\mathcal{H} = M + i\Gamma, \eqno(47)$$
so that the time evolution of a two-state system is described by
$$i\frac{d}{dt} \begin{pmatrix} |B^0(t)\rangle \\ |\bar{B}^0(t)\rangle \end{pmatrix} = \mathcal{H} \begin{pmatrix} |B^0(t)\rangle \\ |\bar{B}^0(t)\rangle \end{pmatrix} = \begin{pmatrix} M_{11} + i\Gamma_{11}, & M_{12} + i\Gamma_{12} \\ M_{21} + i\Gamma_{21}, & M_{22} + i\Gamma_{22} \end{pmatrix} \cdot \begin{pmatrix} |B^0(t)\rangle \\ |\bar{B}^0(t)\rangle \end{pmatrix}. \eqno(48)$$
The $\Gamma$ matrix encodes the effects of $B^0$ and $\bar{B}^0$ decays on the time evolution. The non-unitary evolution describes the "disappearance" of $B^0$ and $\bar{B}^0$ states due to decays into final particles, i.e., outside of the two-state system, $|B^0\rangle, |\bar{B}^0\rangle$. The eigenstates of $\mathcal{H}$ are still given by Eq. (46), though now in general $|B_L\rangle$ and $|B_H\rangle$ are no longer orthogonal.
### 3.3 Different ways of measuring the CP violation
CP violation is an inherently quantum mechanical effect. As we saw in Section 2.8 it is intimately tied to the existence of a physical phase in the Lagrangian. In order to be sensitive to a phase an interference is needed. Thus, CP violating observables necessarily require some kind of interference. Depending on the type of interference there are three distinct categories of CP violating observables
1. *CPV in the decay*, also called *direct CPV*, occurs when there is interference between different contributions to the decay amplitudes so that
$$|A_f| \neq |\bar{A}_f|. \eqno(49)$$
Here we used the short-hand notation
$$A_f \equiv \langle f|\mathcal{H}|B^0\rangle, \quad \bar{A}_f \equiv \langle f|\mathcal{H}|\bar{B}^0\rangle. \eqno(50)$$
2. *CPV in mixing* occurs when there is interference between $M_{12}$ and $\Gamma_{12}$ in the time evolution of the two-state system. This arises when
$$|q/p| \neq 1, \eqno(51)$$
and corresponds to interference between different ways to oscillate between $B^0$ and $\bar{B}^0$ states, either through dispersive matrix elements or through absorptive ones.
3. *CPV in interference between decays with and without mixing*, arises when
$$\text{Im } \lambda_f \neq 0 \eqno(52)$$
where
$$\lambda_f \equiv \frac{q}{p} \frac{\bar{A}_f}{A_f}. \eqno(53)$$
Here the interference is between two different paths of $B^0$ to decay to the final states $f$, see Fig. 9. The two paths are either through direct decay, proportional to $A_f$, or by first oscillating to $\bar{B}^0$, which then decays to $f$, giving a contribution proportional to $(q/p)\bar{A}_f$.

INTRODUCTION TO FLAVOUR PHYSICS
![Diagram showing paths for a $B^0$ meson to decay to a final state $f$. Left: $B^0 \to f$ with amplitude $A_f \equiv \langle f|\mathcal{H}|B^0\rangle$ and $B^0 \xrightarrow{\text{oscill.}} \bar{B}^0 \to f$ with amplitude $\bar{A}_f \equiv \langle f|\mathcal{H}|\bar{B}^0\rangle$. Right: $B \to f$ via two paths with amplitudes $a_1 e^{i\phi_1 + i\delta_1}$ and $a_2 e^{i\phi_2 + i\delta_2}$.]
**Fig. 9:** Left: The two different paths for a $B^0$ meson to decay to a final sate $f$. Right: two interfering amplitudes are required to have direct CPV.
In the next few subsections we will look at two examples: the CPV in the decay, essential to measure the angle $\gamma$ of the standard CKM unitarity triangle, and the determination of angle $\beta$, which relies on the CPV in interference between decays with and without mixing for $B_d$ mesons.
When discussing CPV, it is important to remember that not all of the phases are CP violating. An elementary example is the double slit experiment, in which the interference pattern arises because there is a phase difference between two waves due to different paths, $e^{i\delta} = e^{ik\Delta r}$. This phase difference is not CP violating, since it does not depend on whether the double slit experiment is done with particles or antiparticles.
We thus distinguish two different types of phases. The *weak phases* are the (physical) phases that appear in the Lagrangian. The weak phases violate CP, just as the CKM phase in the weak interaction part of the SM Lagrangian violates CP. The *strong phase* is the name used for CP conserving phases. An example of such a strong phase is, for instance, the phase shift resulting from rescattering of particles due to QCD/strong interactions. Imagine a thought experiment, in which we collide two pion beams with the total center of mass energy close to the rho meson mass. The $\pi^+ \pi^0 \to \rho^+ \to \pi^+ \pi^0$ and $\pi^- \pi^0 \to \rho^- \to \pi^- \pi^0$ scatterings both result in the same complex Breit-Wigner scattering amplitude
$$
A \propto \frac{1}{p^2 - m^2 + im\Gamma}. \eqno(54)
$$
The imaginary term in the propagator is due to on-shell rescattering through decay products of $\rho$. These are CP conserving processes, and so is the resulting phase, $\arg(A)$. This phase does not change sign, when we exchange $\pi^+ \leftrightarrow \pi^-$.
### 3.4 CPV in the decay
We start with the CPV in the decay (or the so called direct CP violation). The CPV observable is the decay asymmetry
$$
\mathcal{A}_f \equiv \frac{\Gamma(\bar{B} \to \bar{f}) - \Gamma(B \to f)}{\Gamma(B \to f) + \Gamma(B \to f)} = \frac{1 - |A_f/\bar{A}_f|^2}{1 - |A_f/\bar{A}_f|^2}, \eqno(55)
$$
where $A_f$ are defined in (50). In order to have non-vanishing CP asymmetry, $\mathcal{A}_f \neq 0$, the $B \to f$ decay amplitude needs to receive contributions from (at least) two different terms with differing weak, $\phi_{1,2}$, and strong phases, $\delta_{1,2}$, see also Fig. 9 (right)
$$
A_f = a_1 e^{i\phi_1 + i\delta_1} + a_2 e^{i\phi_2 + i\delta_2}, \eqno(56)
$$
$$
\bar{A}_f = a_1 e^{-i\phi_1 + i\delta_1} + a_2 e^{-i\phi_2 + i\delta_2}. \eqno(57)
$$
The weak phases are due to the CKM phase in the SM Lagrangian and change the sign under CP transformation, while the strong phases are due to on-shell rescattering of particles (pions, etc) and are thus

![Fig. 10: The two interfering amplitudes in the $B^- \to D[\to f]K^-$ decays. The decay amplitudes for CP conjugate decay $B^+ \to D[\to \bar{f}]K^+$ are obtained by exchanging $\{B^-, K^-, f\} \to \{B^+, K^+, \bar{f}\}$, $D^0 \leftrightarrow \bar{D}^0$, and $\gamma \to -\gamma$ in the above.](https://example.com/image.png)
**Fig. 10**: The two interfering amplitudes in the $B^- \to D[\to f]K^-$ decays. The decay amplitudes for CP conjugate decay $B^+ \to D[\to \bar{f}]K^+$ are obtained by exchanging $\{B^-, K^-, f\} \to \{B^+, K^+, \bar{f}\}$, $D^0 \leftrightarrow \bar{D}^0$, and $\gamma \to -\gamma$ in the above.
CP even, the same as QCD interactions. The CP asymmetry is, in the simplifying limit $a_2/a_1 \ll 1$,
$$\mathcal{A}_f = \frac{a_2}{a_1} \sin(\phi_2 - \phi_1) \sin(\delta_2 - \delta_1) + \mathcal{O}(a_2^2/a_1^2). \eqno(58)$$
The CP asymmetry vanishes in the limit where either (i) there is only one contribution to the amplitude, $a_2 \to 0$, and/or (ii) if the weak phase difference vanishes, $\phi_2 - \phi_1 \to 0$, and/or (iii) if the strong phase difference vanishes, $\delta_2 - \delta_1 \to 0$.
### 3.5 Measuring the CKM angle $\gamma$
The measurements of CKM unitarity triangle angle $\gamma$ use the decays in which there is interference between $b \to c\bar{u}s$ and $b \to u\bar{c}s$ transitions [23–26]. This happens for instance in the $B^- \to [D \to f]K^-$ decay chain. The $B^- \to D^0K^-$ decay is due to the $b \to c\bar{u}s$ transition, while the $B^- \to \bar{D}^0K^-$ decay is mediated by the $b \to u\bar{c}s$ transition, which is proportional to $V_{ub} \propto e^{-i\gamma}$, see the top two diagrams in Fig. 6. If the $D^0$ and $\bar{D}^0$ decay to the same final state, such as $f = \pi^+\pi^-, K^+K^-, K_S\pi^+\pi^-$, the two decay amplitudes interfere, giving sensitivity to the phase $\delta_B - \gamma$. Our notation is defined in Fig. 10, with $\delta_{B,D}$ the strong phases, while $\gamma$ is a weak phase and changes sign under CP conjugation.
In order to extract $\gamma$ both the rates for $B^- \to [D \to f]K^-$ and its CP conjugated mode $B^+ \to [D \to \bar{f}]K^+$ need to be measured. The interference terms in the two rates are proportional to $\delta_B + \delta_D - \gamma$ and $\delta_B + \delta_D + \gamma$, respectively. The difference of the two thus gives the quantity we are after, $\gamma$, if the hadronic parameters, $A_{B,D}, r_{B,D}, \delta_{B,D}$, are known. Note that the direct CPV asymmetries, Eq. (55),
$$\mathcal{A}_f \propto r_B r_D \sin(\delta_B + \delta_D) \sin \gamma, \eqno(59)$$
are crucial. If $\mathcal{A}_f$ vanish, so thus the sensitivity to $\gamma$. The measurement of $\gamma$ requires both $r_{B,D}$ and the strong phases to be nonzero.
Amazingly, all the hadronic inputs can be measured experimentally. The $A_D$ and $r_D$ are obtained from $D^{*+} \to [D^0 \to f]\pi^+$ decays where the charge of $\pi^+$ tags the flavour of $D^0$, i.e., $\bar{D}^0$ would be accompanied by a $\pi^-$. Choosing $N_f$ different final states leaves us with $4 + N_f$ unknowns: $\gamma, A_{B,D}, r_{B,D}, \delta_{B,D}$. On the other hand, we can measure $2N_f$ decay branching ratios, $B^- \to [D \to f]K^-$ and $B^+ \to [D \to \bar{f}]K^+$ (taking $f$ not to be CP conjugate final state for simplicity, such as bins in $K_S\pi^+\pi^-$ Dalitz plot). For $N_f \ge 4$ there is enough information to extract all the unknowns. The situation is in fact even better, since $\delta_D$ can be measured at CLEO and BESS III from entangled decays $\psi(3770) \to D^0\bar{D}^0$, improving the precision with which $\gamma$ is extracted.

INTRODUCTION TO FLAVOUR PHYSICS
![Figure 11: Left: the time dependent $\bar{B}^0(t) \to J/\psi K_S$ (orange) and $B^0(t) \to J/\psi K_S$ (blue) decay rates. Right: the time dependent CP asymmetry.](https://i.imgur.com/example.png)
**Fig. 11:** Left: the time dependent $\bar{B}^0(t) \to J/\psi K_S$ (orange) and $B^0(t) \to J/\psi K_S$ (blue) decay rates. Right: the time dependent CP asymmetry (taken from [30]).
That all the hadronic uncertainties can be obtained experimentally makes this approach a very powerful tool. It means that the angle $\gamma$ can be extracted with basically no theory uncertainties. The theoretical corrections arise only from one loop electroweak corrections, limiting the ultimate precision with which $\gamma$ can be extracted up to minuscule $\gamma_{\text{th}} < 10^{-7}$ [27, 28]. The experimental error bars will be larger than this for a long time. At present they are at $\delta\gamma \lesssim 6^\circ$ [29].
### 3.6 CPV in interference between decays with and without mixing
The state that is created at $t = 0$ as the $\bar{B}^0$ [or $B^0$] time evolves according to
$$
\frac{d}{dt}\Gamma(\bar{B}^0(t)[B^0(t)] \to f_{\text{CP}}) \propto e^{-\Gamma t} \left[ \frac{1}{2} \left( 1 + |\lambda_f|^2 \right) \pm S_f \sin(\Delta m t) \mp C_f \cos(\Delta m t) \right],
$$ (60)
with,
$$
S_f \equiv \frac{2 \text{Im} \lambda_f}{1 + |\lambda_f|^2}, \qquad C_f \equiv \frac{1 - |\lambda_f|^2}{1 + |\lambda_f|^2}.
$$ (61)
Here we assumed for simplicity that the final state is a CP eigenstate, $f_{\text{CP}}$, such as $f_{\text{CP}} = J/\psi K_S$. We also used that the mass splitting between the two mass eigenstates is much bigger than the difference between the two decay widths, $\Delta\Gamma \ll \Delta m$, so that it can be neglected, setting $|q/p| = 1$. The time evolution is plotted in Fig. 12 (left). The exponential decay is modulated by an oscillatory behaviour as $B^0$ converts to $\bar{B}^0$ and back (and vice versa), with the frequency of the oscillations given by the mass splitting, $\Delta m$.
The difference between the two decay rates is the time dependent CP asymmetry
$$
\mathcal{A}_{f_{\text{CP}}}(t) \equiv \frac{\frac{d}{dt}\Gamma[B^0(t) \to f_{\text{CP}}] - \frac{d}{dt}\Gamma[\bar{B}^0(t) \to f_{\text{CP}}]}{\frac{d}{dt}\Gamma[\bar{B}^0(t) \to f_{\text{CP}}] + \frac{d}{dt}\Gamma[B^0(t) \to f_{\text{CP}}]},
$$ (62)
and is described by a purely oscillatory behaviour, see Fig. 12 (right),
$$
\mathcal{A}_{f_{\text{CP}}}(t) = S_f \sin(\Delta m t) - C_f \cos(\Delta m t).
$$ (63)
The coefficient of $\cos(\Delta m t)$ is nonzero, if there is direct CPV, since $C_f = -A_f$ for $|q/p| = 1$. The coefficient of $\sin(\Delta m t)$ is nonzero if there is CPV in interference between decays with and without mixing, cf. Eqs. (52) and (61). We will see that $S_f$ is an important observable in searches for New Physics (NP). In the SM it is a measure of the CKM unitarity triangle angle $\beta$.

### 3.7 The measurement of angle $\beta$
The $q/p$ does not depend on the final state $f$, and is the property of the $B^0 - \bar{B}^0$ system. In the SM it is given by the ratio of one loop diagram in Fig. 8 and its complex conjugated version, so that
$$\frac{q}{p} = e^{-i\phi_B} = \frac{V_{tb}^* V_{td}}{V_{tb} V_{td}^*}, \eqno(64)$$
with hadronic matrix elements cancelling in the ratio.
The decay amplitudes $A_f, \bar{A}_f$ do depend on the final state. However, a simplification occurs for $B^0 \rightarrow J/\psi K_S$ and other decays that are dominated by a single amplitude, in this case due to the tree level $b \rightarrow c\bar{c}s$ transition. In the ratio $\bar{A}_f / A_f$ the hadronic matrix elements largely cancel. To a good approximation it is given by the ratio of the CKM elements
$$\frac{\bar{A}_{J/\psi K_S}}{A_{J/\psi K_S}} = \eta_f \frac{V_{cb} V_{cs}^*}{V_{cb}^* V_{cs}} + \dots, \eqno(65)$$
with $\eta_f = -1$ the CP of $J/\psi K_S$, and the ellipses the corrections due to penguin diagrams that depend on a different product of CKM elements. Therefore,
$$\lambda_{J/\psi K_S} = \eta_f \frac{V_{tb}^* V_{td} V_{cb} V_{cs}^*}{V_{tb} V_{td}^* V_{cb}^* V_{cs}} = \eta_f e^{-i2\beta}, \eqno(66)$$
and thus
$$\text{Im} \lambda_{J/\psi K_S} = \sin 2\beta. \eqno(67)$$
The measurement of $\sin 2\beta$ was the flagship measurement of the $B$ factories which showed that the CP violating phase in the SM is large, cf. Fig. 5.
### 4 New Physics searches
So far we looked at the measurements of the SM parameters. We now turn to a different question: how does one search for New Physics (NP)? Before we tackle this question let us first answer a seemingly unrelated question: why is the weak force weak? The weak and strong interactions are similar in many respects. They are both nonabelian gauge interactions, and at high energies, of a few 100 GeV, they even have coupling constants that are not that different in size. However, at low energies they exhibit very different strengths. The strong force gives rise to a strong binding potential, while the weak force results only in a very weak short range potential. The decays that proceed through strong interactions such as $\rho^+ \rightarrow \pi^+ \pi^0$ occur at time scales $\sim 10^{-23}$ s, while the weak decays are much slower, from $\sim 10^{-12}$ s for $B$ decays to hundreds of seconds in the case of neutron beta decay.
The reason for this disparity is that the strength of the interaction is governed both by the size of the couplings and the mass of the force carriers. The more massive the carrier the shorter the range of the potential, and the weaker the interaction at low energies. The weak force is weak because the force carriers, $W$ and $Z$ are heavy, with masses equal to 80.4 GeV and 91.2 GeV, respectively. The neutron beta decay width is highly suppressed, because the available energy in the decay, $\sim (m_p - m_n)$ up to corrections from electron mass, is much smaller than the mass of the force carrier, the $W$ boson,
$$\Gamma(n \rightarrow pe\bar{\nu}_e) \propto \frac{(m_p - m_n)^5}{m_W^4} \sim 10^{-20}(m_p - m_n). \eqno(68)$$
This detour lead us to an important insight: through rare (or slowly occurring) processes we can probe heavy mediators. Historically, the weak nuclear decays were the first sign of a new force with a heavy mediator, the $W$ boson. Other processes could, in a similar way, hint at new forces beyond the

INTRODUCTION TO FLAVOUR PHYSICS
[Image: Feynman diagram showing neutron beta decay: $n \to p + W^- \to p + e^- + \bar{\nu}_e$]
**Fig. 12:** The neutron beta decay proceeds through a tree level exchange of the $W$ boson.
SM. We thus arrived at the recipe for indirect searches: identify processes that are rare in the SM and then search for deviations from the SM predictions.
A good target are the Flavour Changing Neutral Current (FCNC) processes. In the SM there are no FCNCs at tree level – the gluon, photon, $Z$, and Higgs tree level exchanges are strictly flavour conserving, cf. Fig. 2. The FCNC processes, such as meson mixings, arise only at loop level and are thus suppressed, see Section 2.6. The FCNC processes can be easily modified by NP, either through tree level or loop level NP contributions. Taking $B_s$ mixing as an example the tree level NP contributions will have the form $\propto g_{sb}^2/M_{\text{NP}}^2$, where $g_{sb}$ is the NP coupling to $b$ and $s$ quarks, and $M_{\text{NP}}$ the mass of the new mediator. The NP contributions thus vanish if the NP is very heavy, $M_{\text{NP}} \to \infty$, or if the flavour violating coupling constants are small, $g_{sb} \to 0$.
In the rest of this section we explore in more detail the two main ways of searching for beyond the SM physics in flavour: by measuring the meson mixing amplitudes, and by measuring rare decays such as $b \to s \ell^+ \ell^-$.
### 4.1 New physics searches using meson mixings
There are four neutral meson systems that mix through weak interactions at 1 loop: $K^0 - \bar{K}^0$ ($\bar{s}d \leftrightarrow s\bar{d}$), $D^0 - \bar{D}^0$ ($c\bar{u} \leftrightarrow u\bar{c}$), $B^0 - \bar{B}^0$ ($b\bar{d} \leftrightarrow d\bar{b}$), and $B^0_s - \bar{B}^0_s$ ($\bar{b}s \leftrightarrow b\bar{s}$). We will mainly focus on $B^0 - \bar{B}^0$ and $B^0_s - \bar{B}^0_s$ systems, which are dominated by the $W$-top quark loop, Fig 8.
Since $m_{t,W} \gg m_B$ the top and $W$ can be integrated out, leading to the $B_d - \bar{B}_d$ mixing effective weak Hamiltonian [7]
$$\mathcal{H}_{\text{eff}}^d = \frac{G_F^2}{16\pi^2}m_W^2 \eta_{B S_0} \left(V_{tb}^* V_{td}\right)^2 (\bar{b}d)_{V-A}(\bar{b}d)_{V-A} + \text{h.c.}, \eqno(69)$$
where $G_F \simeq 1.166 \cdot 10^{-5} \text{ GeV}^{-2}$ is the Fermi constant, and $\eta_{BS_0} \simeq 1.26$ is the product of a properly normalized loop function and the QCD correction factor. The effective weak Hamiltonian is local, i.e., it corresponds to the potential that acts only at a point. This is a result of taking the weak mediators to be infinitely heavy. Another way of writing the effective Hamiltonian is
$$\mathcal{H}_{\text{eff}}^d = \frac{1}{\Lambda_{\text{MFV}}^2} \left(V_{tb}^* V_{td}\right)^2 (\bar{b}_L \gamma^\mu d_L) (\bar{b}_L \gamma_\mu d_L) + \text{h.c.}, \eqno(70)$$
where the dimensionful prefactor,
$$\Lambda_{\text{MFV}} = \frac{2\pi}{G_F m_W \sqrt{\eta_{BS_0}}} \simeq 6.0 \text{ TeV}, \eqno(71)$$
is significantly larger than the weak scale, $m_W \simeq 80.2 \text{ GeV}$, because we absorbed in it the loop factor, $1/16\pi^2$ (up to a factor of 4 that went into a redefinition of the operator). For $B_s$ mixing the CKM factors in the weak vertices change, cf. Fig. 8, so that one has instead
$$\mathcal{H}_{\text{eff}}^s = \frac{1}{\Lambda_{\text{MFV}}^2} \left(V_{tb}^* V_{ts}\right)^2 (\bar{b}_L \gamma^\mu s_L) (\bar{b}_L \gamma_\mu s_L) + \text{h.c.}. \eqno(72)$$

The top and $W$ in the loop are much heavier than the available energy in the mixing – the $B$ meson mass. The top and $W$ lines in the diagram are thus always off-shell, and so the dominant diagram only contributes to the dispersive part of the mixing amplitude,
$$M_{12}^d = \frac{1}{2m_B} \langle \bar{B}_d^0 | \mathcal{H}_{\text{eff}}^d | B_d^0 \rangle^*.$$ (73)
The absorptive part of the mixing amplitude, $\Gamma_{12}$, receives contributions from the subleading amplitudes with $c$ and $u$ quarks running in the loop.
When NP is present, then $\mathcal{H}_{\text{eff}}^q = \mathcal{H}_{\text{eff},q}^{\text{SM}} + \mathcal{H}_{\text{eff},q}^{\text{NP}}$, and we can write
$$M_{12}^q = M_{12,q}^{\text{SM}} + M_{12,q}^{\text{NP}} = M_{12,q}^{\text{SM}} \left[ 1 + (A_q^{\text{NP}}/A_q^{\text{SM}}) e^{i\phi_q^{\text{NP}}} \right], \quad q = d, s,$$ (74)
for $B_d$ and $B_s$ systems, respectively. The above parametrization is completely general, as long as NP is heavy, so that it does not appear in the decays of $B_{d,s}$ mesons. There is no NP contribution, when $A_{d,s}^{\text{NP}} = 0$. If $\phi_{d,s}^{\text{NP}} \neq 0$ this means that there are new CP violating phases in the NP contribution, beyond the CKM one. At present $A_{d,s}^{\text{NP}}/A_{d,s}^{\text{SM}}$ of about 0.2 are still allowed, depending on the NP phase. With the future measurements at Belle II and LHCb this will be drastically improved to less than about 0.05, see Fig. 13.
What does this mean in terms of bounds on NP masses? Let us assume that NP has the same $(V - A) \times (V - A)$ structure as the SM, so that the effective Hamiltonian is $(q = d, s)$
$$\mathcal{H}_{\text{eff}} = \left( \frac{(V_{tb}^* V_{iq})^2}{\Lambda_{\text{MFV}}^2} + \frac{C_{\text{NP}}}{\Lambda_{\text{NP}}^2} \right) (\bar{b}_L \gamma^\mu q_L) (\bar{b}_L \gamma_\mu q_L) + \text{h.c.}$$ (75)
For instance, the new physics contribution, $C_{\text{NP}}/\Lambda_{\text{NP}}^2$ could be due to the $Z'$ exchange. This would give for the effective Hamiltonian
$$\mathcal{H}_{\text{eff}} = i(ig_{Z'})^2 (\bar{b}_L \gamma_\mu q_L) \frac{-ig^{\mu\nu}}{q^2 - m_{Z'}^2} (\bar{b}_L \gamma_\nu q_L) \rightarrow \frac{g_{Z'}^2}{2} \frac{1}{m_{Z'}^2} (\bar{b}_L \gamma^\mu q_L) (\bar{b}_L \gamma_\mu q_L),$$ (76)
where $g_{Z'}$ is the flavour violating $Z'$ coupling to quarks, $m_{Z'}$ the $Z'$ mass, and in obtaining the last expression we used that $q^2 \ll m_{Z'}^2$. For the NP Wilson coefficient we thus have
$$\frac{C_{\text{NP}}}{\Lambda_{\text{NP}}^2} = \frac{g_{Z'}^2}{m_{Z'}^2}.$$ (77)
If $g_{Z'} = 1$, then $\Lambda_{\text{NP}}$ can be identified with $m_{Z'}$ for $C_{\text{NP}} = 1$.
In general NP will not have the $V - A$ structure. However, the choice of possible operator structure is still quite limited. The general dimension 6 operator basis for meson mixing contributions is [32]
$$\mathcal{H}_{\text{eff}}^{\text{NP}} = \sum_i \frac{C_i}{\Lambda_{\text{NP}, B_q}^2} Q_{i,q},$$ (78)
where
$$\begin{aligned} Q_{1,q} &= (\bar{b}_L \gamma^\mu q_L) (\bar{b}_L \gamma_\mu q_L), \\ Q_{2,q} &= (\bar{b}_R q_L) (\bar{b}_R q_L), \\ Q_{3,q} &= (\bar{b}_R^\alpha q_L^\beta) (\bar{b}_R^\beta q_L^\alpha) \\ Q_{4,q} &= (\bar{b}_R q_L) (\bar{b}_L q_R), \\ Q_{5,q} &= (\bar{b}_R^\alpha q_L^\beta) (\bar{b}_L^\beta q_R^\alpha), \end{aligned}$$ (79)

![Fig. 13](https://placeholder-image-url)
**Fig. 13:** Present (upper panels) and future (lower panels) constraints, at the end of Belle II, with $50\text{ ab}^{-1}$ of integrated luminosity, and LHCb with $300\text{ fb}^{-1}$, on the NP contributions to the $B_d$ (left) or $B_s$ (right) mixing amplitudes [31].
along with three other operators obtained from $Q_{i,q}$, $i = 1, 2, 3$ by replacing $L \leftrightarrow R$ (the bounds on these parity related operators are the same as for $Q_{i,q}$, $i = 1, 2, 3$, though). The operators for other meson systems are obtained through trivial replacements of quark flavours. Taking $|C_i| = 1$, the present bounds on the NP scale, $\Lambda_{\text{NP}}$ are shown with lighter colors in Fig. 14 (left). The future projections to the end of LHCb Upgrade II are shown with darker colors. A jump in the mass reach is clearly visible even on the logarithmic scale.
Different colours in Fig. 14 denote different meson systems: green bars denote the constraints from $K^0 - \bar{K}^0$ mixing, yellow from $D^0 - \bar{D}^0$ mixing, in both cases assuming maximal new weak phase relative to the SM; orange bar denotes constraints from $B^0 - \bar{B}^0$, marginalized over the weak phase; red (blue) from $B^0_s - \bar{B}^0_s$ system assuming no (maximal) NP phase. Extraction of constraints from $K - \bar{K}$ and $D - \bar{D}$ mixing is more complicated than for $B_q - \bar{B}_q$, since in these two cases the long distance contributions from light quarks running in the loop are important.
The bounds on $\Lambda_{\text{NP}}$ are strikingly different for the various meson systems. This is easy to understand by considering the CKM suppression of the SM contributions, since the precision of experimental measurements and theoretical predicitions is typically at a fraction of the SM amplitude. Demanding for illustration that the contribution from NP is at most $20\%$ of the short-distance SM this would give, for

![Fig 14: Two bar charts showing NP scale $\Lambda$ (TeV) vs $C_1, C_2, C_3, C_4, C_5$. Left panel shows scales up to $10^7$ TeV, right panel shows scales from $10^{-1}$ to $10$ TeV. Both are labeled with UTfit.]
**Fig. 14:** Present constraints (lighter) and expected constraints at the end of LHCb upgrade II (darker) on the NP scale, $\Lambda_{\text{NP}}$, from the UTfit NP analysis for different meson systems. The right panel shows constraints assuming NP is weakly coupled, has MFV structure of couplings, and enters observables only at one loop, see text for details (from [11]).
the operator $Q_{1,q}$
$$\begin{aligned} \text{for NP}=20\% \text{ SM, } \quad K - \bar{K} : \quad \left( \frac{V_{ts}^*}{ \lambda^2} \frac{V_{td}}{\lambda^3} \right)^2 \quad \Rightarrow \quad \Lambda_{\text{NP}} \gtrsim 4 \cdot 10^4 \text{ TeV,} \\ \text{for NP}=20\% \text{ SM, } \quad B_d - \bar{B}_d : \quad \left( \frac{V_{tb}^*}{1} \frac{V_{td}}{\lambda^3} \right)^2 \quad \Rightarrow \quad \Lambda_{\text{NP}} \gtrsim 1.5 \cdot 10^3 \text{ TeV,} \\ \text{for NP}=20\% \text{ SM, } \quad B_s - \bar{B}_s : \quad \left( \frac{V_{tb}^*}{1} \frac{V_{ts}}{\lambda^2} \right)^2 \quad \Rightarrow \quad \Lambda_{\text{NP}} \gtrsim 3 \cdot 10^2 \text{ TeV.} \end{aligned} \eqno(80)$$
roughly in agreement with the constraints shown in Fig. 14.
Note that the interpretation of the bounds in term of NP scale crucially depends on the assumed flavour structure in the dimensionless Wilson coefficient, $C_i$. If the NP contribution also follows the SM CKM suppression, this is referred to as Minimal Flavour Violation (MFV). Fig. 14 (right) shows the bounds for the case of MFV type NP running in the loop, i.e., the Wilson coefficients were set to $\mathcal{C}_a = (V_{ti}^* V_{tj})^2 g^4 / 16\pi^2$, with $V_{ti}, V_{tj}$ the appropriate SM CKM coefficients, and $g$ the weak coupling constant. We see that even for a weakly coupled NP that has the MFV flavour structure and only contributes at 1 loop, the bounds are in the few 100 GeV to few TeV range.
### 4.2 New physics searches using rare decays
We turn next to the other main pathway for searching for new physics - searching for deviations in rare decays. Here the benefit is that there are many observables in flavour physics: the branching ratios, asymmetries, distributions, ... There is also a choice of different parent particles as well as many possible final states. The abundance of observables is clearly illustrated by opening the “bible” of particle physics, the Particle Data Group (PDG) book [15]. Even the condensed version, the PDG booklet, clocks out at more than 170 pages.
To shorten the discussion we will focus on the processes that are at present showing deviations from the SM expectations. The present experimental situation can then succinctly be described in the

INTRODUCTION TO FLAVOUR PHYSICS
![Feynman diagrams showing SM and NP contributions to $b \to s\mu^+\mu^-$](https://via.placeholder.com/500x150)
**Fig. 15:** A representative SM diagram for $b \to s\mu^+\mu^-$ transition (left), and the representative loop level NP contributions (middle and right).
following way. There are many different transitions that were measured, all of which agree with the SM expectations within experimental and theoretical errors. There are only two sets of quark level transitions that are showing $\sim 4\sigma$ deviations from the SM: the $b \to c\tau\nu$ and $b \to s\mu^+\mu^-$ transitions.$^3$ The apparent NP scale that explains the deviations is quite different in the two cases. For instance, if the NP is due to the following $V - A$ operator
$$\mathcal{L}_{\text{NP}} \supset \frac{1}{\Lambda_{\text{NP}}^2} \left( Q_i \gamma^\mu \sigma^A Q_j \right) \left( \bar{L}_k \gamma_\mu \sigma^A L_l \right), \eqno(81)$$
then $\Lambda_{\text{NP}} \sim 3 \text{ TeV}$ in order to explain the deviations in $b \to c\tau\nu$ transitions, and $\Lambda_{\text{NP}} \sim 30 \text{ TeV}$ in order to explain the $b \to s\mu^+\mu^-$ anomalies. We discuss next the possible NP explanations for each of the two.
### 4.3 New physics searches in $b \to s\mu^+\mu^-$ transitions
The upshot of the observed $b \to s\mu^+\mu^-$ anomaly is: choosing only the theoretically clean observables the excess is at the $\sim 4\sigma$ level. From the NP perspective the scale required to explain the anomaly makes sense, since it is high enough to avoid many of the experimental constraints. The models that explain the anomaly do, however, face I.I. Rabi's question: "Who ordered that?", when the muon was first discovered [36].
The FCNC $b \to s\ell^+\ell^-$ transitions are generated at 1-loop in the SM. A representative diagram in the SM is shown in Fig. 15 (left). Integrating out the heavy degrees of freedom, $W, Z, t$, gives the following effective Hamiltonian [37–39]
$$\mathcal{H}_{\text{eff}} = G_F V_{tb} V_{ts}^* \frac{\alpha}{4\pi} \left[ C_9 (\bar{s}_L \gamma^\mu b_L) (\bar{\ell} \gamma_\mu \ell) + C_{10} (\bar{s}_L \gamma^\mu b_L) (\bar{\ell} \gamma_\mu \gamma_5 \ell) \right], \eqno(82)$$
where in the SM $C_9^{\text{SM}} \simeq -C_{10}^{\text{SM}}$, i.e., the SM diagrams give to a good approximation a $V - A$ structure of the leptonic current.
Another prediction of the SM is that the rates for the $b \to se^+e^-$ and $b \to s\mu^+\mu^-$ transitions should be equal to each other as soon as we are reasonably far above the muon production threshold so that the effect of muon mass on the available phase space can be neglected. The SM prediction of Lepton Flavour Universality (LFU) is deeply engrained in the structure of the theory, since it is a consequence of the fact that the electroweak gauge group is the same for all three generations.
The prediction of LFU can be tested experimentally by forming theoretically clean observables such as the ratios of $b \to s\mu\mu$ to $b \to see$ rates,
$$R_{K^{(*)}} = \frac{Br(B \to K^{(*)} \mu\mu)}{Br(B \to K^{(*)} ee)}. \eqno(83)$$
$^3$There are other interesting deviations, e.g., the $\sim 3\sigma$ deviation in $\epsilon'/\epsilon$, see, e.g., [33–35].

![Fig 16: A contour plot showing the fit for NP contributions $C_{9,10}^\mu$ to Wilson coefficients. The y-axis is $\text{Re } C_{10}$ and the x-axis is $\text{Re } C$. Red contours represent LFU only observables, and blue contours represent all observables.](https://placeholder-url.com/image.png)
**Fig. 16:** The fit for NP contributions $C_{9,10}^\mu$ to Wilson coefficients in (82) from LFU only observables (red) or including all the observables (blue). The SM point is $C_{9,10}^\mu = 0$. (from [54].)
In the ratios the uncertainties from hadronic inputs (the form factors) cancel to a very good approximation. Above the muon threshold they are equal to 1 within a percent, and are also presicely predicted close to the muon threshold [40–47]. Experimentally, on the other hand $R_{K^{(*)}} \sim 0.7$ [48–51], violating LFU with a significance of $2.2 - 2.6\sigma$ in each of the three most precise measurements (the measurements are at different dilepton invariant masses). A combined significance for the discrepancy with the SM is $\sim 4\sigma$ [52–57]. The most precise measurements are due to LHCb, which dominates the world averages for $R_{K^{(*)}}$.
LFU ratios is not the only experimental information about the $b \to s \ell \ell$ transitions. In principle there is much more information available, branching ratios for different choices of initial and final state mesons, $Br(B \to K^{(*)}\mu\mu)$, $Br(B_s \to \phi\mu\mu)$, $Br(B \to X_s\mu\mu)$, angular observables in $B^0 \to K^{*0}\mu\mu$, $B_s \to \phi\mu\mu$, etc. However, the interpretation of these is much more sensitive to hadronic inputs. It requires form factor predictions (now coming from QCD sum rules), the estimate of charm loops, nonfactorizable contributions, etc. Using the best available estimates for these inputs the favored interpretation is that the NP is mostly in muons [52–57]. Furthermore, the picture obtained from such global fits to data seems to be in agreement with the LFU only determination, see Fig. 16 for a simultaneous fit to NP contributions in $C_{9,10}$.
If the anomaly is due to NP we thus already have a significant amount of information about it. First of all, there are only four dimension 6 operators that can explain $R_K$ [58]
$$\mathcal{O}_9^{(')\ell} = \frac{\alpha}{4\pi} (\bar{s}\gamma^\mu P_{L(R)}b) (\bar{\ell}\gamma_\mu\ell), \quad \mathcal{O}_{10}^{(')\ell} = \frac{\alpha}{4\pi} (\bar{s}\gamma^\mu P_{L(R)}b) (\bar{\ell}\gamma_\mu\gamma_5\ell). \eqno(84)$$
The other operators are either constrained by $B_s \to \ell\ell$ as is the case for scalar currents, or come from further suppressed dimension 8 operators before electroweak symmetry is broken, as is the case for tensor operators.
Since the $K$ and $K^*$ in the final states differ in their spin-parity quantum numbers, one is pseudoscalar, the other vector meson, the ratios $R_K$ and $R_{K^*}$ give complementary information. For instance, for the central $q^2$ bins we have [52]
$$R_K \simeq 1 + 2\frac{\text{Re}C_{bL+R(\mu-e)L}^{\text{BSM}}}{C_{bL\mu L}^{\text{SM}}}, \quad R_{K^*} \simeq R_K - 4p\frac{\text{Re}C_{bR(\mu-e)L}^{\text{BSM}}}{C_{bL\mu L}^{\text{SM}}}, \eqno(85)$$
when expanded to linear order in the BSM contributions to the Wilson coefficients (here $p \simeq 0.86$ is the polarization fraction of $K^*$). The resulting predictions for several choices of chirality in the NP

![Figure 17: Two plots showing predictions for $R_K$ vs $R_{K^*}$. The left plot is labeled "New physics in $\mu$" and the right plot is labeled "New physics in $e$". Both plots show various BSM Wilson coefficient trajectories relative to the SM point.](https://placeholder-url.com/fig17)
**Fig. 17:** The predictions for the central $q^2$ bins in $R_K$ and $R_{K^*}$ for several NP scenarios, assuming NP is only in muons (left) or only in electrons (right). The experimental values are given by the black error bars, the SM value by a point (from [52]).
contributions to the Wilson coefficients are shown in Fig. 17. Using just the "clean" observables, $R_K$ and $R_{K^*}$, NP can be either due to a deficit in muons or an increase in the electron channel. In both cases the operators with $(\bar{s}\gamma^\mu b)_L$ current can explain the anomaly, with significant freedom for the chirality of the leptonic current. For electrons also the NP due to $(\bar{s}\gamma^\mu b)_R(\bar{e}\gamma_\mu e)_R$ is possible. In this case the NP contribution enters only quadratically to a good approximation, since there is almost no interference with the SM predominantly $V - A$ leptonic current. The NP thus increases the rate for the electron channel, reducing the $R_{K^{(*)}}$ ratios below 1. It is only once additional observables, such as the absolute branching ratios, are taking into account that the possibility of NP right-handed currents is disfavored. These additional observables do require theoretical inputs

![Feynman diagrams showing SM and NP contributions to $b \to c\tau\nu$ and $b \to s\mu\mu$ transitions]
**Fig. 18:** The SM diagrams for $b \to c\tau\nu$ transition (left), and the possible tree level NP contributions to $b \to c\tau\nu$ or $b \to s\mu\mu$ transitions (middle and right).
models with $Z'$, since this contributes at tree level, giving [59, 63]
$$\frac{g_{bsZ'}}{m_{Z'}} \lesssim \frac{0.01}{2.5\text{ TeV}}.$$ (87)
Thus a 2.5 TeV $Z'$ has to have a relatively small, but not extremely small, flavour violating coupling, $g_{bsZ'} \lesssim 0.01$ (comparable, for instance, with $|V_{ts}| \simeq 0.04$). This also means that the $Z'$ has to have sizeable couplings to muons. If the coupling is to left-handed muons, this implies nontrivial constraints from neutrino trident production in neutrino scattering on nuclei, i.e., from bounds on the process $\nu N \to \nu N\mu^+\mu^-$ mediated by a $Z'$ [60, 64]. For couplings to left-handed muons the $b \to s\mu^+\mu^-$ is also accompanied by a $b \to s\bar{\nu}\nu$ signal, giving stringent constraints on the parameter space. Another important constraint are the $Z'$ searches at the LHC.
To recap, the NP explanations of the $b \to s\mu^+\mu^-$ anomaly should lead to new signals in a number of observables. The present constraints give meaningful bounds on the models already, but they are not too constraining. For instance, simply raising the mass of $Z'$ avoids the high $p_T$ constraints at the LHC. The bounds are more stringent for loop induced models [65–69], Fig. 15 (middle and right), since there the NP particles need to be lighter, below about a TeV.
### 4.4 New physics searches in $b \to c\tau\nu$ transitions
The $b \to c\tau\nu$ flavour anomaly is similarly very clean theoretically [70], and the disagreement with the SM predictions is also about $\sim 4\sigma$. However, the NP effect is large, $\mathcal{O}(20\%)$ of the SM tree level contribution given in Fig. 18 (left). This means that the scale of NP needs to be low, and consequently the NP interpretations are often in conflict with the other constraints.
The two main observables are
$$R(D^{(*)}) = \frac{\Gamma(\bar{B} \to D^{(*)}\tau\bar{\nu})}{\Gamma(\bar{B} \to D^{(*)}\ell\bar{\nu})}, \quad \ell = \mu, e,$$ (88)
where $\bar{B}^+ \sim b\bar{u}$, $D \sim c\bar{u}$, etc. The SM predictions are shown in 19. Even though these are flavour universality ratios, the SM predictions are well below 1, because the $b \to c\tau\nu$ decays have much less final state phase space available due to the large $\tau$ mass. The thing to note is that the trend $R(D^{(*)})_{\text{exp}} > R(D^{(*)})_{\text{SM}}$ is seen in several experiments. Furthermore, the theoretical predicitions are well under control. Another comment is that, since the neutrino is not seen in the experiments, it does not need to be the SM neutrino. It could be a new state, possibly even of right-handed chirality [71–74].
What kind of NP could explain this anomaly? The most obvious candidates are ruled out. Theoretical bias would have been that the new charged currents are either due to a charged Higgs, $H^+$, or a new vector boson, $W'$, see Fig. 18 (middle). The charged Higgs option is in conflict with total $B_c$ lifetime [87], the $b \to c\tau\nu$ leptonic mass distributions, and searches in $pp \to \tau^+\tau^-$ [88]. The $W'$ is

# INTRODUCTION TO FLAVOUR PHYSICS
![Fig. 19: Left panel: the measurements of $R(D)$ and $R(D^*)$ by different experiments [75–82], with the world average shown in red and the SM prediction in blue [83–86]. Right panel shows that the variation in the SM predictions is small even when some of the theoretical constraints are relaxed (from [84]).](https://example.com/image.png)
**Fig. 19**: Left panel: the measurements of $R(D)$ and $R(D^*)$ by different experiments [75–82], with the world average shown in red and the SM prediction in blue [83–86]. Right panel shows that the variation in the SM predictions is small even when some of the theoretical constraints are relaxed (from [84]).
excluded by $pp \to \tau + \text{MET}$ searches at the LHC [89], while in addition the $pp \to \tau^+ \tau^-$ in conjunction with $B$ mixing constraints exclude the related $Z'$.
There are several viable leptoquark solutions, both with SM neutrinos [90] and for right-handed neutrinos [91]. The vector leptoquark $V_1$ also allows to simultaneously explain the $b \to c \tau \nu$ and the $b \to s \mu^+ \mu^-$ anomalies [92]. A simultaneous explanation is also possible, if there are more than one scalar leptoquarks contributing [93].
### 4.5 Other modes
Besides the two quark level transitions that are showing experimental discrepancies there are a number of other rare decays that are important probes of NP. The useful rare decays are such that we can predict them precisely and that NP contributions are possible or even likely. The modes with only one final state hadron, $K \to \pi \nu \nu, B \to K \ell \ell, \dots$, fall into this category. The hadronic matrix elements for these decays are easier to predict than for the fully hadronic decays. Another example are inclusive decays, where one sums over all hadronic final states, which are also easier to predict theoretically. We look at one important example for each of these two categories.
The inclusive $b \to s \gamma$ decay is a classic example of a GIM suppressed loop induced SM process. The loop contributions that do not depend on masses of the quarks running in the loop cancel due to CKM unitarity, $M \propto \sum_i V_{ib}^* V_{is} = 0$. The first nonzero contribution is thus proportional to mass differences of the quarks on the internal line in Fig. 20 (right). The SM contribution is finite, since it is described by the effective Hamiltonian of dimension 5 [38]
$$\mathcal{H}_{\text{eff}} = -\frac{G_F}{\sqrt{2}} V_{ts}^* V_{tb} C_{7\gamma}(m_b) \frac{e}{4\pi^2} m_b (\bar{s}_L \sigma^{\mu\nu} b_R) F_{\mu\nu}. \eqno(89)$$
In the renormalizable SM Lagrangian there is no such counter-term, thus the contribution needs to be finite. The operator in (89) is chirality flipping. In the SM the chirality flip occurs on the external leg, and is thus proportional to the $b$ quark mass, $m_b$. NP contributions, on the other hand, can have the chirality flip on the internal line, leading to a relative enhancement of the NP contributions compared to the SM. This happens for instance in the Minimal Supersymmetric Standard Model (MSSM) for the gluino-squark diagram, or for the exchange of a charged Higgs in the loop. The measurements of $b \to s \gamma$ are therefore very sensitive to such NP contributions. A great theoretical effort has thus been devoted to obtain a precise theoretical prediction for the SM $b \to s \gamma$ rate [94].

![Feynman diagrams showing SM processes for $K \rightarrow \pi \nu \bar{\nu}$ and $b \rightarrow s \gamma$]
**Fig. 20:** The representative SM diagrams for $K \rightarrow \pi \nu \bar{\nu}$ (left) and $b \rightarrow s \gamma$ transitions (right).
The decays $K^+ \rightarrow \pi^+ \nu \bar{\nu}$ and $K_L \rightarrow \pi^0 \nu \bar{\nu}$ stand out, since these are one of the few rare decays in kaon sector that are the golden modes for NP searches. They are suppressed by a loop factor, CKM factors, and the GIM mechanism. They are also extremely well predicted theoretically [95]
$$
\begin{aligned}
Br(K^+ \rightarrow \pi^+ \nu \bar{\nu}) &= (8.4 \pm 1.0) \times 10^{-11}, \\
Br(K_L \rightarrow \pi^0 \nu \bar{\nu}) &= (3.4 \pm 0.6) \times 10^{-11},
\end{aligned}
\eqno(90)
$$
because the hadronic matrix elements, $\langle \pi | (\bar{s}d)_{V-A} | K \rangle$, are known precisely – they are extracted from data on $K^+ \rightarrow \pi^0 e^+ \nu$ using isospin symmetry. The largest uncertainties are from the CKM inputs, $V_{cb}$ and $\gamma$, which will be improved in the future.
The experimental challenge is that the two processes are very rare. They are set to be measured by the NA62 experiment at CERN [96], and KOTO at J-PARC [97], respectively, even if the rates are at the SM values. On the positive note, since these decays are so suppressed, the scales probed are very high, $\sim 10^3$ TeV for $Z'$ models with $\mathcal{O}(1)$ couplings. On top of this, $K_L \rightarrow \pi^0 \nu \bar{\nu}$ is also CP violating.
### 4.6 The future of NP searches with rare decays
The NP searches with rare decays, as well as the tests of the CKM unitarity will receive a significant boost with the upcoming Belle II and LHCb upgrades. Belle II expects to collect 50 times the Belle dataset. First collisions were seen in May 2018, and the first $B$ physics run is expected in March 2019. LHCb after upgrade II aims for roughly 100 times the present data set with an upgraded detector. A rule of thumb on the improved NP reach gives, for instance for Belle II, that the reach in $\Lambda_{\text{NP}}$ will be improved by $\sim \sqrt[4]{50} = 2.7\times$. Similar if not larger increase applies to LHCb Upgrade II sensitivity improvements. This is a similar jump in energy reach as going from 13TeV LHC to a 35TeV LHC!
Among other things this also means that, if the two anomalies discussed in Sections 4.3, 4.4 are not mere statistical fluctuations, we should have available measurements with $5\sigma$ significance in a relatively near future.
### 5 Higgs and flavour
In the SM all flavour structure is due to the Higgs Yukawa couplings, $y_f = \sqrt{2}m_f/v$. The very hierarchical values of fermion masses therefore imply similarly very hierarchical Yukawa couplings. How well have we tested this? There are a number of tests that are experimentally accessible to different degrees of accuracy [98]
1. proportionality: is $y_{ii} \propto m_i$?
2. factor of proportionality: is $y_{ii}/m_i = \sqrt{2}/v$?
3. diagonality (flavour violation): is $y_{ij} = 0$ for $i \neq j$?
4. reality (CP violation): is $\text{Im}(y_{ij}) = 0$?
Each of these questions probes a slightly different set of NP models. The proportionality, $y_{ii} \propto m_i$, and factor of proportionality, $y_{ii}/m_i = \sqrt{2}/v$, are relatively well tested for 3rd generation fermions, i.e.,

![Fig. 21: The constraints on the Higgs flavour violating couplings to $\tau\mu$ (left) and $\tau e$ (right) (from [105]).](https://cdn.openai.com/imagination/placeholder_fig21.png)
**Fig. 21:** The constraints on the Higgs flavour violating couplings to $\tau\mu$ (left) and $\tau e$ (right) (from [105]).
![Fig. 22: Representative diagrams for $\tau \to \mu\gamma$ induced by Higgs flavour violating couplings at 1 loop (left) and 2 loops (middle), as well as the tree level diagram leading to $\tau \to 3\mu$ (from [106]).](https://cdn.openai.com/imagination/placeholder_fig22.png)
**Fig. 22:** Representative diagrams for $\tau \to \mu\gamma$ induced by Higgs flavour violating couplings at 1 loop (left) and 2 loops (middle), as well as the tree level diagram leading to $\tau \to 3\mu$ (from [106]).
the Higgs couplings to top, bottom and tau. Experimentally much more difficult question is how Higgs couples to the first two generations. This is difficult to address since the SM Yukawa couplings are so small. A more modest question is: can we show that the couplings are hierarchical? The answer is already now a positive one, though for quarks this is achieved with some assumptions. Experimentally [99–102],
$$ \frac{Y_{e(\mu)}^{\text{exp}}}{Y_{\tau}^{\text{exp}}} < 0.22(0.10), \quad \frac{Y_{u(c)}^{\text{exp}}}{Y_{t}^{\text{exp}}} \lesssim 0.04, \quad \frac{Y_{d(s)}^{\text{exp}}}{Y_{t}^{\text{exp}}} < 0.7(6), \eqno(91) $$
where the bounds for leptons come from direct measurements, on up quarks from a global fit, and on down quarks from Higgs $p_T$ distributions (global fit).
Pushing these bounds to the SM values would be very challenging, if not impossible. The one bright exception is the muon Yukawa, which will become accessible at the high-luminosity LHC as the only one among the first two generations of fermions [103]. This is quite exciting, since it is easy to imagine that part of the muon mass comes not from the SM Higgs vev, but from new small sources of the electroweak breaking (see, e.g., [104]). The muon Yukawa could deviate significantly from the SM, in the extreme case it could even be zero.
Another important NP test are searches for flavour violating Higgs couplings. In the SM Higgs couplings are flavour diagonal (up to very small 1-loop corrections). Discovering flavour violating Higgs couplings would thus immediately mean New Physics. For charged lepton final states these couplings are accessible directly, by searching for $h \to \tau\mu, \tau e$ decays [106, 107]. The resulting bounds are shown

in Fig. 21. If the NP corrections come from dimension 6 operators then the Higgs Yukawa couplings are,
$$Y_{ij} = \frac{m_i}{v} \delta_{ij} + \frac{v^2}{\sqrt{2}\Lambda^2} \hat{\lambda}_{ij}. \eqno(92)$$
The present bounds give for the NP scale, $\Lambda_{\mu\tau} > 5.5 \text{ TeV}$, $\Lambda_{e\tau} > 4.4 \text{ TeV}$, taking $\hat{\lambda}_{ij} = 1$. The Higgs decay measurements thus already probe interesting NP scales. There are also indirect bounds on flavour violating Higgs Yukawas that come from charged lepton FCNC transition. The $\tau \to \mu\gamma$ and $\tau \to 3\mu$ are induced by the diagrams shown in Fig. 22. While these lead to less stringent constraints on flavour violating couplings of the Higgs, see Fig. 21, this is not the case for $h \to \mu e$ decays, where the bounds on $\mu \to e\gamma$ limits the branching ratio to $Br(h \to \mu e) \lesssim 10^{-8}$, barring cancellations.
# 6 Conclusions
In the SM the flavour violation and CP violation are due to the Higgs couplings to the charged fermions. Experimentally, we know that the CKM is the dominant source of flavour violation in Nature, with the CKM phase responsible for the bulk of the CP violation in quark transitions. New physics contributions at the level of $\mathcal{O}(20\%)$ of the SM amplitude are still allowed, e.g., in the meson mixing.
Most of the measured flavoured transitions agree with the SM predictions, with the possible exception of two quark level transitions, $b \to s\mu^+\mu^-$ and $b \to c\tau\nu$, which show $\sim 4\sigma$ discrepancies with the SM predictions. If true, this would imply many new signals in both high $p_T$ processes measured by CMS and ATLAS, as well as in precision flavour experiments LHCb, Belle II, NA62, KOTO, the muon $g-2$ experiment, etc.
There are many excellent reviews and books that go beyond the scope of these lectures, some of which were mentioned in the Introduction. A good starting point for exploring the scope of future flavour programmes at LHCb and Belle II can be found in [10,21], and for general flavour physics possibilities at high-luminosity LHC in [11]. A good starting point for a study of new physics models that are bounded by flavour physics measurements is the introductory book [108], or the somewhat more detailed, albeit older Ref. [8].
**Acknowledgements.** We thank the organizers of the ESHEP 2018, SSI 2018 and the US Belle II summer schools for the excellent organization and the students for the stimulating discussions. We thank Marco Ciuchini for providing the plots in Fig. 13, Jorge Martin Camalich for help with diagrams in Fig. 15, and A. Greljo for careful reading of the manuscript. We acknowledge support in part by the DOE grant de-sc0011784.
# Appendices
## A Nonzero neutrino masses
When the neutrino masses are included, the counting of physical parameters in the SM changes from what was given in Section 2.4. We show this for (i) the case that the neutrinos are Majorana fermions and (ii) the neutrinos are Dirac.
For the case of Dirac neutrinos we enlarge the SM field content, Eqs. (3), (4) by three right-handed neutrinos that are complete singlets under the SM gauge group,
$$\nu_{R,i} \sim (1,1)_0. \eqno(\text{A.1})$$
The Yukawa interaction Lagrangian is then enlarged by the
$$\mathcal{L}_{\text{Yukawa}} \supset -Y_{\nu}^{ij} \overline{L}_L^i H \nu_R^j + \text{h.c.}, \eqno(\text{A.2})$$
while we assume that the Majorana mass terms, $m_{ij} \overline{\nu_{R,i}^c} \nu_{R,j}$, are forbidden by the conservation of total lepton number which this term would violate by two units. The counting of the physical parameters for

the leptons is now completely analogous to the counting we did for the quarks in Section 2.4. Using unitary transformations
$$L_L \to V_L L_L, \quad \ell_R \to V_\ell \ell_R, \quad \nu_R \to V_\nu \nu_R, \eqno(\text{A.3})$$
one can bring the lepton Yukawa couplings to the form
$$Y_\ell = \text{diag}(y_e, y_\mu, y_\tau), \quad Y_\nu = V_{\text{PMNS}}^\dagger \text{diag}(y_\nu^1, y_\nu^2, y_\nu^3). \eqno(\text{A.4})$$
The $3 \times 3$ unitary Pontecorvo-Maki-Nakagawa-Sakata (PMNS) matrix [109, 110] is the analogue of the CKM matrix for the quarks. It has three mixing angles and one physical phase. The remaining six real parameters are the three charged lepton masses and the three neutrino masses.
This agrees with the counting of physical parameters that follows from the general rule in Eq. (18). The $Y_\ell, Y_\nu$ matrices have $2 \times (9 \text{ real} + 9 \text{ im.})$ parameters, while the three unitary matrices, $V_L, V_\ell, V_\nu$ have in total $3 \times (3 \text{ real} + 6 \text{ im.})$ parameters. Out of these one corresponds to an unbroken generator, the lepton number, under which all the lepton fields change by the same phase, $L_L \to \exp(i\phi)L_L, \ell_R \to \exp(i\phi)\ell_R, \nu_R \to \exp(i\phi)\nu_R$. Using (18) there are $2 \times 9 - 3 \times 3 = 9$ real parameters, the six leptonic masses and three PMNS mixing angles, and $2 \times 9 - (3 \times 6 - 1) = 1$ imaginary physical parameter, the phase in the PMNS matrix, as anticipated.
If the neutrinos are Majorana, the field content is the same as for the SM with neutrino masses set to zero, Eqs. (3), (4). In this case the neutrino masses come from dimension 5 Weinberg operator after the Higgs obtains a vev. In two-component notation this is
$$\mathcal{L}_{\text{eff}} \supset -\frac{c_{ij}}{\Lambda}(H^c \ell_i)(H^c \ell_j) + \text{h.c..} \eqno(\text{A.5})$$
The coefficient $c_{ij}$ form a $3 \times 3$ symmetric complex matrix, which is described by 6 real and 6 imaginary entries. In addition, there are the 9 real and 9 imaginary parameters that describe the charge lepton Yukawa matrix, $Y_\ell$, Eq. (16). The generators of unitary transformations $L_L \to V_L L_L, \ell_R \to V_\ell \ell_R$ are now completely broken by the Weinberg operator in conjunction with the charged lepton Yukawa couplings. This means that we have broken generators described by $2 \times (3 \text{ real} + 6 \text{ im.})$ parameters. From the general rule (18) it then follows that we have $9 + 6 - 2 \times 3 = 9$ real and $9 + 6 - 2 \times 6 = 3$ imaginary physical parameters. The nine real parameters are the three charged lepton masses, three neutrino masses, and the three mixing angles of the PMNS matrix. The three physical phases are the phase in the PMNS matrix, and the two Majorana phases in the Majorana mass matrix, $M_\nu = \text{diag}(m_1, m_2 e^{i\phi_2}, m_3 e^{i\phi_3})$.
Other options for neutrino mass matrix are possible. There could be just one, two or more than three sterile neutrinos, $\nu_{R,i}$. For an introduction of phenomenological implications see, e.g., [111]. In the case where there are only Dirac mass terms, these break the individual lepton flavour numbers $U(1)_e \times U(1)_\mu \times U(1)_\tau$ down to a total lepton number $U(1)_L$. Majorana mass terms, such as the Weinberg operator in (A.5), break also the $U(1)_L$.
### References
[1] T. E. Browder, T. Gershon, D. Pirjol, A. Soni, and J. Zupan, Rev. Mod. Phys. $\mathbf{81}$, 1887 (2009), 0802.3201.
[2] Y. Grossman and P. Tanedo, Just a Taste: Lectures on Flavor Physics, in Theoretical Advanced Study Institute in Elementary Particle Physics: Anticipating the Next Discoveries in Particle Physics (TASI 2016) Boulder, CO, USA, June 6-July 1, 2016, 2017, 1711.03264.
[3] M. Blanke, Introduction to Flavour Physics and CP Violation, in Proceedings, 2016 European School of High-Energy Physics (ESHEP2016): Skeikampen, Norway, June 15-28 2016, pp. 71–100, 2017, 1704.03753.

[4] O. Gedalia and G. Perez, Flavor Physics, in Physics of the large and the small, TASI 09, proceedings of the Theoretical Advanced Study Institute in Elementary Particle Physics, Boulder, Colorado, USA, 1-26 June 2009, pp. 309–382, 2011, 1005.3106.
[5] Y. Nir, Probing new physics with flavor physics (and probing flavor physics with new physics), in Prospects in Theoretical Physics (PiTP) summer program on The Standard Model and Beyond IAS, Princeton, NJ, June 16-27, 2007, 2007, 0708.1872.
[6] J. F. Kamenik, Flavour Physics and CP Violation, in Proceedings, 2014 European School of High-Energy Physics (ESHEP 20

ph/9512380.
[39] K. G. Chetyrkin, M. Misiak, and M. Munz, Phys. Lett. $\mathbf{B400}$, 206 (1997), hep-ph/9612313, [Erratum: Phys. Lett.B425,414(1998)].
[40] M. Bordone, G. Isidori, and A. Pattori, Eur. Phys. J. $\mathbf{C76}$, 440 (2016), 1605.07633.
[41] S. Descotes-Genon, L. Hofer, J. Matias, and J. Virto, JHEP $\mathbf{06}$, 092 (2016), 1510.04239.
[42] B. Capdevila, S. Descotes-Genon, J. Matias, and J. Virto, JHEP $\mathbf{10}$, 075 (2016), 1605.03156.
[43] B. Capdevila, S. Descotes-Genon, L. Hofer, and J. Matias, JHEP $\mathbf{04}$, 016 (2017), 1701.08672.
[44] N. Serra, R. Silva Coutinho, and D. van Dyk, Phys. Rev. $\mathbf{D95}$, 035029 (2017), 1610.08761.
[45] A. Bharucha, D. M. Straub, and R. Zwicky, JHEP $\mathbf{08}$, 098 (2016), 1503.05534.
[46] W. Altmannshofer, C. Niehoff, P. Stangl, and D. M. Straub, Eur. Phys. J. $\mathbf{C77}$, 377 (2017), 1703.09189.
[47] S. Jäger and J. Martin Camalich, Phys. Rev. $\mathbf{D93}$, 014028 (2016), 1412.3183.
[48] LHCb, R. Aaij $et\ al.$, Phys. Rev. Lett. $\mathbf{113}$, 151601 (2014), 1406.6482.
[49] LHCb, R. Aaij $et\ al.$, JHEP $\mathbf{08}$, 055 (2017), 1705.05802.
[50] Belle, J. T. Wei $et\ al.$, Phys. Rev. Lett. $\mathbf{103}$, 171801 (2009), 0904.0770.
[51] BaBar, J. P. Lees $et\ al.$, Phys. Rev. $\mathbf{D86}$, 032012 (2012), 1204.3933.
[52] G. D'Amico $et\ al.$, JHEP $\mathbf{09}$, 010 (2017), 1704.05438.
[53] L.-S. Geng $et\ al.$, Phys. Rev. $\mathbf{D96}$, 093006 (2017), 1704.05446.
[54] W. Altmannshofer, P. Stangl, and D. M. Straub, Phys. Rev. $\mathbf{D96}$, 055008 (2017), 1704.05435.
[55] B. Capdevila, A. Crivellin, S. Descotes-Genon, J. Matias, and J. Virto, JHEP $\mathbf{01}$, 093 (2018), 1704.05340.
[56] T. Hurth, F. Mahmoudi, D. Martinez Santos, and S. Neshatpour, Phys. Rev. $\mathbf{D96}$, 095034 (2017), 1705.06274.
[57] G. Hiller and I. Nisandzic, Phys. Rev. $\mathbf{D96}$, 035003 (2017), 1704.05444.
[58] R. Alonso, B. Grinstein, and J. Martin Camalich, Phys. Rev. Lett. $\mathbf{113}$, 241802 (2014), 1407.7044.
[59] W. Altmannshofer and D. M. Straub, Eur. Phys. J. $\mathbf{C73}$, 2646 (2013), 1308.1501.
[60] W. Altmannshofer, S. Gori, M. Pospelov, and I. Yavin, Phys. Rev. $\mathbf{D89}$, 095033 (2014), 1403.1269.
[61] A. Greljo, G. Isidori, and D. Marzocca, JHEP $\mathbf{07}$, 142 (2015), 1506.01705.
[62] G. Hiller and M. Schmaltz, JHEP $\mathbf{02}$, 055 (2015), 1411.4773.
[63] W. Altmannshofer and D. M. Straub, Eur. Phys. J. $\mathbf{C75}$, 382 (2015), 1411.3161.
[64] W. Altmannshofer, S. Gori, M. Pospelov, and I. Yavin, Phys. Rev. Lett. $\mathbf{113}$, 091801 (2014), 1406.2332.
[65] J. F. Kamenik, Y. Soreq, and J. Zupan, Phys. Rev. $\mathbf{D97}$, 035002 (2018), 1704.06005.
[66] G. Bélanger and C. Delaunay, Phys. Rev. $\mathbf{D94}$, 075019 (2016), 1603.03333.
[67] B. Gripaios, M. Nardecchia, and S. A. Renner, JHEP $\mathbf{06}$, 083 (2016), 1509.05020.
[68] M. Bauer and M. Neubert, Phys. Rev. Lett. $\mathbf{116}$, 141802 (2016), 1511.01900.
[69] D. Bečirević and O. Sumensari, JHEP $\mathbf{08}$, 104 (2017), 1704.06835.
[70] S. Fajfer, J. F. Kamenik, and I. Nisandzic, Phys. Rev. $\mathbf{D85}$, 094025 (2012), 1203.2654.
[71] P. Asadi, M. R. Buckley, and D. Shih, JHEP $\mathbf{09}$, 010 (2018), 1804.04135.
[72] A. Greljo, D. J. Robinson, B. Shakya, and J. Zupan, JHEP $\mathbf{09}$, 169 (2018), 1804.04642.
[73] D. Bečirević, S. Fajfer, N. Košnik, and O. Sumensari, Phys. Rev. $\mathbf{D94}$, 115021 (2016), 1608.08501.
[74] G. Cvetič, F. Halzen, C. S. Kim, and S. Oh, Chin. Phys. $\mathbf{C41}$, 113102 (2017), 1702.04335.
[75] BaBar, J. P. Lees $et\ al.$, Phys. Rev. Lett. $\mathbf{109}$, 101802 (2012), 1205.5442.

[76] BaBar, J. P. Lees $et\ al.$, Phys. Rev. **D88**, 072012 (2013), 1303.0571.
[77] Belle, M. Huschle $et\ al.$, Phys. Rev. **D92**, 072014 (2015), 1507.03233.
[78] Belle, Y. Sato $et\ al.$, Phys. Rev. **D94**, 072007 (2016), 1607.07923.
[79] LHCb