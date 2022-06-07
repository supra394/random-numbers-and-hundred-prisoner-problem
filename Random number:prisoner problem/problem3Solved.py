import random
from random import shuffle
import time


randomSuccessCount = 0                #counts the number of time random method succeeds in freeing the prisoners 
methodSuccessCount = 0               #counts the number of time given method succeeds in freeing the prisoners 
begin_time = time.time()


numberTrial = 10000                     #number od trials we are running
subjectNumbers = 100                    #number of prisoners and doors under observation
numberOfTriesAllowed = 50               #number of tries each priosner can make = subjectNumbers/2
prisoners = list(range(subjectNumbers)) #list of prisoners
doors = list(range(subjectNumbers))     #list of doors




def prisonerProblem(nTrials, rc, mc, number, tries):
    #iteration through each trial
    for a in range (1, nTrials+1):
        global randomSuccessCount
        global methodSuccessCount

        #flags to indicate that the trial will go on. When this is set to be true i.e when a priosner fails to find their number in the given number of tries
        # this is set to True and we stoo checking for any more priosners in that trial as the trial will not be successful anyway
        trialStopRandom = False
        trialStopMethod = False

        shuffle(doors)
        
        #running the trial for each prisoner
        for i in range (number):

            randomFlag = False
            methodFlag = False

            #as long as the previous prisoner found the door, trial keeps on going for the next prisoner
            if(trialStopRandom == False):

                x = 0
                list1 = []
                
                #as long as all the allowed tries aren't used up and the priosner hasn't found their door, they can keep on trying
                while x < tries and randomFlag == False:
                    choice = random.choice(doors)

            
                    #simulating that random selection won't result in prisoner selecting the same door
                    if(choice in list1):
                        continue        #if the same choice was made before, another random number is chosen for the same loop iteration
       
                    list1.append(choice)

                    trialStopRandom = True
                    
                    if(prisoners[i] ==  choice):
                        randomFlag = True           
                        trialStopRandom = False         #if a prisoner finds their number flag is set to False so that another prisoner can check their number as well
                         
                    x += 1
    
            #for method 1
            #assign the initial choice of door number to be whatever number the prisoner is   
            doorNumber = i
            x = 0

            #as long as the previous prisoner found the door, trial keeps on going for the next prisoner
            if(trialStopMethod == False):

                #as long as all the allowed tries aren't used up and the priosner hasn't found their door, they can keep on trying
                while x < tries and methodFlag == False:
                    
                    #the number inside the door will be 'b' which could be or could not be the prisoner's number
                    b = doors[doorNumber]       

                    trialStopMethod = True
                    
                    if(prisoners[i] == b):
                        methodFlag = True
                        trialStopMethod = False
                        
            
                    else: 
                        doorNumber = b     #the new door number the prisoner will try will be whatever they found inside the door i.e.
                                          
                    x += 1

        #if throughout the trial of the random guesses, all prisoners correctly guessed their door in 50 tries, it is a success for that random trial 
        if(trialStopRandom == False):
            randomSuccessCount += 1

         #if throughout the trial of the methodical appraoch, all prisoners correctly chose their door in 50 tries, it is a success for that controlled trial
        if(trialStopMethod == False):
            methodSuccessCount += 1
        

prisonerProblem(numberTrial, randomSuccessCount, methodSuccessCount, subjectNumbers, numberOfTriesAllowed)
print('Success rate for random method: ', (randomSuccessCount/numberTrial)*100, '%')
print('Success rate for given method: ',(methodSuccessCount/numberTrial)*100, '%')
print(time.time() - begin_time)


    
