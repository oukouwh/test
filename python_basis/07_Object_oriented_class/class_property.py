# 属性(Property)是通过__init__函数定义，并通过self传递给实例的一种数据类型。
# 属性值的初始化
# 在__init__里直接初始化值
class Box():
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
T1 = Box()
print(T1.length) # 0


# 传递参数初始化
class Box2():
    def __init__(self,length1,width1,height1):
        self.length = length1
        self.width = width1
        self.height = height1

T2 = Box2(12,13,15)
print(T2.length) # 12
# 属性值的修改
# 直接对属性值进行修改
class Box3():
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
T3 = Box3()
print(T3.length) # 0
T3.length = 99
print('修改后的属性值%d'%(T3.length)) # 修改后的属性值99

# 通过方法对属性值进行修改
class Box4():
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
    def property_update(self,length1):
        self.length = length1

T4 = Box4()
T4.property_update(45)
print('通过方法赋值之后属性值%d'%(T4.length))
# 通过方法赋值之后属性值45

# 把类赋值给属性
class Color():
    def __init__(self,index=0):
        self.set_color = ['red','black','green','white']
        self.index = index
    def setColor(self):
        return self.set_color[self.index]

class Box5():
    def __init__(self,length2,width2,height2,cl=0):
        self.length = length2
        self.width = width2
        self.height = height2
        self.color = Color(cl).setColor()
    def volume(self):
        return self.length*self.width*self.height

my_Box5 = Box5(10,20,30,1)
print(my_Box5.color) # black

     
