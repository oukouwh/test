# json的读写操作
import json
import sys


def save_json(filename, dictObject): #json的写入操作
    flag = False
    if type(dictObject) != dict: # 判断传入类型是字典类型的数据
        return flag
    try:
        json_file = open(filename, 'w') # 以写入方式打开json文件
        json.dump(dictObject, json_file, ensure_ascii=False) # 以json格式写数据
        flag = True
    except:
        print('像%s写入出现异常，请重试'%(filename))
    finally:
        if flag:
            json_file.close()
        return flag

def get_josn(filename):
    flag = False
    dictObject = {}
    try:
        json_file = open(filename,'r')
        dictObject = json.load(json_file)
        flag = True
    except:
        print('从%s读取数据失败，请重试'%(filename))
    finally:
        if flag:
            json_file.close()
    return dictObject

json_data = {'111':'A','2222':'B','333':'C'}
filename = 'test.json'
file_success = save_json(filename,json_data)
if file_success:
    print('保存成功')
else:
    sys.exit()
d_json = get_josn(filename)
if d_json:
    print(d_json)
# 保存成功
# {'111': 'A', '2222': 'B', '333': 'C'}

