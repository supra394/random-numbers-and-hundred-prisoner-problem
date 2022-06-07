import random
import time

mtb = 0
rtb = 0
begin_time = time.time()

def part2(nTrial, manualBetter, randomBetter, numberRange):
    global mtb
    global rtb
    for i in range(1, nTrial+1):
        r = random.randrange(1, numberRange + 1)
        counter = 0
        found = False
        list1 = []
        while(found == False):
            
            randomChoice = random.randrange(1, numberRange + 1)
            
            if randomChoice in list1:
                continue
            
            list1.append(randomChoice)
            
            if(randomChoice == r):
                found = True

            counter += 1


        if(counter < r):
            rtb += 1
            
        elif (r< counter):
            mtb += 1
            
        else:
            mtb += 0
            rtb += 0



rangeNum = 10000
part2(1000, mtb, rtb, rangeNum)


print('\nRandom guess was better ', rtb, ' times.')
print('Manual increment method was better ', mtb, ' times.\n')
#print('It took ', time.time() - begin_time, ' seconds.')
