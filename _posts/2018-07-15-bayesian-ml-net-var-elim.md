---
layout: post
title: Variable Elimination In Bayesian Network
---

## Prologue To Variable Elimination In <font color="Red">Bayesian Network</font>
<p class="message">
<font color="Red">Inference</font> via <font color="Red">Bayesian Network</font> could be achieved by probabilistic marginalization, i.e. summing out over <font color="DeepSkyBlue">irrelevant</font> or <font color="DeepSkyBlue">hidden</font> variables.  
</p>

### <font color="Red">Inference</font> Via <font color="Red">Bayesian Network</font>
>Given a well-constructed BN of nodes, 2 types of inference are supported:  
>&#10112;<font color="Red">predictive</font> support(<font color="Red">top-down reasoning</font>) with the evidence nodes connected to node $X$, through its parent nodes, the same direction as predictive propagation.  
>&#10113;<font color="Red">diagnostic</font> support(<font color="Red">bottom-up reasoning</font>), with vidence nodes connected to node $X$, through its children nodes, the same direction as <font color="Red">retrospective</font> propagation.  
>
>In my Bayesian articles, I have guided you through both types of support by means of <font color="DeepSkyBlue">variable enumeration</font> over the factorized terms of full joint PDF(probability distribution function).  Most of the examples are all in small network, trivially, <font color="DeepSkyBlue">variable enumeration</font> is old, she will hold for complex model consisting of a lot random variables, resulting in high expenditure of computation efficiency.  Therefore, another technique of <font color="Red">variable elimination</font> is introduced.   

### <font color="RoyalBlue">Example</font>: Illustration Of <font color="Red">Variable Elimination</font>
><font color="RoyalBlue">[Question]</font>  
>Suppose you are using a <font color="Red">Bayesian network</font> to infer the relationship in between raining, traffic and late(to office).  The probability of raining and the conditional probability of traffic jam, given raining, and being late, given traffic jam are all depicted in this graph.  What's the probability of being late?  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-ezex.png "ve ex")
><font color="DeepSkyBlue">[Answer]</font>  
>This is to ask for $P(L=t)$.  The full joint PDF would be $P(R,T,L)$=$P(L\vert T)\cdot P(T\vert R)\cdot P(R)$.  
>
>By the old <font color="DeepSkyBlue">variable enumeration</font>, $P(L=t)$=$\sum_{R}\sum_{T}P(R,T,L)$, the nested summation over $T$ would be proceeded inside the outer summation over $R$.  Here, we'd like to further reduce the computation complexity by means of <font color="Red">variable elimination</font>.  
>[1]The first would be to <font color="Red">join factors</font>:  
>&#10112;a <font color="OrangeRed">factor</font> is one of these tables of probability, $P(R)$, or the conditional probability, $P(T\vert R)$, $P(L\vert T)$.  By usual, they are multi-dimensional matrix.  
>&#10113;what we do is to <font color="OrangeRed">choose 2 or more</font> of these factors.  In this case, we choose $P(R)$ and $P(T\vert R)$, to <font color="OrangeRed">combine</font> them together to <font color="OrangeRed">form a new factor</font> which represent the joint probability of all variables, $R$ and $T$ in that new factor $P(R,T)$.  
>&#10114;we perform the operation of joining factors on these 2 factors, $P(R)$, $P(T\vert R)$, getting a new factor which is part of the existing network.  Below exhibits what we have now.  
![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-07-15-bayesian-ml-net-var-elim-ezex-join-factor.png "ve ex")
>
>[2]The second is the operation of <font color="Red">elimination</font>, also called <font color="OrangeRed">summing out</font> or <font color="OrangeRed">marginalization</font>, to take the table $P(R,T)$, reduce it to $P(T)$, finally <font color="OrangeRed">combine</font> it with $P(L\vert T)$ to get $P(L)$.  
>

<!--
### Addendum
>&#10112;[](http://kuleshov.github.io/cs228-notes/inference/ve/)  
>&#10113;[](https://www.youtube.com/watch?v=FDNB0A61PGE)  
>&#10114;[](https://www.youtube.com/watch?v=qyXspkUOhGc&list=PLBF898A2F63224F39&t=0s&index=14)  
>&#10115;[Bayesian Networks, Ben-Gal Irad, in Ruggeri F., Faltin F. & Kenett R., Encyclopedia of Statistics in Quality & Reliability, Wiley & Sons (2007).](http://www.eng.tau.ac.il/~bengal/BN.pdf)  
-->

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

<!-- 
[1]Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Given the vehicles pass through a highway toll station is $6$ per minute, what is the probability that no cars within $30$ seconds?</font>  
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->