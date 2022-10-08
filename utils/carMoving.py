def carMoving(carLines,reverseCarLines,carList,count):
    print("开始车辆的移动")
    for i in range(0, carLines.shape[0]):
        for j in range(0, carLines.shape[1] - 1):
            if (carLines[i][j] == -1 and carLines[i][j + 1] != -1 and carList[carLines[i][j + 1]].isMoving == False):
                carList[carLines[i][j + 1]].isMoving = True
                carList[carLines[i][j + 1]].pending = [[i, j], count.time + 9]

    for i in range(0, reverseCarLines.shape[0] - 1):  # 返回车道要倒着
        if (reverseCarLines[i + 1] == -1 and reverseCarLines[i] != -1 and carList[
            reverseCarLines[i]].isMoving == False):
            carList[reverseCarLines[i]].isMoving = True
            carList[reverseCarLines[i]].pending = [[6, i + 1], count.time + 9]
    print("移动车辆完成")