Journal of Holography Applications in Physics
Volume 5, Issue 2, Spring 2025, 10–21
©Available online at http://jhap.du.ac.ir
DOI: 10.22128/jhap.2025.1024.1118
Online ISSN: 2783–3518

### Letter

## Consequences of Undecidability in Physics on the Theory of Everything

Mir Faizal^1,2,3,4 · Lawrence M. Krauss^5 · Arshid Shabir^2 · Francesco Marino^6

1 Irving K. Barber School of Arts and Sciences, University of British Columbia Okanagan, Kelowna, BC V1V 1V7, Canada;
E-mail: mirfaizalmir@gmail.com

2 Canadian Quantum Research Center, 204-3002 32 Ave, Vernon, BC V1T 2L7, Canada;
Corresponding Author E-mail: aslone186@gmail.com

3 Department of Mathematical Sciences, Durham University, Upper Mountjoy, Stockton Road, Durham DH1 3LE, UK.

4 Faculty of Sciences, Hasselt University, Agoralaan Gebouw D, Diepenbeek, 3590 Belgium.

5 Origin Project Foundation, Phoenix, AZ 85018, USA;
E-mail: lawrence@originsproject.org

6 CNR-Istituto Nazionale di Ottica and INFN, Via Sansone 1, I-50019 Sesto Fiorentino (FI), Italy;
E-mail: francesco.marino@ino.cnr.it

**Received:** June 6, 2025; **Accepted:** June 17, 2025

**Abstract.** General relativity treats spacetime as dynamical and exhibits its breakdown at singularities. This failure is interpreted as evidence that quantum gravity is not a theory formulated within spacetime; instead, it must explain the very emergence of spacetime from deeper quantum degrees of freedom, thereby resolving singularities. Quantum gravity is therefore envisaged as an axiomatic structure, and algorithmic calculations acting on these axioms are expected to generate spacetime. However, Gödel's incompleteness theorems, Tarski's undefinability theorem, and Chaitin's information-theoretic incompleteness establish intrinsic limits on any such algorithmic program. Together, these results imply that a wholly algorithmic "Theory of Everything" is impossible: certain facets of reality will remain computationally undecidable and can be accessed only through non-algorithmic understanding. We formalize this by constructing a "Meta-Theory of Everything" grounded in non-algorithmic understanding, showing how it can account for undecidable phenomena and demonstrating that the breakdown of computational descriptions of nature does not entail a breakdown of science. Because any putative simulation of the universe would itself be algorithmic, this framework also implies that the universe cannot be a simulation.

**Keywords:** Non-Algorithmic Understanding; Quantum Gravity; It from Bit, Gödel's incompleteness theorems; Tarski's undefinability theorem; Chaitin's information-theoretic incompleteness.

---

**COPYRIGHTS:** ©2025, Journal of Holography Applications in Physics. Published by Damghan University. This article is an open-access article distributed under the terms and conditions of the Creative Commons Attribution 4.0 International (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0

10

---

Consequences of Undecidability in Physics on the Theory of Everything 11

Physics has journeyed from classical tangible "stuff" to ever deeper layers of abstraction. In Newtonian mechanics reality consists of point-like masses tracing deterministic trajectories in an immutable Euclidean space with a universal time parameter [1]. This picture sufficed for celestial mechanics and terrestrial dynamics, yet its very foundations, including the separability of space and time and the notion of absolute simultaneity, were overturned by Einstein's special relativity. By welding space and time into a single Lorentzian continuum, special relativity replaced Newton's rigid arena with an observer-dependent spacetime geometry whose interval, not time or space separately, is invariant [2].

Quantum mechanics introduced a second conceptual revolution: even with a fixed space-time backdrop, the microscopic world resists classical deterministic descriptions. Wave functions evolve unitarily, but measurement outcomes are inherently probabilistic, encoded in the Born rule and constrained by complementarity and uncertainty principles [3]. When the relativistic requirement of locality is imposed on quantum theory, particles cease to be fundamental. Instead, quantum field theory (QFT) elevates fields to primary status; "particles" emerge from those fields via creation and annihilation operators acting on the vacuum state [4]. Here the vacuum is itself a seething medium. Time-dependent boundary conditions in superconducting wave-guides emulate moving mirrors and catalyse the dynamical Casimir effect, producing real particles from vacuum fluctuations [5]. Likewise, an accelerated observer perceives the Minkowski vacuum as a thermal bath via the so-called Unruh effect, emphasizing that particle content is observer-dependent rather than absolute [6]. These phenomena confirm QFT: what we call a particle is contingent on both the quantum state of quantum fields and even the kinematics of the detector. Thus, particles moving in spacetime become a contingent structure, yet spacetime remains fundamental and fixed.

All these theories presuppose a fixed background spacetime. General relativity (GR), by contrast, is a theory of spacetime itself. It accurately describes phenomena from Mercury's perihelion precession to the direct detection of gravitational waves [7,8]. Nevertheless, GR predicts curvature singularities at the center of black holes and at the big bang, where the spacetime description of reality breaks down [9,10]. Singular behavior of this sort is not unique to gravity; it signals the breakdown of any effective model once its underlying degrees of freedom are pushed beyond their domain of validity [11,12]. Classical fluid discontinuities, for example, correspond to curvature singularities of an acoustic metric and are smoothed out in a full quantum-hydrodynamic treatment [13,14].

Thus, it is expected that curvature singularities in GR will also be removed in a full quantum theory of gravity. These singularities do not indicate a breakdown of physics, but the breakdown of a spacetime description of nature. Instead, it is presumed the physics of a quantum theory of gravity will not break down, even in such extreme conditions. Candidate quantum gravity frameworks likewise remove curvature singularities. Loop quantum cosmology replaces the big bang singularity with a big bounce [15,16], while the fuzzball paradigm in string theory substitutes extended microstate geometries for point-like singularity at the center of black holes [17,18]. More broadly, both loop quantum gravity and string theory depict spacetime as emergent: spin-foam models build it from discrete quantum structures [19], and the doubled-geometry formalism of double field theory introduces T-folds whose transition functions involve T-duality rather than ordinary diffeomorphisms, showing that classical spacetime may fail to be well defined at some points [20,21].

These insights resonate with Wheeler's "it from bit" program and its modern versions in both string theory [22,23] and loop quantum gravity [24], which propose that information is more fundamental than physical reality consisting of spacetime and quantum fields defined on it [25]. Singularities in classical models then mark precisely those regions where the informational degrees of freedom can no longer be captured by a spacetime geometry. Although the emergent "it" spacetime with its quantum fields fails at singularities, one might hope

---

12 Mir Faizal et al.

that the underlying "bit", a complete quantum-gravity theory, could be formulated as a consistent, computable "theory of everything." However, we now argue that such a purely algorithmic formulation is unattainable.

As we do not have a fully consistent theory of quantum gravity, several different axiomatic systems have been proposed to model quantum gravity [26–32]. In all these programs, it is assumed a candidate theory of quantum gravity is encoded as a computational formal system

$$\mathcal{F}_{QG} = \{\mathcal{L}_{QG}, \Sigma_{QG}, \mathcal{R}_{\text{alg}}\}. \tag{0.1}$$

Here, $\mathcal{L}_{QG}$ a first-order language whose non-logical symbols denote quantum states, fields, curvature, causal relations, etc. $\Sigma_{QG} = \{A_1, A_2, \ldots\}$ is a finite (or at least recursively-enumerable) set of closed $\mathcal{L}_{QG}$-sentences embodying the fundamental physical principles. $\mathcal{R}_{\text{alg}}$ the standard, effective rules of inference used for computations. They operationalise "algorithmic calculations"; we write $\Sigma_{QG} \vdash_{\text{alg}} \varphi \Longleftrightarrow \varphi$ is derivable from $\Sigma_{QG}$ via $\mathcal{R}_{\text{alg}}$. Crucially, spacetime is not a primitive backdrop but a theorem-level construct emergent inside models of $\mathcal{F}_{QG}$. Concrete mechanisms for which such geometry can emerge include dynamics in string theory [33,34], entanglement in holography [22,23], and spin-network dynamics in LQG [19,24,35].

Any viable $\mathcal{F}_{QG}$ must meet four intertwined criteria: Effective axiomatizability; The number of axioms in $\Sigma_{QG}$ are finite. This ensures that proofs are well-posed. In fact, it is expected that spacetime can be algorithmically generated from this, and so it has to be computationally well defined [14,36]. Arithmetic expressiveness; $\mathcal{L}_{QG}$ can internally model the natural numbers with their basic operations. This is important as quantum gravity should reproduce calculations used for amplitudes, curvature scalars, entropy, etc in appropriate limits. Both string theory [34,37] and LQG [35,38] satisfy this by reproducing GR and QM in appropriate limits. Internal consistency; no $\Sigma_{QG} \vdash_{\text{alg}} \perp$. Strings secure this via anomaly cancellation [34,39]; LQG via an anomaly-free constraint algebra [35,40]. Empirical completeness; predictive all physical phenomena from the Planck scale to cosmology, and even resolves singularities.

The axiom set $\Sigma_{QG}$ is finite, arithmetically expressive and consistent. As a result, Gödel's incompleteness theorems apply [41,42]. Here, we consider the algorithmic core of quantum gravity as a finite, consistent and arithmetically expressive formal system $\mathcal{F}_{QG} = (\mathcal{L}_{QG}, \Sigma_{QG}, \mathcal{R}_{\text{alg}})$. Its deductive closure is the recursively enumerable set of theorems $\text{Th}(\mathcal{F}_{QG}) = \{\varphi \in \mathcal{L}_{QG} \mid \Sigma_{QG} \vdash_{\mathcal{R}_{\text{alg}}} \varphi\}$, while the semantically true sentences are $\text{True}(\mathcal{F}_{QG}) = \{\varphi \in \mathcal{L}_{QG} \mid \mathbb{N} \models \varphi\}$. Thus, Gödel's first incompleteness theorem asserts the strict containment $\text{Th}(\mathcal{F}_{QG}) \subsetneq \text{True}(\mathcal{F}_{QG})$ [41,42], guaranteeing the existence of well-formed $\mathcal{L}_{QG}$-statements that are true but unprovable within the algorithmic machinery of $\mathcal{F}_{QG}$. Physically these Gödel sentences correspond to empirically meaningful facts—e.g., specific black-hole microstates—that elude any finite, rule-based derivation. Gödel's second theorem deepens the impasse: the self-referential consistency statement $\text{Con}(\mathcal{F}_{QG}) \equiv \neg \text{Prov}_{\Sigma_{QG}}(\perp)$ cannot itself be proved by $\mathcal{F}_{QG}$ without contradiction [41,42]. A purely computational theory of everything would therefore not be able to establish its own internal soundness. Tarski's undefinability theorem further bars the construction of an internal truth predicate $\text{Truth}(x) \in \mathcal{L}_{QG}$ obeying $\Sigma_{QG} \vdash_{\mathcal{R}_{\text{alg}}} [\text{Truth}(\ulcorner\varphi\urcorner) \leftrightarrow \varphi]$ for all $\varphi$ [43–45]. So, a truth predicate for quantum gravity cannot be defined within the theory itself. Finally, Chaitin's information-theoretic incompleteness establishes a constant $K_{\mathcal{F}_{QG}}$ such that any sentence $S$ with prefix-free Kolmogorov complexity $K(S) > K_{\mathcal{F}_{QG}}$ is undecidable in $\mathcal{F}_{QG}$ [46–48]. This bound caps the epistemic reach of algorithmic deduction by declaring ultra-complex statements—inevitable in high-energy quantum gravity—formally inaccessible.

Together, the Gödel–Tarski–Chaitin triad delineates an insurmountable frontier for any

---

Consequences of Undecidability in Physics on the Theory of Everything 13

strictly computable framework. To attain a genuinely complete and self-justifying theory of quantum gravity one must augment $\mathcal{F}_{QG}$ with non-algorithmic resources— external truth predicate axioms, or other meta-logical mechanisms—that transcend recursive enumeration while remaining empirically consonant with physics at the Planck scale. Although these limits restrict what can be known computationally, the Lucas–Penrose argument shows that non-algorithmic understanding can access truths beyond formal proofs [49–53]. Purely algorithmic deduction is therefore insufficient for a complete foundational account.

To transcend these computations limitations, we adjoin an external truth predicate $T(x)$ and a non-effective inference mechanism $\mathcal{R}_{\text{nonalg}}$, enlarging the formal apparatus to

$$\mathcal{M}_{\text{ToE}} = \{\mathcal{L}_{QG} \cup \{T\},\, \Sigma_{QG} \cup \Sigma_T,\, \mathcal{R}_{\text{alg}} \cup \mathcal{R}_{\text{nonalg}}\}. \qquad (0.2)$$

Here $\Sigma_T$ is an external, non-recursively-enumerable set of axioms about $T$. We write $\Sigma_T \vdash_{\text{nonalg}} \varphi$ precisely when $T(\ulcorner \varphi \urcorner) \in \Sigma_T$. The external truth predicate axioms obey four intertwined conditions. (S1) Soundness for $\mathcal{F}_{QG}$: whenever $T(\ulcorner \varphi \urcorner)$ is an axiom, $\varphi$ holds in every model of the base theory. (S2) Reflective completeness: if $\varphi$ is algorithmically derivable from $\Sigma_{QG}$, then the implication $\varphi \to T(\ulcorner \varphi \urcorner)$ itself belongs to $\Sigma_T$. (S3) Modus-ponens closure: $T$ respects logical consequence, for $T(\ulcorner \varphi \to \psi \urcorner)$ together with $T(\ulcorner \varphi \urcorner)$ entails $T(\ulcorner \psi \urcorner)$. (S4) Trans-algorithmicity: the induced theory $\text{Th}_T = \{\varphi \mid T(\ulcorner \varphi \urcorner) \in \Sigma_T\}$ is not recursively enumerable; sentences of arbitrarily high Kolmogorov complexity can still be $T$-true, exceeding the information bound $K_{\mathcal{F}_{QG}}$.

With these properties the external truth predicate certifies every Gödel sentence of $\mathcal{F}_{QG}$ and can single out, for instance, concrete black-hole microstates that elude all algorithmic searches, thereby side-stepping the information-loss puzzle and illuminating Planck-scale dynamics. The non-algorithmic understanding encoded by $\mathcal{R}_{\text{nonalg}}$ and $\Sigma_T$ thus supplies conceptual resources inaccessible to purely computational physics.

For clarity of notation: $\Sigma_{QG}$ is the computable axiom set; $\mathcal{R}_{\text{alg}}$ comprises the standard, effective inference rules; $\mathcal{R}_{\text{nonalg}}$ is the non-effective external truth predicate rule that certifies $T$-truths; $\mathcal{F}_{QG} = \{\mathcal{L}_{QG}, \Sigma_{QG}, \mathcal{R}_{\text{alg}}\}$ denotes the computational core; and $\mathcal{M}_{\text{ToE}} = \{\mathcal{L}_{QG} \cup \{T\}, \Sigma_{QG} \cup \Sigma_T, \mathcal{R}_{\text{alg}} \cup \mathcal{R}_{\text{nonalg}}\}$ denotes the full meta-theory that weds algorithmic deduction to an external truth predicate.

Crucially, the appearance of undecidable phenomena in physics already offers empirical backing for $\mathcal{M}_{\text{ToE}}$. Whenever an experiment or exact model realises a property whose truth value provably eludes every recursive procedure, that property functions as a concrete witness to the truth predicate $T(x)$ operating within the fabric of the universe itself. Far from being a purely philosophical embellishment, $\mathcal{M}_{\text{ToE}}$ thus emerges as a structural necessity forced upon us by the physics of undecidable observables. Working at the deepest layer of description, $\mathcal{M}_{\text{ToE}}$ fuses algorithmic and non-algorithmic modes of reasoning into a single coherent architecture, providing the semantic closure that a purely formal system $\mathcal{F}_{QG}$ cannot reach on its own. In this enriched setting, quantum measurements, Planck-scale processes, quantum-gravitational amplitudes and cosmological initial conditions might all become accessible to principled yet non-computable inference, ensuring that no physically meaningful truth is left outside the scope of theoretical understanding. Just as Riemannian geometry, which describes general relativity, or gauge theories, which describe various interactions of the Standard Model, are each actualized in nature, this truth predicate $T(x)$ would also be actualized in nature.

The logical limitations reviewed above bear directly on several open questions in quantum gravity, beginning with the black-hole information paradox [54]. If the microstates responsible for the Bekenstein–Hawking entropy live at Planckian scales, where smooth geometry breaks down, Chaitin's incompleteness theorem suggests that their detailed structure may

---

14 Mir Faizal et al.

forever lie beyond algorithmic derivation. In such circumstances, classical spacetime must re-emerge through a collective, effectively thermal, behaviour of microscopic degrees of freedom. Yet deciding whether a given many-body system thermalises is itself algorithmically undecidable [55]. Here $\mathcal{M}_{\mathrm{ToE}}$ becomes indispensable: by adjoining the external truth predicate $T(x)$ that certifies physically admissible yet uncomputable properties, the meta-theory legitimizes the passage from undecidable Planck-scale microphysics to the macroscopic notion of spacetime thermalization.

Thermalization already plays a central role in leading quantum-gravity models. In AdS/CFT, bulk perturbations relax into black-hole horizons whose thermodynamic parameters are sharply defined [56]; in the fuzzball paradigm, an ensemble of horizonless microstate geometries reproduces the Hawking spectrum [57]; and in LQG, coarse-graining drives discrete quantum geometries toward a classical continuum phase [58]. Because thermalisation is undecidable in the general many-body setting [55], each route from Planck-scale physics to smooth spacetime must contain steps that transcend algorithmic control. The non-algorithmic scaffold provided by $\mathcal{M}_{\mathrm{ToE}}$ supplies precisely the logical footing required to keep such trans-computational steps consistent.

Computational undecidability likewise shadows other structural questions in many-body physics and hence in quantum gravity. No algorithm can decide in full generality whether a local quantum Hamiltonian is gapped or gapless [59]; the proof embeds Turing's halting problem [60], which links back to Chaitin's theorem [61]. Entire renormalization-group flows can behave uncomputably [62], even though RG ideas underpin string-theoretic beta-functions [63], background-independent flows in LQG [64] and continuum-limit programs such as asymptotic safety and causal dynamical triangulations [65,66]. If generic RG trajectories defy algorithmic prediction, then translating fundamental quantum-gravity data into classical spacetime observables again lies beyond finite computation. By embedding these flows into $\mathcal{M}_{\mathrm{ToE}}$, one places them under a broader logical umbrella where non-computational criteria rooted in $T(x)$ can still certify physical viability.

Related undecidable sectors abound. Key properties of tensor networks ubiquitous in holography [67] and LQG [68] are formally uncomputable [69]. Deducing supersymmetry breaking in certain two-dimensional theories is undecidable [70], influencing model building in string theory [39]. Phase diagrams of engineered spin models encode uncomputable problems [71], and the mathematical kinship between such systems and LQG kinematics [72] hints at analogous intractabilities in the full phase structure of loop gravity. Each undecidable domain slots naturally into $\mathcal{M}_{\mathrm{ToE}}$, which extends explanatory reach beyond algorithmic barriers while maintaining logical coherence through its external truth predicates axioms.

These technical results respect rather than undermine the principle of sufficient reason [73,74]. The core demand of that principle is that every true fact must be grounded in an adequate explanation. This forms the basis of science. Gödel incompleteness, Tarski undefinability, and Chaitin bounds do not negate this demand; they merely show that "adequate explanation" is broader than "derivable by a finite, mechanical procedure." In other words, the existence of true but unprovable $\mathcal{L}_{QG}$-sentences does not imply that those facts lack reasons, but only that their reasons need not be encoded syntactically within any recursively enumerable axiom set. The semantic external truth predicate $T$ introduced above models such non-algorithmic grounding: it certifies truth directly at the level of the underlying mathematical structure, thereby supplying sufficient reasons that transcend the deductive reach of $\Sigma_{QG}$. Thus, far from conflicting with the principle of sufficient reason, the logical limits on computation affirm it by revealing that explanatory resources extend beyond formal proof theory. So, a breakdown of computational explanations does not imply a breakdown of science.

---

Many undecidable statements encountered in physics ultimately trace back to the halting problem [75], yet non-algorithmic understanding can still apprehend such truths [76]. The Lucas–Penrose proposal that human cognition surpasses formal computation [49–53] finds a mathematical expression in $\mathcal{M}_{\text{ToE}}$, whose external truth predicate $T(x)$ certifies propositions that no algorithmic verifier can capture. In line with the orchestrated objective-reduction (OR) proposal, they claim that human observers can have a truth predicate because cognitive processes exploit quantum collapse, which is produced by the truth predicate of quantum gravity [52]. This is why they argue that human mathematicians can apprehend Gödelian truths, whereas computers cannot.

Non-algorithmic reasoning already supplements GR through the Novikov self-consistency principle [77,78], which imposes a global logical constraint on spacetimes with closed time-like curves. By housing such meta-principles in $\mathcal{M}_{\text{ToE}}$ one side-steps Gödelian obstructions that would cripple a purely formal $\mathcal{F}_{QG}$. As quantum logic is itself undecidable [79,80], any proper wave-function-collapse mechanism must operate outside the algorithmic domain of quantum mechanics. So, such dynamics naturally reside in the non-algorithmic $\mathcal{M}_{\text{ToE}}$. Gravitationally induced objective-collapse proposals can therefore be interpreted as concrete instantiations of the $\mathcal{M}_{\text{ToE}}$ action on quantum states [81,82]. Here, the meta-layer supplies a non-algorithmic gravity-triggered collapse that is not derivable from $\Sigma_{QG}$, but is nonetheless well-defined at the semantic level. A key advantage of using objective-collapse models might be cosmological: it could offer an explanation of the quantum-to-classical transition in cosmology, thereby addressing the measurement problem in quantum cosmology [83].

A growing survey confirms that undecidability permeates diverse areas of physics [84]. These examples jointly reinforce the proposition that a quantum-gravity rooted solely in computation can be neither complete nor consistent, whereas augmenting it with the non-algorithmic resources encoded in $\mathcal{M}_{\text{ToE}}$ could restore explanatory power without losing logical soundness.

The claim that our universe is itself a computer simulation has been advanced in several forms, from Bostrom's statistical "trilemma" [85] to more recent analyses by Chalmers [86] and Deutsch [87]. These proposals assume that every physical truth is reducible to the output of a finite algorithm executed on a sufficiently powerful substrate. Yet this assumption tacitly identifies the full physical theory with its computable slice $\mathcal{F}_{QG}$.

Our framework separates the computable fragment $\mathcal{F}_{QG}$ from the non-algorithmic meta-layer $\mathcal{M}_{\text{ToE}}$. Because $\mathcal{M}_{\text{ToE}}$ contains an external truth predicate $T(x)$ that by construction escapes formal verification, any finite algorithm can at best emulate $\mathcal{F}_{QG}$ while systematically omitting the meta-theoretic truths enforced by $T(x)$. Consequently, no simulation could in principle reproduce what would otherwise be the full underlying structure of the physics of our universe. Our analysis instead suggests that genuine physical reality embeds non-computational content that cannot be instantiated on a Turing-equivalent device. Since it is impossible to simulate a complete and consistent universe, our universe is definitely not a simulation. As the universe is produced by $\mathcal{M}_{\text{ToE}}$, the simulation hypothesis is logically impossible rather than merely implausible.

The arguments presented here suggest that neither 'its' nor 'bits' may be sufficient to describe reality. Rather, a deeper description, expressed not in terms of information but in terms of non-algorithmic understanding, is required for a complete and consistent theory of everything.

## Authors' Contributions

All authors have the same contribution.

---

16 Mir Faizal et al.

## Data Availability

The manuscript has no associated data or the data will not be deposited.

## Conflicts of Interest

The authors declare that there is no conflict of interest.

## Ethical Considerations

The authors have diligently addressed ethical concerns, such as informed consent, plagiarism, data fabrication, misconduct, falsification, double publication, redundancy, submission, and other related matters.

## Funding

This research did not receive any grant from funding agencies in the public, commercial, or non-profit sectors.

## Acknowledgment

We would like to thank İzzet Sakallı, Salman Sajad Wani, and Aatif Kaisar Khan for useful discussions. We would also like to thank Aatif Kaisar Khan for sharing with us an important paper on undecidability. Stephen Hawking's discussion on Gödel's theorems and the end of physics motivated the current work. We would also like to thank Roger Penrose for his exploration of Gödel's theorems and the Lucas-Penrose argument, which forms the basis of meta-theoretical perspective based on non-algorithmic understanding.

## References

[1] L. D. Landau and E. M. Lifshitz, "Mechanics", Butterworth-Heinemann, Oxford, (1976). DOI: https://doi.org/10.1016/C2009-0-25569-3

[2] W. Rindler, "Essential Relativity: Special, General, and Cosmological", Springer, Berlin, (1977). DOI: https://doi.org/10.1007/978-3-642-86650-0

[3] J. J. Sakurai and J. J. Napolitano, "Modern Quantum Mechanics", Cambridge University Press, Cambridge, (2017). DOI: https://doi.org/10.1017/9781108499996

[4] M. Srednicki, "Quantum Field Theory", Cambridge University Press, Cambridge, (2007). DOI: https://doi.org/10.1017/CBO9780511813917

[5] C. M. Wilson, G. Johansson, A. Pourkabirian, M. Simoen, J. R. Johansson, T. Duty, F. Nori, and P. Delsing, "Observation of the dynamical Casimir effect in a superconducting circuit", Nature **479**, 376 (2011). DOI: https://doi.org/10.1038/nature10561

[6] L. C. B. Crispino, A. Higuchi, and G. E. A. Matsas, "The Unruh effect and its applications", Reviews of Modern Physics **80**, 787 (2008). DOI: https://doi.org/10.1103/RevModPhys.80.787

---

Consequences of Undecidability in Physics on the Theory of Everything 17

[7] A. Einstein, "Die Feldgleichungen der Gravitation", Sitzungsberichte der Preussischen Akademie der Wissenschaften zu Berlin (1915). DOI: https://doi.org/10.1007/978-3-322-83770-7_10

[8] B. P. Abbott et al., "Observation of Gravitational Waves from a Binary Black Hole Merger", Physical Review Letters **116**, 061102 (2016). DOI: 10.1103/PhysRevLett.116.061102

[9] R. Penrose, "Gravitational Collapse and Space-Time Singularities", Physical Review Letters **14**, 57 (1965). DOI: 10.1103/PhysRevLett.14.57

[10] S. Hawking and R. Penrose, "The Singularities of Gravitational Collapse and Cosmology", Proceedings of the Royal Society A **314**, 529 (1970). DOI: 10.1098/rspa.1970.0021

[11] V. I. Arnold, "Catastrophe Theory", Springer Berlin, Heidelberg, (1992). DOI: https://doi.org/10.1007/978-3-642-57884-7_9

[12] M. Berry, "The singularities of light: intensity, phase, polarisation", Light Sci. Appl. **12**, 238 (2023). DOI: https://doi.org/10.1038/s41377-023-01270-8

[13] F. Marino, C. Maitland, D. Vocke, O. Ortolan, and D. Faccio, "Emergent geometries and nonlinear-wave dynamics in photon fluids", Scientific Reports **6**, 23282 (2016). DOI: https://doi.org/10.1038/srep23282

[14] S. L. Braunstein, M. Faizal, L. M. Krauss, F. Marino, and N. A. Shah, "Analogue simulations of quantum gravity with fluids", Nature Rev. Phys. **5**, 612 (2023). DOI: 10.1038/s42254-023-00630-y

[15] M. Bojowald, "Absence of Singularity in Loop Quantum Cosmology", Physical Review Letters **86**, 5227 (2001). DOI: 10.1103/PhysRevLett.86.5227

[16] A. Ashtekar, T. Pawlowski, and P. Singh, "Quantum Nature of the Big Bang: Improved Dynamics", Phys. Rev. D **74**, 084003 (2006). DOI: 10.1103/PhysRevD.74.084003

[17] S. D. Mathur, "The Fuzzball Proposal for Black Holes: An Elementary Review", Fortschritte der Physik **53**, 793 (2005). DOI: 10.1002/prop.200410203

[18] S. D. Mathur, "Tunneling into fuzzball states", Gen. Rel. Grav. **42**, 113 (2010). DOI: 10.1007/s10714-009-0837-3

[19] A. Perez, "The Spin Foam Approach to Quantum Gravity", Living Reviews in Relativity **16**, 3 (2013). DOI: 10.12942/lrr-2013-3

[20] O. Hohm, C. Hull, and B. Zwiebach, "Generalized Metric Formulation of Double Field Theory", Journal of High Energy Physics **08**, 008 (2010). DOI: 10.1007/JHEP08(2010)008

[21] C. M. Hull, "A Geometry for Non-Geometric String Backgrounds", Journal of High Energy Physics **10**, 065 (2005). DOI: 10.1088/1126-6708/2005/10/065

[22] D. Jafferis, A. Zlokapa, J. D. Lykken, D. K. Kolchmeyer, S. I. Davis, N. Lauk, H. Neven, and M. Spiropulu, "Traversable wormhole dynamics on a quantum processor", Nature **612**, 51 (2022). DOI: 10.1038/s41586-022-05424-3

[23] M. Van Raamsdonk, "Spacetime from bits", Science **370**, 198 (2020). DOI: 10.1126/science.aay9560

---

18

Mir Faizal et al.

- [24] J. Mäkelä, "Wheeler's it from bit proposal in loop quantum gravity", Int. J. Mod. Phys. D **28**, 1950129 (2019). DOI: 10.1142/S0218271819501293

- [25] J. A. Wheeler, "Information, physics, quantum: The search for links", in Proceedings III International Symposium on Foundations of Quantum Mechanics, W. J. Archibald, ed., 354 (1989). https://philarchive.org/rec/WHEIPQ

- [26] E. Witten, "Noncommutative Geometry and String Field Theory", Nucl. Phys. B **268**, 253 (1986). DOI: 10.1016/0550-3213(86)90155-0

- [27] H. Ziaepour, "Comparing Quantum Gravity Models: String Theory, Loop Quantum Gravity, and Entanglement Gravity versus SU($\infty$)-QGR", Symmetry **14**, 58 (2022). DOI: 10.3390/sym14010058

- [28] M. Faizal, A. Shabir, and A. K. Khan, "Consequences of Gödel theorems on third quantized theories like string field theory and group field theory", Nucl. Phys. B **1010**, 116774 (2025). DOI: 10.1016/j.nuclphysb.2024.116774

- [29] L. Bombelli, J. Lee, D. Meyer, and R. D. Sorkin, "Spacetime as a causal set", Physical Review Letters **59**, 521 (1987). DOI: 10.1103/PhysRevLett.59.521

- [30] S. Majid, "On the emergence of the structure of Physics", Phil. Trans. Roy. Soc. Lond. A **376**, 0231 (2018). DOI: 10.1098/rsta.2017.0231

- [31] G. M. D'Ariano, "Physics Without Physics: The Power of Information-theoretical Principles", Int. J. Theor. Phys. **56**, 97 (2017). DOI: 10.1007/s10773-016-3172-y

- [32] X. D. Arsiwalla and J. Gorard, "Pregeometric Spaces from Wolfram Model Rewriting Systems as Homotopy Types", Int. J. Theor. Phys. **63**, 83 (2024). DOI: 10.1007/s10773-024-05576-0

- [33] N. Seiberg, "Emergent spacetime", in 23rd Solvay Conference in Physics: The Quantum Structure of Space and Time, **1**, 163 (2006). DOI: 10.1142/9789812706768_0005 arXiv:hep-th/0601234.

- [34] J. Polchinski, "String Theory", Cambridge University Press, (1998). DOI: https://doi.org/10.1017/CBO9780511816079

- [35] C. Rovelli, "Quantum Gravity", Cambridge University Press, Cambridge, UK, (2004). DOI: https://doi.org/10.1017/CBO9780511755804

- [36] M. Faizal, "The end of space–time", Int. J. Mod. Phys. A **38**, 2350188 (2023). DOI: 10.1142/S0217751X23501889

- [37] M. B. Green, J. H. Schwarz, and E. Witten, "Superstring Theory", Cambridge University Press, (1987). DOI: https://doi.org/10.1017/CBO9781139248563

- [38] T. Thiemann, "Modern Canonical Quantum General Relativity", Cambridge University Press, (2007). DOI: https://doi.org/10.1017/CBO9780511755682

- [39] M. B. Green and J. H. Schwarz, "Anomaly cancellation in supersymmetric $d=10$ gauge theory", Physics Letters B **149**, 117 (1984). DOI: 10.1016/0370-2693(84)91565-X

- [40] A. Ashtekar, "New variables for classical and quantum gravity", Physical Review Letters **57**, 2244 (1986). DOI: https://doi.org/10.1103/PhysRevLett.57.2244

---

Consequences of Undecidability in Physics on the Theory of Everything 19

[41] K. Gödel, "Über formal unentscheidbare sätze der principia mathematica und verwandter systeme i", Monatshefte für Mathematik **38**, 173 (1931). DOI: https://doi.org/10.1007/BF01700692

[42] P. Smith, "An Introduction to Gödel's Theorems". Cambridge University Press, Cambridge, 2nd ed., (2007). DOI: https://doi.org/10.1017/CBO9781139149105

[43] A. Tarski, "Pojecie Prawdy w Jezykach Nauk Dedukcyjnych (The Concept of Truth in the Languages of the Deductive Sciences)", Prace Towarzystwa Naukowego Warszawskiego, Wydział III **34** (1933). https://openlibrary.org/books/0L5813583M/Poje%CC%A8cie_prawdy_w_je%CC%A8zykach_nauk_dedukcyjnych

[44] A. Tarski, "Logic, Semantics, Metamathematics: Papers from 1923 to 1938". Hackett Publishing Company, Indianapolis, (1983). DOI: http://dx.doi.org/10.2307/2275031

[45] M. Faizal, A. Shabir, and A. K. Khan, "Implications of Tarski's undefinability theorem on the Theory of Everything", EPL **148**, 39001 (2024). DOI: 10.1209/0295-5075/ad80c2

[46] G. J. Chaitin, "A theory of program size formally identical to information theory", Journal of the ACM **22**, 329 (1975). DOI: 10.1145/321892.321894

[47] G. J. Chaitin, "Meta Math!: The Quest for Omega", Pantheon Books, New York, (2004). DOI: https://doi.org/10.48550/arXiv.math/0404335

[48] S. Kritchman and R. Raz, "The surprise examination paradox and the second incompleteness theorem", Notices of the AMS **57**, 1454 (2010). DOI: 10.48550/arXiv.1011.4974

[49] J. R. Lucas, "Minds, machines and gödel", Philosophy **36**, 112 (1961). DOI: 10.1017/S0031819100057983

[50] R. Penrose, "Gödel, the mind, and the laws of physics", in Kurt Gödel's and the foundations of mathematics: horizons of truth, 339. Cambridge University Press, (2011). DOI: https://doi.org/10.1017/CBO9780511974236.019

[51] R. Penrose, "The nonalgorithmic mind", Behavioral and Brain Sciences **13**, 692 (1990). DOI: 10.1017/s0140525x0008105x

[52] S. Hameroff and R. Penrose, "Consciousness in the universe: A review of the 'orch or' theory", Physics of Life Reviews **11**, 39 (2014). DOI: 10.1016/j.plrev.2013.08.002

[53] J. P. S., "The lucas-penrose arguments", in The Argument of Mathematics, p. Chapter 7. Springer, (2023). DOI: 10.1007/978-3-031-64217-3_7

[54] A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, and A. Tajdini, "The entropy of hawking radiation", Reviews of Modern Physics **93**, 035002 (2021). DOI: 10.1103/RevModPhys.93.035002

[55] N. Shiraishi and K. Matsumoto, "Undecidability in quantum thermalization", Nature Communications **12**, 5084 (2021). DOI: 10.1038/s41467-021-25053-0

[56] P. M. Chesler and L. G. Yaffe, "Horizon formation and far-from-equilibrium isotropization in a supersymmetric yang-mills plasma", Phys. Rev. Lett. **102** 211601 (2009). DOI: 10.1103/PhysRevLett.102.211601

---

20 Mir Faizal et al.

[57] S. D. Mathur, "The fuzzball proposal for black holes: An elementary review", Fortsch. Phys. **53**, 793 (2005). DOI: 10.1002/prop.200410203

[58] S. Steinhaus, "Coarse graining spin foam quantum gravity—a review", Frontiers in Physics **8** (2020). DOI: 10.3389/fphy.2020.00295

[59] T. Cubitt, D. Perez-Garcia, and M. M. Wolf, "Undecidability of the spectral gap", Forum of Mathematics, Pi **10**, 14 (2022). DOI: 10.1017/fmp.2021.15

[60] A. M. Turing, "On computable numbers, with an application to the entscheidungsproblem", Proceedings of the London Mathematical Society **s2-42**, 230 (1937). DOI: 10.1112/plms/s2-42.1.230

[61] M. Li and P. Vitányi, "An Introduction to Kolmogorov Complexity and Its Applications", Springer, (2019). DOI: 10.1007/978-3-030-11298-1

[62] J. D. Watson, E. Onorati, and T. S. Cubitt, "Uncomputably complex renormalisation group flows", Nature Communications **13**, 7618 (2022). DOI: 10.1038/s41467-022-35179-4

[63] C. G. Callan, D. Friedan, E. J. Martinec, and M. J. Perry, "Strings in background fields", Nucl. Phys. B **262**, 593 (1985). DOI: 10.1016/0550-3213(85)90506-1

[64] S. Steinhaus and J. Thürigen, "Emergence of spacetime in a restricted spin-foam model", Phys. Rev. D **98**, 026013 (2018). DOI: 10.1103/PhysRevD.98.026013

[65] D. Litim, "Fixed points of quantum gravity", Phys. Rev. Lett. **92**, 201301 (2004). DOI: 10.1103/PhysRevLett.92.201301

[66] J. Ambjørn, J. Jurkiewicz, and R. Loll, "The spectral dimension of the universe is scale dependent", Phys. Rev. Lett. **95**, 171301 (2005). DOI: 10.1103/PhysRevLett.95.171301

[67] P. Hayden, S. Nezami, X.-L. Qi, N. Thomas, M. Walter, and Z. Yang, "Holographic duality from random tensor networks", Journal of High Energy Physics **2016**, 009 (2016). DOI: 10.1007/JHEP11(2016)009

[68] B. Dittrich, F. C. Eckert, and M. Martin-Benito, "Coarse graining methods for spin net and spin foam models", New J. Phys. **14**, 035008 (2012). DOI: 10.1088/1367-2630/14/3/035008

[69] M. Kliesch, D. Gross, and J. Eisert, "Matrix-product operators and states: Np-hardness and undecidability", Physical Review Letters **113**, 160503 (2014). DOI: 10.1103/PhysRevLett.113.160503

[70] Y. Tachikawa, "Undecidable problems in quantum field theory", International Journal of Theoretical Physics **62**, 199 (2023). DOI: 10.1007/s10773-023-05357-1

[71] J. Bausch, T. S. Cubitt, and J. D. Watson, "Uncomputability of phase diagrams", Nature Communications **12**, 452 (2021). DOI: 10.1038/s41467-020-20504-6

[72] A. Feller and E. R. Livine, "Ising spin network states for loop quantum gravity: A toy model for phase transitions", Class. Quant. Grav. **33**, 065005 (2016). DOI: 10.1088/0264-9381/33/6/065005

---

Consequences of Undecidability in Physics on the Theory of Everything 21

[73] F. Amijee, "Principle of sufficient reason", in Encyclopedia of Early Modern Philosophy and the Sciences, D. Jalobeanu and C. T. Wolfe, eds. Springer, (2021). DOI: 10.1007/978-3-319-20791-9_593-1

[74] G. W. Leibniz, "Discourse on Metaphysics", Hackett Publishing Company, Indianapolis, (1996). A seminal work where Leibniz famously asserts that "nothing happens without a reason". https://www.earlymoderntexts.com/assets/pdfs/leibniz1686d.pdf.

[75] C. H. Bennett, "Undecidable dynamics", Nature **346**, 606 (1990). DOI: 10.1038/346606a0

[76] I. Stewart, "Deciding the undecidable", Nature **352**, 664 (1991). DOI: 10.1038/352664a0

[77] J. L. Friedman, M. S. Morris, I. D. Novikov, F. Echeverria, G. Klinkhammer, K. S. Thorne, and U. Yurtsever, "Cauchy problem in spacetimes with closed timelike curves", Physical Review D **42**, 1915 (1990). DOI: 10.1103/PhysRevD.42.1915

[78] I. D. Novikov, "Time machine and self-consistent evolution in problems with self-interaction", Phys. Rev. D **45** (1992). DOI: https://doi.org/10.1103/PhysRevD.45.1989

[79] M. Van den Nest and H. J. Briegel, "Measurement-based quantum computation and undecidable logic", Foundations of Physics **38**, 448 (2008). DOI: 10.1007/s10701-008-9212-6

[80] S. Lloyd, "Quantum-mechanical computers and uncomputability", Physical Review Letters **71**, 943 (1993). DOI: 10.1103/PhysRevLett.71.943

[81] R. Penrose, "On gravity's role in quantum state reduction", General Relativity and Gravitation **28**, 581 (1996). DOI: 10.1007/BF02105068

[82] L. Diósi, "A universal master equation for the gravitational violation of quantum mechanics", Physics Letters A **120**, 377 (1987). DOI: https://doi.org/10.1016/0375-9601(87)90681-5

[83] J. L. Gaona-Reyes, L. Menéndez-Pidal, M. Faizal, and M. Carlesso, "Spontaneous collapse models lead to the emergence of classicality of the Universe", JHEP **02**, 193 (2024). DOI: https://doi.org/10.1007/JHEP02(2024)193

[84] Álvaro Perales-Eceiza, T. Cubitt, M. Gu, D. Pérez-García, and M. M. Wolf, "Undecidability in physics: a review", (2024). https://arxiv.org/abs/2410.16532.

[85] N. Bostrom, "Are we living in a computer simulation?", Philosophical Quarterly **53**, 243 (2003). DOI: 10.1111/1467-9213.00309

[86] S. Guttenplan, "David J. Chalmers, Reality+: Virtual Worlds and the Problems of Philosophy", 60. (2023). DOI: 10.1007/s12115-023-00832-1

[87] D. Deutsch, "The Fabric of Reality", Penguin, London, (1997). https://www.daviddeutsch.org.uk/books/the-fabric-of-reality/.

---

