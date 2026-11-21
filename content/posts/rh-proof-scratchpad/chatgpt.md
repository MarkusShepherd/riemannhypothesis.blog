
There was the recent exciting breakthrough in the Riemann Hypothesis proved with the help of AI that there's no zeros with Re s > 7/8. What was the largest confirmed zero free region before this?

9 Nov, 19:01
The previous all-height cutoff was 
ℜ
s
=
1
ℜs=1. Before the 
7
/
8
7/8 result, no fixed half-plane 
ℜ
s
>
c
ℜs>c with 
c
<
1
c<1 had been proved zero-free for the Riemann zeta function. The known regions extended left of 
1
1 by a margin that shrank as 
∣
ℑ
s
∣
∣ℑs∣ grew. Bellotti, Trudgian and Yang, OpenAI’s quasi-Riemann hypothesis preprint

At sufficiently large heights, the strongest bounds were of Vinogradov–Korobov type. For 
s
=
σ
+
i
t
s=σ+it, Bellotti proved that there are no zeros in

σ
≥
1
−
1
48.0718
 
(
log
⁡
∣
t
∣
)
2
/
3
(
log
⁡
log
⁡
∣
t
∣
)
1
/
3
σ≥1− 
48.0718(log∣t∣) 
2/3
 (loglog∣t∣) 
1/3
 
1
​
 
for sufficiently large 
∣
t
∣
∣t∣. The boundary approaches 
1
1, whereas 
7
/
8
=
0.875
7/8=0.875 gives a fixed margin of 
0.125
0.125 at every height. Bellotti’s paper

At lower heights, the known region went further left. Platt and Trudgian had already rigorously verified that every nontrivial zero with 
∣
ℑ
s
∣
≤
3
×
10
12
∣ℑs∣≤3×10 
12
  lies on 
ℜ
s
=
1
2
ℜs= 
2
1
​
 . Platt and Trudgian’s verification

9 Nov, 19:47
What's that claim of no Landau Siegel zeros?

9 Nov, 20:55
A Landau–Siegel zero would be an exceptional real zero 
β
β of a Dirichlet 
L
L-function 
L
(
s
,
χ
)
L(s,χ) for a primitive quadratic character 
χ
χ. What makes it exceptional is how close it is to 
1
1 relative to the conductor 
q
q. The classical zero-free region left open the possibility of a real zero with 
1
−
β
<
c
/
log
⁡
q
1−β<c/logq for a small absolute constant 
c
c. Such a zero could cause a large bias in how primes are distributed among residue classes modulo 
q
q. Tao’s explanation

The claim is that one absolute 
c
>
0
c>0 works for every conductor, with every real zero satisfying

(
1
−
β
)
log
⁡
q
≥
c
.
(1−β)logq≥c.
OpenAI released a separate preprint proving this bound. It also follows from the stronger 
7
/
8
7/8 result because that result covers every Dirichlet 
L
L-function, including the quadratic ones. Any real zero then has 
β
≤
7
/
8
β≤7/8, so its distance from 
1
1 is at least 
1
/
8
1/8, regardless of 
q
q. Landau–Siegel preprint, 
7
/
8
7/8 preprint

9 Nov, 20:56
Give me one or two key ideas or insights of each of those RH papers. The stuff that the AI found that humans have overlooked before or simply couldn't come up with. I'd like to understand the spark of genius behind those proofs - if any.

10 Nov, 21:35
The clearest “how did they see that?” moment is in the 
11
/
12
11/12 paper. The 
7
/
8
7/8 paper adds a clever way to isolate the contribution of a zero, while the Landau–Siegel paper finds a different route through polynomial interpolation.

11
/
12
11/12 — Turn Möbius signs into Fourier coefficients
Use sixth roots of unity to absorb the Möbius sign. A zero of 
L
(
s
)
L(s) is a pole of 
1
/
L
(
s
)
1/L(s), so enough cancellation in the Möbius-type coefficients of 
1
/
L
1/L rules out zeros. The hard part is proving that cancellation. The paper multiplies the coefficients by sixth-root-of-unity weights and applies Poisson summation. An identity for Gauss sums then absorbs the Möbius sign, and the resulting coefficients belong to a cubic theta function. That gives the proof a symmetry it can use to turn the problem into a quadratic average it knows how to bound. The theta machinery was already there, notably in work by Patterson and by Dunn and Radziwiłł. Seeing that it could be used to control Möbius sums is the surprising connection. OpenAI preprint, Dunn and Radziwiłł, Rubinstein’s working notes
Make the sum you want appear many times. In the average over twists, a prime sixth power gives essentially the original sum, because a sixth-root character evaluated at a sixth power is 
1
1 away from divisibility exceptions. So the mean square contains many near-copies of the quantity you care about. With about 
X
1
/
6
X 
1/6
  copies in a mean square of size about 
X
2
X 
2
 , the original sum is bounded by roughly 
(
X
2
/
X
1
/
6
)
1
/
2
=
X
11
/
12
(X 
2
 /X 
1/6
 ) 
1/2
 =X 
11/12
 . That is where the fraction comes from. Preprint, §3
7
/
8
7/8 — Make the zero’s signal add up across primes
The paper builds a sum that can be evaluated two ways. One evaluation says it must be small. In the other, one term contains 
1
/
L
(
s
)
1/L(s), so a zero too far right would produce a large contribution. The difficulty is that the other terms could swamp it. The clever move is to insert selected primes and, for each prime, subtract a rescaled copy of the sum. That subtraction removes a contribution shared by all the terms. What remains adds with the same phase across primes in the term the proof wants, while the other terms carry varying character phases that moment estimates can control. That makes a longer transformed sum usable and pushes the boundary from 
11
/
12
11/12 to 
7
/
8
7/8. OpenAI preprint, Part II, Rubinstein’s working notes, §4

Landau–Siegel zeros — Turn a bias among primes into impossible divisibility
A Siegel zero would force overwhelmingly many primes, in a suitable weighted range, to have 
χ
(
p
)
=
−
1
χ(p)=−1. The paper makes each of those primes impose a divisibility constraint on the same nonzero integer. The key is that at such a prime, raising 
d
d
​
  to the 
p
p-th power acts like conjugation modulo 
p
p: 
(
d
)
p
≡
−
d
( 
d
​
 ) 
p
 ≡− 
d
​
 . The proof builds a polynomial interpolation determinant that converts those congruences into large powers of 
p
p dividing its norm. Multiply the prime powers together and the norm would have to be larger than a direct size estimate allows. The leap is recognizing that a bias in the primes can be tested this way. OpenAI preprint, Tao’s sketch of Ben Green’s reformulation

My pick for the strongest creative leap is the first one. Of all the ways to weight a Möbius sum, the sixth-root twist does two jobs at once: it produces near-copies of the original sum and gives the transformed sum exactly the coefficients for which the old cubic theta machinery works.

10 Nov, 21:35
Terence Tao said that the RH proof (and I'm not sure which one he referred to) contains "a very unusual combination of arguments" that no living mathematician would've come up with, or maybe if you locked enough of the leading experts in for long enough, they might have brute forced it. What exactly did he mean by that?

11 Nov, 14:01
Tao was talking about OpenAI’s quasi-Riemann hypothesis breakthrough in his October 15 Numberphile interview, around 16:04. He describes “three or four existing ideas arranged in a very unusual way” and imagines the right group of mathematicians finding the combination after enough trial and error. He gives neither a numerical cutoff nor a list of the ideas in that passage. The 
7
/
8
7/8 paper is the headline result, but the shorter 
11
/
12
11/12 paper makes the shared mathematical surprise easier to see. Numberphile interview, 16:04, Tao’s later comments on the two proofs

The surprising choice was to study Möbius cancellation using sixth-order character twists over 
Q
(
−
3
)
Q( 
−3
​
 ). The proof needs cancellation in the coefficients of 
1
/
L
(
s
)
1/L(s), since a zero of 
L
L would give its reciprocal a pole. The sixth-order twists do two jobs that are hard to get from the same family. 
11
/
12
11/12 preprint, proof outline

They put the original sum inside a larger average many times. At a prime sixth power, the twist is 
1
1 except on multiples of that prime. So a bound for the whole mean square bounds the original sum too.
They make that average tractable after two transformations. Poisson summation produces sextic Gauss sums. A Gauss-sum identity absorbs the Möbius sign and turns the resulting coefficients into cubic Gauss sums, which occur as Fourier coefficients of the cubic theta function. The theta transformation then turns the remaining sextic twist into a quadratic one, where a substantially sharper large-sieve estimate is available. Starting with quadratic twists directly misses this mechanism. The square-indexed terms that reproduce the original sum are precisely the ones the squarefree quadratic large sieve would exclude. Rubinstein’s working notes, §7
That last point explains why the route was easy to miss. The proof starts with a more complicated family to get access to a simpler estimate after transformation. Sarnak had advocated studying zeta through a larger family, and Iwaniec had considered closely related families. Dunn and Radziwiłł had developed the relevant theta transformation for a different problem. Radziwiłł later said specialists had thought their tools were insufficient for quasi-RH. The 
7
/
8
7/8 paper uses the same cubic-theta machinery and adds a subtraction at selected primes that preserves the target contribution while making the other terms easier to control. Quanta’s interviews with the specialists, 
7
/
8
7/8 working notes, §4

11 Nov, 14:02







