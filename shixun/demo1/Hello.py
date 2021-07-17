# -*- codeing = utf-8 -*-
# @Time : 2021/7/7 15:47
# @Author : 胡振
# @File : Hello.py
# @Software: PyCharm

'''
这是我的第一个python程序
print("hello,python")
'''

'''
if True:
    print("我爱你")
else:
    print("我不爱你")
print("end")
'''

'''
import random  # 引入随机库
print("猜拳")
user = input("请输入数字(1.石头2.剪刀3.布)")
com = random.randint(1, 3)
while user != "1" or user != "2" or user != "3":
    print("请输入1-3的数字")
    user = input("请输入数字(1.石头2.剪刀3.布)")
    if user == "1" or user == "2" or user == "3":
        break
user = int(user)
if user == 1:
    if com == 1:
        print("都出石头,平局")
    elif com == 2:
        print("你出石头,电脑出剪刀,你赢了")
    elif com == 3:
        print("你出石头,电脑出布,你输了")
elif user == 2:
    if com == 1:
        print("你出剪刀,电脑出石头,你输了")
    elif com == 2:
        print("都出剪刀,平局")
    elif com == 3:
        print("你出剪刀,电脑出布,你赢了")
elif user == 3:
    if com == 1:
        print("你出布,电脑出石头,你赢了")
    elif com == 2:
        print("你出布,电脑出剪刀,你输了")
    elif com == 3:
        print("都出布,平局")
'''
'''
# 1-100求和
counter = 1
total = 0
x = 100
while counter <= x:
    total += counter
    counter += 1
print("1到%d的和为%d" % (x, total))
'''
'''
for i in range(1, 10, 1):
    for x in range(1, i + 1, 1):
        print("%d*%d=%d" % (x, i, i * x), end=" ")
    print(end="\n")
'''
'''
num = [1, 2, 3, 4, 5, 6]
nums = [1, 3]
#extend 加数据
#append 直接加整个类型
num.extend(nums)
print(num)
'''
'''
index = 0
print("----- 商品列表 -----")
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
for product in products:
    print(index,end=" ")
    for pro in product:
        print(pro,end=" ")
    print()
    index+=1
'''
'''
x = [1,3,4,5,6]
x.reverse() #降序
print(x)
'''

index = 0
money = 0
js = "q"
print("----- 商品列表 -----")
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
for product in products:
    print(index, end=" ")
    for pro in product:
        print(pro, end=" ")
    print()
    index += 1
while True:
    num = input("请选择要购买的商品序号(q结束)")
    if num == js:
        print("共消费%d元"%(money))
        break
    elif num != "q":
        if int(num) < len(products):
            print("%s成功添加至购物车" % (products[int(num)][0]))
            money += products[int(num)][1]
        else:
            print("不存在该商品")
            break
