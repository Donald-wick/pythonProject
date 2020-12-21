import csv
import bank_main as bm



# 打印出各个功能模块对应的数字
def show_menu(userName):
    print("---------------【银行资金管理系统】---------------")
    print("1:\t资金存入/取出")
    print("2:\t交易账单打印")
    print("3:\t退出系统")
    print("-----------------------------------------------")
    k=0
    showName=userName
    while k<3:
        userInputAct=int(input("请输入数字进行相关操作："))
        if userInputAct==1:
            bm.funds_trade(showName)
        elif userInputAct==2:
            bm.funds_print(showName)
        elif userInputAct==3:
            print("很高心您的使用，祝您生意兴隆！")
            break
        else:
            print("请您输入有效数字！")
        k+=1




# 通过userInfo参数传入用户注册信息进行登录
def user_login(userInfo):
    i = 0
    with open('userInfo.csv', mode='r+', encoding='utf-8') as f1:
        next(f1)
        f=csv.reader(f1)
        final_list=list(f)
        length = int(len(final_list))
        f1.close()
    k=1
    userName=""
    while i < 3:
        pwd = input('请输入你的密码：')
        for index in range(0,length) :
            if userInfo == final_list[index][0] and pwd==final_list[index][4]:
                k=1
                userName = userInfo
                break
            else:
                k=0
                if index==length-1:
                    break
        if k==1:
            print("登录成功")
            show_menu(userName)
            break
        else:
            print("登录失败请从新登录")
            i+=1


# 用于用户第一次使用系统时提供资金组测功能
def user_register():
    username = input('请输入你要注册的用户名：')
    password = input('请输入你要注册的密码：')
    with open('userInfo.csv', mode='a+', encoding='utf-8') as f:
        f.write('\n{},{},{},{},{}'.format(username,"","","",password))
    print('恭喜您，注册成功')
# user_register()
# user_login("wang")
