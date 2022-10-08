import numpy as np

def randomSelect(carLines):
    ans = 0
    while(True):
        ans = np.random.randint(0, 6)
        if(carLines[ans,9] == -1):
            return ans

def opt1Rules(opt1,energyType):
    #  优化目标1 看能否加入 能的话就返回True，否则返回False
    #  符合条件的

    # 每次调用的时候把开头为燃油的这种情形去掉
    temp = opt1[:]

    if(len(opt1)>0 and opt1[0]!="混动" and "混动" in opt1):
        opt1 = opt1[opt1.index('混动'):]
    elif(len(opt1)>0 and opt1[0]!="混动"):
        opt1.clear()


    if(len(opt1)==0):
        opt1.clear()
        opt1.extend(temp)
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
                    opt1.clear()
                    opt1.extend(temp)
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
                    opt1.clear()
                    opt1.extend(temp)
                    return True




def opt2Rules(opt2,energyNum):

    temp=opt2[:]#做个标记 下面把opt2切割成余块
    if(len(opt2)==0):
        return True

    if(opt2.count('两驱')==len(opt2) or opt2.count('四驱')==len(opt2)):#只有一种的 直接ok
        return True

    fg1=opt2[0]
    if(fg1=='四驱'):
        fg2 = '两驱'
    else:
        fg2='四驱'

    while(True):
        if((opt2.count('两驱')==len(opt2) or opt2.count('四驱')==len(opt2)) or isPair(opt2)):
            break
        opt2 = opt2[opt2.index(fg2):]
        opt2 = opt2[opt2.index(fg1):]#每次都切两刀

    #对切割后的对子做判断
    num1 = opt2[0]  # 四驱还是两驱
    if(num1=='四驱'):
        num2  = '两驱'
    else:
        num2 = '四驱'
    if (opt2.count(num1) < opt2.count(num2)):
        if (energyNum == num1):
            opt2.clear()
            opt2.extend(temp)
            return True
        else:
            opt2.clear()
            opt2.extend(temp)
            return False
    elif(opt2.count(num1) == opt2.count(num2)):
        if (energyNum == num1):
            opt2.clear()
            opt2.extend(temp)
            return True
        else:
            return False
    else:
        if(energyNum == num2):
            opt2.clear()
            opt2.extend(temp)
            return True
        else:
            return False
def isPair(opt2):
    #判断切下的序列是否为4422 22244这种不含波动的纯对子 222这种纯数字和长度为0的在opt2Rules里完成校验
    temp=opt2[:]
    fg1 = opt2[0]
    if(fg1=='两驱'):
        index = opt2.index('四驱')
        fg2='四驱'
    else:
        index = opt2.index('两驱')
        fg2 = '两驱'
    if(opt2[index:].count(fg2)==len(opt2[index:])):
        opt2.clear()
        opt2.extend(temp)
        return True
    else:
        opt2.clear()
        opt2.extend(temp)
        return False
def isThereAnswer(carLines,carList,opt1,opt2):

    for i in range(carLines.shape[0]):
        for j in range(carLines.shape[1]):
            if(carLines[i][j]!=-1 and opt1Rules(opt1,carList[carLines[i][j]].energyType)):#会触发-1语法糖
                return True
            elif(carLines[i][j]!=-1 and opt2Rules(opt2,carList[carLines[i][j]].energyNum)):
                return True

    return False
