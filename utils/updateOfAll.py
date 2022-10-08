

def update(carList,carLines,reverseCarLines,ansList,leftMachine,rightMachine,count,opt1,opt2):
    for car in carList:

        if (car.isMoving and count.time == car.pending[1]):
            # 下面两种情况属于车的自动往前开 还要把原来的位置的标记改一下，注意position更新顺序
            if (car.position[0] >= 0 and car.position[0] < 6):
                carLines[car.position[0], car.position[1]] = -1
            if (car.position[0] == 6):
                reverseCarLines[car.position[1]] = -1  # 在reverseline上car.position是(6,xxx)
            if (car.pending[0] == [101, 101]):
                count.rightCount += 1
                ansList.append(car)
                opt1.append(car.energyType)
                opt2.append(car.energyNum)
            car.isMoving = False
            car.position = car.pending[0]
            if (car.pending[0][0] != 6 and car.pending[0][0] < 10):
                carLines[car.position[0], car.position[1]] = car.inOrder
            elif (car.pending[0][0] < 10):
                reverseCarLines[car.position[1]] = car.inOrder
            car.pending = [[-1, -1], -1]
            car.arriveTime = count.time

    if (count.time == leftMachine.pendingTime):
        leftMachine.isMoving = False  # 空闲
        leftMachine.pendingTime = -1
    if (count.time == rightMachine.pendingTime):
        rightMachine.isMoving = False
        rightMachine.pendingTime = -1

    print("状态更新完成")