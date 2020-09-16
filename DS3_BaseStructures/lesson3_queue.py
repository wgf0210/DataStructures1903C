# 队列
'''
    什么是队列？
        队列是一系列有顺序的元素的集合，
        1. 新元素的加入在队列的一端，这一段叫做：“队尾”（rear）
        2. 已有元素的移除发生在队列的另一端，“队首”（front）
            rear              front
        3. 特点：FIFO先进先出（先到先服务）
    队列的抽象数据结构：
        Queue()创建一个空队列对象，不需要参数，返回空的队列
        enqueue()：加。将数据项添加到队尾，无返回值
        dequeue()：删。从队首移除数据项，不需要参数，返回值为队首数据项
        isEmpty()：测试队列是否为空，不需要参数，返回值为布尔值
        size()：返回队列中的数据项的个数，不需要参数
'''

'''
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.size())
print(q.dequeue())
'''

# 练习题
'''
    热土豆的儿童游戏（击鼓传花）：
        小孩们围成一个圈并以最快的速度接连传递物品，并在游戏的一个特定时间停止传递
        这时手中拿着物品的孩子就要离开圆圈，游戏进行至只剩一个小孩
'''
from pythonds.basic.queue import Queue
namelist = ['小明','小红','小绿','小蓝','小黑','小狗','小猫','小兔','小熊']
# rear 小熊 ....... 小明 front
q = Queue()
for name in namelist:
    q.enqueue(name)
while q.size() > 1:
    for i in range(7):
        q.enqueue(q.dequeue())
    q.dequeue()

'''
    打印机：
        平均每天任意 “一小时” 大约有 “10个学生” 在实验室中，在这一个小时中通常每人发起2次打印任务，
        每个打印任务的页数从1到20页不等。
        实验室中的打印机如果以草稿模式打印，每分钟可打印10页；
        如果以高品质模式打印，每分钟只能打5页。
        应采取哪种打印模式？
    分析：
        1.打印队列类PrintQueue，打印任务类PrintTask，打印机类Printer
        2.概率，1-20页 random
        3.一小时内 10*2 = 20次任务 ， 60/20 = 3分钟 = 180s。每180s产生一个任务
        4.每秒钟产生一个任务的概率是多少？ random(1,181)，如果产生的随机数是180，此时就产生了一个任务 180/180=1
    模拟过程：
        1.创建一个打印任务的队列，每个任务在生成的时候被赋予一个“时间戳”。队列在开始时是空的。
        2.对于每一秒钟  判断是否有新的任务产生：
        （1）有，把它加入到打印队列，并且把当前的秒作为其“时间戳”
        （2）无，打印机空闲状态，并且有任务正在等待队列中：
            1 从打印队列中移除一个打印任务并将其提交给打印机
            2 从当前秒中减去“时间戳”值，计算得到该任务的等待时间
            3 将该任务的等待时间添加到一个列表中，用于后续操作
            4 基于打印任务的页数，求出需要多长时间打印
        （3）打印机处于工作状态，打印机工作了当前1s；当前任务结束的时间-1s
        （4）正好上一个任务已打印完成，也就是剩余时间为0时，这时打印机进入空闲状态

    打印机类：检测是否正在执行打印任务。
        是，表明当前为工作状态，计算出需等待多长
        时间当前任务完成，任务完成将打印机设置为空闲状态
'''
import random
from pythonds.basic.queue import Queue
class Printer:
    def __init__(self,pagesPerMinute):
        self.pagerate = pagesPerMinute  # 打印速率
        self.currentTask = None  # 当前任务
        self.timeRemaining = 0  # 剩余多长时间完成当前任务
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    # 是否处于工作状态
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self,newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages()*60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    def getstamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    # 任务被加入打印机执行的时间 - 任务生成的时间 = 等待的时间
    def waitTime(self,currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1,61)
    if num == 60:
        return True
    else:
        return False

for i in range(10):
    pagesPerMinute = 10
    printer = Printer(pagesPerMinute)
    printQueue = Queue()
    # 计算平均等待时间，所以需将所有的等待时间进行存储
    waitingtimes = []
    # 模拟的是一小时当中的   60m=3600s
    for currentSecond in range(3600):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not printer.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            printer.startNext(nexttask)
        printer.tick()
    # 平均等待时间
    averageWatingTime = sum(waitingtimes)/len(waitingtimes)
    print('平均等待时间：%6.2f s，剩下%3d任务'%(averageWatingTime,printQueue.size()))










    

