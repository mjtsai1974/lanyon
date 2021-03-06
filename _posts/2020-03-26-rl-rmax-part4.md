---
layout: post
title: Model-Based RL Algorithm RMAX - Part 4
---

## Prologue To Model-Based RL Algorithm <font color="Red">RMAX</font> - Part 4
<p class="message">
The <font color="Red">RMAX</font> theorem guarantees that <font color="DeepPink">the learning efficiency is polynomial</font> and would be proved in this article.
</p>

### The <font color="Red">RMAX</font> Theorem
><font color="Brown">[Theorem of optimality and convergence]</font>  
>Given below condition:  
>&#10112;let $M$ be the <font color="OrangeRed">stochastic game</font> with $N$ states and $k$ actions.  
>&#10113;let $0 < \delta < 1$ and $\varepsilon > 0$ be constants, where <font color="OrangeRed">$\delta$</font> is the <font color="OrangeRed">error probability</font> and <font color="OrangeRed">$\varepsilon$</font> is the <font color="OrangeRed">error term</font>.  
>&#10114;denote the policy for $M$ whose <font color="OrangeRed">$\varepsilon$-return mixing time</font> is $T$ by $\prod_{M}(\varepsilon,T)$.  
>&#10115;denote the <font color="#00ADAD">optimal</font> expected return by such policy by $Opt(\prod_{M}(\varepsilon,T))$.  
>
>Then, <font color="DeepPink">with probability of no less than $1-\delta$ the <font color="Red">RMAX</font> algorithm will attain an expected return of $Opt(\prod_{M}(\varepsilon,T))-2\cdot\varepsilon$, within a number of steps polynomial in $N$,$k$,$T$,$\frac {1}{\varepsilon}$ and $\frac {1}{\delta}$</font>.  
>
><font color="Brown">Notes::mjtsai1974</font>
>Why the execution of the <font color="Red">RMAX</font> algorithm will attain an expected return of $Opt(\prod_{M}(\varepsilon,T))-2\cdot\varepsilon$?  
>
>As a result of the fact that the <font color="#00ADAD">optimal policy</font> is defined on <font color="OrangeRed">$\varepsilon$-return mixing time</font> of $T$, the <font color="#D600D6">real return</font> of the execution of the <font color="Red">RMAX</font> algorithm must be smaller than it, thus we choose it to be $-2\cdot\varepsilon$.  

### <font color="RoyalBlue">Why the RMAX algorithm is polynomial?</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Recap on implicit explore or exploit lemma</font>  
>The implicit explore or exploit lemma guarantees that the policy generated from the simulated model $M_{L}$ onto the target model $M$ could either leads to $\alpha$ close to optimal reward or explore efficiently with hight probability of at least $\frac {\alpha}{R_{max}}$, where $M_{L}\rightarrow_{\alpha}M$ and $\alpha$=$\frac {\varepsilon}{N\cdot T\cdot R_{max}}$.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Due to $\alpha$ approximation</font>  
>Since $\alpha$=$\frac {\varepsilon}{N\cdot T\cdot R_{max}}$, the $T$ step phases in which we are exploring in the execution of the <font color="Red">RMAX</font> algorithm is polynomial in $N$,$T$,$\varepsilon$.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Learn over $N$ states and $k^{2}$ actions</font>  
>There are totally $N$ states(or stage games) in model $M$ with $k$ actions for the agent and the adversary, therefore, we have a polynomial number of parameters to learn, say $N$ and $k$.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">The probability to update the unknown information</font>  
>The probability the <font color="Red">RMAX</font> alrorithm to turn a state from unknown to known or to update statistics information is polynomial in $\varepsilon$,$T$,$N$.  
>
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">A brief summary</font>  
>Base on all of above, <font color="OrangeRed">by sampling in a large number of times</font>, the implicit explore or exploit lemma guarantees <font color="DeepSkyBlue">the least probabilistic exploration</font>, and we can ensure that <font color="OrangeRed">the fail rate in attaining the optimal reward is quiet small</font>, say $\delta$.  
>
>The <font color="Red">RMAX</font> algorithm claims that we can get near optimal reward with probability $1-\delta$ <font color="OrangeRed">by sampling a sufficient large number of trials over the same state</font>, which is polynomial in $\frac {1}{\delta}$.  
>
>Watch out that <font color="OrangeRed">each trial contains either exploration or exploitation</font>, next to prove this theorem.  

### The <font color="Red">RMAX</font> Theorem Proof::1
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">The accuracy in the estimate of transitive probability</font>  
>First, we'd like to prove that <font color="OrangeRed">the estimate of transitive probability in the implicit explore or exploit is accurate</font>.  
>
>The majority focus on <font color="Red">the number of trials in this same state</font>, that is <font color="RoyalBlue">how many times of state transition in this same state for explore or exploit could we believe that the estimated transitive probability is accurate?</font>  
>
><font color="DeepSkyBlue">[2]</font>
><font color="Red">By sampling in a large number of trials over the same state</font>  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-03-26-rl-rmax-part4-trials-over-same-state.png "trials over same state")
>How many number of trials on $G_{i}$(<font color="Red">in this same state</font>) could we update the transitive statistics of $G_{i}$?  
>&#10112;suppose there exists such transitive probability $p$ on $G_{i}$, <font color="RosyBrown">it could not be guaranteed with probability $1$</font>, that is $0\leq p\leq 1$.  
>&#10113;totally, there are $N\cdot k^{2}$ such probabilities, for we have $N$ states, with agent and adversary each having $k$ actions.  
>&#10114;treat the random variable <font color="DeepSkyBlue">$X_{i}$</font> to be <font color="DeepSkyBlue">the distinct trial on state $G_{i}$</font>, with above denoted transitive probability $p$ to transite from state $G_{i}$ to $G_{i^{\'}}$, that is to say  
>* The value of $X_{i}$=$1$, iff it transits from $G_{i}$ to $G_{i^{\'}}$ with probability $p$; otherwise, 
>the value of $X_{i}$=$0$, iff it just revisits over the same state $G_{i}$ with probability $1-p$.  
>
>&#10115;let $Z_{i}$=$X_{i}-p$, then  
>$E\lbrack Z_{i}\rbrack$  
>=$E\lbrack X_{i}-p\rbrack$  
>=$E\lbrack X_{i}\rbrack$-$p$  
>=$1\cdot p$-$p$  
>=$0$, and $\vert Z_{i}\vert\leq 1$  
>* By [Chernoff Bounds For Bernoulli Random Variable]({{ site.baseurl }}/2019/12/09/prob-bound-chernoff-bound-bernoulli/)  
>We have $P(\sum_{i=1}^{n}Z_{i}>a)<e^{-\frac {a^{2}}{2\cdot n}}$, where $Z_{1}$,$Z_{2}$,...,$Z_{n}$ are the $n$ distinct independent trials on state $G_{i}$, and $a$ is the error term, such inequality is to ask for the error probability that after $n$ independent trials on state $G_{i}$, the total estimate bias is greater than the error term $a$.  This error probability is upper bounded by $e^{-\frac {a^{2}}{2\cdot n}}$.  
>
>&#10116;if we perform the test on this state $G_{i}$ for $K_{1}$ times, then we have the inequality holds  
>$P(\sum_{i=1}^{K_{1}}Z_{i}>K_{1}^{\frac {2}{3}})<e^{-\frac {K_{1}^{\frac {1}{3}}}{2}}$  
>The [RMAX paper]((http://www.jmlr.org/papers/volume3/brafman02a/brafman02a.pdf)) would like to restrict the total loss(or bias) in the estimate of transitive probability $p$ on $G_{i}$ over $K_{1}$ times to be less than $K_{1}^{\frac {2}{3}}$ and such error probability is upper bounded by $e^{-\frac {K_{1}^{\frac {1}{3}}}{2}}$.  
>* <font color="OrangeRed">Inequality symmetry and regularization</font>  
>If we take $Z_{i}^{\'}$=$p-X_{i}$,  
>then $P(\sum_{i=1}^{K_{1}}Z_{i}^{\'}>K_{1}^{\frac {2}{3}})<e^{-\frac {K_{1}^{\frac {1}{3}}}{2}}$,  
>therefore, $P(\vert\sum_{i=1}^{K_{1}}(X_{i}-p)\vert>K_{1}^{\frac {2}{3}})<2\cdot e^{-\frac {K_{1}^{\frac {1}{3}}}{2}}$ by symmetry,  
>finally, $P(\vert\frac {\sum_{i=1}^{K_{1}}X_{i}}{K_{1}}-p\vert>K_{1}^{-\frac {1}{3}})<2\cdot e^{-\frac {K_{1}^{\frac {1}{3}}}{2}}$.  
>
>&#10117;back to our departuring point that the <font color="Red">RMAX</font> algorithm would like to attain/get close to the optimal reward with probability $1-\delta$, where $\delta$ is the error probability.  
>* <font color="OrangeRed">To limit the probabilistic failure of the estimated transitive probability</font>  
>We want this probabilistic failure smaller than $\delta$, in the paper proof, it was upper bounded by $\frac {\delta}{3\cdot N\cdot k^{2}}$, this would be definitely be smaller than $\delta$, by taking $2\cdot e^{-\frac {K_{1}^{\frac {1}{3}}}{2}}<\frac {\delta}{3\cdot N\cdot k^{2}}$.  
>* <font color="OrangeRed">To limit the total estimated loss after $K_{1}$ trials</font>  
>In the paper proof, we choose the error term to be expressed as $K_{1}^{-\frac {1}{3}}<\frac {\varepsilon}{2\cdot N\cdot T\cdot R_{max}}$, then the total estimated loss must be less than $\varepsilon$.  
>
>&#10118;expand from $2\cdot e^{-\frac {K_{1}^{\frac {1}{3}}}{2}}<\frac {\delta}{3\cdot N\cdot k^{2}}$  
>$\Rightarrow K_{1}>-8\cdot ln^{3}(\frac {\delta}{6\cdot N\cdot k^{2}})$  
>, and we can choose $K_{1}>-6\cdot ln^{3}(\frac {\delta}{6\cdot N\cdot k^{2}})$ to narrow down the interval of probabilistic estimation failure.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-03-26-rl-rmax-part4-trials-over-same-state-num.png "trials over same state")
>
>&#10119;expand from $K_{1}^{-\frac {1}{3}}<\frac {\varepsilon}{2\cdot N\cdot T\cdot R_{max}}$  
>$\Rightarrow K_{1}>(\frac {2\cdot N\cdot T\cdot R_{max}}{\varepsilon})^{3}$  
>, and $K_{1}>(\frac {4\cdot N\cdot T\cdot R_{max}}{\varepsilon})^{3}$ holds for it.  
>
>Finally, $K_{1}$=$max((\frac {4\cdot N\cdot T\cdot R_{max}}{\varepsilon})^{3},-6\cdot ln^{3}(\frac {\delta}{6\cdot N\cdot k^{2}}))+1$, <font color="DeepPink">after this $K_{1}$ trials over the same state, we are confident to to turn a state from unknown to known or to update its statistics information, we believe that the estimated transitive probability is accurate</font>.  

### The <font color="Red">RMAX</font> Theorem Proof::2
>The implicit explore or exploit lemma yields a transitive probability of $\frac {\alpha}{R_{max}}$, we next show that <font color="DeepSkyBlue">after pure exploration</font> over $K_{2}$ trials on this same state $G_{i}$, we can obtain $K_{1}$ required visits on $G_{i}$.  
>
>&#10112;let $X_i$ be the random variable of indicator for each trial, whose value is $1$ iff it transits from $G_{i}$ to $G_{i^{\'}}$; or $0$ iff it justs exploits in the same $G_{i}$.  
>
>&#10113;let $Z_{i}$=$X_{i}-\frac {\alpha}{R_{max}}$ and $Z_{i}^{\'}$=$\frac {\alpha}{R_{max}-X_{i}}$, then $E\lbrack Z_{i}\rbrack$=$0$ and $E\lbrack Z_{i}^{\'}\rbrack$=$0$ respectively.  
>* By [Chernoff Bounds For Bernoulli Random Variable]({{ site.baseurl }}/2019/12/09/prob-bound-chernoff-bound-bernoulli/)  
>$P(\vert\sum_{i=1}^{K_{2}}(X_{i}-\frac {\alpha}{R_{max}})\vert>K_{2}^{\frac {1}{3}})<2\cdot e^{-\frac {K_{2}^{-\frac {1}{3}}}{2}}$  
>$\Rightarrow P(\vert\sum_{i=1}^{K_{2}}X_{i}-\frac {K_{2}\cdot\alpha}{R_{max}}\vert>K_{2}^{\frac {1}{3}})<2\cdot e^{-\frac {K_{2}^{-\frac {1}{3}}}{2}}$  
>* To limit the error terms  
>Take $2\cdot e^{-\frac {K_{2}^{-\frac {1}{3}}}{2}}<\frac {\delta}{3\cdot N\cdot k^{2}}$  
>, and take $\frac {K_{2}\cdot\alpha}{R_max}+K_{2}^{\frac {1}{3}}>K_{1}\cdot N\cdot k^{2}$  
>, for totally we have $N\cdot k^{2}\cdot K_{1}$ number of visits to unknown slots.  These guarantee that the fail probability less than $\frac {\delta}{3}$, which is much smaller than $\delta$.  
>* <font color="RoyalBlue">Why $K_{2}^{\frac {1}{3}}$ as the error term instead of $K_{2}^{\frac {2}{3}}$?</font>  
>The design of this proof is to find the least $K_{2}$ pure exploration trials, thus guarantees that we could have $K_{1}$ visits on this same state.  Since $K_{1}$ contains exploration and exploitation, $K_{2}\leq K_{1}$, therefore, the error term is expressed in terms of $K_{2}^{\frac {1}{3}}$, rather than $K_{2}^{\frac {2}{3}}$!!  We want a smaller $K_{2}<K_{1}$ and $K_{2}^{\frac {1}{3}}<K_{1}^{\frac {2}{3}}$.  

### The <font color="Red">RMAX</font> Theorem Proof::3
>This section discuss the scenario that we <font color="RosyBrown">perform $T$-step iterations without learning</font>, that is to say it exploits over $T$ steps, and the optimal expected reward would be $Opt(\prod_{M}(T,\varepsilon))-\varepsilon$.  
>
>* <font color="RosyBrown">The actual return may be lower</font>  
>Since the actual reward after execution of the <font color="Red">RMAX</font> algorithm would be some distance from optimal reward, it is at most $Opt(\prod_{M}(T,\varepsilon))-\varepsilon$, it is <font color="RosyBrown">lower</font> than $Opt(\prod_{M}(T,\varepsilon))-\varepsilon$, which is plausible.  <font color="OrangeRed">If we prevent it from exploring, we are at least staying in some local suboptimal</font>.  
>* We want it to be more closer  
>To align the design in above section, we choose the real return of exploitation after $T$-step iterations to be $Opt(\prod_{M}(T,\varepsilon))-\frac {3}{2}\varepsilon$, then it is $\frac {1}{2}\varepsilon$ close to the optimal reward $Opt(\prod_{M}(T,\varepsilon))-\varepsilon$.  The <font color="Red">RMAX</font> paper upper bound the failure probability by $\frac {\delta}{3}$.  
>
>&#10112;take $X_{i}$ to be the actual reward obtained in each trial  
>&#10113;treat $\mu$ as the optimal reward  
>&#10114;then by $y_{i}$=$\frac {\mu-X_{i}}{R_{max}}$ could we stablize the standard deviation, since it is bounded by $R_{max}$  
>&#10115;suppose $Z$=$M\cdot N\cdot T$, where $M>0$, after $Z$ exploitations, the failure probability that the total loss greater than $Z^{\frac {2}{3}}$ is upper bounded by $e^{-\frac {Z^{\frac {1}{3}}}{2}}$  
>* By [Chernoff Bounds For Bernoulli Random Variable]({{ site.baseurl }}/2019/12/09/prob-bound-chernoff-bound-bernoulli/)  
>$P(\sum_{i=1}^{Z}Y_{i}>Z^{\frac {2}{3}})<e^{-\frac {Z^{\frac {1}{3}}}{2}}$  
>$\Rightarrow P(\sum_{i=1}^{Z}\frac {\mu-X_{i}}{R_{max}}>Z^{\frac {2}{3}})<e^{-\frac {Z^{\frac {1}{3}}}{2}}$  
>$\Rightarrow P(\sum_{i=1}^{Z}\frac {\mu-X_{i}}{Z\cdot R_{max}}>Z^{-\frac {1}{3}})<e^{-\frac {Z^{\frac {1}{3}}}{2}}$  
>$\Rightarrow P(\sum_{i=1}^{Z}\frac {\mu-X_{i}}{Z}>\frac {R_{max}}{Z^{\frac {1}{3}}})<e^{-\frac {Z^{\frac {1}{3}}}{2}}$  
>
>&#10116;by choosing $M$ such that  
>$\frac {R_{max}}{Z^{\frac {1}{3}}}<\frac {\varepsilon}{2}$ and $e^{-\frac {Z^{\frac {1}{3}}}{2}}<\frac {\delta}{3}$  
>$\Rightarrow Z>(\frac {2\cdot R_Max}{\varepsilon})^{3}$ and $Z>6\cdot ln^{3}(\frac {\delta}{3})$,  
>We thus have the failure probability less than $\frac {\delta}{3}$ for the real return obtained is $\frac {\varepsilon}{2}$ far away from the optimal reward.  

### Addendum
>&#10112;[R-max: A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning, Ronen I. Brafman, CS in Ben-Gurion University, Moshe Tennenholtz, CS in Stanford University](http://www.jmlr.org/papers/volume3/brafman02a/brafman02a.pdf)  

<!-- Γ -->
<!-- \Omega -->
<!-- \cap intersection -->
<!-- \cup union -->
<!-- \frac{\Gamma(k + n)}{\Gamma(n)} \frac{1}{r^k}  -->
<!-- \mbox{\large$\vert$}\nolimits_0^\infty -->
<!-- \vert_0^\infty -->
<!-- \vert_{0.5}^{\infty} -->
<!-- &prime; ′ -->
<!-- &Prime; ″ -->
<!-- $E\lbrack X\rbrack$ -->
<!-- \overline{X_n} -->
<!-- \underset{Succss}P -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->
<!-- \int_{0}^{a}\lambda\cdot e^{-\lambda\cdot t}\operatorname dt -->
<!-- \Leftrightarrow -->
<!-- \prod_{v\in V} -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \varnothing -->
<!-- \perp -->
<!-- \overset\triangle= -->
<!-- \left|X\right| -->
<!-- \xrightarrow{r_t} -->
<!-- \left\|?\right\| => ||?||-->
<!-- \left|?\right| => |?|-->
<!-- \lbrack BQ\rbrack => [BQ] -->
<!-- \subset -->
<!-- \subseteq -->
<!-- \widehat -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus, mathematic expression</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="#C20000">conclusion, finding</font> -->
<!-- <font color="DeepPink">positive conclusion, finding</font> -->
<!-- <font color="RosyBrown">negative conclusion, finding</font> -->

<!-- <font color="#00ADAD">policy</font> -->
<!-- <font color="#6100A8">full observable</font> -->
<!-- <font color="#FFAC12">partial observable</font> -->
<!-- <font color="#EB00EB">stochastic</font> -->
<!-- <font color="#8400E6">state transition</font> -->
<!-- <font color="#D600D6">discount factor gamma $\gamma$</font> -->
<!-- <font color="#D600D6">$V(S)$</font> -->
<!-- <font color="#9300FF">immediate reward R(S)</font> -->

<!-- ### <font color="RoyalBlue">Example</font>: Illustration By Rainy And Sunny Days In One Week -->
<!-- <font color="RoyalBlue">[Question]</font> -->
<!-- <font color="DeepSkyBlue">[Answer]</font> -->

<!-- <font color="Brown">Notes::mjtsai1974</font> -->

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!--
><font color="DeepSkyBlue">[Notes]</font>
><font color="OrangeRed">Why at this moment, the Poisson and exponential probability come out with different result?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->