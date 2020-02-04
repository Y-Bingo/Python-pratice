# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/4   11:58
# 文件名称     ： 05-匿名函数.PY
# 开发工具     ： PyCharm

import math

def circleArea( r ):
    result = math.pi * r * r
    return result

r = 10
print( '半径：', r, '的圆面积为：', circleArea( r ) )

# 使用lambda表达式
print( "---------- 分割线 ----------" )
r = 10
result = lambda r: math.pi * r * r
print( '半径：', r, '的圆面积为：', result( r ) )
