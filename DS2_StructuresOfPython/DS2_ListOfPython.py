# python 数据结构的性能

import timeit
from timeit import Timer
'''
    my_list = [1,2,3,4,5,6,7]
    1. 索引和分派到一个索引位置这俩操作，无论列表有多大，操作花费的时间都相同,为O(1)
    2. 扩充列表：append(),时间复杂度也是O(1)
'''
'''
    # 1.列表创建
def test1():
    my_list = []
    for i in range(1000):
        my_list = my_list + [i]
def test2():
    my_list = []
    for i in range(1000):
        my_list.append(i)
def test3():
    my_list = [i for i in range(1000)]
def test4():
    my_list = list(range(1000))
t1 = Timer("test1()","from __main__ import test1")
t2 = Timer("test2()","from __main__ import test2")
t3 = Timer("test3()","from __main__ import test3")
t4 = Timer("test4()","from __main__ import test4")
print("test1连接",t1.timeit(number=1000),"秒")
print("test2 append 连接",t2.timeit(number=1000),"秒")
print("test3 列表推导式 连接",t3.timeit(number=1000),"秒")
print("test4 list.range 连接",t4.timeit(number=1000),"秒")
''' 

'''
    2. pop()（从列表最后删除一个元素）和pop(0)（删除列表第一个元素）
        pop()    O(1)
        pop(i)    O(n)

l = list(range(2000000))
pop_zero = Timer('l.pop(0)','from __main__ import l')
pop_end = Timer('l.pop()','from __main__ import l')
print('pop_zero',pop_zero.timeit(number=1000),'秒')
print('pop_end',pop_end.timeit(number=1000),'秒')
'''

'''
    3. insert(i,item) O(n)
        reverse       O(n)
        sort()        O(nlogn)

'''
l = list(range(2000000))
l_insert = Timer('l.insert(10,100)','from __main__ import l')
print('l_insesrt',l_insert.timeit(number=1000),'秒')




'''
    作业：验证列表的索引操作是O(1),将时间复杂度改成O(n)
        
'''
a = ['a','b','c','d','e','f']
print(a.index('b',0,4))




































