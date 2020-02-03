# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/3   10:37
# 文件名称     ： 01.PY
# 开发工具     ： PyCharm

print( "计算1+2+3+...+100的结果为：" )
result = 0
for i in range( 101 ):
    result += i
print( result )

print( "---------- 分割线 ----------" )
for i in range( 1, 10, 2 ):
    print( i, end = " " )

print( "---------- 分割线 ----------" )
string = "天道酬勤"
print( string )  # 横向显示
for ch in string:
    print( ch )  # 纵向显示

# while 循环
print( "---------- 分割线 ----------" )
i = 1
while i <= 3:
    print( "笑傲江湖" )
    i += 1
