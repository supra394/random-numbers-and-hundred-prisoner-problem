import random

randList = {}

def generateRand():

    ## For 10000 random rumbers
    for i in range(10000):
        
        n = random.randint(-1000, 1000)

        ## If random is in the list
        if n in randList:
            randList[n] += 1
        else:
            randList[n] = 1
            
    ## Count the frequency
    count()
            
def count():
    for n in sorted(randList.keys()):
        count = randList[n]
        print("frequency of {} is {}".format(n, count))
        
## Run simulation 100 times
for j in range(100):
    generateRand()
    print("______________________________________________\n")
