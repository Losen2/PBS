import numpy as np
from classes.Car import Car
from classes.Machine import RightMachine
from utils.count import Count


'''#测试1
rightMachine = RightMachine(isMoving=False,pending=-1)
count = Count(rightCount=0,carListptr=0,time=10,returnTimes=0)
ansList=[]
carLines = np.full((10,10),-1,int)
carLines[3,0] = 0
reverseCarLines = np.full(10,-1,int)
car = Car(inOrder=0,
          carType='A',
          energyType='混动',
          energyNum='四驱',
          position=[3,0],
          arriveTime=-1,
          isMoving=False,
          pending=[[-1,-1],-1]
          )
targetPosition = 101
'''

rightMachine = RightMachine(isMoving=False,pending=-1)
count = Count(rightCount=0,carListptr=0,time=10,returnTimes=0)
ansList=[]
carLines = np.full((10,10),-1,int)
carLines[2,0] = 0
reverseCarLines = np.full(10,-1,int)
car = Car(inOrder=0,
          carType='A',
          energyType='混动',
          energyNum='四驱',
          position=[2,0],
          arriveTime=-1,
          isMoving=False,
          pending=[[-1,-1],-1]
          )
targetPosition = 6








#-----------------测试-------------------
rightMachine.dispatch(carLines,reverseCarLines,car,targetPosition, count,ansList)