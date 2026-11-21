There was the recent exciting breakthrough in the Riemann Hypothesis proved with the help of AI that there's no zeros with Re s > 7/8. What was the largest confirmed zero free region before this?

Before this, there was no zero-free half-plane at all. Nobody had proved ζ(s) ≠ 0 for Re s > σ₀ for any fixed σ₀ < 1. That’s why the result is such a big deal. Every unconditional zero-free region shrank toward the line Re s = 1 as |t| grows.

The best known regions were:

Vinogradov–Korobov (best for large t): σ > 1 − c/((log t)^{2/3}(log log t)^{1/3}). The best explicit version I found is from 2024: no zeros in the region σ ≥ 1 − 1/(55.241 (log |t|)^{2/3} (log log |t|)^{1/3}) for |t| ≥ 3. 
jioinstitute
Classical de la Vallée Poussin form: σ > 1 − A/log t. The same 2024 paper has no zeros in the region σ ≥ 1 − 1/(5.558691 log |t|) for |t| ≥ 2. A March 2026 preprint by Bellotti, Trudgian and Yang improves this to σ > 1 − 1/(4.896 log t), but only for 3 ≤ t ≤ exp(76.47). 
jioinstitute
arxiv
Littlewood-type regions fill in the middle ranges. An explicit one is σ > 1 − log log t/(21.233 log t), t ≥ 3. 
arxiv
Low zeros: RH itself has been checked numerically up to height about 3·10¹². That’s a finite verification, not a region of any width.

The jump was from “a region whose width goes to 0 like (log t)^{−2/3−ε}” straight to a fixed strip.

Two caveats on the new result:

It’s OpenAI’s work, and the 7/8 claim is not the main focus. Quanta reports that the first version, dated September 30, 2026, claimed to show that all nontrivial zeros must be between 1/8 and 7/8, and was formally verified using the Lean programming language. The second version, which was completed almost a week later (and is not yet formally verified), claimed to prove a weaker result: that the zeros must have a real part between 1/12 and 11/12. It also says mathematicians have set aside the 7/8 paper to focus on the 11/12 one. 
quantamagazine
None of it is peer reviewed yet. As of mid-October, the public sources do not establish peer-reviewed confirmation of the full OpenAI claim. 
letsdatascience

Sources:

Quanta: AI Proved the Quasi-Riemann Hypothesis. What Happens Now?
Explicit zero-free regions for the Riemann zeta-function (Res. Number Theory, 2024)
Bellotti–Trudgian–Yang, Zero-free regions inspired by work of Heath-Brown (arXiv 2603.21490)
Let’s Data Science: OpenAI Publishes Claimed Quasi-Riemann Result

What's that claim of no Landau Siegel zeros?

Yes, there’s a separate claim, and from a specialist’s point of view it may matter more than the 7/8 headline.

What a Siegel zero is. The classical zero-free region for Dirichlet L-functions is L(s,χ) ≠ 0 for σ > 1 − c/log(q(|t|+2)). It holds for every L(s,χ) with one possible exception: a single real, simple zero β of L(s,χ) for one real (quadratic) character χ, sitting very close to 1. If such zeros exist for infinitely many moduli q with 1 − β = o(1/log q), those are Landau–Siegel zeros. Siegel’s theorem only gives 1 − β ≫_ε q^{−ε}, and the implied constant is ineffective. That one ineffective constant is why so many results about class numbers and primes in progressions come with no computable constants.

What OpenAI claims. There are two separate manuscripts: Landau–Siegel zero exclusion, dated October 1, 2026, and Quasi-Riemann hypothesis, dated October 5, 2026. If the quasi-RH result holds uniformly in q (Re s > 11/12 for every Dirichlet L-function), then Siegel zeros are ruled out immediately, since a real zero would have to satisfy β ≤ 11/12. The standalone Siegel-zero paper came first, though, and seems to be the more basic of the two. I couldn’t find the exact form of its statement, for example whether it’s an effective β < 1 − c/log q or a lower bound on L(1,χ). 
kingy

Independent reconstructions. Two human-authored preprints claim to redo the Siegel-zero argument:

Banks: a direct proof with explicit constants, arXiv:2610.15483 
kingy
Kerr: a simplified Landau–Siegel proof, arXiv:2610.21099 
kingy

The tracker that lists them describes them as independently authored, AI-assisted expositions. 
kingy

Why it would matter (standard consequences, not specific to these papers):

Siegel’s bound L(1,χ) ≫_ε q^{−ε} becomes effective. Through the class number formula, so do lower bounds for h(−d), which opens the way to computing every imaginary quadratic field with a given class number.
Siegel–Walfisz, Linnik’s theorem on the least prime in a progression, and other results on primes in progressions get computable constants.
A long list of results proved conditionally on “no Siegel zeros”, or proved in two separate cases depending on whether one exists, simplify.

Status. Neither OpenAI manuscript nor the independent preprints are peer reviewed. The positive expert assessments I found are mainly about the 11/12 argument. Per Quanta, experts “largely agree that the result is correct.” Radziwiłł says he can sketch it in half a page, and Sarnak says he won’t consider it “a Theorem” until humans check and understand all the details. I haven’t seen an equally explicit expert verdict on the standalone Siegel-zero manuscript, apart from the Banks and Kerr rewrites. 
kingy
quantamagazine

The Banks preprint is the one to read if you want to see the actual argument. It’s human-written and claims explicit constants.

Sources:

Breakthrough Tracker: quasi-Riemann and Landau–Siegel claims
Quanta: AI Proved the Quasi-Riemann Hypothesis. What Happens Now?
OfficeChai: OpenAI Solves Quasi Riemann Hypothesis
Wikipedia: Siegel zero

What kind of concrete results for Linnik’s theorem could we expect?

The quasi-RH result alone doesn’t improve Linnik’s constant. Combined with existing zero-density estimates, it should give L ≈ 12/5. I haven’t found a paper that actually does this yet, so what follows is my own back-of-envelope reasoning.

Baseline. Linnik’s original theorem (1944) asserts that the least prime p ≡ a (mod q) is ≪ q^{L+o(1)} for an absolute constant L (currently L=5 by Xylouris). GRH implies L=2, a natural “square root barrier.” Linnik’s theorem is also already effective. Both the exponent and the implied constant are effectively computable, unlike Siegel–Walfisz. 
themoonlight
arxiv

1. Excluding Siegel zeros by itself gives you basically nothing for L. The exceptional zero was never the bottleneck in Heath-Brown’s or Xylouris’s arguments. If it exists, Deuring–Heilbronn repulsion actually helps. Friedlander–Iwaniec note that if permitted the assistance of the exceptional character χ₁ (mod q), one can accomplish a lot more for this problem than with the Riemann Hypothesis, with L = 2 − 1/55 under suitable conditions. The hard case is the “generic” one: many zeros at distance ≍ 1/log q from the line Re s = 1. 
arxiv

2. The half-plane alone is worse than what we already have. Take a zero-free half-plane σ > θ, uniform over all χ mod q and all t. A smoothed explicit formula gives

ψ(x; q, a) = x/φ(q) + O(x^θ log q),

so you need x^{1−θ} ≫ φ(q) log q, which means L = 1/(1−θ). That’s 12 for θ = 11/12 and 8 for θ = 7/8. Both are worse than 5.

3. Half-plane plus zero-density estimates: L ≈ 12/5. Here the fixed gap δ = 1 − θ does real work. Count zeros with a density bound Σ_χ N(σ, T, χ) ≪ (qT)^{A(1−σ)+ε}. The contribution of zeros to the error is roughly

Σ_{χ,ρ} x^{β−1} ≲ max_{1/2 ≤ σ ≤ θ} q^{A(1−σ)+ε} x^{σ−1},

which tends to 0 once x ≥ q^{A + ε/δ}. Three things follow:

Because 1 − σ ≥ δ is bounded below, the q^ε losses get absorbed. You no longer need Linnik’s log-free density estimate, which is what forces large constants today.
Zeros near σ = 1/2 put a floor of 2 on L, so you can never beat the GRH exponent this way.
With the Ingham/Montgomery and Huxley-type hybrid estimates, the worst case is A = 12/5, at σ = 3/4. If I recall correctly, these are known for the full family of characters mod q, not just ζ. So you’d get L = 12/5 + ε, with an effective constant.

Some refinements:

Better density estimates: any improvement to A in the q-aspect for σ ≤ 11/12 lowers L directly. Guth–Maynard gives 30/13 ≈ 2.31 for ζ in the T-aspect. I’m not sure whether a hybrid q-aspect version exists yet.
Density hypothesis: A = 2 would give L = 2 + ε, essentially GRH quality. That’s the same mechanism as Bruna’s recent conditional result: Assuming the generalized Lindelöf hypothesis for Dirichlet L-functions, we establish that the least prime p ≡ a (mod q) satisfies p ≪_ε q^{2+ε}. As he puts it, under GLH, we obtain an arbitrarily large zero-free region and the density hypothesis in the entire half-strip. 
arxiv

4. The bigger payoff is uniform asymptotics, not just the least prime. The same argument gives the asymptotic count ψ(x; q, a) ~ x/φ(q) effectively for q ≤ x^{5/12−ε}. That’s a power-range Siegel–Walfisz, versus the current q ≤ (log x)^A with an ineffective constant.

5. Explicit versions. Banks’ preprint claims explicit constants. If those hold up, an explicit “p(q, a) ≤ C·q^{L}” for all q with L well under 5 looks within reach. The quality of the constant would depend on how small the explicit constants in the zero-free and density inputs are.

The expected outcome is Linnik’s constant dropping from 5 to about 2.4 (perhaps around 2.3 with newer density estimates), still above the GRH value of 2. If nobody has posted this in the last few weeks, it’s a fairly mechanical write-up.

Sources:

Bruna, A conditional bound for the least prime in an arithmetic progression (arXiv 2603.25612)
Ford–Radziwiłł, Sign changes of the Liouville function in arithmetic progressions (arXiv 2605.03349)
Friedlander–Iwaniec, Sifting for small primes from an arithmetic progression
Review of Matomäki–Teräväinen, Linnik’s problem for multiplicative functions

Can you schematically visualise the known zero free regions before and after this breakthrough for the RH?

There are three separate proofs here, and the AI’s contribution looks different in each. The experts quoted so far agree on one point: the proof introduces no new concepts. Dunn calls it “a surprising synthesis of well-known ideas.” The spark is in which existing tools it combined, and in its belief that they were already strong enough. I’ve worked from summaries and expositions here, not a line-by-line reading of the papers. 
quantamagazine

1. Quasi-RH, 11/12 version (the one experts actually read)

Idea A: put ζ inside the right family, built over Q(√−3), and amplify. The proof bounds a smoothed Möbius sum A₁(D) = Σ μ(n)ν(n)W(N(n)/D) over the Eisenstein integers, where ν is a Hecke character. Its Mellin transform is W̃(s)/L_K(s,ν), so a power saving for A₁ continues 1/L_K to the left. The trick is to embed A₁ in a family A_u twisted by sextic residue symbols χ_n(u). For u = p⁶ the twist is trivial unless p | n, so A_(p⁶) = A₁ + O(D/Y). In other words, A₁ shows up about Y/log Y times inside the family. A mean-square bound over the whole family then gives a saving for A₁, at a cost tied to the sixth power: taking Y = H^(1/6), gives |A₁|² ≪ D^(2+ϑ)/Y + D²/Y², which is where 11/12 comes from. This is Sarnak’s old idea of studying ζ through a family. The model identified a family that had been overlooked. Henryk Iwaniec came close in 2002 but missed it. 
judegomila
quantamagazine

Idea B: Poisson summation turns μ into an automorphic object. I think this is the real spark. Expanding Σ|A_u|² and applying Poisson in u replaces the sextic characters by Gauss sums. Then a classical Gauss-sum identity (Hasse, Heath-Brown) gives μ(n)γ₋₁(n) = (unimodular factors)·γ₂(n). The Möbius function is replaced by a cubic Gauss sum. That matters because cubic Gauss sums are Fourier coefficients of Kubota’s cubic metaplectic theta function, so they have automorphy and a reflection formula. The Möbius function, the very thing that resists any structure, gets traded for coefficients of a modular form. The level-aspect Voronoi formula from Dunn–Radziwiłł’s 2021 proof of Patterson’s conjecture then does the analytic work. 
judegomila

There are also two technical moves worth knowing:

Using the quadratic large sieve instead of the cubic one. Dunn and Radziwiłł had shown that Heath-Brown’s cubic large sieve is sharp up to factors of X^(o(1)) under the Generalized Riemann Hypothesis, so the cubic sieve is a dead end. Theta reflection converts the twist χ_n(h) into χ_h(m)³. The cube of a sextic character is quadratic, and the quadratic large sieve is optimal. 
researchgate
judegomila
A shrinking recursion. Two Poisson steps map (R, X) to (R/N(b)³, X/N(b)³) while the ratio R/X stays fixed. That means the process terminates after about (1−2ϑ)/(2ϑ) rounds, a number that depends only on ϑ. 
judegomila

Radziwiłł’s verdict on the overall strategy was that the implicit belief that existing tools would suffice was “a pretty bold belief to have!” 
quantamagazine

2. Quasi-RH, 7/8 version

This version adds a bootstrap over the whole family at once. Let β* be the supremum of the real parts of zeros of all primitive Hecke L-functions over K, and assume β* > 7/8. The proof then finds a uniform margin ε* that continues 1/L_K to Re s > β* − ε*, which contradicts the definition of β*. Making ε* uniform across characters needs new moment bounds, prime compensation, and asymmetric scales Z^(17/48) and Z^(23/48). This reads more like heavy optimisation than a new insight. Liu has since pushed the exponent to about 0.87496 and argued it is essentially optimal for this method. 
judegomila

Transfer to ζ (both versions). This step is standard but essential: L_K(s, χ∘N) = L(s,χ)·L(s, χχ₋₃). So any zero of a Dirichlet L-function, ζ included, is also a zero of an L-function over Q(√−3). The insight is to solve the problem over a field where cubic and sextic reciprocity exist, rather than over ℚ. 
judegomila

3. No Landau–Siegel zeros: a completely different idea

There’s no harmonic analysis here at all. It’s an interpolation-determinant argument from transcendence theory, which to me is the more surprising of the two results. Banks’s reconstruction goes like this:

A Siegel zero forces bias in χ(p). If δ = (1−β)log q is small, the explicit formula shows that primes with χ(p)=−1 carry almost all the logarithmic mass up to X. This is the only place β enters. 
arxiv.org
Frobenius acts as a Galois conjugation mod p. Work in K = ℚ(√d, √2). For p with χ(p) = −1, Euler’s criterion gives a^p≡ −a and b^p≡(2/p)b (mod p𝒪). So θ^p≡ g_p(θ) (mod p𝒪), where g_p∈{σ,στ}. 
arxiv.org
The determinant is very divisible. Build a nonzero determinant Δ ∈ ℤ[√d, √2] from monomials in θ, σθ and στθ, evaluated at lattice points. In each row you can replace θ^{pk} by (θ^p − g_p(θ))^k without changing Δ. So Δ is divisible by p^{Σ⌊α₁/p⌋} for every such p. When almost all primes are inert in this sense, the norm of Δ must be enormous.
Hadamard’s inequality caps the size. It bounds |N(Δ)| from above. The numerology comes out as follows: the upper bound’s main term is at most 13/16 S₁ log M, while the lower bound’s main term is about S₁ log M times the prime-bias fraction. Since 13/16 < 1, a Siegel zero gives a contradiction. 
arxiv.org
The role of √2. It’s a clever gadget. It makes the lattice rank 4 while the interpolation uses only 3 variables, giving log N = 3/4 log M. It also pins down the Frobenius at the χ(p) = −1 primes to σ or στ, both of which are among those 3 variables. 
arxiv.org

The insight is to turn the Siegel zero’s own consequence, "χ behaves like λ(n)", into p-adic arithmetic information, and then play it against an archimedean bound. Transcendence methods had touched class numbers before (Baker, Stark), but as far as I know never in a way that exploits the Siegel zero this directly. Banks also gets explicit constants: δ₀ = 3.0 × 10⁻³ for q ≥ 10¹⁰. 
arxiv.org

Overall: one argument converts μ into cubic Gauss sums so that automorphy applies; the other converts a Siegel zero into p-adic divisibility. In both cases the input tools had sat on the shelf for decades. What humans apparently missed was that these particular combinations close. This is still my reading of secondary expositions, so treat the details as provisional. Banks’s paper is the clearest place to check the Siegel argument yourself.

Sources:

Quanta: AI Proved the Quasi-Riemann Hypothesis. What Happens Now?
Gomila: The quasi-Riemann hypothesis, an exposition
Banks: On the OpenAI proof that Landau–Siegel zeros do not exist (arXiv 2610.15483)
Kerr: A simpler proof that there are no Landau–Siegel zeros (arXiv 2610.21099)
Liu: Zero-free half-planes for Hecke L-functions over number fields (arXiv 2610.26835)
Dunn–Radziwiłł: Bias in cubic Gauss sums, Patterson’s conjecture (arXiv 2109.07463)
Slightly improved zero-free half-planes for the quasi-RH (arXiv 2610.12234)

Terence Tao said that the RH proof (and I'm not sure which one he referred to) contains "a very unusual combination of arguments" that no living mathematician would've come up with, or maybe if you locked enough of the leading experts in for long enough, they might have brute forced it. What exactly did he mean by that?

Tao said this in a Numberphile interview, “No More Heroes — Terence Tao Talks to Numberphile About AI” (15 October 2026). He was talking about the quasi-RH proof, not the Siegel-zero paper. I can’t watch the video, so I don’t have his exact words, only MathWorld’s paraphrase: Tao viewed the argument as a novel blend of established methods that he doubted any one mathematician would have devised, though a suitable team might have found it through trial and error. A second-hand summary of a post quoting him talks of a technique combining three or four existing ideas in an unusual way. 
wolfram

The pieces were already known. The 11/12 proof combines four strands from different communities:

The classical part. Bound a Möbius sum, continue 1/L, and get a contradiction at a hypothetical zero. This is textbook analytic number theory going back to de la Vallée Poussin.
An amplified family over Q(√−3). Twist by sextic residue symbols and use u = p⁶ to make the target sum appear many times. Amplification is standard in moment and subconvexity problems, but nobody had used this particular family for zero-free regions.
Metaplectic forms. Poisson summation and a Gauss-sum identity turn μ into cubic Gauss sums. Those are Fourier coefficients of Kubota’s cubic theta function, and Dunn–Radziwiłł’s level-aspect Voronoi formula then applies. Quanta describes these as obscure objects that Alexander Dunn has studied for about five years. Very few people work on them, and those who do study Patterson’s conjecture and Gauss-sum bias, not zero-free regions. 
quantamagazine
The large sieve. The key move is switching from the cubic large sieve to the quadratic one, since cubing a sextic character makes it quadratic. A Poisson recursion that ends after a fixed number of steps closes the argument.

What makes the combination unusual. No single expert has all four in their working toolkit. The metaplectic specialists don’t work on zero-free regions, and the zero-free-region specialists don’t use metaplectic theta functions. On top of that, the field believed the existing tools were too weak: Experts had believed the relevant tools were insufficient and that a different branch of number theory would be needed. So nobody had a reason to look for this combination. Even the people whose formula is the crucial ingredient didn’t see it coming. Dunn said, “Nobody expected this.” 
quantamagazine

What “brute forced” means here. Each step can be checked by an expert in that step. The hard part is the search: choosing a family (why Q(√−3)? why sextic twists? why p⁶?) and then a sequence of transformations that happens to close up. If you locked Dunn, Radziwiłł, Heath-Brown and a few others in a room, their combined expertise covers every ingredient. With enough time trying combinations, they might have found it. The AI’s advantage seems to have been breadth across subfields plus tireless trial and error, not a new concept. That fits Radziwiłł’s comment that the core argument fits in half a page once you know it.

The same paraphrase records a limit Tao saw: He also said the method couldn’t move the zero-free boundary left of Re[s]=3/4 without another highly clever idea. So he sees this as a new combination that pushes known tools to their limit, not as a road to RH. 
wolfram

Sources:

MathWorld: Quasi-Riemann Hypothesis
Quanta: AI Proved the Quasi-Riemann Hypothesis. What Happens Now?
Digg summary of the Tao remarks