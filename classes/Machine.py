#进车过程（左过程）时间 1-6车道
leftTime = [18, 12, 6, 0, 12, 18]
#出车过程（右过程）时间 1-6车道
rightTime = [18, 12, 6, 0, 12, 18]
#左机械把返回道的car运出去的时间
returnOutTime = [24, 18, 12, 6, 12, 18]
#右机械把car运到返回道的时间
returnInTime = [24, 18, 12, 6, 12, 18]

class leftMachine:
    # 接车横移机
    isMoving = False  # 此刻是否正在移动

    pendingTime = -1  # 表示什么时候做完本次任务。注意这里不要设置那种瞬间完成的任务，瞬间完成的任务直接更新，不要放在pending里面

    def __init__(self, isMoving, pending):
        self.isMoving = isMoving
        self.pendingTime = pending

    def dispatch(self,carLines,reverseCarLines,car,targetPosition, curTime):
        #左机器调度操作，即接车横移机
        # 将当前涂装-PBS出车口队列第一个车身
        # 或者返回道10停车位的车身送入任意进车道的10停车位,
        #targetPostion=7表示调度返回车道上的10位的车
        # 在这里面要把该改变的属性全改变了比如carLines，reverseCarLines，car自身的属性，leftMachine的自身属性都要更新
        # targetPosition 整数，表示第几行
        #
        #被移动的位置如果是4(索引为3)的话需要立即更新，否则更新pending

        # 移动左边涂装-PBS出车口队列第一个车身
        if(car.position == [98,98]):
            if(targetPosition == 3):
                #调度的时候机器必然是空闲的所以isMoving不用恢复空闲,car.isMoving同理
                carLines[3,9] = car.inOrder
                car.position = [3,9]


            else:
                #在被调度的过程中算是在左机器上 position到了还是要更新
                car.position = [99,99]
                car.pending = [[targetPosition, 9], curTime + leftTime[targetPosition]]
                car.isMoving = True
                self.isMoving = True
                self.pendingTime = curTime + leftTime[targetPosition]


        # 返回车道
        elif(car.position==[6,9]):
            reverseCarLines[9] = -1
            car.position = [99, 99]
            car.pending = [[targetPosition, 9], curTime + returnOutTime[targetPosition]]
            car.isMoving = True
            self.isMoving = True
            self.pendingTime = curTime + returnOutTime[targetPosition]




class rightMachine:
    # 送车横移机
    isMoving = False  # 此刻是否正在移动

    pendingTime = -1  # 表示什么时候做完本次任务。注意这里不要设置那种瞬间完成的任务，瞬间完成的任务直接更新，不要放在pending里面

    def __init__(self, isMoving, pending):
        self.isMoving = isMoving
        self.pendingTime = pending

    #  将任意进车道1停车位的车送入返回道1停车位或者PBS-总装接车口。
    def dispatch(self,carLines,reverseCarLines,car,targetPosition, count):
        #  送入返回道1停车位
        if(targetPosition == 6):
            carLines[car.position[0],car.position[1]] = -1
            car.isMoving = True
            car.pending = [[targetPosition,0], count.time +returnInTime[car.position[0]]]#注意顺序
            self.pendingTime = count.time+returnInTime[car.position[0]]
            car.position = [100,100]
            self.isMoving = True

        #  送入总装接口
        elif(targetPosition == 101):
            if(car.position[0]==3):
                carLines[3, 0] = -1
                car.position = [101,101]
                count.rightCount+=1

            else:
                # 在被调度的过程中算是在右机器上 position到了还是要更新

                carLines[car.position[0], car.position[1]] = -1
                car.pending = [[101, 101], count.time + rightTime[car.position[0]]]
                car.isMoving = True
                self.isMoving = True
                self.pendingTime = count.time + rightTime[car.position[0]]
                car.position = [100, 100]




