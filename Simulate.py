import numpy as np
import pandas as pd
from classes.Car import Car
from classes.Machine import LeftMachine,RightMachine
from utils.commonUtils import randomSelect
from utils.commonUtils import opt1Rules,opt2Rules
from utils.count import Count
from utils.judge import judgeLeft,judgeRight
import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)


yangRunOuOrder = np.random.randint(0, 6, (318,))  # 模拟杨润鸥给的序列
#为了统一起见 车从左边的进车顺序是[0,317] 车道顺序是[0,5] 一条车道的索引顺序为[0,9]
print("杨润鸥序列为")
print(yangRunOuOrder)



def getAns(yangRunOuOrder):
    # 初始化成car实例放在list里，初始位置(98, 98)
    carList = []
    data = pd.read_csv('question1.csv')
    ansList = []

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
    print("carLines初始化完成")
    reverseCarLines = np.full(10, -1, dtype=int)
    print("reverseCarLines初始化完成")
    #  模拟左右机械,left是接车机 right送车机
    leftMachine = LeftMachine(isMoving=False, pending=-1)
    print("leftMachine初始化完成")
    rightMachine = RightMachine(isMoving=False, pending=-1)
    print("rightMachine初始化完成")

    #   时间大循环


    count = Count(rightCount=0,carListptr=0,time=0,returnTimes = 0)
    print("计数器初始化完成")
    opt1 = []
    opt2 = []
    print("opt1 opt2初始化完成")

    while(count.rightCount != len(carList)-1):
        if(count.time==20000):
            print("异常终止")
            break
        print("------------------------------------------------------------")
        print("当前时间是第{}秒".format(count.time),"开始进行本秒的循环测试")
        #  一、做isMoving状态的更新，两个machine+所有car
        print("开始做两个machine+所有car的状态的更新")
        for car in carList:

            if(car.isMoving and count.time==car.pending[1]):
                # 下面两种情况属于车的自动往前开 还要把原来的位置的标记改一下，注意position更新顺序
                if (car.position[0] >= 0 and car.position[0] < 6):
                    carLines[car.position[0], car.position[1]] = -1
                if (car.position[0] == 6):
                    reverseCarLines[car.position[1]] = -1#在reverseline上car.position是(6,xxx)
                if(car.pending[0]==[101,101]):
                    count.rightCount+=1
                    ansList.append(car)
                car.isMoving = False
                car.position = car.pending[0]
                if(car.pending[0][0]!=6 and car.pending[0][0]<10):
                    carLines[car.position[0],car.position[1]] = car.inOrder
                elif(car.pending[0][0]<10):
                    reverseCarLines[car.position[1]] = car.inOrder
                car.pending = [[-1,-1],-1]
                car.arriveTime = count.time

        if(count.time == leftMachine.pendingTime):
            leftMachine.isMoving = False#空闲
            leftMachine.pendingTime = -1
        if(count.time == rightMachine.pendingTime):
            rightMachine.isMoving = False
            rightMachine.pendingTime = -1

        print("状态更新完成")

        #  二、检查左机器是否空闲并决定是否分配任务
        print("开始为左机器分配任务")
        while(not leftMachine.isMoving):
            #  之所以用while就是有干完事需要0s立马去干另外一个事情的情景
            ans = judgeLeft(reverseCarLines,carLines,leftMachine,carList,count,yangRunOuOrder)
            if (ans == -1):
                break
        print("左机器分配任务完成")







        #  三、检查右机器是否空闲并分配任务（瞬间空闲（指本循环开始时置的空闲）！= 送车机闲置）
        print("开始为右机器分配任务")

        while(not rightMachine.isMoving):
            ans = judgeRight(reverseCarLines,carLines,rightMachine,carList,count,opt1,opt2,ansList)
            if(ans==-1):
                break
        print("右机器分配任务完成")








        #  四、检查所有车辆并按规则移动
        print("开始车辆的移动")
        for i in range(0,carLines.shape[0]):
            for j in range(0,carLines.shape[1]-1):
                if(carLines[i][j]==-1 and carLines[i][j+1]!=-1 and carList[carLines[i][j+1]].isMoving == False):
                    carList[carLines[i][j+1]].isMoving = True
                    carList[carLines[i][j+1]].pending = [[i,j], count.time+9]

        for i in range(0, reverseCarLines.shape[0]-1):#返回车道要倒着
            if(reverseCarLines[i+1]==-1 and reverseCarLines[i]!=-1 and carList[reverseCarLines[i]].isMoving == False):
                carList[reverseCarLines[i]].isMoving = True
                carList[reverseCarLines[i]].pending = [[6,i+1],count.time+9]
        print("移动车辆完成")
        #最后时间变化
        count.time += 1
        print("本秒分配任务后carLines")
        print(carLines)
        print("本秒分配任务结束后reverseCarLines")
        print(reverseCarLines)
        print("到达右出口的car数量（从0起计）{}".format(count.rightCount))
        print("左边指针位置{}（最大{}，{}表示左边已经处理完）".format(count.carListptr,len(carList),len(carList)))
        print("-----------------------------------")
    return ansList,count


ans = getAns(yangRunOuOrder)