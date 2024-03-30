from random import randint

class Die:
    """表示一个骰子的类"""
    def __init__(self,num_face_size = 6):
        """骰子默认为六面"""
        self.num_face_size = num_face_size


    def roll(self):
        """返回一到六之间的随机值"""
        return randint(1,self.num_face_size)