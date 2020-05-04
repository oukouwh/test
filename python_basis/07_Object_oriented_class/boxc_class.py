# 面向对象编程是一种对现实世界理解和抽象的方法。
# 把现实世界的任何事物当做一个独立的对象来看待
# 将现实世界的事物进行抽象，就会出现新的可以高效利用的数据类型--类
class Box(): # 定义类名
    # 求一个正方体体积的类
    def __init__(self,length1,width1,height1): # 传递类参数的保留函数
        self.length = length1 # 长
        self.width = width1 # 宽
        self.height = height1 # 高
    # 定义一个求体积的函数
    def volume(self):
        return self.length*self.width*self.height

my_class = Box(20,20,20)
print('立方体的体积等于%d'%(my_class.volume()))
# 立方体的体积等于8000

# class 关键字，所有的类名定义都是class开始。
# 类名Python语言建议类名首字母大写，只是为了容易阅读，做统一约定
# 类开始的第一行格式 class 类名():
# 类函数 类函数在类或者实例中又叫做方法(Method),方法必须依赖类或者实例而存在。上面的案例中有两个函数
# def __init__   def volume
# 保留函数__init__和self关键字
# 保留函数,就是不能用其他函数代替该函数，函数名的写法必须按照__init__格式输入
# 所有的类都需要先进行实例化，必须先在类中声明__init__函数，不然类的实例无法使用
# 类在实例化的同时，会自动调用__init__ 函数，所以可以通过他初始化属性值。

# 实例(Instance)是把类通过=赋值给一个变量的过程。就是实例化的过程，这个变量就是实例，实例的核心是由属性和方法组成
# my_class = Box(20,20,20) 就是建立类Box的一个实例对象过程，该过程又叫实例化过程。
# 多实例， 同一个类可以给多个实例对象赋值，那就是多个实例，每个实例之间互不干扰。
my_class1 = Box(10,10,20)
print('立方体的体积等于%d'%(my_class1.volume()))
# 立方体的体积等于2000
my_class2 = Box(30,10,20)
print('立方体的体积等于%d'%(my_class2.volume()))
# 立方体的体积等于6000

# 实例的属性，方法
# 实例通过 . 调用属性方法两个对象
# 实例名.属性名
len_test = my_class2.length
print(len_test) # 30
