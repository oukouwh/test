# os模块
import os 
print(os.environ)
print(os.getcwd())  # c:\py_vscod 返回当前工作路径的字符串
print(os.system('ping 127.0.0.1')) # 0
# 返回一串适合加密使用的n字节大小的随机字符串
print(os.urandom(6)) # b' \x82\xa6\x9b\x19S'

