import numpy as np
import pandas as pd
from classes.Car import Car
from classes.Machine import LeftMachine,RightMachine
from utils.commonUtils import randomSelect
from utils.commonUtils import opt1Rules,opt2Rules
from utils.count import Count
from utils.judge import judgeLeft,judgeRight
import logging
from utils.updateOfAll import update
from utils.carMoving import carMoving
from utils.resultMap import resultMap
# logging.basicConfig(filename='example.log', level=logging.DEBUG)


yangRunOuOrder = np.random.randint(0, 6, (318,))  # 模拟杨润鸥给的序列
#为了统一起见 车从左边的进车顺序是[0,317] 车道顺序是[0,5] 一条车道的索引顺序为[0,9]
print("杨润鸥序列为")
print(yangRunOuOrder)


recordingFlag = False#输出结果的标志位 训练时请关闭
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

    # 生成题目所需要求的答案
    recordcsv = pd.DataFrame()

    while(count.rightCount < len(carList)):
        # if(count.time==20000):
        #     print("异常终止")
        #     break
        print("------------------------------------------------------------")
        print("当前时间是第{}秒".format(count.time),"开始进行本秒的循环测试")
        #  一、做isMoving状态的更新，两个machine+所有car
        print("开始做两个machine+所有car的状态的更新")
        update(carList, carLines, reverseCarLines, ansList, leftMachine, rightMachine, count)

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
        carMoving(carLines,reverseCarLines,carList,count)

        #最后时间变化
        count.time += 1
        print("本秒分配任务后carLines")
        print(carLines)
        print("本秒分配任务结束后reverseCarLines")
        print(reverseCarLines)
        print("到达右出口的car数量（从0起计）{}".format(count.rightCount))
        print("左边指针位置{}（最大{}，{}表示左边已经处理完）".format(count.carListptr,len(carList),len(carList)))
        print("-----------------------------------")
        #题目要求的输出
        if(recordingFlag):
            temp = []
            for car in carList:
                temp.append(resultMap[str(car.position)])
            recordcsv[count.time] = temp
    if (recordingFlag):
        recordcsv.to_csv("answerOfQues1.csv")


    return ansList,count


ans = getAns(yangRunOuOrder)