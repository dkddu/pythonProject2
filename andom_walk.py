from random import  choice

class RandomWalik:
    """一个生成随机漫步的属性"""

    def __init__(self,number_points=50):
        """初始化漫步的属性"""
        self.number_points = number_points

        #所有漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        #不断漫步,直到到达指定长度
        while len(self.x_values) < self.number_points:

            x_step = self.get_step()

            y_step = self.get_step()
            #拒绝原地踏步
            if x_step ==0 and y_step==0:
                continue
            #计算下一个点
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        wk_direction = choice([-1, 1])

        wk_distance = choice([0, 1, 2, 3, 4])
        wk_step = wk_direction * wk_distance
        return  wk_step