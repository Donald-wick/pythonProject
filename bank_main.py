# coding:utf-8


# 导入
import datetime
import csv
import pandas as pd
import bank_tooks as bt
import math


# 对user_name的资金进行存取操作
def funds_trade(user_name):
    # k=0
    with open('bank.csv', mode='r+', encoding='utf-8') as f1:
        next(f1)
        g = csv.reader(f1)
        final_list = list(g)
        length = int(len(final_list))
        # print(length)
    # df=pd.read_csv("bank.csv",encoding="utf-8")
    for item in range(0,length):
            with open('bank.csv', mode='r+', encoding='utf-8') as f2:
                # next(f2)
                f_b = csv.reader(f2)
                bank_list = list(f_b)
                length_bank = int(len(final_list))
                f2.close()
            year_money=0
            for k in range(0,length_bank+1):
                if bank_list[k][0]==user_name:
                    year_money=float(bank_list[k][3])
                    continue
            # print(year_money)
                # print("您的余额有{}\n".format(final_list[item][3]))
            saveMoney=int(input("请输入您存（+）取（-）的金额："))
            new_money=year_money+saveMoney
            print("数据更新成功！")
            # with open('userInfo.csv', mode='r+', encoding='utf-8') as f3:
            #     next(f3)
            #     f3 = csv.reader(f3)
            #     final_list = list(f3)
            #     length2 = int(len(final_list))
            # f3.close()
            time1_str =  datetime.datetime.today()
            with open('bank.csv', mode='a+', encoding='utf-8') as f4:
                f4.write('\n{},{},{},{}'.format(user_name, time1_str, saveMoney, new_money))
            print("数据保存成功！")
            if saveMoney>=0:
                print("您已成功存入{}元，当前余额：{}".format(saveMoney,new_money))
            else:
                print("您已成功取出{}元，当前余额：{}".format(math.fabs(saveMoney),new_money))
            yourChoice=int(input("继续存储请按【1】，返回主菜单请按【2】"))
            if yourChoice==1:
                # print(user_name)
                funds_trade(user_name)
            else:
                bt.show_menu(user_name)
            break



# 打印交易详情
def funds_print(user_name):
    csv_data=pd.read_csv('bank.csv',encoding="utf-8")
    # # print(csv_data["用户名"].loc[1])
    # for i in range(0,len(csv_data)):
    print(csv_data[(csv_data['用户名']==user_name)])

if __name__=="__main__":
    print("欢迎来到【银行资金管理系统】，请登录：")
    while(True):
        userChoice=int(input("直接登录请按【1】，注册请按【2】："))
        if userChoice==1:
            userName1=input("请输入用户名")
            bt.user_login(userName1)
            break
        elif userChoice==2:
            bt.user_register()
            userName2 = input("请输入用户名")
            bt.user_login(userName2)
            break
        else:
            print("请输入合理值！")
            continue