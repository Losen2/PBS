class Count:
    rightCount = 0  # 到达最右边的车辆个数
    carListptr = 0  # 左边的入口现在堆放的是第几辆车
    time = 0

    def __init__(self,rightCount,carListptr,time):
        self.rightCount = rightCount
        self.carListptr = carListptr
        self.time = time
