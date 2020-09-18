# 递归
'''
    什么是递归？
        递归是一种解决问题的方法。
        他把问题分解为越来越小的子问题，直到问题的规模小到可以被简单直接解决。
    特征：通常为了达到分解问题的效果，“递归过程要引入一个调用自身的函数”
    解决问题类型：

'''

'''
    使用递归 计算列表元素的和
'''
'''
    禁止使用while/for
    (((1+2)+3)+4)+5
    num_list[i]+num_list[i+1]
    list_num(num_list) = first(num_list)+listSum(rest(num_list))
'''
import time
# 递归
num_list = [x for x in range(1,501)]
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])
start_time1 = time.time()
for i in range(1001):
    list_sum(num_list)
end_time1 = time.time()
print('时间1：',end_time1-start_time1)

# 非递归
def list_sum2(num_list):
    the_num = 0
    for i in num_list:
        the_num += i
    return the_num
start_time2 = time.time()
for i in range(1001):
    list_sum2(num_list)
end_time2 = time.time()
print('时间2：',end_time2-start_time2)



'''
    递归的三大定律：
        1.递归算法必须有结束条件
        2.递归算法必须改变自己的状态，并向基本结束条件演进
        3.递归算法必须递归的调用自身
'''
'''
    计算某个数的阶乘   5！ = 1*2*3*4*5
'''
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(3))


'''
    将整数转换为任意进制表示的字符串形式
    十进制   二进制     八进制     十六进制
    7       0000011     7           7
    10      00001010    12          A
    0-9ABCDEF
'''
def to_str(n,base):
    convert_string = '0123456789ABCDEF'
    if n<base:
        return convert_string[n]
    else:
        return to_str(n//base,base)+convert_string[n%base]
print(to_str(7,2))



'''
    1. 写一个函数，接收一个字符串作为参数，并返回一个反向的新的字符串
    2. 使用递归判断回文字符串
'''
a = '王国芳'
def aa(a):
    b = []
    return a
print(aa(a))


'''
    汉诺塔问题：
        相传在古印度圣庙中，有一种被称为汉诺塔(Hanoi)的游戏。
        该游戏是在一块铜板装置上，有三根杆(编号A、B、C)，
        在A杆自下而上、由大到小按顺序放置64个金盘(如下图)。
        游戏的目标：
            把A杆上的金盘全部移到C杆上，并仍保持原有顺序叠好。
        操作规则：
             每次只能移动一个盘子，并且在移动过程中三根杆上都始终保持大盘在下，
            小盘在上，操作过程中盘子可以置于A、B、C任一杆上。

        1. 下图模型中，灰、黄、蓝三种颜色的收集装置各1个。
        灰、黄、蓝三种颜色的方形环各3个。方形环随机摆放在收集装置上。
        要求将方形环进行移动，通过最少次移动，使方形环颜色与收集装置颜色一致。
        每次可移动一个方形环。每个收集装置上面方形环的数量不超过5个。

    递归三要素
    1.最小条件：正确挪动一次盘子
    2.三个杆，每一次挪动的杆需挪动剩余63个。然后继续挪动1个。还剩62个，依次类推
    3.函数

    (1)以C盘为中介，从A杆将1至n-1号盘移至B杆；
    (2)将A杆中剩下的第n号盘移至C杆；
    (3)以A杆为中介；从B杆将1至n-1号盘移至C杆。
    height：表示塔还剩多少层
'''
def moveTower(height,fromPole,withPole,toPole):
    if height>1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
def moveDisk(fp,tp):
    print('移动盘子，从',fp,'到',tp)

from pythonds.basic.stack import Stack
A = Stack()
for i in range(1,4):
    A.push(i)
B = Stack()
for i in range(1,4):
    B.push(i)
C = Stack()
for i in range(1,4):
    C.push(i)

moveTower(3,A,B,C)









