import numpy as np
from classes.Car import Car
from classes.Machine import LeftMachine


#测试1
leftMachine = LeftMachine(isMoving=False,pending=-1)
carLines = np.full((10,10),-1,int)
reverseCarLines = np.full(10,-1,int)
car = Car(inOrder=0,
          carType='A',
          energyType='混动',
          energyNum='四驱',
          position=[98,98],
          arriveTime=-1,
          isMoving=False,
          pending=[[-1,-1],-1]
          )
targetPosition = 3
curTime = 10


'''#测试2
leftMachine = LeftMachine(isMoving=False,pending=-1)
carLines = np.full((10,10),-1,int)
reverseCarLines = np.full(10,-1,int)
car = Car(inOrder=0,
          carType='A',
          energyType='混动',
          energyNum='四驱',
          position=[98,98],
          arriveTime=-1,
          isMoving=False,
          pending=[[-1,-1],-1]
          )
targetPosition = 2
curTime = 10
'''

'''#测试3
leftMachine = LeftMachine(isMoving=False,pending=-1)
carLines = np.full((10,10),-1,int)
reverseCarLines = np.full(10,-1,int)
reverseCarLines[9] = 0
car = Car(inOrder=0,
          carType='A',
          energyType='混动',
          energyNum='四驱',
          position=[6,9],
          arriveTime=-1,
          isMoving=False,
          pending=[[-1,-1],-1]
          )
targetPosition = 2
curTime = 10
'''


#-----------------测试-------------------
leftMachine.dispatch(carLines,reverseCarLines,car,targetPosition, curTime)