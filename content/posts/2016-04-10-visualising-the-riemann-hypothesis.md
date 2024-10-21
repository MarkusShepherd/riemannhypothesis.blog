---
title: Visualising the Riemann Hypothesis
author: Markus Shepherd
type: post
date: 2016-04-10T18:59:25+00:00
url: /2016/04/visualising-the-riemann-hypothesis/
categories:
  - Zeta Function
tags:
  - Complex numbers
  - Dimensions
  - Graph
  - Sage
  - SageMath
  - Video
  - Visualisation
  - Zeta function
---

*Update 2024-10-20: Watch the [video now in 4K](https://youtu.be/CkwlwL8hv2Q)!*

One stubborn source of frustration when working with complex numbers is the fact that visualisation becomes tedious, if not impossible. Complex numbers have 2 "real" dimensions in themselves, which give rise to the complex plane. That's all good and fair. But if you talk about a function with complex domain and codomain, you already deal with a 4-dimensional graph. Unfortunately, my mind can only handle 3 dimensions (on a good day). One can resort to taking the absolute value of the function instead, or map real and imaginary part individually, resulting in a 3-dimensional graph, but all of these solutions fail to satisfy in one respect or another.

However, there _is_ one more dimension we can exploit: time! Used in the right way, this can produce wonderful videos like this one:

{{< youtube CkwlwL8hv2Q >}}

<!-- more -->

What are we looking at? These are the values of \\(\zeta(s)\\) as \\(s\\) goes up the critical line \\(s=\frac12+ti\\). We start at[^complex] \\(t=0\\) at the beginning of the video and go all the way up to \\(t=200\\). \\(\zeta(\frac12)\approx-1.4603545\ldots\\), so this is where the values start. From there, we make an anti-clockwise semicircle until we hit the real axis again. After that, the \\(\zeta\\)-function "turns right" and settles into a clockwise spiral with most of the action happing in the right half-plane. This goes on and on forever. Notably, after about eight seconds, the graph passes the origin for the first time. This is the first of infinitely many \\(\zeta\\)-zeros on the critical line, at about \\(t\approx14.134725\ldots\\). From now, it winds around in seemingly unpredictable circles, sometimes small and hasty, sometimes wide and elegant, but it never forgets to visit the origin every so often.

I produced this video with a [relatively simple Python script](https://gitlab.com/mshepherd/riemannhypothesis.info/-/tree/master/experiments/zeta_animation/). You can modify and run it for yourself if you want to play with the colours, the length, the speed, or even the function we're plotting. What does the \\(\zeta\\)-function look like when we step off the critical line?

One more video I produced is this hour-long version, showing the values up to \\(\zeta(\frac12+6\\,000i)\\):

{{< youtube TzeZGQfVlsw >}}

I found it striking how the spiral speeds up as we go up the critical line, indicating a higher density of \\(\zeta\\)-zeros as \\(t\\) increases.

*PS*: If you feel nostalgic, you can still find the orginal video on YouTube and the [SageMath script](/plot_critical_line.sage) I used to produce it:

{{< youtube NAMuls4q2f4 >}}

[^complex]: As far as I know, it's total coincidence we conventionally use \\(t\\) for both the imaginary part of a complex argument and a time variable, but it makes talking about this animation surprisingly natural.
