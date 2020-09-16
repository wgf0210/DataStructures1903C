import timeit
from timeit import Timer
'''
    2. 字典Dict
        除了复制和迭代是O(n)；
        其他 in、删除、访问 都是O(1)
        字典的包含关系始终比列表快

        字典里的方法：
            info={}
            添加：info['id'] = 1000
            修改：info['id'] = 2000
            删除：一个个删除del info['id']  |  删除整个字典 del info
            清空：info.clear()
            包含/遍历：for key in info.keys()
                  for value in info.values()
                  for item in info.items()
                  for key,value in info.items()
'''
info = {'name':"tzmm",'age':'30'}
def test_dict():
    for i in range(1001):
        for key,value in info.items():
            pass
t = Timer('test_dict()','from __main__ import test_dict')
print('test_dict',t.timeit(number=1000),'秒')

def test1():
    for i in range(1001):
        d = dict()
t1 = Timer('test1()','from __main__ import test1')
print('test1',t1.timeit(number=1000),'秒')











