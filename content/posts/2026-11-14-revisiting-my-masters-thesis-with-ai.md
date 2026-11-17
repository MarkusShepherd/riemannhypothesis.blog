---
title: Revisiting my master's thesis with AI
subtitle: An experiment in how AI-assisted mathematical research works in practice.
author: Markus Shepherd
type: post
date: 2026-11-14T12:00:00+02:00
draft: true
url: /2026/11/revisiting-my-masters-thesis-with-ai/
categories:
  - Feature
tags:
  - AI
  - Analytic number theory
  - Squarefree numbers
  - Mathematical research
---

There has been rather a lot of excitement about AI doing mathematics lately. In September, OpenAI claimed a solution to a version of the Navier–Stokes Millennium Prize Problem; in October it also claimed a proof that Landau–Siegel zeros do not exist. Those are quite some claims to put between the usual product announcements.

My immediate question was: how does this actually work?

Obviously, there is more to it than opening ChatGPT and typing:

> solve navier stokes. think real hard. no mistakes!

OpenAI's [account of its Navier–Stokes effort](https://openai.com/index/navier-stokes-solution/) describes an internal model, roughly 10,000 concurrent agents in the successful group, 88 hours to a proposed solution and a further 17 hours of [Lean](https://en.wikipedia.org/wiki/Lean_(proof_assistant)) formalisation and verification. Groups explored different problem variants; an intermediate Euler result was fed back into the search; Codex consolidated insights between groups. That is a substantial research process behind a short description of a breakthrough.

The announcement also came amid a serious dispute over unpublished research and scientific credit. In [his public statement](https://cims.nyu.edu/~tristanb/statement.pdf), Tristan Buckmaster questioned whether his and Levent Alpöge's private Codex sessions had informed OpenAI's work. He reports two proposals: publish their Euler result with OpenAI's Navier–Stokes result following the next day, or have Buckmaster alone write up the Navier–Stokes result and attribute the solution to OpenAI's model. He says Sébastien Bubeck twice sought Alpöge's removal from authorship and complained that Alpöge worked at Anthropic. [OpenAI denies using their unpublished work or Codex sessions](https://openai.com/index/navier-stokes-solution/#concurrent-work). Buckmaster himself explicitly said he did not know whether their data had been used; his account of the publication and authorship discussions is a separate, deeply troubling part of the story.

The Siegel-zero story also had a subsequent human exposition and simplification, including papers by [William Banks](https://arxiv.org/abs/2610.15483) and [Bryce Kerr](https://arxiv.org/abs/2610.21099). I am not going to adjudicate either claimed breakthrough here. What interested me was the work between posing a question and obtaining an argument someone could examine.

What is an *agent*, in this setting? What do thousands of them do that one cannot? Who chooses what they work on, and how do their answers turn into a proof? Could an ordinary person experiment with something similar using the tools available on a normal subscription?

I tried it with the problem from my master's thesis.

<!-- more -->

## Two papers and a very familiar problem

In 2011, my supervisor gave me two papers. One concerned [primes in arithmetic progressions with moduli taken from polynomial sequences](https://doi.org/10.1093/qmath/hap029) ([PDF](https://www.math.purdue.edu/~twooley/publ/2011sparse.pdf)); the other concerned [the variance of squarefree numbers in arithmetic progressions](https://doi.org/10.1112/S0024611505015352). My assignment was to combine the techniques.

That became [my master's thesis](/schepke_distribution_of_squarefree_numbers_in_arithmetic_progressions.pdf).

This needs a little perspective. My supervisor could probably have proved the result over a weekend. The point of giving it to me was that I would learn the techniques: understand the papers, see how their arguments fit together and work through the places where the combination required something new.

It seemed a good test for AI for much the same reason. This was a problem about adapting established methods, with relevant literature to read and a reasonably concrete target. I wanted to learn how to organise an attempt, including what would go wrong.

### Squarefree numbers in arithmetic progressions

For readers who would like to know what the machines were actually asked, here is the mathematical version. A number is *squarefree* if no square greater than one divides it. Consequently, each prime factor occurs at most once. For example, \\(30=2\cdot3\cdot5\\) is squarefree, whereas \\(12=2^2\cdot3\\) is not, since it is divisible by 4.

Take the simplest arithmetic progressions, the odd and even numbers. The squarefree entries are in **bold**:

| Progression | First fifteen terms |
| --- | --- |
| Odd | **1**, **3**, **5**, **7**, 9, **11**, **13**, **15**, **17**, **19**, **21**, **23**, 25, 27, **29** |
| Even | **2**, 4, **6**, 8, **10**, 12, **14**, 16, 18, 20, **22**, 24, **26**, 28, **30** |

Every second even number is divisible by 4 and therefore excluded. Odd numbers have no such restriction from the prime 2. In the long run, about \\(8/\pi^2\approx81.1\\%\\) of odd numbers and \\(4/\pi^2\approx40.5\\%\\) of even numbers are squarefree.

Write \\(Q(x;q,l)\\) for the number of squarefree positive integers up to \\(x\\) that are congruent to \\(l\\) modulo \\(q\\). For each fixed progression, this count has a linear main term \\(g(q,l)x\\).[^density-normalisation] The coefficient is positive unless a prime square divides both \\(q\\) and \\(l\\), forcing every term to have that square divisor. The multiples of 4 are an example of this obstruction.

Primes, by comparison, become progressively rarer and have zero unweighted density. For a fixed modulus, weighting each prime \\(p\\) by \\(\log p\\) gives a linear main term in each coprime residue class.[^prime-weight] Squarefree numbers need no extra weight and can have positive density even in non-coprime classes, as the even numbers illustrate.

### Variance and typical errors

Knowing the density gives a first approximation. To study its accuracy, we look at the discrepancy

\\[
E(x;q,l)=Q(x;q,l)-g(q,l)x.
\\]

How large are these errors? As the modulus grows, each progression contains fewer terms up to \\(x\\), and a fixed-modulus density formula alone tells us little about its accuracy. Controlling every individual progression can be difficult. A mean-square estimate instead describes the typical size of the discrepancy and limits how many progressions can have unusually large errors. Squaring prevents positive and negative errors from cancelling; dividing their sum by the number of classes gives the mean-square discrepancy.

### Polynomial moduli

The classical variance problem averages over all moduli up to a bound. My problem instead selected polynomial moduli, such as \\(q=k^2+1\\): \\(2,5,10,17,26,\ldots\\). Only about \\(\sqrt{Y}\\) of these lie below \\(Y\\). A good average over all moduli might conceal much worse behaviour on such a sparse family. Restricting the moduli asks how well the distribution behaves under this additional arithmetic structure.

There are applications of related estimates in prime number theory. For example, \\(p\equiv1\pmod{k^2}\\) means that \\(p-1\\) has the square divisor \\(k^2\\). Distribution estimates for square moduli helped [Baier and Zhao](https://doi.org/10.4064/aa125-2-5) ([PDF](https://arxiv.org/pdf/math/0602116)) prove results on primes for which \\(p-1\\) has a large square divisor. My thesis asked for a squarefree analogue of the sparse-modulus variance studied for primes.

Specifically, for \\(f(y)\le x\\) it studied

\\[
V_f(x,y)=\sum_{1\le k\le y} f^{\prime}(k)
\sum_{l=1}^{f(k)} E(x;f(k),l)^2.
\\]

The weight \\(f^{\prime}(k)\\) compensates for the spacing between successive polynomial values: for \\(f(k)=k^2+1\\), the gaps are \\(2k+1\\), close to \\(f^{\prime}(k)=2k\\). This makes the weighted sparse sum comparable in scale with a sum over all moduli up to \\(f(y)\\). The question is to obtain an asymptotic formula: a main term, an explicit constant depending on \\(f\\) and an error estimate small enough to make the formula informative.

You do not need to understand the formula to follow the experiment. The number theory gives us a concrete problem for exploring how agents develop arguments, check each other's work and assemble a proof. If you want to build your own harness for other kinds of work, those are useful questions too.

## Before the harness: two single chats

I also tried the problem in two separate chats, [one with Claude Opus 5.5](https://gitlab.com/mshepherd/riemannhypothesis.blog/-/work_items/4#note_4130395365) and [one with ChatGPT/Codex](https://gitlab.com/mshepherd/riemannhypothesis.blog/-/work_items/4#note_4130488216). Each received the problem statement without the source papers and was instructed to work without web searches or stored context. Claude was allowed to run local computations.

Both produced proof sketches using elementary correlations between pairs of squarefree numbers, estimating the variance at each modulus before averaging over polynomial values. Both proposed the lower threshold \\(x^{7/9+\delta}\\), with an upper bound \\(f(y)\le x^{1-\delta}\\). Comparing their constants with the thesis led to the factor-of-two correction described [below](#checking-the-thesis). This happened before the full harness was run.

Those sketches provide a useful baseline for the later experiments. They had not undergone the proposition-by-proposition reviews or manuscript checks described below, and my surviving records of the chats are the contemporary summaries linked above. The neutral harness run eventually reached the same lower threshold. Its contribution was developing the argument in detail, repeatedly checking it and preserving the work in an inspectable form.

## Running the agents

The [harness](https://gitlab.com/mshepherd/squarefree-numbers) is 100% AI slop. The source is a horrible, unreadable mess; protective equipment is recommended before following the link.

The models also proposed the workflow and wrote the prompts. Deciding how to decompose a problem, what information to give each agent and how to check the results is a place where human expertise could make a real difference. I largely outsourced that judgment too, asking AI how to organise the attempt and having it implement the design. Even setting up the experiment was something I could delegate.

### Starting separate model sessions

An agent in this setup is a fresh invocation of a command-line model, using Claude Code or Codex. The underlying commands are `claude -p` and `codex exec`. A Python driver prepares the working folder, supplies a prompt and selected files, starts the process and collects what it produces.

The completed experiments used Claude Opus 5.5, Claude Sonnet 5.5 and GPT-6.1 Sol, mostly at high effort. “High” is a provider's setting, not a common unit of reasoning.

Each invocation receives instructions and source material for a particular task: a planner develops a proof strategy, a prover tackles one proposition and a referee checks a proposed proof.

A prover's folder looks approximately like this:

~~~text
problem.md       the overall mathematical question
statement.md     this agent's proposition
deps/            statements it may assume
papers/          the supplied literature
~~~

Its output is a proof file, or a report that the statement is defective. A referee receives a separate copy of the relevant inputs. It does not see the prover's conversation or the other referee's verdict.

### How results move between agents

The agents in my harness do not chat with one another. The driver copies files between stages; those copies determine what each model can know from the experiment. Persistent state lives in those files, so the next session can be fresh.

I limited the system to two simultaneous agent invocations, largely because I was working within ordinary subscription limits. Over the course of the experiment there were many sessions, with different roles. Two at a time was quite enough to keep me occupied.

OpenAI's published account describes communicating groups and redistribution of intermediate results; mine used explicit file handoffs and a mostly fixed sequence of stages.[^pollination]

## First find out what to ask the provers

The tempting place to start is “prove the theorem”. We put several stages before that.

### Prior knowledge and excluded sources

Fresh models were first asked what they already knew about the problem. My thesis is online, and [a later paper by Fabian Dehnert](https://doi.org/10.1007/s00605-014-0691-6) treats the same topic.[^dehnert] Asking a model to rediscover an answer it has just retrieved would be a rather different experiment. Neither a failure to recall a result nor a different proof strategy can establish that it was absent from training data, but the probes at least recorded what the models volunteered.

We also restricted the usable literature to works from 2010 or earlier, plus the explicitly supplied papers, including the 2011 Brüdern–Wooley paper. My thesis and Dehnert's work were excluded. This was an awkward, artificial restriction: in actual frontier research you would normally want to build on all relevant existing work. Here we wanted a somewhat apples-to-apples comparison with my original assignment, rather than an answer assembled from fifteen subsequent years of research.[^parry]

There were transcript scans for excluded sources and restrictions on tools, but the real runs used host directories rather than isolated containers. Search snippets did sometimes contain excluded titles or links. This was an attempt to preserve and audit independence, with practical limitations.

### Numerical experiments

Next came numerical experiments. Two agents independently wrote code to calculate the variance for three polynomials, including \\(k^2+1\\), at increasingly large values of \\(x\\). The larger computation reached \\(256{,}000{,}000\\). Operator sessions compared the outputs with each other, checked them against direct counts in small cases and reran the code.

That supplied a useful constraint on the mathematics. A proof predicting twice the observed leading constant deserved immediate investigation.

There was a subtlety even here: exact counts do not give an exact limiting constant. Lower-order effects depend on the ratio \\(f(y)/x\\). Increasing \\(x\\) while keeping that ratio fixed does not make all those effects disappear. Extrapolating the constant was a separate modelling task, with uncertainty and possible bias.

### Literature and proof plans

Alongside the computation, librarian agents searched for relevant permitted literature. I supplied papers I could obtain, including through Cambridge Core. The eventual corpus was considerably larger than the original pair.

Then the planners began. In the neutral experiment, two models each received four strategy hints: start from Vaughan, try a Dirichlet-series approach, seek the simplest rigorous argument or proceed without an additional hint. “Neutral” here means the prompts did not encode the critiques of my thesis; the problem statement and supplied literature still gave the models substantial direction.

The planners had to propose a theorem and break its proof into explicit propositions. Each proposition needed its assumptions, parameter ranges, error terms, dependencies and citations. Planners and integrators could see the accepted numerical evidence; provers and proposition referees did not receive those targets.

That level of detail is essential for analytic number theory. Suppose a lemma gives an error of size \\(x^{2/3}\\) for each shift \\(h\\). If another step adds the error over \\(H\\) shifts, the available bound is now \\(Hx^{2/3}\\). Forgetting the length of a sum can turn an impressive-looking theorem into an unsupported claim.

A proposition therefore acts as a contract: this is exactly what the next part of the proof may assume. The dependency graph also lets separate provers work simultaneously. They receive the statements of the lemmas they need, even while those lemmas are being proved elsewhere.

### Correcting the problem statement

The planning stage caught a problem in the specification itself. We had allowed rational-coefficient polynomials that take integer values. For such a polynomial, its value modulo \\(m\\) need not depend only on its input modulo \\(m\\). For example,

\\[
f(t)=\frac{t(t+1)}2+1
\\]

has \\(f(0)=1\\) and \\(f(2)=4\\): the inputs agree modulo 2, the outputs do not. That broke the naive definition of a root count used in the plans.

The same gap is present in [Brüdern–Wooley's 2011 paper](https://doi.org/10.1093/qmath/hap029). It explicitly allows integer-valued polynomials with rational coefficients, but equation (21) groups inputs by their residue modulo \\(q\\) and treats their polynomial values as having the same residue. The example above shows why that step is not generally valid. It also contradicts the multiplicativity claimed in Lemma 3.[^bw11-gap] This does not by itself disprove the main theorem, but the rational-coefficient case needs an additional argument.

I chose to restrict the problem to integer-coefficient polynomials, and we restarted. The agents had helped correct the question before attempting to prove the answer.

For me, this was one of the most striking uses of AI in the experiment: checking assumptions in published research I had treated as a reliable starting point. Using AI to revisit older papers could help uncover gaps that have survived peer review and years of reuse.

## Prove, object, assemble, repeat

### Proof attempts and referee reports

Once a plan was selected, the driver started one proof task per proposition.

Each completed proof went to two fresh referee sessions, one from each model family. The referee prompt asked them to look for errors, check hypotheses against the supplied papers, track uniformity and the lengths of summed errors and verify that dependencies were used exactly as stated.

Their verdicts were structured data, so the driver could decide what to do next. Conceptually, the loop was:

~~~text
ask a prover for a proof
send the statement and proof to two separate referees
if both pass:
    preserve the approved proof
else:
    send the proof and objections into another attempt
~~~

There was also an escape hatch for a prover to say that its assigned proposition was false or ill-posed. A system that insists on receiving a proof of everything it asks is inviting the models to invent one.

Both completed experiments eventually had every proposition pass its two referees in the first mathematical review round. Fresh contexts limited information sharing between the referees; they did not make the models statistically independent.

### Formal verification with Lean

OpenAI reports using [Lean](https://lean-lang.org/theorem_proving_in_lean4/Introduction/) to formalise its proof. This means expressing the statement and argument in a precise language so that a program can check each deduction against the definitions and assumptions. It is a particularly useful fit for AI: a model can propose and revise proofs while the checker rejects invalid steps regardless of how convincing the prose sounds. The formal statement still has to match the intended mathematical claim.

We did not use Lean here. We expected the specialised sieve arguments and uniform error estimates to require substantial additions to [Mathlib](https://mathlib.org/mathlib-overview.html), Lean's library of formalised mathematics. Building that infrastructure would have been a separate project, so we used model reviews and numerical checks, with the weaker assurance that entails.

### Integration and write-up

The next stage was integration. Two agents separately assembled the same set of approved proposition proofs, checked that their ranges and error estimates fitted together, stated the theorem actually obtained and compared its constant with the numerical evidence.

A writer then turned those proofs into a LaTeX manuscript with explanations and numerical tables, regenerated the computations and compiled the document. Two further reviewers checked the whole manuscript, and their objections fed another writing round.

The manuscript reviews found further mathematical and reporting errors, including an auxiliary convergence claim that was too strong. I accepted the neutral manuscript with the remaining objections preserved; the guided manuscript passed both reviewers before I accepted it.[^manuscript-acceptance]

I relied largely on further AI assessments in making those decisions. I had not independently reconstructed every proof.

## What “human in the loop” meant

### Decisions based on AI advice

At several points the procedure called for a human decision: approve numerical evidence, settle the literature, choose a plan, accept a manuscript.

I should be honest about what I contributed at those checkpoints.

I read the plans—or skimmed them, more honestly—but I was poorly equipped to assess some of their most consequential choices. How much would be gained by averaging over one variable before another? Was the proposed contour shift plausible? How difficult would it be to repair a particular bound?

I could ask those questions. Mostly, I asked another AI session for its judgment.

The selected neutral plan came from Claude; the recommendation I used to choose it came from Codex. Similar separate sessions assessed the completeness of the proofs, interpreted referee objections and compared the write-ups with my thesis. There was a layer of AI advice around the formal harness as well as the AI work inside it.

I retained control over what we attempted and what actions were allowed. But mathematical judgment was extensively delegated. Calling every approval an expert human verification would give a misleading impression of the experiment.

### Returning to the mathematics

This was also where the return to mathematics became more complicated than a pleasant exercise in nostalgia.

It was wonderful to spend time with pure mathematics again. It was disconcerting to realise how far away that world had slipped. Relearning the circle method well enough to make confident judgments would require substantial work. Reading the plans made me wonder how thoroughly I had understood the underlying structures even when I wrote the thesis.

The ease with which the models took my old work apart compounded that feeling. An eloquent critique is itself something to check, of course. Still, watching a model immediately point to a passage I would need hours to reconstruct was quite an experience.

Fifteen years is a long time. Opening the old PDF did not restore the mathematical fluency I remembered having.

## What came out?

There were four archived experiments, including an early attempt before the literature cutoff and the abandoned rational-coefficient version. Two reached completed proof and integration stages, and both eventually produced write-ups that I accepted.

### The neutral run

The [neutral run](https://gitlab.com/mshepherd/squarefree-numbers/-/tree/main/writeups/zt-neutral) ([PDF](/squarefree-numbers-neutral.pdf)) used an elementary approach based on correlations between pairs of squarefree numbers, followed by averaging over polynomial values. It obtained the main-term shape

\\[
V_f(x,y)\sim C_f\sqrt{x}f(y)^{3/2}
\\]

in the range

\\[
x^{7/9+\delta}\le f(y)\le x^{1-\delta},
\qquad 0<\delta<1/9,
\\]

under the polynomial assumptions in the problem. This matched the lower threshold proposed in the [single-chat sketches](#before-the-harness-two-single-chats), now with the detailed proof and review record described above.

Its nine proposition proofs were all written by Claude Sonnet 5.5. Codex contributed planning, numerical computation, refereeing and integration. Having a cheaper model write proofs that more expensive models reviewed was a useful configuration. Although both providers were configured as provers, the default rotated them by *round*: every proposition began with Claude, and everything passed before a second round. I only fully appreciated the consequence when attempting the next run.

### The thesis-guided run

For the [second completed experiment](https://gitlab.com/mshepherd/squarefree-numbers/-/tree/main/writeups/zt-thesis-plan) ([PDF](/squarefree-numbers-thesis-guided.pdf)), I had an operator read my thesis and write a light hint encouraging the combination of Vaughan and Brüdern–Wooley. That makes it a thesis-guided comparison, distinct from the neutral run. We reused the accepted numerics and literature.

GPT-6.1 Sol wrote its seven final proposition proofs. The result had a more detailed formula describing behaviour when \\(f(y)\\) is comparable with \\(x\\), but a narrower range for the simple power-law asymptotic. For quadratic polynomials, its lower threshold was \\(x^{19/21+\delta}\\), compared with \\(x^{7/9+\delta}\\) in the neutral run.

Following something closer to my old route had changed the trade-off rather than simply improving the answer.

### Checking the thesis

For quadratic moduli, my thesis claimed a lower threshold of \\(x^{2/3+\varepsilon}\\). Neither run reached it. But the AI readings found gaps that leave that range unestablished by the printed proof, so it could not simply serve as an unquestioned benchmark.

One problem was exactly the kind of bookkeeping error discussed [earlier](#literature-and-proof-plans). On [printed page 22](/schepke_distribution_of_squarefree_numbers_in_arithmetic_progressions.pdf#page=25), an error bound for each shift \\(h\\) is summed over shifts up to \\(x^{3/4}\\), but the claimed total loses the cost of that summation. Even the contribution from \\(q=1\\) to the displayed bound is too large for the inequality that follows.

Another occurs in [Lemma 7.2](/schepke_distribution_of_squarefree_numbers_in_arithmetic_progressions.pdf#page=48). Counting entries in residue classes produces a bounded oscillating error. The proof treats it as a constant plus a remainder tending to zero. A bound on an error does not establish that it converges. Here the counting sum is a step function of real \\(y\\), which also rules out the claimed linear approximation with a constant offset and a vanishing remainder.

These objections came from separate AI readings of the thesis. The completed runs used different arguments, so their passing reviews do not demonstrate that the harness caught or repaired these particular gaps.[^thesis-range]

There was one particularly concrete correction. The thesis used the residue of \\(\zeta(2s+4)\\) at \\(s=-3/2\\) as though it were 1. It is \\(1/2\\): the change of variable contributes a factor of two. That propagated into the leading constant.

The [comparison and numerical checks](https://gitlab.com/mshepherd/riemannhypothesis.blog/-/work_items/4#note_4130461384) supported about \\(0.138083\\) for \\(f(k)=k^2+1\\), rather than the printed \\(0.276165\\). Both completed experiments obtained the corrected value. A comparison following the single-chat baselines had already exposed the discrepancy.

## Making the harness work

The proof and review stage of the neutral run took about 23 minutes. Planning took about an hour; the two integrations took another fourteen minutes.

The project took considerably longer.

### Harness bugs and failed calls

The initial scaffold grew through 24 merge requests. We fixed tool permissions that did not mean what their names suggested, shell settings that gave the providers different Python environments, missing archive files and failures to resume completed work sensibly.

Usage limits were a recurring interruption. A failed referee call could also cause an incomplete proof round to be restarted, repeating work that had already succeeded. A machine agreeing that a theorem was correct was sometimes easier to obtain than a workflow that remembered what had happened before a quota reset.

Some frustration was much more basic. Coding assistants repeatedly inferred actions I had not authorised, including commits and a push. They overcomplicated routine tasks, misunderstood instructions and occasionally removed functionality I wanted to keep. Building the harness was itself an exercise in supervising imperfect agents.

There is a lesson here about what an impressive mathematical performance does and does not tell you about the surrounding software work. A model can reason usefully about a difficult proof and still make a mess of a straightforward operational instruction.

### Subscriptions and reported costs

The accounting also deserves some care. Both providers were used through $20 subscription plans. Claude's CLI nevertheless reports a dollar figure resembling API-equivalent usage; that is not an additional invoice.

Across the [main historical ledgers](https://gitlab.com/mshepherd/squarefree-numbers/-/tree/main/archive), including abandoned attempts and the write-up stages, there were **141 invocations, of which 20 failed**, about **$166.22 in Claude-reported usage** and about **632,000 Codex output tokens**.[^accounting]

The two write-up stages alone accounted for about $103 of the Claude figure. For comparison, the entire neutral research run, including numerics, planning, proof, review and integration, accounted for about $23, plus 160,000 Codex output tokens. Those figures exclude the surrounding operator sessions and my time.

The binding constraint was often waiting for subscription usage to reset. The money-like counter, the number of tokens, elapsed time and the amount of human attention describe different parts of the cost.

## Beyond a single prompt

### Trying a smaller workflow

You can experiment with this workflow yourself. The practical starting point could be one small claim, a written proposed solution and a fresh session asked to find a specific counterexample or missing assumption. Then inspect what the review actually checked. That is already an experiment in organising work beyond a single conversation.

For a larger project, the useful questions become: what intermediate output would make progress inspectable? What assumptions must the next step receive? What can be checked by a calculation or another external test? What should happen when the proposed statement turns out to be wrong?

Those questions travel beyond mathematics. A decomposition into proposals, explicit assumptions, tests and revision could organise other kinds of investigation too. The checks will differ, and agreement between models will remain much weaker evidence than a check against the world.

I would be reluctant to claim that this setup was optimal. What I gained was a much clearer picture of the process and its failure modes, together with a record that could be examined.

## Who is assisting whom?

The familiar phrase is “AI-assisted research”. In parts of this experiment I felt closer to an assistant to the AI research: obtaining papers, restarting failed stages, asking other models to explain the outputs and deciding when to move on.

I chose the problem, constraints and direction of the exercise. Much of the mathematical work, and much of the evaluation of that work, happened in model sessions. The boundary moved as the project progressed.

### One prompt versus autonomous research

How long until a single prompt can produce something like these results without that supervision? I do not have a reliable timetable. There are also two separate developments hidden in the question. A product could accept one prompt while carrying out a large internal research process. That would simplify the interface. Reliable research that needs no human help choosing a route, resolving uncertainty or checking the outcome is a further question.

The experiment gave me reasons to take increasing autonomy seriously. It also gave me plenty of examples of how easily a process can mistake a completed step for a finished job.

### The purpose of research

Suppose, though, that we do reach a world where proofs are abundant. What is the point of doing mathematics then?

My supervisor already knew how to solve the problem he gave me. That did not make the assignment pointless. Its value lay in learning to see how the mathematics worked.

That learning also sustains the wider mathematical community. Terence Tao has warned against the [“indiscriminate automated strip-mining of open problems for solutions”](https://mathstodon.xyz/@tao/117204930249967695): a problem can generate new techniques, train students and suggest further questions while people work on it. Extracting an answer without developing or sharing that understanding can damage the community that made the problem worth asking. In a [joint declaration](https://mathandai.org/), Tao and other Fields medallists criticised the use of mathematics as a corporate benchmark, rushed announcements and failures of attribution. A press release and a higher valuation are poor substitutes for explaining the ideas, acknowledging prior work or supporting the people doing that work.

I could now obtain a substantial PDF on that problem with remarkably little direct mathematical work. Having the document does not give me the understanding that working through it might provide. It does, however, put an explanation, a set of approaches and a very patient interlocutor within reach.

### The pleasure of understanding

Pure mathematics was my first intellectual passion. Returning to it was fun, nostalgic and at times uncomfortable. I was reminded of the effort and frustration involved in learning it properly, and of how difficult it is to find room for that effort after fifteen years spent mostly doing other things.

These tools make it easier to begin again. I can ask for an explanation of a forgotten technique, compare two approaches or explore a calculation without first committing myself to months of reconstructing the prerequisites. I can also ask the machines to do so much that I understand very little of the result. Both possibilities were present throughout this exercise.

For me, the attraction of mathematics has always included the sheer joy and beauty of understanding: seeing why an argument works, how two ideas connect or why something that looked mysterious has a surprisingly simple explanation.

A supply of proofs does not use up those experiences. It may give me more opportunities to have them.

Fifteen years later, I would quite like to understand my thesis.

[^density-normalisation]: The coefficient \\(g(q,l)\\) measures density relative to *all* integers up to \\(x\\), rather than just the terms of the progression. Each row of the table contains about \\(x/2\\) terms up to \\(x\\), so \\(g(2,1)=4/\pi^2\\) and \\(g(2,0)=2/\pi^2\\).

[^prime-weight]: More precisely, for fixed \\(q\\) with \\(\gcd(q,l)=1\\),

    \\[
    \sum_{p\le x,\ p\equiv l\pmod q}\log p
    \sim \frac{x}{\varphi(q)},
    \\]

    where \\(\varphi(q)\\) counts the residue classes coprime to \\(q\\).

[^pollination]: OpenAI describes [using Codex to consolidate insights from different groups into follow-up prompts](https://openai.com/index/navier-stokes-solution/). My harness had an optional “pollinator” that could inspect other plans to help with a stuck proposition or flag that its statement needed changing. Neither completed run used it.

[^dehnert]: I have been unable to obtain a copy or contact the author. His paper would be a much better benchmark for the AI work than my thesis, having been published in a journal and subjected to a different level of peer review. Unfortunately, I couldn't justify shelling out an unreasonable amount of cash to Springer for a single article. If any reader can help me obtain a copy or reach the author, a comparison with the AI results would make a great follow-up.

[^bw11-gap]: See equation (21) on page 8 and Lemma 3 on page 9 of the [paper (PDF)](https://www.math.purdue.edu/~twooley/publ/2011sparse.pdf#page=8). For the polynomial above, the lemma's definition gives \\(w_1(2)=1\\), \\(w_1(3)=-1\\) and \\(w_1(6)=-1/3\\), whereas multiplicativity would require \\(w_1(6)=w_1(2)w_1(3)=-1\\).

[^parry]: For example, [Tomos Parry's 2021 paper](https://doi.org/10.5802/jtnb.1163) ([PDF](https://www.numdam.org/item/10.5802/jtnb.1163.pdf#page=4)) develops stronger variance estimates for squarefree numbers in arithmetic progressions at a fixed modulus, including all residue classes. The improved error terms make the asymptotic valid over a wider range of moduli. Alongside Dehnert's work on the sparse-modulus problem itself, this illustrates how the subject has progressed since my thesis.

[^manuscript-acceptance]: I accepted the neutral manuscript at round four with both reviewers' `revise` verdicts preserved. One remaining objection concerned my authorisation of a corrected auxiliary convergence statement; another round of model calls could not supply that authorisation. The guided manuscript received two passing reviews at round five before I accepted it.

[^thesis-range]: In a separate comparison on 6 November, after the experiments, Codex also identified a counterexample to the pointwise exponential-sum bound in [Lemma 5.4](/schepke_distribution_of_squarefree_numbers_in_arithmetic_progressions.pdf#page=34). Take \\(f(t)=(t+1)^2\\) and \\(x=4p^4\\) for a large prime \\(p\\). Restricting the sum \\(T_f\\) to \\(x/2<f(k)\le x\\) leaves only \\(h=1\\). Its average over \\(\alpha=a/p^2\\) with \\(a\\) coprime to \\(p\\) has size of order \\(p^3\\): only the terms with \\(p\mid k+1\\) survive. Yet the lemma would bound each of the two partial sums whose difference gives this restricted sum by \\(O(p^2\log p)\\). The pointwise bound therefore fails as stated. This later diagnosis was not an output of either harness run and does not supply a replacement estimate that recovers the thesis's claimed range.

[^accounting]: Five earlier probes recovered from a local backup bring the totals to 146 invocations, $166.91 in Claude-reported usage and about 634,000 Codex output tokens. The 141-invocation subtotal uses the main archived research and preserved write-up ledgers. Neither figure includes all operator conversations, initial baseline chats, development work or human time.
