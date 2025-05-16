import random
from typing import List, Tuple
from player import Player


def olisort_challenge() -> Tuple[bool, str, str]:
    """
    Challenge: sort a list of random integers.

    Steps:
      1. Generate a random list of 10 ints between 0 and 100.
      2. Call Player.olisort to get the player's sorted list.
      3. Compute the expected sorted list using Python's sorted().
      4. Compare and return (passed, expected_str, actual_str).
    """
    # 1) generate input
    data: List[int] = [random.randint(0, 100) for _ in range(10)]

    # 2) get player's result via stub
    # We assume Player.olisort is implemented in player.py
    player = Player((0, 0), 0, 0)  # dummy position and bounds
    player_result: List[int] = player.olisort(data)

    # 3) expected result
    expected: List[int] = sorted(data)

    # 4) compare and return
    passed: bool = player_result == expected
    return passed, str(expected), str(player_result)

import random
import statistics
from numpy import random 
#from numpy import random 

class Task():
    def __init__(self):
        # set energy
        self.energy = genratorEnergy
        self.success = generatorSuccess

    def getEnergy(self):
        return self.energy

    def getSuccess(self):
        return self.success

def ekf7ue(b):
    thing = (5*(b+1))
    thing1 = (5*b)
    print(thing1, thing)
    return random.randint(thing1,thing)
def genratorEnergy():
    probabiltyBounds=[.01,.06,.13,.22,.45,.6,.7,.81,.86,.90,.94,.97,.975,.978,.98,.985,.987,.985,.994,.999]
    pig =[]                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    jig = [range(1,len(pig)+1)]
    cricky = map(ekf7ue, pig, jig)

    value=random.random()
    value=round(value,3)
    print("random: ",value)
   
    found=False
    x=0
    while found!=True:
        #print(x)
        if probabiltyBounds[x]>=value:
            found=True
            energy=ekf7ue(x)
        else:
            x+=1
    print("Ener: ",energy)
    return energy
def generatorSuccess():
    value=random.random()
    value=round(value,3)
    n=random.normal(25,13,(2,3))
    return n




def nextDay():
    dt = []
    energy = 100
    success = 0
    for i in range(0,5):
        newTask = Task()
        dt.append(newTask)
    
    dailyTasks = (dt[0],dt[1],dt[2],dt[3],dt[4])
    
    #joliQueue(dailyTasks)
    test = joliQueue_challenge(dailyTasks)
    try:
        for i in test:
            energy-=i.getEnergy()
            if energy >= 100:
                success+=i.getSuccess()
            else:
                break
    except AttributeError:
        print('Your queue should only contain task variables')
        return False
    
    return success


def main():
    success=0
    successReq=1000
    for i in range(0,8):
        suc = nextDay()
        if suc:
            success+=suc
        else:
            return False

    if success >= 1000:
        return True
    else:
        return False
#def myfunc(n):

