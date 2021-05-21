import time
startTime = time.time()

y = []
for i in range(0, 1000000):
    y.append(i)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
executionTime = time.time()

x = [i for i in range(0, 1000000)]

executionTime2 = (time.time() - executionTime)
print('Execution time in seconds: ' + str(executionTime2))

executionTime = time.time()

x = (i for i in range(0, 1000000))

executionTime3 = (time.time() - executionTime)
print('Execution time in seconds: ' + str(executionTime3))
