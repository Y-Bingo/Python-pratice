# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/4   10:34
# 文件名称     ： 01-函数的创建和调动.PY
# 开发工具     ： PyCharm

def fun_bmi( person, height, weight ):
    """功能: 根据身高和体重计算BMI指数
    :param person: 姓名
    :param height: 身高，单位：米
    :param weight: 体重，单位，千克
    :return:
    """
    print( person + '的身高：', str( height ) + '米\t 体重：' + str( weight ) + '千克' )
    bmi = weight / (height * height)
    print( person + '的BIM指数为：' + str( bmi ) )
    # 判断身材是否合理
    if bmi < 18.5:
        print( '您的体重过轻 ~@_@~' )
    if 18.5 <= bmi <= 24.9:
        print( '正常范围： 注意保持' )
    if 24.9 <= bmi <= 29.9:
        print( '你的体重过重！' )
    if 29.9 <= bmi:
        print( '肥胖！' )

fun_bmi( '匿名', 1.76, 50 )

fun_bmi( height = 1.83, person = '路人甲', weight = 60 )
# pass空语句
print( "---------- 分割线 ----------" )

def func():
    pass

def func():
    ...
