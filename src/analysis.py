import csv
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
from pyspark import SparkContext, SparkConf

def probability(sample):
	total_entries = sample.count()
	reduced_sample = sample.map(lambda x: (x[1], 1)).reduceByKey(lambda a,b: a+b).collect()
	return total_entries, reduced_sample

def rebill(sample, trans):
	clean_trans = trans.map(lambda x: (x[1], x[2])).filter(lambda x: x[1] == 'REBILL')
	intersect = sample.join(clean_trans)
	reduced_intersection_no_dupe = intersect.distinct().map(lambda x: (x[1][0], 1)).reduceByKey(lambda a,b: a+b).collect()
	reduced_intersection = intersect.map(lambda x: (x[1][0], 1)).reduceByKey(lambda a,b: a+b).collect()
	return reduced_intersection_no_dupe, reduced_intersection

def revenue(sample, trans):
	clean_trans = trans.map(lambda x: (x[1], x[3]))
	intersect = sample.join(clean_trans)
	total_users = intersect.distinct().map(lambda x: (x[1][0], 1)).reduceByKey(lambda a,b: a+b).collect()
	reduced_intersection = intersect.map(lambda x: (x[1][0], (1, float(x[1][1])))).reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1])).collect()
	return total_users, reduced_intersection

def chargeback(sample, trans):
	clean_trans = trans.filter(lambda x: x[2] == 'REFUND' or x[2] == 'CHARGEBACK').map(lambda x: (x[1], x[3]))
	intersect = sample.join(clean_trans)
	total_users = intersect.distinct().map(lambda x: (x[1][0], 1)).reduceByKey(lambda a,b: a+b).collect()
	reduced_intersection = intersect.map(lambda x: (x[1][0], (1, float(x[1][1])))).reduceByKey(lambda a,b: (a[0]+b[0], a[1]+b[1])).collect()
	return total_users, reduced_intersection

conf = SparkConf().setAppName("seedbox-test").setMaster("local")
sc = SparkContext(conf=conf)

sampleRDD = sc.textFile("../data/testSamples.csv").mapPartitions(lambda x: csv.reader(x))
transactionRDD = sc.textFile("../data/transData.csv").mapPartitions(lambda x: csv.reader(x))

sampleHeader = sampleRDD.first()
transactionHeader = transactionRDD.first()

sampleRDD = sampleRDD.filter(lambda x: x != sampleHeader)
transactionRDD = transactionRDD.filter(lambda x: x != transactionHeader)

#print(probability(sampleRDD))
#print(rebill(sampleRDD, transactionRDD))
#print(revenue(sampleRDD, transactionRDD))
#print(chargeback(sampleRDD, transactionRDD))

### Probability Distribution Graph
x = np.arange(-1, 200)
n, p = 59721, 0.752
dist = binom(n, p)
plt.plot(x, dist.pmf(x), c='red', linestyle='steps-mid')

plt.show()