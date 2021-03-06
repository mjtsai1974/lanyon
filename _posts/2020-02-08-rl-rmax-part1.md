---
layout: post
title: Model-Based RL Algorithm RMAX - Part 1
---

## Prologue To Model-Based RL Algorithm <font color="Red">RMAX</font> - Part 1
<p class="message">
<font color="Red">RMAX</font> is a <font color="DeepPink">simple model-based reinforcement learning algorithm that can attain near-optimal average reward in polynomial time</font>.  
</p>

### MDP Model Construct From Given Data
><font color="RoyalBlue">[Question]</font>
>Here is the condition, suppose you are given:  
>&#10112;a sample of probabilistic transitions and immediate rewards pertaining to a MDP model  
>&#10113;the <font color="DeepSkyBlue">full set of states is known</font> in advance   
>&#10114;<font color="OrangeRed">but</font>, only the contour, <font color="OrangeRed">exclusive of the path in between states</font>  
>&#10115;<font color="OrangeRed">all states are initialized as unknown</font>  
>
>We don't have the whole MDP yet, <font color="RoyalBlue">what would you do to construct a complete MDP model?</font>  What do we do along the way?  
>
><font color="DeepSkyBlue">[Answer]</font>
>We would be able to refer to the [Temporal Difference Learning - Part 1]({{ site.github.repo }}{{ site.baseurl }}/2018/12/23/rl-temp-diff-learn-part1/), [Temporal Difference Learning - Part 2]({{ site.github.repo }}{{ site.baseurl }}/2019/01/22/rl-temp-diff-learn-part2/), [Temporal Difference In Q Form]({{ site.github.repo }}{{ site.baseurl }}/2019/02/19/rl-temp-diff-q/) in my prior post, which is a <font color="DeepSkyBlue">model-free</font> algorithm.  
>
>However, we are given the <font color="DeepSkyBlue">full set of states</font>, the suggestion would be made to use the <font color="Red">RMAX</font>, which is a <font color="Red">model-based algorithm</font>.  

### Before We Enter <font color="Red">RMAX</font> Algorithm
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Brief description</font>  
>The approach used by <font color="Red">RMAX</font> has been refered to as <font color="DeepPink">the optimism in the face of uncertainty heuristic</font>.  It propose a specific approach in which <font color="DeepPink">the choice in between exploration and exploitation is implicit</font>.  
>
>The major insight behind this algorithm is the optimal policy with respect to the agent's fictitious model has a very interesting and useful property that <font color="DeepPink">it is always optimal or it leads to efficient learning</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Preliminaries</font>  
>The <font color="Red">RMAX</font> algorithm was presented in the context of a model called <font color="OrangeRed">stochastic game</font> in [R-max: A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning, Ronen I. Brafman, CS in Ben-Gurion University, Moshe Tennenholtz, CS in Stanford University](http://www.jmlr.org/papers/volume3/brafman02a/brafman02a.pdf).  <font color="OrangeRed">Stochastic game</font> is more general than MDP, because <font color="RosyBrown">it doesn't necessarily assume that the environment is stochastic</font>.  
>
>Please recall <font color="OrangeRed">in MDP, the execution of the action might not go as well as it has been expected</font>, it is a <font color="OrangeRed">stochastic environment</font>.  
>
>A <font color="OrangeRed">stochastic game</font> is a model of <font color="OrangeRed">multi-agent</font> interaction.  It has a set of players, each of whom chooses some action to perform from within a given set of actions.  As a result of the combinatory choices, some outcome is obtained and is described numerically in the form of a <font color="OrangeRed">payoff vector</font>, vector of values, one for each of the players.  
>
>The <font color="Red">RMAX</font> was developed on <font color="OrangeRed">2 palyers, fixed-sum games</font>, in which <font color="OrangeRed">the sum of values in the payoff vector is constant</font>.  The <font color="DeepSkyBlue">player under our control</font> is called the <font color="DeepSkyBlue">agent</font>, whereas the other one is the <font color="RoyalBlue">adversary</font>.  
>
>The game is commonly described in strategic form of matrix, the rows of a matrix correspond to the agent't actions and the columns correspond to the adversary's actions.  The entry of row i and column j contains the rewards obtained for the agent chooses i-th and the adversary chooses the j-th action.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-02-08-rl-rmax-part1-strategic-form.png "S.G matrix")
>
>In <font color="OrangeRed">stochastic game</font>, the player plays a sequence of standard games, which represents the states in normal MDP.  After playing a game, it obtains rewards and transits to a new game(or maybe stay in the same place), in both models, actions lead to transitions between states, such similarity could be found.  
>
>You could <font color="DeepPink">treat MDP as an stochastic game in which the adversary has only a single action at each state</font>.  

### The <font color="Red">RMAX</font> Algorithm
><font color="Brown">[Input]</font>  
>Below are the basic defines:  
>&#10112;$N$: the number of stage games(or states).  
>&#10113;$k$: the number of actions for each state.  
>&#10114;$\varepsilon$: the error bound.  
>&#10115;$\delta$: the algorithm's failure probability.  
>&#10116;$R_{max}$: the upper bound on the reward function.  
>&#10117;$T$: <font color="OrangeRed">the maximum number of steps</font> for the optimal policy of the algorithm to get $\varepsilon$ close to the <font color="DeepSkyBlue">average expected(undiscounted) reward</font>.  
<!--
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-02-08-rl-rmax-part1-input.png "RMAX input")
-->
>
><font color="Brown">[Inintialize]</font>  
>Initialize by constructing a model $M^{\'}$ consisting of  
>&#10112;$N+1$ stage games, $\{G_{0},G_{1},...,G_{N+1}\}$, corresponding to the real states.  
>&#10113;$k$ actions, $\{a_{1},...,a_{k}\}$, which would then be played by the <font color="RoyalBlue">agent</font> and the <font color="RoyalBlue">adversary</font>.  
>&#10114;set each $G_{i}$ in <font color="OrangeRed">unknown</font> status.  
>
>Where the $G_{0}$ is an additional fictitious game, of which we are in need to initialize the probability for each $G_{i}$ to transite to $G_{0}$ by the <font color="RoyalBlue">agent</font> choosing action $a$ and the <font color="RoyalBlue">adversary</font> choosing $a^{\'}$ to be $1$, that is $P_{M}(G_{i},G_{0},a,a^{\'})$=$1$, $i$=$\{0,1,...,N\}$.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-02-08-rl-rmax-part1-init.png "RMAX init")
>
>Cautions must be made that the <font color="Red">RMAX</font> Algorithm is using the <font color="OrangeRed">constructed</font> model $M^{\'}$ to approximate the <font color="OrangeRed">real</font> model $M$, that's why it is $P_{M}(G_{i},G_{0},a,a^{\'})$, <font color="RosyBrown">not</font> $P_{M^{\'}}(G_{i},G_{0},a,a^{\'})$.  
>
><font color="Brown">[Repeat]</font>  
>* Compute an <font color="#00ADAD">optimal $T$-step policy</font> and take action:  
>&#10112;execute this policy for $T$-steps.  
>&#10113;<font color="OrangeRed">or until a new entry of $G_{i}$ becomes known</font>.  
>
>* Keep track of action execution results:  
>&#10112;update the <font color="#9300FF">reward</font> thus obtained upon state transition from $G_{i}$ to $G_{j}$ after the execution of joint action of actions $a$ and $a^{\'}$ for its <font color="OrangeRed">very first time</font>.  
>&#10113;update the set of states thus reached in accordance to each action pair $(a,a^{\'})$ in $G_{i}$.  
>&#10114;if <font color="OrangeRed">this entry of $G_{i}$ has been explored over $K_{1}$ times</font>, in other words, <font color="OrangeRed">the set of states reached from this $G_{i}$ contains $K_{1}$ elements</font>, <font color="OrangeRed">mark this $G_{i}$ as known</font>, and update the transition probabilities in the unit of distinct transition from $G_{i}$ to $G_{j}$.  
>
>Where $K_{1}$=$max((\frac {4\cdot N\cdot T\cdot R_{max}}{\varepsilon})^{3},-6\cdot ln^{3}(\frac {\delta}{6\cdot N\cdot k^{2}}))+1$, which would then be proved in the following secction.  
>
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2020-02-08-rl-rmax-part1-repeat.png "RMAX repeat")
>
><font color="Brown">[Brief summary]</font>  
>The <font color="Red">RMAX</font> algorithm constructs a model $M^{\'}$ to approximate the real model $M$, by initializing all states as unknown and the probability for each $G_{i}$ of all action pairs $(a,a^{\'})$ to $G_{0}$ be $1$.  
>
>Based on model $M^{\'}$, compute an optimal $T$-step policy, follow from the departuring state in each eposide, say $G_{i}$, keep record of all states reached in accordance to the execution of action pairs $(a, a^{\'})$.
>
>At the moment <font color="Brown">$T$ steps has been reached</font> or <font color="Brown">the departuring $G_{i}$ turns into known</font>, update the probabilistic transition from this state to its next states.  <font color="OrangeRed">Each time, after such $G_{i}$ has been updated</font>, <font color="OrangeRed">recompute</font> an optimal $T$-step policy and <font color="OrangeRed">repeat</font>.  

<!--
### The <font color="Red">RMAX</font> Algorithm Theorem
><font color="Brown">[Theorem of optimality and convergence]</font>  
>Given below condition:  
>&#10112;let $M$ be the <font color="OrangeRed">stochastic game</font> with $N$ states and $k$ actions.  
>&#10113;let $0 < \delta < 1$ and $\varepsilon > 0$ be constants, where <font color="OrangeRed">$\delta$</font> is the <font color="OrangeRed">error probability</font> and <font color="OrangeRed">$\varepsilon$</font> is the <font color="OrangeRed">error term</font>.  
>&#10114;denote the policy for $M$ whose <font color="OrangeRed">$\varepsilon$-return mixing time</font> is $T$ by $\prod_{M}(\varepsilon,T)$.  
>&#10115;denote the <font color="#00ADAD">optimal</font> expected return by such policy by $Opt(\prod_{M}(\varepsilon,T))$.  
>
>Then, with probability of no less than $1-\delta$ the <font color="Red">RMAX</font> algorithm will attain an expected return of $Opt(\prod_{M}(\varepsilon,T))-2\cdot\varepsilon$, within a number of steps polynomial in $N$,$k$,$T$,$\frac {1}{\varepsilon}$ and $\frac {1}{\delta}$.  
>
><font color="Brown">Notes::mjtsai1974</font>
>Why the execution of the <font color="Red">RMAX</font> algorithm will attain an expected return of $Opt(\prod_{M}(\varepsilon,T))-2\cdot\varepsilon$?  
>
>As a result of the fact that the <font color="#00ADAD">optimal policy</font> is defined on <font color="OrangeRed">$\varepsilon$-return mixing time</font> of $T$, the <font color="#D600D6">real return</font> of the execution of the <font color="Red">RMAX</font> algorithm must be smaller than it, thus we choose it to be $-2\cdot\varepsilon$.  
-->

### Addendum
>&#10112;[Exploring Deterministics MDP, Charles IsBell, Michael Littman, Reinforcement Learning By Georgia Tech(CS8803)](https://classroom.udacity.com/courses/ud600/lessons/4402978778/concepts/44303424040923)  
>&#10113;[R-max: A General Polynomial Time Algorithm for Near-Optimal Reinforcement Learning, Ronen I. Brafman, CS in Ben-Gurion University, Moshe Tennenholtz, CS in Stanford University](http://www.jmlr.org/papers/volume3/brafman02a/brafman02a.pdf)  

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