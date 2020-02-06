# _*_ coding  : utf-8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/6   10:06
# 文件名称     ： 01.PY
# 开发工具     ： PyCharm

with open( 'message.txt', 'r' ) as file:
    file.seek( 14 )
    string = file.read( 8 )
    print( string )

# 按行读取文件
print( '=' * 20, '分割线', "=" * 20 )
print( '=' * 15, '开始读文件', "=" * 15, end = '\n' )
with open( 'message.txt', 'r' ) as file:
    number = 0
    while True:
        number += 1
        line = file.readline()
        if line == '':
            break
        print( number, line )
print( '=' * 15, '文件读取结束', "=" * 15, end = '\n' )

# 读取全部行
print( '=' * 20, '分割线', "=" * 20 )
print( '=' * 15, '开始读文件', "=" * 15, end = '\n' )
with open( 'message.txt', 'r' ) as file:
    message = file.readlines()
    print( message )
    print( '=' * 15, '文件读取结束', "=" * 15, end = '\n' )
