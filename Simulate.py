import numpy as np
import pandas as pd
from classes.Car import Car
from classes.Machine import leftMachine,rightMachine
from utils.commonUtils import randomSelect
from utils.commonUtils import opt1Rules,opt2Rules
from utils.count import Count
from utils.judge import judgeLeft,judgeRight



yangRunOuOrder = np.random.randint(0, 6, (318,))  # 模拟杨润鸥给的序列
#为了统一起见 车从左边的进车顺序是[0,317] 车道顺序是[0,5] 一条车道的索引顺序为[0,9]

# 初始化成car实例放在list里，初始位置(98, 98)
carList = []
data = pd.read_csv('question1.csv')

for i in range(0, 318):
    car = Car(inOrder=i,
              carType=data['车型'][i],
              energyType=data['动力'][i],
              energyNum=data['驱动'][i],
              position=[98, 98],
              arriveTime=0,
              isMoving=False,
              pending=[[-1, -1], -1],
              )
    carList.append(car)

#  模拟场地，注意-1表示空位置 其他数字表示车的索引
carLines = np.full((6,10),-1, dtype=int)
reverseCarLines = np.full(10, -1, dtype=int)

#  模拟左右机械,left是接车机 right送车机
leftMachine = leftMachine(isMoving=False, pending=-1)
rightMachine = rightMachine(isMoving=False, pending=-1)


#   时间大循环


count = Count(rightCount=0,carListptr=0,time=0)

opt1 = []
opt2 = []

while(count.rightCount == len(carList)-1):
    #  一、做isMoving状态的更新，两个machine+318个car
    for car in carList:

        if(car.isMoving and count.time==car.pending[1]):
            # 下面两种情况属于车的自动往前开 还要把原来的位置的标记改一下，注意position更新顺序
            if (car.position[0] >= 0 and car.position[0] < 6):
                carLines[car.position[0], car.position[1]] = -1
            if (car.position[0] == 6):
                reverseCarLines[car.position[1]] = -1#在reverseline上car.position是(6,xxx)
            if(car.pending[0]==[101,101]):
                count.rightCount+=1
            car.isMoving = False
            car.position = car.pending[0]
            car.pending = [[-1,-1],-1]
            car.arriveTime = count.time

    if(count.time == leftMachine.pendingTime):
        leftMachine.isMoving = False#空闲
        leftMachine.pendingTime = -1
    if(count.time == rightMachine.pendingTime):
        rightMachine.isMoving = False
        rightMachine.pendingTime = -1



    #  二、检查左机器是否空闲并决定是否分配任务
    while(not leftMachine.isMoving):
        #  之所以用while就是有干完事需要0s立马去干另外一个事情的情景
        judgeLeft(reverseCarLines,carLines,leftMachine,carList,count,yangRunOuOrder)









    #  三、检查右机器是否空闲并分配任务（瞬间空闲（指本循环开始时置的空闲）！= 送车机闲置）
    while(not rightMachine.isMoving):
        judgeRight(reverseCarLines,carLines,rightMachine,carList,count,opt1,opt2)










    #  四、检查所有车辆并按规则移动
    for i in range(0,carLines.shape[0]):
        for j in range(0,carLines.shape[1]-1):
            if(carLines[i][j]==-1 and carLines[i][j+1]!=-1):
                carList[carLines[i][j+1]].isMoving = True
                carList[carLines[i][j+1]].pending = [[i,j], count.time+9]

    for i in range(0, reverseCarLines.shape[0]-1):#返回车道要倒着
        if(reverseCarLines[i+1]==-1 and reverseCarLines[i]!=-1):
            carList[reverseCarLines[i]].isMoving = True
            carList[reverseCarLines[i]].pending = [[6,i+1],count.time+9]

    #最后时间变化
    count.time += 1