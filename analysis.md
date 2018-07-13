# seedbox-test

## Environment 
OS: Scientific Linux 7.3
Engine: Apache Spark 2.2.0 (Pyspark - Python 3.5.1)

## Analysis

### Probability Distributions
With n = 59721, our two groups are split quite unevenly with 44886 in the control group and 14835 in the test group.
If we denote our control group as A and our test group as B we have the following exact probabilities (to three significant figures):

P(A) = 0.752
P(B) = 0.248

Considering that the distribution is clearly binomial (dichotomy: you are either in the control group or the test group), we can use either normal or Poisson approximation to determine the "approximate probability distribution". Without knowing our N (population size) it is difficult to say whether n is large enough to yield a result which would be significant, ignoring this we can say that because n * P(A) or n * P(B) would result in relatively large numbers, a Poisson approximation would not be ideal. Thus a normal approximation to the binomial distribution can be used to approximate the probability of any given number of individuals being in the control or test group.

### Rebill Comparison
With the total number of rebills being 6961, my analysis found that 3756 of these were from the control group, and 3205 of these were from the test group.
Removing duplicate rebills (rather, multiple rebills that were made by the same user) I found that there were precisely 941 control group users who had at least 1 rebill and 1556 test group users who had at least 1 rebill.

From the second analysis it clearly follows that those in the test group were more likely to have at least 1 rebill.
~2.10% of users in control group rebilled at least once
~10.5% of users in test group rebilled at least once

### Revenue Comparison

### Chargeback Rate Comparison