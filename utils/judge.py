from utils.commonUtils import randomSelect
from utils.commonUtils import opt1Rules,opt2Rules


def judgeLeft(reverseCarLines,carLines,leftMachine,carList,count,yangRunOuOrder):


    # 处理涂装 - PBS出车口上的车
    if(count.carListptr<len(carList)):
        car = carList[count.carListptr]
        if (carLines[yangRunOuOrder[count.carListptr], 9] != -1):
            # leftMachine.dispatch(carLines, reverseCarLines, car, randomSelect(carLines), count.time)
            print("序列被占用，左机器等待")
            return -1
        else:
            leftMachine.dispatch(carLines, reverseCarLines, car, yangRunOuOrder[count.carListptr], count.time)

        count.carListptr += 1
        # 返回车道10（index 9）有车 未必优先处理（这是第二题的分支）
    elif (reverseCarLines[9] != -1):
        car = carLines[reverseCarLines[9]]
        leftMachine.dispatch(carLines, reverseCarLines, car, randomSelect(carLines), count.time)

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
            rightMachine.dispatch(carLines, reverseCarLines, carList[carLines[i][0]], 101, count,ansList)
            break
    if(flag1==0):#没有满足条件1的
        for i in range(0, 6):
            if (carLines[i][0] != -1 and opt2Rules(opt2, carList[carLines[i][0]].energyNum)):
                flag2=0
                rightMachine.dispatch(carLines, reverseCarLines, carList[carLines[i][0]], 101, count,ansList)
                break
    if(flag1==0 and flag2==0):#没满足1也没满足2
        arr = []
        for i in range(0, 6):
            if (carLines[i][0] != -1):
                arr.append([carList[carLines[i][0]],carList[carLines[i][0]].arriveTime])
        if len(arr)!=0:
            min = arr[0][1]
            obj = None
            for ar in arr:
                if ar[1]<=min:
                    obj = ar[0]#最早到达的 carLines[i][0]=-1会触发语法糖问题
            rightMachine.dispatch(carLines, reverseCarLines, obj, 101, count,ansList)
