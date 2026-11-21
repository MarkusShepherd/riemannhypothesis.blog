PDF

Please read this paper and summarise the argument of chapter 3 for me.

Core argument of Chapter 3: some prime-generating sequences use only gcd/lcm recurrences that weren't designed to produce primes, yet they seem to output only 1s and primes. Rowland's case is proved, Cloitre's partly, Stevens' not at all. None of them is a practical way to generate primes.

3.1 Rowland: a(n) = a(n−1) + gcd(n, a(n−1)), a(1) = 7, g(n) = a(n) − a(n−1)

Lemma 3.1: suppose a(n₁) = r·n₁ with r ∈ {2,3}, and let p be the least prime factor of (r−1)n₁ − 1. On the following run, each g(n₁+i) divides both (r−1)n₁ − 1 and (r−1)i + 1. So g = 1 until i = (p−1)/(r−1). At that step g = p exactly, and a = r·n₂ again, so the state reproduces itself.
Theorem 3.2: a(3) = 9 = 3·3, so induction with r = 3 gives the result. Skipping the (p−3)/2 ones before each prime requires finding a least prime factor, so there is no computational gain.
Props 3.3 and 3.4: for a(1) = 7, 2 < a(n)/n ≤ 3, with equality exactly at the prime steps.
Other start values: everything reduces to reaching a(N) = 3N once (Conjecture 3.5). Before that point, composites can occur, e.g. g(18) = 9 for a(1) = 532. Cor. 3.7 locates the nontrivial steps for any a(n₁) = n₁ + d but doesn't control their values. Rowland's claim that every odd prime appears is treated sceptically: 587 is already missing.

3.2 Cloitre: b₁(n) = b₁(n−1) + lcm(n, b₁(n−1)), so q₁(n) = n/gcd(n, b₁(n−1)) and b₁(n) = ∏(1+q₁(i))

Lemma 3.9: ν₂(b₁) rises every step, so q₁ is odd for n > 4. All prime factors of b₁(n) are smaller than n.
Theorem 3.10: therefore q₁(p) = p for every prime p > 3. Every prime except 3 occurs.
w(n) = min{k : kn−1 prime}: q₁(w(p)p) = 1, because the prime w(p)p−1 contributes the factor w(p)p. Conjecture 3.12 says q₁(kp) = p for k < w(p). The proof is reduced to showing p ∤ b₁(kp−1) and k | b₁(kp−1), which is left open. The 1s stay uncontrolled anyway, since q₁(25) = 5.
b₂ variant (2·b₂(n−1) + lcm): q₂ empirically misses exactly the larger twin primes except 7. That would tie the twin prime conjecture to infinitely many primes being missing.
General b_k: composites appear, e.g. q₆(25) = 25.

3.3 Stevens: e(n) = gcd(p(n), p(n−1) − 3k), using Euler's n² − n + 41, with k incremented after each nontrivial gcd. The 1s-and-primes property is only empirical, with no proof in sight.

3.4 Conclusion: this inverts Section 2. There, the definitions are artificial and the proofs easy. Here, the definitions are simple and the proofs are hard.

Two remarks of my own:

The twin-prime pattern follows from the paper's own machinery. Since b₂(n) = b₂(n−1)·(2 + q₂(n)), q₂(p−2) = p−2 puts the factor p into b₂ early, which forces q₂(p) = 1. 7 survives only because (3, 5, 7) is the unique prime triple: 5 is already killed, so q₂(5) = 1. This only explains why p is missing at index p, not at later multiples.
The sketch for 3.12 has a gap. "i ∤ b₁(i−1), also ggT(i, b₁(i−1)) = 1" doesn't follow, so i = lp−1 isn't established.

Let's start from Rowland. His proof is reproduced, but there's also the open conjecture 3.5 from his paper. Do you think it's true or false? Why? Could you think of general approaches on how to prove or disprove?

Short answer: I'd bet on true, and on it being very hard to prove. As far as I can find it's still open. Rowland's own later talk slides still state it as a conjecture. Chamizo, Raboso and Ruiz-Cabello (EJC 2011) show it follows from another conjecture of theirs, but don't settle it.

A reformulation that explains most of the behaviour

Look only at collision indices n, where g(n) > 1. Set Δ = a(n) − n − 1 and G = a(n) − 3n.

After the first even-index collision, Δ stays odd: d | Δ forces d odd, so Δ + d − 1 is odd.
In the following run, g(k) = gcd(k, Δ). Substitute o = 2k − Δ, which is odd.
Then k is a collision iff o is a multiple of a prime factor of Δ, and k > n iff o ≥ 3 − G.
At that collision, g(k) = gcd(o, Δ). So with o the smallest admissible value and m the next collision index:

a(m) − 3m = gcd(o, Δ) − o.

Consequences:

Sign invariance. The sign of a(n) − 3n at collision times never changes until it hits 0. An orbit can't cross ratio 3 from either side without landing on it exactly.
From above (G > 0): the orbit reaches a(m) = 3m at the next collision iff lpf(Δ) > G − 3. Lemma 3.1 is the case G = 0.
From below (G < 0): it reaches 3m iff o | Δ. The condition lpf(Δ) ≥ 3 − G suffices.
Below ratio 2: the same substitution with o = k − Δ works, with 2n as the barrier.
Why only r ∈ {2, 3} give absorbing states: the substitution needs r − 1 to be invertible mod every prime factor of Δ.

I checked this map against direct simulation. That covered all a(1) ≤ 20 000, and all n₁ ≤ 400 with 2n₁+1 < a(n₁) < 3n₁. There were no mismatches once Δ is odd.

For a(1) = s you stay above ratio 3 throughout, and early on G ≈ Δ. So reaching 3N is essentially "Δ is prime". The transient is a walk Δ ↦ Δ + d − 1, driven by small prime factors, waiting to hit a prime.

Why I think it's true

Random model. At each collision, the chance of reaching 3N is at least P(odd Δ is prime) ≈ 2/log Δ. Since Δ' < 2Δ, log Δₖ grows at most linearly in k. So Σ 2/log Δₖ diverges, and escaping forever has probability 0. This needs no drift estimate for G. A counterexample also needs infinitely many composite gcds, which is a stronger requirement.
The model's prediction holds up. It predicts about (log s)/2 collisions before reaching 3N. Measured over 3000 random s per decade:
s ~ 10³: 3.7 observed vs 3.7 predicted
s ~ 10⁶: 6.7 vs 7.1
s ~ 10⁹: 10.1 vs 10.6, with a maximum of 72 collisions
Bounded excursions are harmless, at least for small bounds. Suppose a(n) − 3n ≤ B at every collision from above. Then the dynamics depends only on Δ mod lcm(1,…,B), so it is a finite automaton. I searched it exhaustively and found no cycle that avoids reaching 3N for B ≤ 18 (43M states). So any counterexample from above has a(n) − 3n > 18 at collision times infinitely often.

Approaches to a proof

Split into low G and excursions. Low G is a finite check for each bound B, but the state space grows like e^B. The real content is showing G can't stay large forever while Δ avoids being rough. That is Rowland's "ratio can't stay above 3" obstruction, in a sharper form.
Face the parity barrier. The excursion problem asks whether an adaptively defined walk hits a G-rough number. Sieves give almost-primes, not primes, and this walk isn't polynomial in anything. Unconditionally I'd aim lower: show G drops below a fixed bound infinitely often, or that Δₖ equidistributes mod small primes.
Average over the initial value. "Reaches 3N within k collisions" becomes a residue condition on s plus "a linear form in s is prime". The catch is that you need ≫ log s collisions, and the conditioning modulus grows like a primorial, leaving Bombieri–Vinogradov range quickly. Cloitre hits the same wall for the lcm variant, where a complete proof would need a strengthening of Linnik's theorem that is currently out of reach. "Almost all initial conditions" under Elliott–Halberstam or Hardy–Littlewood looks like the realistic target.

Approaches to a disproof

Extend the automaton search. A cycle that never reaches 3N for some B, with a composite gcd on it, would be a rigorous counterexample. The residue dynamics is exact, so every Δ in that class repeats the cycle forever. In C with bitsets B ≈ 22–24 seems feasible; beyond that the e^B growth wins.
Build long transients with CRT. Chamizo et al. characterize which finite chains of least prime factors can occur, via modular conditions; their example has length 27. That gives arbitrarily long transients, but an infinite one needs exactly the periodic conspiracy that (4) searches for.
Rowland's r ≥ 4 repetitions are the obvious candidates, and they decay. Each repetition requires lpf((r−1)n − 1) ≡ 1 mod (r−1). This fails with positive probability every time, which is why his search found ratio 7 recurring only eleven times.

I can send the verification scripts if you want to push B further.

Sources:

Rowland, A natural prime-generating recurrence (arXiv)
Rowland, Formulas for primes (talk slides)
Chamizo, Raboso, Ruiz-Cabello, On Rowland's sequence (EJC 2011)
Cloitre, Primes in LCM recurrences (arXiv 2025)

Why do you think it'll be hard to prove? (Apart from it being apparently open for 20 years now.)

The existing proof works for a reason that is absent in the transient. What remains is a primality question about every single deterministic orbit, and we have essentially no tools for that kind of statement.

There is no invariant outside the 3N state.
Rowland's lemma works because a = 3n holds at every collision. That pins the next gcd to lpf(2n−1), and g | p rules out composites algebraically.
In the transient nothing is conserved. G = a − 3n isn't monotone: one step can nearly double it, since G' = |o| + gcd(|o|, Δ) ≤ 2G − 6.
The big up-jumps occur exactly when gcd(o, Δ) is large, which is also where composite gcds come from.
Props 3.3/3.4 only make ⌈a/n⌉ monotone, and that still allows an orbit to hover above 3 forever.
Any potential function would effectively have to know when Δ is prime.
Reaching 3N is a primality event.
For a(1) = s and n < Δ/4, we have G − 3 > Δ/2 − 2. So the condition lpf(Δ) > G − 3 just says Δ is prime.
The conjecture therefore contains a statement of the form: for every s, a factorization-driven sequence Δₖ(s) eventually hits a prime.
Statements of that shape are open across the board. Collatz is one example. Home primes are another: iterating "concatenate the prime factors" is conjectured to always reach a prime, and HP(49) is still unknown.
The heuristic Σ 2/log Δₖ = ∞ is the same one that makes all of those look obviously true.
Sieves need distribution we don't have, and parity blocks the rest.
Where G ≪ √Δ, reaching 3N only needs Δ to be G-rough, which sieves can detect in principle. But a sieve needs a family with known distribution in residue classes. Here the only family is the orbit itself, and its distribution mod small primes is the unknown dynamics.
The orbit is also deliberately non-random: Δ' ≡ −1 mod the prime it just collided with, so it steers away from its recent primes.
Where G > √Δ you need actual primes. Selberg's parity problem says sieve information alone gives at best P₂.
Averaging over s doesn't rescue "for all s".
The best template is Tao's Collatz theorem: almost all orbits attain almost bounded values, in logarithmic density. The method gives no handle on every orbit.
Here, averaging turns "reaches 3N within k collisions" into primes in residue classes. But you need ≫ log s collisions, and the conditioning modulus grows like a primorial, so you leave Bombieri–Vinogradov range almost immediately.
Cloitre's lcm paper hits the same wall. Even an "almost all s" result probably needs Elliott–Halberstam-strength input.
The tractable part is already done; the rest couples size and arithmetic.
Bounded G is a finite automaton, decidable for each bound. I checked up to 18 and found no cycle that avoids reaching 3N.
All the difficulty sits in unbounded excursions, where the reaching-3N test degenerates into a primality test.
A proof has to control the size of G relative to Δ and the arithmetic of Δ at the same time, along one orbit. I don't know a technique that couples those two.

What would change my mind is a hidden semi-invariant that forces G down, the way Δ was the hidden quantity behind Lemma 3.1. It would have to tolerate the large-gcd up-jumps, so that's where I'd look first.

Let's move on to Cloitre's sequence. First give me a summary of what's known, either from my thesis or anything that has been published since.

Status: the full conjecture (b_n is always 1 or prime) is still open. What's proved: the prime values that occur, the exclusion of 3, a conditional proof assuming a strong Linnik-type hypothesis, and (in a 2025 preprint) a density-1 result.

Notation: b(n) = b(n−1) + lcm(n, b(n−1)), b(1) = 1, and q(n) = n/gcd(n, b(n−1)), so that b(n) = ∏(1 + q(i)).

From your thesis (2010)

Lemma 3.9: ν₂(b) grows at every step, q(n) is odd for n > 4, and every prime factor of b(n) is smaller than n.
Theorem 3.10: q(p) = p for every prime p > 3, so every prime except 3 occurs. "3 never occurs" was asserted, not proved.
Lemma 3.11: q(w(p)p) = 1, where w(p) is the least k with kp − 1 prime.
Conjecture 3.12: q(kp) = p for k < w(p). You noted that controlling this needs w(p) ≤ p, which is Dirichlet/Linnik territory.
The b₂ variant: the missing primes look like the larger members of twin pairs. The general b_k produces composites (q₆(25) = 25). You also remarked that the start value is inessential.

Ruiz-Cabello (arXiv 2015, IJNT 2017)

3 never occurs: proved unconditionally, using an explicit prime-counting bound. He credits your Theorem 3.10 for b_p = p.
Conditional proof: suppose that for every prime p and every k ≥ 1 there are at least k primes ≡ −1 (mod p) below p^(k+1). Then b_n is 1 or the largest prime factor of n. That is sharper than "1 or prime", and it matches your q(25) = 5, q(52) = 13 and q(169) = 13.
The mechanism is your Lemma 3.11 generalized: each prime q ≡ −1 (mod p) contributes a factor q + 1 to b, which builds up ν_p fast enough.
General start value s: composites do occur, and he classifies exactly which odd composites can appear. 15 is the smallest that never does. Every odd prime power does, e.g. 49 at n = 49 for s = 533. So the start value is not inessential after all.

Cloitre (arXiv preprint, Oct 2025)

Density result (claimed unconditional): b_n ∈ {1} ∪ P for a set of n of density 1. Small primes are handled by Siegel–Walfisz, medium ones by Bombieri–Vinogradov, and large ones by counting.
Effective result (claimed): beyond an effective bound N*(P₀), any counterexample has all prime factors > P₀.
Full conjecture: he states that a complete proof needs a Linnik strengthening that is currently out of reach.
The K = 2 variant (your q₂), unconditional:
If (p, p+2) are twin primes and c_p = p, then c_(p+2) = 1. This is the mechanism behind the twin-prime gaps.
c at index 2^(2k+1) equals 2, so 2 occurs infinitely often.
The K = 2 variant, assuming q₂ is always 1 or prime:
For primes q ≥ 5, c_q = 1 iff q − 2 is prime and q ≠ 7.
A larger twin prime q ≥ 13 can only appear at indices divisible by q².
He cites your thesis, and OEIS A135508 links to it.
I haven't checked his proofs. The density argument reads as a sketch in places, and it's an unrefereed preprint as far as I can tell.

My own remark on where the difficulty sits:

For k ≥ 2, GRH gives Ruiz-Cabello's hypothesis for all large p, uniformly in k: the main term p^k/((k+1) log p) beats the error term, which is roughly p^((k+1)/2).
So under GRH everything reduces to k = 1 plus a finite check. The k = 1 case asks for one prime ≡ −1 (mod p) below p², which is exactly your w(p) ≤ p.
Even GRH only puts the least such prime at about p² log² p. So the crux sits just beyond GRH.

Sources:

Ruiz-Cabello, On the use of the least common multiple to build a prime-generating recurrence (arXiv)
Cloitre, Primes in LCM recurrences (arXiv)
OEIS A135506
OEIS A135508

So, do you reckon either of those open question would be tractable for an AI proof, assuming it would receive the same level of attention and resources as some of the latest advances in maths, e.g., Navier-Stokes, Siegel zeroes or the AI proof dump?

The two differ in an important way. Cloitre's conjecture runs into a known barrier. Rowland's has no known barrier, but also no known foothold.

Cloitre: the full conjecture, almost certainly not.

Cloitre's conjecture implies that for every prime p there is a prime q ≡ −1 (mod p) with q < p². In your notation, that is w(p) ≤ p.

Proof: suppose all b_i with i < p² are 1 or prime.

Then p divides 1 + b_i only when b_i is a prime ≡ −1 (mod p). Such a b_i is below p².
Conversely, every such prime q does occur, since b_q = q.
So if no such q exists, ν_p(a_(p²−1)) = 0, and b_(p²) = p² is composite.

In the other direction, Ruiz-Cabello showed the conjecture follows if, for every k, there are at least k primes ≡ −1 (mod p) below p^(k+1). For k ≥ 2, GRH gives this for all large p, uniformly in k. So modulo GRH and a finite computation, Cloitre's conjecture is equivalent to "w(p) ≤ p for every p". The combinatorics is essentially solved; what's left is a least-prime statement.

That statement is beyond GRH, which only puts the least prime ≡ −1 (mod p) at about p² log² p. The claimed quasi-Riemann result (no zeros with real part above 7/8 or 11/12, no Siegel zeros) would give an exponent around 8. A proof of the full conjecture therefore has to contain a least-prime theorem stronger than GRH delivers. That would be the real headline, not the sequence.

Realistic AI outcomes for Cloitre:

writing up and formalizing the conditional equivalence;
checking or repairing Cloitre's density-1 argument;
the K = 2 statements.

Your thesis already flagged w(p) ≤ p as the bottleneck. It turns out to be forced by the conjecture, not just an obstacle to one proof idea.

Rowland: plausible, but a lottery ticket.

Points in favour:

It's elementary, has no known barrier, and is easy to state in Lean.
The reduction to the (Δ, G) map gives a crisp target.
Candidate semi-invariants can be tested on billions of orbits for almost nothing.
10 000 agents proposing potentials, with cheap numerical filtering and Lean checking, is exactly the regime where that scale helps.

Points against:

If no semi-invariant exists, a proof needs control of primality along a single orbit, and scale doesn't create theory that may not exist.
The forced Navier–Stokes blow-up was a construction: find an object, verify it. That is the sweet spot for this kind of effort. Rowland's conjecture needs a universal statement over all orbits. Only a disproof would be a construction, and I think the conjecture is true.

Gut odds at that level of effort:

Outcome	Odds
Proof of Rowland's conjecture	10–20%
Disproof of Rowland's conjecture	< 5%
Proof of Cloitre's full conjecture	low single digits, and only via a least-prime breakthrough
Substantial partial results on both	near certain

Caveat on the benchmarks. The Navier–Stokes result is the forced case. The quasi-RH paper is unrefereed, and coverage disagrees on 7/8 versus 11/12. If it holds up, it shows these systems can do deep analytic number theory. That raises my odds on Cloitre's partial results, but not on the full conjecture, which needs more than GRH.

Sources:

Inside OpenAI's Navier–Stokes claim (The Neuron)
OpenAI's Quasi-Riemann Hypothesis explained (OfficeChai)
OpenAI's batch of 372 results (zeli.app)
Ruiz-Cabello (arXiv)

I'm thinking of making an AI proof of my master's thesis into a blog post: https://gitlab.com/mshepherd/riemannhypothesis.info/-/work_items/4
Could something similar be done with this topic?

Yes, and I'd make it the companion post rather than a copy of #4. #4 tests whether off-the-shelf AI can redo known maths, built from known techniques. This topic tests whether it can make progress on open problems whose statements are elementary. That changes three things.

1. Lean works here.

gcd, lcm, primes and factorizations are all in Mathlib.
So for most targets the verifier is a proof checker, not two referees plus your final read.
Only the analytic parts need referees: Linnik, sieves, Cloitre's density argument.

2. There's already a baseline to compare against.

OEIS Open (Adamczewski, Aug 2026) runs frontier models against 492 Lean-formalized OEIS conjectures.
One of them is McEachen's conjecture for A135508, which is your b₂ twin-prime observation: q₂(p) = p whenever p − 2 is not prime.
It was attempted 19 times, at $50–200 per attempt, including Fable 5.1, GPT-6 Astra and Gemini 3.1 Pro. All 19 failed.
Rowland's conjecture and A135506 aren't in the set.

3. Success has to be graded, not pass/fail. Here's why those runs failed, and what was there to find. I checked all of the following numerically up to 10⁶.

Reformulation: q₂(p) = p ⟺ q₂(p−2) ≠ p−2 ⟺ gcd(p−2, b₂(p−3)) > 1. This is elementary, because b₂(n) = b₂(n−1)(2 + q₂(n)), and p | 2 + q₂(i) forces i = p − 2.
Half the cases are trivial: q₂(4) = 1 puts a factor 3 into b₂(n) for every n ≥ 4. So q₂(q) = q for every prime q ≡ 2 (mod 3) with q ≥ 11, and every p ≡ 2 (mod 3) is settled in two lines.
Almost all of the rest: for p ≡ 1 (mod 3), it's enough that some prime factor r of p − 2 admits a prime q ≡ 2 (mod 3) with q ≡ −2 (mod r) and 11 ≤ q ≤ p − 3.
Linnik's theorem (effective, exponent ≤ 5) covers every p where p − 2 has a prime factor below c·p^(1/5).
The leftover p form a sieve-thin set. So the conjecture holds for almost all primes, unconditionally, once the sieve bound is written out.
What blocks the full statement: the case p − 2 = r·s with r ≈ s needs a prime ≡ −2 (mod r) below about r². That's Linnik exponent 2, which even GRH doesn't give. It's the same barrier as Cloitre's main conjecture.

So a single $200 attempt at the full Lean statement was never going to succeed, and the benchmark scores it 0. Meanwhile the partial results are the real content. I haven't checked whether they're already known. Cloitre's preprint proves the statement only by assuming the full 1-or-prime conjecture.

Targets, from easiest to hardest:

Control: reproduce your Chapter 3 in Lean, i.e. Lemma 3.1 and Theorem 3.2, Theorem 3.10, Lemma 3.11 and the b₂ inhibition step. Also repair the gap in the 3.12 sketch. This should succeed and tells you the minimum cost.
New and Lean-checkable:
the A135508 results above;
Rowland's (Δ, G) reduction with sign invariance;
"bounded excess implies absorption" from the automaton search (computer-assisted);
Cloitre ⟺ w(p) ≤ p, assuming GRH plus a finite check.
Referee mode, no Lean: check Cloitre's density-1 argument. It's unrefereed and reads like a sketch in places.
Lottery ticket: Rowland's conjecture itself, via a search for a semi-invariant.

Changes to the #4 harness:

Lean replaces the referees for targets 1 and 2.
The numerics agent becomes a falsifier: every proposed lemma gets tested numerically before anyone tries to prove it. That's how the reformulations above came out.
Add a literature and novelty agent. The Erdős audit, which found a "solved" problem already implied by earlier work, shows why.
Report how far each target got, and the cost against the OEIS Open baseline: a single agent at $200 versus your harness at $X.

That makes a natural two-part series using the same harness. Post 1 asks whether AI can redo known work. Post 2 asks whether it can make progress on open problems, and how you'd even measure that.

Should I file this as an issue next to #4?

Sources:

Adamczewski, OEIS Open (arXiv 2608.11941)
Announcement on SeqFan
OEIS Open run results (GitHub)
Cloitre, Primes in LCM recurrences
OEIS A135508

Raise this as a follow up GH issue with as many relevant details as possible.

I filed it as #5 in your GitLab repo (you said GH, but the repo and #4 are on GitLab) and linked it to #4 as related: https://gitlab.com/mshepherd/riemannhypothesis.info/-/work_items/5

It holds:

The thesis's Chapter 3 results, with your own numbering, plus three review points from my read.
What's known since: Chamizo–Raboso–Ruiz-Cabello 2011, Ruiz-Cabello 2017 and Cloitre's 2025 preprint, with my concerns about Cloitre's preprint.
The new observations from this chat, each with what was checked numerically:
Rowland: the two-variable reduction, the bounded-excess automaton and the random-model numbers.
Cloitre: the conjecture forces w(p) ≤ p.
The K = 2 results: the mod-3 lemma, the "almost all primes" result and why the full statement is blocked.
The OEIS Open baseline: the exact Lean statement of the A135508 conjecture and all 19 failed runs.
The plan: the ladder of targets, the harness changes compared to #4, a to-do checklist, all the verification scripts in collapsible blocks with their outputs, and sources.

Things I added or corrected while writing it up:

Contamination: the issue now effectively contains the answer key for the middle targets. I noted that the harness has to run without access to it, and that the issue then serves for grading.
OEIS Open found that literature access and more elaborate agent loops didn't help. That directly challenges the idea behind the harness, so I flagged it as something the post needs to address.
Two small facts: your thesis is dated 11 April 2010 (Cloitre cites it as 2009). And the start values a(1) = 800 (your thesis) and 801 (Rowland's paper) are both correct, because the two orbits coincide from n = 2.

The scripts only exist in this session's temporary workspace. If you want them in the repo, I can commit them under a scripts/ folder.
