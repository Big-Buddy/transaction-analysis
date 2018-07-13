import csv
from pyspark import SparkContext, SparkConf

def probability_distribution(sample):
	total_entries = sample.count()
	reduced_sample = sample.map(lambda x: x[1], 1).reduceByKey(lambda a,b: a+b).collect()
	return total_entries, reduced_sample

conf = SparkConf().setAppName("seedbox-test").setMaster("local")
sc = SparkContext(conf=conf)

sampleRDD = sc.textFile("./data/testSamples.csv").mapPartitions(lambda x: csv.reader(x))
transactionRDD = sc.textFile("./data/transData.csv").mapPartitions(lambda x: csv.reader(x))

sampleHeader = sampleRDD.first()
transactionHeader = transactionRDD.first()

sampleRDD = sampleRDD.filter(lambda x: x != sampleHeader)
transactionRDD = transactionRDD.filter(lambda x: x != transactionHeader)

print(probability_distribution(sampleRDD))