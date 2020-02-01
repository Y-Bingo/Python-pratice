# _python_ 学习与练习
#     作者： YBingo
# 开发时间： 2020/1/18   1:46
# 文件名称： 06.PY
# 开发工具： PyCharm

import datetime  # 调入时间模块

imyear = input( "请输入您的出身年份：" )  # 输入出生年份，必须4位数字的，如1981
nowyaer = datetime.datetime.now().year  # 计算当前年份
age = nowyaer - int( imyear )  # 用于计算实际年龄
print( "您的年龄为： " + str( age ) )  # 输出年龄

# 根据年龄判断所在的年龄阶段，判定标准是根据联合国组织给出的新年龄分段判定标准
if age < 18:
    print( "你现在为未成年人" )
if 18 <= age < 66:
    print( "你现在为青年人" )
if 66 <= age < 80:
    print( "你现在为中年人" )
if 80 <= age:
    print( "你现在为老年人" )
