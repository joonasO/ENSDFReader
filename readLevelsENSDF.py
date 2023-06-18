import sys
import numpy as np
import os.path
from matplotlib import pyplot as plt

def readENSDF(path,element,massNumber):
    with open(path,"r") as f:
        input=f.readlines()
        levelEnergies=[]
        levelUncertainties=[]
        levelSpins=[]
        halfLifes=[]
        searchValueName=str(massNumber)+element
        print(searchValueName)
        for line in input:
            levelEnergy=""
            levelUncertainty=""
            levelSpin=""
            halfLife=""

            if line[0]!="#":
                inputs=line.split( )
                
                if len(inputs)>1:
                    if(searchValueName==inputs[0] and "L"==inputs[1]):
                        print(inputs)
                        levelEnergy=inputs[2]
                        if len(inputs)>3:
                            levelUncertainty=inputs[3]
                            if levelUncertainty.find('(')!=-1:
                                uncertaintySpin=levelUncertainty.split('(')
                                levelUncertainty=uncertaintySpin[0]
                                levelSpin=uncertaintySpin[1]
                                if (len(inputs)>5):
                                    halfLife=inputs[4]+" "+inputs[5]
                            elif(levelUncertainty.find('/')!=-1):
                                levelUncertainty=" "
                                levelSpin=inputs[3]
                                if (len(inputs)>5):
                                     halfLife=inputs[4]+" "+inputs[5]
                            elif(len(inputs)>4):
                                levelSpin=inputs[4]
                                if(len(inputs)>6):
                                    print(inputs)
                                    halfLife=inputs[5]+" "+inputs[6]
                               
                        levelEnergies.append(levelEnergy)
                        levelUncertainties.append(levelUncertainty)
                        levelSpins.append(levelSpin)
                        halfLifes.append(halfLife)
    return levelEnergies,levelUncertainties,levelSpins,halfLifes
path=sys.argv[1]
element=sys.argv[2]
massNumber = sys.argv[3]
levelEnergies,levelUncertainties,levelSpins,halfLifes=readENSDF(path,element,massNumber)
values=[levelEnergies,levelUncertainties,levelSpins,halfLifes]
print("LevelUncertainty:\n")
print(levelUncertainties)
print("\n")
print("LevelSpin:\n")
print(levelSpins)
print("\n")
print("HalfLives:\n")
print(halfLifes)
