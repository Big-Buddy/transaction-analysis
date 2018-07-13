# seedbox-test

## Environment 
OS: Scientific Linux 7.3
Engine: Apache Spark 2.2.0 (Pyspark - Python 3.5.1)

## Analysis

### Probability Distributions
With n = 59721, our two groups are split quite unevenly with 44886 in the control group and 14835 in the test group.
If we denote our control group as A and our test group as B we have the following probabilities (to three significant figures):
P(A) = 0.752
P(B) = 0.248
Considering that the distribution is clearly binomial (dichotomy: you are either in the control group or the test group), we can use either normal or Poisson approximation to determine the "approximate probability distribution". Without knowing our N (population size) it is difficult to say whether n is large enough to yield a result which would be significant, ignoring this we can say that because n * P(A) or n * P(B) would result in relatively large numbers, a Poisson approximation would not be ideal. Thus a normal approximation to the binomial distribution can be used to approximate the probability of any given number of individuals being in the control or test group.