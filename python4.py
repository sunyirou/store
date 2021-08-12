'''
    商城：
        1.初始化钱包余额
        2.推个空的购物车
        3.正常购物：
            输入商品的编号
            看是否有这个商品
                有：
                    看钱是否足够
                        够：
                            添加到购物车里
                            余额减去相对应的钱
                        不够：
                            温馨：穷鬼，别瞎弄！请买个其他商品
                没有：
                    买个其他商品，别瞎弄！
        4.打印购物小条
    任务：
        1.购物小条的商品重复打印问题
        2.  10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
            随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''
shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]
# 1.空的购物车
mycart = []

#  2.初始化您的余额
money = input("请输入您本月工资：")
money = int(money)

import random

# 3.正常购物
i = 1
while i <= 20:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)

    #是否随机抽取一张优惠券，10张联想电脑 0.5，20老干妈优惠券 0.1，15 华为优惠券 0.6
    free = input("是否要抽一张优惠券?Y/N：")
    if free == 'Y'or free == 'y':
        data = random.randint(0,5)#随机数方便获取抽奖信息
        a = 10#联想优惠券
        b = 20#老干妈优惠券
        c = 15#华为优惠券
        if data <=1 and a <= 10:#随机数0，1 联想
            print("恭喜获得lenovo PC 5折优惠券！")
        elif data >1 and data <= 3 and b <= 20:#随机数2，3 老干妈
            print("恭喜获得老干妈1折优惠券！")
        elif data >3 and c <= 15:#随机数4，5 华为
            print("恭喜获得HUAWEI  WATCH PRO 20 6折优惠券！")
        else:
            print("优惠券不足，抽奖失败！")
    else:#正常买东西
        pass

    #请输入您想要的商品
    chose = input("请输入您想要的商品：")
    if chose.isdigit():
        chose = int(chose)
        #判断是否存在该商品
        if chose > len(shop): # len
            print("没有该号商品！请重新输入！")
        else:
            # 钱够不够
            if money > shop[chose][1]:
                mycart.append(shop[chose])

                #优惠价格
                if free == 'Y' or free == 'y':  # 随机给一张，最终要进行使用优惠券的进行结算
                    if data <= 1 and a <= 10:  # 随机数0，1 联想5折
                        money = money - shop[chose][1]*0.5
                    elif data > 1 and data <= 3 and b <= 20:  # 随机数2，3 老干妈1折
                        money = money - shop[chose][1]*0.1
                    elif data > 3 and c <= 15:  # 随机数4，5 华为6折
                        money = money - shop[chose][1]*0.6
                    else:
                        print("没有优惠券，优惠失败！")
                else:
                    money = money - shop[chose][1] # 减去价格

                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("穷鬼，钱不够了，别瞎弄！买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("对不起，您输入错误，别瞎弄！")


    i = i + 1




count = []

for key,value  in enumerate(mycart): #统计每个商品在列表中出现几次
    if value in mycart[:key]:
        continue
    count.append(mycart.count(mycart[key]))

#删除二维列表这重复的行，必须先把列表中每个元素转化为tuple，因为list不可哈希但是tuple可哈希
mycart = list(set([tuple(t) for t in mycart]))

for k in mycart:    #tuple换回list
    mycart[mycart.index(k)] = list(k)

# 打印购物小条
print("以下是您的购物小条，请拿好！")
print("---------------------------------------")
for key,value  in enumerate(mycart):
     print(key,"------",value[0],"价格：￥",value[1],"数量",num)

print("---------------------------------------")
print("您的余额还剩：￥",money)


































