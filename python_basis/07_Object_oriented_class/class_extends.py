# 类的继承
# 继承就是在继承原有类的功能基础上，增加新的功能(属性或者方法)，形成新的类叫做子类，被继承的类叫做父类
# 继承的格式 class 子类名(父类名)
# Python支持多继承，不推荐使用多继承
# 多继承的格式 class 子类名(父类1，父类2......)


class Box1():
    def __init__(self, length1, width1, height1):
        self.length = length1
        self.width = width1
        self.height = height1

    def volume(self):  # 求体积
        return self.length*self.width*self.height


class Box2(Box1):
    def __init__(self, length1, width1, height1):
        super().__init__(length1, width1, height1)
        self.color = 'red'  # 增加颜色属性
        self.material = 'paper'  # 增加类型属性
        self.num = '88'  # 增加编号属性

    def area(self):  # 增加求表面积的函数
        re = (self.length*self.width)+(self.width*self.height)+(self.length*self.height)
        return re*2
    # 创建box2的实例
box2 = Box2(10, 10, 10)

print('立方体的体积等于%d' % (box2.volume()))
print('立方体的面积等于%d' % (box2.area()))
print('立方体的颜色%s类型%s编号%s'%(box2.color, box2.material, box2.num))
# 立方体的体积等于1000
# 立方体的面积等于600
# 立方体的颜色red类型paper编号88