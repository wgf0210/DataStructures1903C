# 链表
'''
    有序列表和无序列表：
        1.由计算机中的存储位置来区分的。
            有序列表存储在一块连续的内存中,升序 降序
            无需列表存储在不连续的内存中
'''
'''           
    无序列表：

    自己实现列表
    list unorderedlist  无序列表 的ADT

    unorderedlist的抽象数据类型(ADT)：
        list() 创建一个空列表
        add(item)  将新项添加到列表，无返回值，假设元素不在列表中
        remove(item)  从列表中删除元素，需要一个参数，会修改列表，假设元素在列表中
        search(item)  搜索列表中的元素，需要一个参数，返回一个布尔值
        isEmpty()  判断是否为空，无参数，返回布尔值
        size()  返回列表的元素数，无参数，返回一个整数
        append(item)  在列表末端添加一个新的元素。需要一个参数，无返回值
        index(item)  返回元素在列表中的位置，需要一个参数，返回位置索引值
        insert(pos,item)  在指定的位置插入一个新的元素，需要俩参数，无返回值
        pop()  从列表末端移除一个元素并且返回它，无参数。假设列表中至少有一个元素
        pop(pos)   从指定的位置移除一个元素并返回它。需要一个位置参数，返回一个元素
    
    1.使用链表实现无序列表
        54,26,93,17,77,31
        该列表第一箱的位置必须被明确指出
        最后一项告诉我们没有下一个项目了
        链表概念：节点Node，
            每一节点中 存储着两条信息：当前节点的值（数据区）和 下一个节点的地址（/引用）
        Node(节点类)：
            访问和修改节点值和下一个节点引用的方法
'''
class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None
    def getData(self):
        return self.data
    def setData(self,newData):
        self.data = newData
    def getNext(self):
        return self.next
    def setNext(self,newNext):
        self.next = newNext
headFirst = Node(54)
print(headFirst.getData())   #54


class Unorderedlist:
    def __init__(self):
        self.head = None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def isEmpty(self):
        return self.head == None
    def size(self):
        currentHead = self.head
        count = 0
        while currentHead != None:
            count += 1
            currentHead = currentHead.getNext()
        return count
    def search(self,item):
        currentHead = self.head
        flag = False
        while not flag and currentHead != None:
            if currentHead.getData() == item:
                flag = True
            else:
                currentHead = currentHead.getNext()
        return flag
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

mylist = Unorderedlist()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print(mylist.size())
print(mylist.search(31))
mylist.remove(31)
print(mylist.size())



'''
    有序列表：  orderlist
    17,26,31,54,77,93 升序
    93,77,54,31,26,17 降序
    OrderedList()
    add(item)
    remove(item)
    search(item)
    isEmpty()
    size()
    index(item)
    pop()
    pop(pos)
'''
# head 头指针，指向None，表示一个空列表
# 升序的列表
class OrderedList:
    def __init__(self):
        self.head = None
    def size(self):
        current = self.head 
        count = 0
        while current != None:
            count += 1
            current.getNext()
        return count
    def isEmpty(self):
        return self.head == None
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data()>item:
                    stop = True
                else:
                    current = current.get_next()
        return found 

    

















