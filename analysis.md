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
Of the total number of transactions in the sample (7430), 4050 were from the control group while 3380 were from the test group. The total revenues from both groups were ~89838.90 and ~95433.50 respectively.
From these results we can see that while the proportion of test group users is much smaller than the control group, the test group is responsible for more overall revenues, thus we can conclude that the test group (being a representative sample of all users who have to call-in) is disproportionately responsible for giving the company revenue from these transactions.

The average total transaction amount for users who had a transaction of any type is:
~83.03 for control group
~58.08 for test group

The average total transaction amount for all users (thus here we expand our scope to include users who have no transactions and assign them a default transaction amount of 0):
~2.00 for control group
~6.43 for test group

Given all these results we can conclude that users who call-in do in fact generate more revenue on average when we take into consideration the sheer amount of control group users who do not make any transactions at all. The proportion of test group users who have at least 1 transaction is simply greater which means they not only contribute more overall, they contribute more on average (contributions is in terms of revenue here).

### Chargeback Rate Comparison