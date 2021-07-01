import time
from data import *
from cluster import *


data = Data("Leukemia_sample.csv")
samples = data.create_samples()
first = samples[0]
second = samples[1]


startTime = time.time()
s2 = sum([(x-y) * (x-y) for x, y in zip(first.genes, second.genes)]) ** 0.5
print(time.time() - startTime)

startTime = time.time()
s1 = sum((x-y) * (x-y) for x, y in zip(first.genes, second.genes)) ** 0.5
print(time.time() - startTime)

startTime = time.time()
sum = 0
length = len(first.genes)
first_genes = first.genes
second_genes = second.genes
for i in range(length):
    asd = first_genes[i]-second_genes[i]
    sum += asd*asd
sum = sum**0.5
print(time.time() - startTime)

startTime = time.time()
sum = 0
length = len(first.genes)
first_genes = first.genes
second_genes = second.genes
for i in range(length):
    sum += (first_genes[i]-second_genes[i])**2
sum = sum*0.5
print(time.time() - startTime)
