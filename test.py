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

opt1 = ['混动']
a = opt1Rules(opt1,"混动")