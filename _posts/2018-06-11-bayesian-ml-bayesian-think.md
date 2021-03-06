---
layout: post
title: The Bayesian Thinking
---

## Prologue To The <font color="Red">Bayesian Thinking</font>
<p class="message">
<font color="Red">Bayesian thinking</font> is an approach <font color="DeepPink">to systematizing reasoning under uncertainty</font> by means of the <font color="Red">Bayes theorem</font>.
</p>

### The <font color="DeepSkyBlue">Intuition</font> Behind The <font color="Red">Bayes Theorem</font>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">ReCap the Bayes theorem</font>  
>![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-05-28-bayesian-ml-significance-4-factors.png "4 factors")
>The detailed explanation of 4 factors are in my prior post, [The Bayes Theorem Significance](({{ site.github.repo }}{{ site.baseurl }}/2018/05/28/bayesian-ml-significance/)).  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">The intuition behind the theorem</font>  
>![]({{ site.github.repo }}{{ site.baseurl }}/images/pic/2018-06-11-bayesian-ml-bayesian-think-intuition.png "intuition")
>The intuition behind encourages you to make further inference.  
>&#10112;the <font color="Red">hypothesis</font>, mapped to the <font color="DeepSkyBlue">prior</font>, which are all probabilities.  
>&#10113;the <font color="Red">likelihood function</font> related to prior is expressed as the probability of the event occurrence of the <font color="Red">observation</font> given the event occurrence of <font color="Red">hypothesis</font>.  
>&#10114;the <font color="Red">total probability of the observation</font> is the well regularized <font color="Red">evidence</font>.  
>&#10115;the <font color="Red">posterior is the probability of the hypothesis, given the observation</font>.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">The Bayesian inference</font>  
>&#10112;at the first glance, we make an <font color="Red">observation</font> in the real world.  
>&#10113;we'd like to identify it by making certain <font color="Red">hypothesis</font> of some classification.  
>&#10114;the <font color="Red">likelihood function</font> estimates the possible probability of the observation given the hypothesis.  
>&#10115;finally, the <font color="Red">posterior</font> is the probability of the <font color="Red">hypothesis</font> given the <font color="Red">observation</font>.  
>Such process is called the <font color="Red">Bayesian inference</font>, full compliant with the classification of an observed object, which the hypothesis is made all about.  
>
>By the way, <font color="#C20000">observation, hypothesis, likelihood function are all based on the <font color="RosyBrown">qualitative</font> belief, the total probability of the observation and the posterior are the <font color="DeepPink">quantitative</font> outcomes</font>.  

### The <font color="Red">Bayesian Inference</font> Illustration
>My illustration in this article was inspired from [Introduction to Bayesian Thinking: from Bayes theorem to Bayes networks, Felipe Sanchez](https://towardsdatascience.com/will-you-become-a-zombie-if-a-99-accuracy-test-result-positive-3da371f5134), it is using an example from [The Anatomy Of Bayes Theorem, The Cthaeh](https://www.probabilisticworld.com/anatomy-bayes-theorem/).  But, I have some different opinion.  
>
><font color="DeepSkyBlue">[1]</font>
><font color="OrangeRed">Begin by a question</font>  
>&#10112;suppose everyone could casually find some mass in your body, like skin. It might be a rare disease, according to the medical library, only 1 from 1000 people having a mass would be the cancer, given in below table.  

<table>
  <tr>
    <td width="50px"></td>
    <td width="75px">Probability</td>
  </tr>
  <tr>
    <td>Cancer</td>
    <td>0.001</td>
  </tr>
  <tr>
    <td>Mass</td>
    <td>0.999</td>
  </tr>
</table>

>This table reveals the already known <font color="DeepSkyBlue">prior</font>, now turns into be the <font color="Red">hypothesis</font> of the probability of having a cancer.    
>&#10113;suppose the accuracy of the medical detection is given in below table, where malignant stands for cancer of result, and benign stands for being detected as a normal mass.  

<table>
  <tr>
    <td width="55px"></td>
    <td width="65px">Cancer</td>
    <td width="65px">Mass</td>
  </tr>
  <tr>
    <td>Malignant<br>(Cancer)</td>
    <td>$P(Malignant\vert Cancer)$=0.99</td>
    <td>$P(Malignant\vert Mass)$=0.01</td>
  </tr>
  <tr>
    <td>Benign<br>(Not a cancer)</td>
    <td>$P(Benign\vert Cancer)=0.01$</td>
    <td>$P(Benign\vert Mass)$=0.99</td>
  </tr>
</table>

>This table directly reflects the possible <font color="Red">likelihood</font> for all conditional combinations of 2 observations, malignant and benign.  
>&#10114;unfortunately, you are detected as having a cancer, then, <font color="RoyalBlue">what's the probability that you are really having a cancer given that you are medically detected as a victim of cancer?</font>  
>This given question is asking for $P(Cancer\vert Malignant)$, which is the <font color="Red">posterior</font>.  
>
><font color="DeepSkyBlue">[2]</font>
><font color="OrangeRed">Test of run #1</font>  
>By the given <font color="Red">hypothesis</font>, <font color="Red">likelihood</font>, the <font color="Red">Bayes theorem</font> could be used for the <font color="Red">posterior</font>:  
>&#10112;$P(Cancer\vert Malignant)$  
>=$\frac {P(Malignant\vert Cancer)\cdot P(Cancer)}{P(Malignant)}$  
>&#10113;the total probability of malignant <font color="Red">evidence</font>:  
>$P(Malignant)$  
>=$P(Malignant\vert Cancer)\cdot P(Cancer)$+$P(Malignant\vert Mass)\cdot P(Mass)$  
>&#10114;therefore, the posterior is   
>$P(Cancer\vert Malignant)$  
>=$\frac {0.99\cdot 0.001}{0.99\cdot 0.001+0.01\cdot 0.999}$=$0.090163$    
>; where $P(Mass\vert Malignant)$=$0.909837$, take it as $0.91$ after rounding.  
>
><font color="DeepSkyBlue">[3]</font>
><font color="OrangeRed">Test of run #2</font>  
>Even if the accuracy of the medical detection is up to $0.99$, the probability for your mass is really a cancer given the malignant diagnostic result is only $0.09$.  That's why we decide to make the 2nd test.  
>&#10112;first, we update the <font color="Red">prior</font> table with regard to the given run #1 result:  

<table>
  <tr>
    <td width="50px"></td>
    <td width="75px">Probability</td>
  </tr>
  <tr>
    <td>Cancer</td>
    <td>0.09</td>
  </tr>
  <tr>
    <td>Mass</td>
    <td>0.91</td>
  </tr>
</table>

>It is under the assumption that the run #1 is rather a <font color="OrangeRed">plausible</font>, not a vague result!!  
>&#10113;recalculate with the <font color="Red">Bayes theorem</font>:  
>$P(Cancer\vert Malignant)$  
>=$\frac {0.99\cdot 0.09}{0.99\cdot 0.09+0.01\cdot 0.91}$  
>=$0.90733$  
>$\approx 0.91$    
>; where $P(Mass\vert Malignant)$=$0.09266\approx 0.09$, after rounding.  Wow, it seems there is a great improvement in a malignant report and you do really have a cancer.  
>
><font color="DeepSkyBlue">[4]</font>
><font color="OrangeRed">Test of run #3</font>  
>Let's do it the 3rd run.  
>&#10112;first, we update the <font color="Red">prior</font> table with regard to the given run #2 result:  

<table>
  <tr>
    <td width="50px"></td>
    <td width="75px">Probability</td>
  </tr>
  <tr>
    <td>Cancer</td>
    <td>0.91</td>
  </tr>
  <tr>
    <td>Mass</td>
    <td>0.09</td>
  </tr>
</table>

>It is under the assumption that the run #2 is rather a <font color="OrangeRed">plausible</font>, not a vague result!!  
>&#10113;recalculate with the <font color="Red">Bayes theorem</font>:  
>$P(Cancer\vert Malignant)$  
>=$\frac {0.99\cdot 0.91}{0.99\cdot 0.91+0.01\cdot 0.09}$  
>=$0.999$  
>$\approx 1$  
>; where $P(Mass\vert Malignant)$=$0.0001$, after rounding.  
>It is now almost $100\%$ correct that the malignant report says that you have a cancer!!!  
>
><font color="DeepSkyBlue">[5]</font>
><font color="OrangeRed">Summary</font>  
>This illustration begins with the given prior of having cancer, executes from run #1 to run #3, constantly <font color="DeepPink">updates the next prior probability with the current estimated posterior</font>, finally get the expected result.  It is called the <font color="Red">Bayesian inference</font>.  

### The Review::mjtsai1974 
>Above illustration of <font color="Red">Bayesian inference</font> might strike you on your head that <font color="DeepPink">by constantly updating the given prior(so that you can make finer hypothesis) would you gradually adjust the posterior(the experiment result) toward the direction you want</font>.  
>
><font color="RoyalBlue">[Question]</font>  
>Below I comment out with 2 doubtable points:  
>&#10112;why we update the prior, $P(Cancer)$ with $P(Cancel\vert Malignant)$ after each test?  
>&#10113;is this the artificial bias leads to the contribution of $100\%$ identification of having a cancer given the malignant result?  
>
><font color="DeepSkyBlue">[Answer]</font>  
>&#10112;I think it is indeed an artificial bias, since the term $P(Cancer\vert Malignant)$ is not equivalent to the very first given $P(Cancer)$ for all possible diseases one can have as a sample or population.  
>&#10113;be remembered that it is <font color="OrangeRed">the common practices in Bayesian inference</font>.  

### Addendum
>&#10112;[Introduction to Bayesian Thinking: from Bayes theorem to Bayes networks, Felipe Sanchez](https://towardsdatascience.com/will-you-become-a-zombie-if-a-99-accuracy-test-result-positive-3da371f5134)  
>&#10113;[The Bayesian trap, Veritasium channel](https://www.youtube.com/watch?v=R13BD8qKeTg&vl=en)  
>&#10114;[The Anatomy Of Bayes Theorem, The Cthaeh](https://www.probabilisticworld.com/anatomy-bayes-theorem/)  

<!--
[1]What is a Bayesian network?
Bayes theorem offers a fundamental mechanism for changing your opinion in the light of evidence. This is what Bayesian networks are about.

https://www.quora.com/What-is-a-Bayesian-network

[2]What are the relationships of Bayes' theorem, Bayesian inference, Naive Bayes, and Bayesian network (in simple English)?
[2.1]Bayesianism is an approach to systematizing reasoning under uncertainty.
[2.2]We can characterize how one’s beliefs ought to change when new information is gained.
[2.3]If we observe the truth or falsity of a relevant event, we can then use Bayes’ theorem to revise our probability assessment for other related events. This is called Bayesian inference.
[2.4]If we are thinking about a complex situation, in which our probability for events depend upon various others, we can use a Bayesian network (also called Bayes net) to represent what we believe. 
[2.5]In a Bayes net, there are nodes connected by arrows. Each node is the probability of an event. An arrow from event A to event B means that our probability of B depends on our probability of A. 
[2.6]Naive Bayes refers to a particularly simple form of a Bayes net, where your event of interest depends on other things, but none of them depends on one another.

https://www.quora.com/What-are-the-relationships-of-Bayes-theorem-Bayesian-inference-Naive-Bayes-and-Bayesian-network-in-simple-English

[3]How does Bayesian networks work?
[3.1]A Bayesian network is good at classifying based on observations.
[3.2]Therefore you can make a network that models relations between events in the present situation, symptoms of these and potential future effects. The BN would then be able to classify the present situation and hence predict future events with a probability.
[3.3]You can do unsupervised learning with a BN from a dataset and allow the learning algorithm to find both structure and probabilities.
[3.4]you can also do supervised learning with a BN, aiding the learning algorithm with a priori knowledge about relations and probabilities in the model. Here, results should become better than ANN and SVM.
[3.5]A BN is a white box approach where you can represent and evaluate the structure of the model explicitly whereas ANN and SVM are black box approaches where you really don't know why you get your results. This puts a limit to how good they can become.

https://www.quora.com/How-does-Bayesian-networks-work

[4]What is Bayesian machine learning?
[4.1]Machine learning is a set of methods for creating models that describe or predicting something about the world. It does so by learning those models from data.
[4.2]Bayesian machine learning allows us to encode our prior beliefs about what those models should look like, independent of what the data tells us. This is especially useful when we don’t have a ton of data to confidently learn our model.

https://www.quora.com/What-is-Bayesian-machine-learning

[5]What does Bayesian networks mean in Machine Learning?
[5.1]A Bayesian network essentially has random variables, and a graph structure that encodes the dependencies between the variables.
[5.2]A Bayesian network is a statistical model which connects random variables with their conditional probabilities. Bayes' theorem is used for the computation of probabilities in the network.

https://www.quora.com/What-does-Bayesian-networks-mean-in-Machine-Learning
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
<!-- \widehat X -->
<!-- \overline{X_n} -->
<!-- \underset{w_{real}}{maxarg} -->
<!-- \underset{Succss}P -->
<!-- \frac{{\overline {X_n}}-\mu}{S/\sqrt n} -->
<!-- \lim_{t\rightarrow\infty} -->
<!-- \int_{0}^{a}\lambda\cdot e^{-\lambda\cdot t}\operatorname dt -->

<!-- Notes -->
<!-- <font color="OrangeRed">items, verb, to make it the focus</font> -->
<!-- <font color="Red">KKT</font> -->
<!-- <font color="Red">SMO heuristics</font> -->
<!-- <font color="Red">F</font> distribution -->
<!-- <font color="Red">t</font> distribution -->
<!-- <font color="DeepSkyBlue">suggested item, soft item</font> -->
<!-- <font color="RoyalBlue">old alpha, quiz, example</font> -->
<!-- <font color="Green">new alpha</font> -->

<!-- <font color="#C20000">conclusion, finding, more details</font> -->
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

<!--
<table>
  <tr>
    <td>項次</td>
    <td>品名</td>
    <td>描述</td>
  </tr>
  <tr>
    <td>1</td>
    <td>iPhone 5</td>
    <td>iPhone 6 > 5</td>
  </tr>
</table>

<TABLE border="1">
  <TR>
    <TD width="50px">A</TD>
    <TD width="100px">B</TD>
  </TR>
</TABLE>

<TABLE border="1">
  <TR>
    <TD width="50px">A</TD>
    <TD width="100px">B</TD>
  </TR>
  <TR>
    <TD>C</TD>
    <TD>D</TD>
  </TR>
</TABLE>

<TABLE border="1">
  <COL width="50px">
  <COL width="100px">
  <COL width="50px">
  <TR>
    <TD colspan="2">A</TD>
    <TD>B</TD>
  </TR>
  <TR>
    <TD>C</TD>
    <TD>D</TD>
    <TD>E</TD>
  </TR>
</TABLE>
-->

<!--
name | age
---- | ---
LearnShare | 12
Mike |  32

| left | center | right |
| :--- | :----: | ----: |
| aaaa | bbbbbb | ccccc |
| a    | b      | c     |
-->

<!-- https://www.medcalc.org/manual/gamma_distribution_functions.php -->
<!-- https://www.statlect.com/probability-distributions/student-t-distribution#hid5 -->
<!-- http://www.wiris.com/editor/demo/en/ -->
<!-- http://www.astroml.org/book_figures/chapter3/fig_gaussian_distribution.html -->