import numpy as np

def randomSelect(carLines):
    ans = 0
    while(True):
        ans = np.random.randint(0, 6)
        if(carLines[ans,9] == -1):
            return ans

def opt1Rules(opt1,energyType):
    #  优化目标1 看能否加入 能的话就更新opt1返回True，否则返回False
    #  符合条件的

    # 每次调用的时候把开头为燃油的这种情形去掉

    if(len(opt1)>0 and opt1[0]!="混动" and "混动" in opt1):
        opt1 = opt1[opt1.index('混动'):]
    elif(len(opt1)>0 and opt1[0]!="混动"):
        opt1.clear()


    if(len(opt1)==0):
        opt1.append(energyType)
        return True

    if(energyType=='混动'):
        i = -1
        while(True):
            if(opt1[i]!='混动'):#一定能找到这个一开始的混动车型
                i-=1
            else:
                num = -i-1
                if(num!=2):
                    return False
                else:
                    opt1.append(energyType)
                    return True
    else:#eneryType为燃油
        i = -1
        while (True):
            if (opt1[i] != '混动'):  # 一定能找到这个一开始的混动车型
                i -= 1
            else:
                num = -i
                if (num > 2):
                    return False
                else:
                    opt1.append(energyType)
                    return True




def opt2Rules(opt2,energyNum):
    #  区别于opt1 opt2内我们留的是现存的还没分块好的序列
    #  根据我们的写法 不会出现2244新增2的情况 因为2244满足的时候会被移除
    num1 = opt2.count(energyNum)#四驱还是两驱
    num2 = len(opt2) - num1
    if(num2==0):
        opt2.append(energyNum)
        return True
    if(num1<num2):
        # 首先不可能22444的情况加2，所以
        if(num1+1==num2):
            opt2.clear()
            return True
        opt2.append(energyNum)
        return True
    if(num1>num2):
        # 首先不可能出现22444的情况加4 那么只可能出现44422的情况下加4 这种是false
        return False

def isThereAnswer(carLines,carList,opt1,opt2):
    temp1 = opt1
    temp2 = opt2
    for i in range(carLines.shape[0]):
        for j in range(carLines.shape[1]):

            if(opt1Rules(opt1,carList[carLines[i][j]])):#注意还原，我们上面两个rules都是会改变原来的
                opt1.clear()
                opt1.append(temp1)
                return True
            elif(opt2Rules(opt2,carList[carLines[i][j]])):
                opt2.clear()
                opt2.append(temp2)
                return True

def isTopAnswer(carLines,carList,opt1,opt2):
    temp1 = opt1
    temp2 = opt2
    for i in range(carLines.shape[0]):
        for j in range(carLines.shape[1]):
            if(carLines[i,j]!=-1):
                if(opt1Rules(opt1,carList[carLines[i][j]])):#注意还原，我们上面两个rules都是会改变原来的
                    opt1.clear()
                    opt1.append(temp1)
                    return True
                elif(opt2Rules(opt2,carList[carLines[i][j]])):
                    opt2.clear()
                    opt2.append(temp2)
                    return True
                break