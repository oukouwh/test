# 多任务进程和线程简介
# 进程(Process).正在运行的一个独立的软件，在计算机内存中是一个软件的实例，是线程的容器
# 线程(Threading),线程有时候被称为轻量级的进程，是程序执行流的最小单元。线程是进程的一部分，进程可以包含多个线程
# 守护线程(Daemon Thread),运行在后台的一种特殊线程，独立于控制终端并且周期的执行某种任务或者等待处理发生的事件
# 多线程模块
# Python的多线程模块包括_thread, threading, queue等模块
# _thread模块，更加面向底层技术，不过现在已经被废弃
# threading模块
# threading取代了thread模块，提供了更多的线程相关功能
# threading模块中的一些函数
# active_count() 返回当前活动的线程对象的数量
# current_thread() 返回当前线程对象
# get_ident() 返回当前线程的id，是一个非零的正整数
# enumerate() 枚举函数，返货当前活动的所有线程对象(列表形式)
# main_thread() 返回主线程对象，在正常情况下，主线程是python解释器启动的线程
# settrace(func) 为从线程模块启动的所有线程设置跟踪功能func为自定的函数名
# setprofile(func) 为从线程模块启动的所有线程设置配置文件的功能，func参数为自定义的函数名
# stack_size([size]) 返回创建吸纳县城是使用的线程堆栈大小， size可选参数可以设置0~32768(32KB),范围的数值默认为0
# 常量
# threading提供TIMEOUT_MAX常量。
# Lock.acquire(),RLock.acquire(),Condition.wait()等方法超过这个常量限定的最大时间后，将跑出OverflowError异常错误信息
import threading
print(threading.active_count()) # 1
print(threading.enumerate()) # [<_MainThread(MainThread, started 3692)>]
print(threading.TIMEOUT_MAX) # 4294967.0
# 类，threading模块提供了Thread，Lock，RLock，Condition，Semaphore,Event等
# thread类 第一种:thread创建实例对象时，把func以参数的形式传递给构造函数。
# 第二种:通过集成Thread类，重写run()方法调用func函数，在thread的子类中，只允许对__init__()和run()方法进行重写
# thread类构造函数的调用形式
# Thread(group=None,target=None,name=None,args=(),kwargs={},*,daemon=None)
# group参数，用于保留。扩展功能，可以忽略该参数，或者设置为None
# target参数，设置线程需要执行的自定义函数func，target=func，设置完成后，被run()方法调用，target=None时，线程不执行任何动作
# name参数，指定需要执行的线程名称，
# args 参数当自定义函数fun带有参数是，把参数以元组的形式通过args传递给func
# kwargs参数，当自定义函数func带有参数是，把参数以字典形式通过kwargs传递给func
# daemon参数，当daemon不是None是，通过设置True或者False确定是否守护线程，当daemon=None时，守护线程属性将会继承父线程的状态(主线程默认情况下都是为非守护线程)
# 一旦一个线程对象呗创建，其活动必须通过调用线程的start()方法来启动，然后调用run()方法执行指定的用户自定义函数func join()方法在run()方法后执行
# 这会阻塞调用线程，知道调用join()方法的线程运行终止，才能执行后续程序代码
# Lock类
# Lock类对象是原始锁，提供低级别的同步
# 原始锁有锁定和解锁两种状态，对应两个基本操作方法acquire()和release()
# acquire()建立一个锁，建立成功返回一个True值，建立失败返回False
# release()释放一个锁
# RLock()类
# RLock类对象为可重复锁，可以被同一个线程多次获取，可以避免Lock多次锁定产生的死锁问题
# acquire()和release()同样提供锁定解锁的功能，与Lock的区别可以嵌套调用锁定和解锁方法
# Condition类
# Condition(条件变量)对象提供了对复杂线程同步问题的支持功能，除了提供解锁和锁定的功能外还提供wait()和notify()方法
