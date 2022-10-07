class Car:
    inOrder = -1  # 进车顺序1~318;
    carType = ''  # A B;
    energyType = ''  # 燃油 混动;
    energyNum = ''  # 四驱 两驱;
    position = [-1, -1]
    '''当前所在位置，(a, b)
    第几行第几列
    1 - 6 ；几个特殊的情景：
    // 在返回序列上，规定为(7, x)
    x~(1, 10);
    // 涂装 - PBS出车口：(98, 98)
    左边的口所有car一开始都堆在这里，但是要按顺序调用。这里对实际情况进行了抽象

    // PBS - 总装接车口：(101, 101)右边的口

    // 接车横移机：(99, 99)
    左边的机器

    // 送车横移机： (100, 100)
    右边的机器
    '''
    arriveTime = -1  # 到达此position的时间
    isMoving = False  # 此刻是否正在移动
    pending = [[-1, -1], -1]  # 第一个参数表示该车正在进行的移动位置，第二个参数表示该移动完成的时刻

    # 注意这里不要设置那种瞬间完成的任务，瞬间完成的任务直接更新，不要放在pending里面
    def __init__(self, inOrder, carType, energyType, energyNum, position, arriveTime ,isMoving, pending):
        self.inOrder = inOrder
        self.carType = carType
        self.energyType = energyType
        self.energyNum = energyNum
        self.position = position
        self.arriveTime = arriveTime
        self.isMoving = isMoving
        self.pending = pending



