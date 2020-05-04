# 变量和函数私有化仅供自身访问private
class Private_Class():
    def __init__(self):
        self.hello = 'hello'

    def say(self):
        print(self.hello)

    def __say(self):
        print(self.hello)


show = Private_Class()
show.say()  # hello
