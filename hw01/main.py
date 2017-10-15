class Shape(object):
    '''形状'''
    # 都有一个area方法
    # 这里用了属性装饰器
    # 下面继承的子类都overwrite了这个方法
    @property
    def area(self):
        pass
 
         
class Rectangle(Shape):
    '''矩形'''
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
         
    @property
    def area(self):
        return self.width * self.height
         
         
class Square(Rectangle):
    '''正方形'''
    def __init__(self, side=0):
        super().__init__(side, side)
