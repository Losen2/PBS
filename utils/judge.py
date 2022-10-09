from utils.commonUtils import randomSelect
from utils.commonUtils import opt1Rules,opt2Rules
from utils.commonUtils import isThereAnswer
import numpy as np

def judgeLeft(reverseCarLines,carLines,leftMachine,carList,count,yangRunOuOrder):

    # 返回车道10（index 9）有车 优先处理
    if (reverseCarLines[9] != -1):
        car = carList[reverseCarLines[9]]
        if (np.all(carLines[:, 9] != -1)):
            return -1
        elif(carLines[yangRunOuOrder[car.inOrder],9]==-1):
            # leftMachine.dispatch(carLines, reverseCarLines, car, yangRunOuOrder[car.inOrder], count.time)
            leftMachine.dispatch(carLines, reverseCarLines, car, randomSelect(carLines), count.time)
        else:
            return -1


    # 处理涂装 - PBS出车口上的车
    elif(count.carListptr<len(carList)):
        car = carList[count.carListptr]
        if (carLines[yangRunOuOrder[count.carListptr], 9] != -1):
            print("序列被占用，左机器等待")
            return -1
        else:
            leftMachine.dispatch(carLines, reverseCarLines, car, yangRunOuOrder[count.carListptr], count.time)

        count.carListptr += 1
    else:
        return -1



def judgeRight(reverseCarLines,carLines,rightMachine,carList,count,opt1,opt2,ansList):
    if(carLines[:,0].sum()==-6):
        print("右机器没有可以进行的操作 跳过")
        print(carLines)
        return -1
    flag1=0
    flag2=0
    for i in range(0, 6):
        if (carLines[i][0] != -1 and opt1Rules(opt1, carList[carLines[i][0]].energyType)):
            flag1=1

            rightMachine.dispatch(carLines, reverseCarLines, carList[carLines[i][0]], 101, count,ansList,opt1,opt2)
            break
    if(flag1==0):#没有满足条件1的
        for i in range(0, 6):
            if (carLines[i][0] != -1 and opt2Rules(opt2, carList[carLines[i][0]].energyNum)):
                flag2=1

                rightMachine.dispatch(carLines, reverseCarLines, carList[carLines[i][0]], 101, count,ansList,opt1,opt2)
                break
    if(flag1==0 and flag2==0):#没满足1也没满足2
        arr = []
        for i in range(0, 6):
            if (carLines[i][0] != -1):
                arr.append([carList[carLines[i][0]],carList[carLines[i][0]].arriveTime])
        #arr为1号位置为-1的车
        if len(arr)!=0:
            min = arr[0][1]
            obj = None
            for ar in arr:
                if ar[1]<=min:
                    obj = ar[0]#最早到达的 carLines[i][0]=-1会触发语法糖问题
            if(isThereAnswer(carLines,carList,opt1,opt2) and reverseCarLines[0]==-1):
                rightMachine.dispatch(carLines, reverseCarLines, obj, 6, count, ansList,opt1,opt2)
            else:
                rightMachine.dispatch(carLines, reverseCarLines, obj, 101, count,ansList,opt1,opt2)
