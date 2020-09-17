# 双端队列
''' 
    栈：    后进先出。例：垒书。     顶（进/出）    底  append pop
    队列：  先进先出。例：排队打饭。 rear（队尾进） front（队首出）
  双端队列：两端都成为队首front和队尾rear，元素可以从两端插入，也可以从两端删除
        rear    front
    Deque() 创建一个空的双端队列，无参数，返回值为Deque对象
    addFront() 在队首插入一个元素，无返回值
    addRear()  在队尾插入一个元素，无返回值
    removeFront() 在队首移除一个元素，返回值为移除的元素
    removeRear()  在队首移除一个元素，返回值为移除的元素
    size()  返回双端队列中数据项的个数，返回值为整数类型
    isEmpty()  判断双端队列是否为空，返回布尔值
'''
'''
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
d = Deque()
d.addRear(1)
d.addRear(2)
d.addFront(3)
d.addFront(4)
print(d.isEmpty())
print(d.size())
print(d.removeFront())
print(d.removeRear())
'''


'''
    验证回文词
    reer   toot   madam   上海自来水来自海上
'''
from pythonds.basic.deque import Deque
str1 = '上海自来水来自海上'
def palChecker(str1):
    flag = True
    charDeque = Deque()
    for ch in str1:
        charDeque.addRear(ch)
    while charDeque.size() > 1 and flag==True:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            flag = False
    return flag
print(palChecker(str1))











