# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/4   11:53
# 文件名称     ： 04-变量的作用域.PY
# 开发工具     ： PyCharm

# 全局变量
message = '唯有在被追赶的时候，你才能真正的奔跑。'

def f_demo1():
    print( '函数体内：全局变量message = ', message )

f_demo1()
print( '函数体外：全局变量message = ', message )

print( "---------- 分割线 ----------" )
print( '函数体外：全局变量message = ', message )

def f_demo2():
    message = '命运给予我们的不是失望之酒，而是机会之怀。'
    print( '函数体内：全局变量message = ', message )

f_demo2()
print( '函数体外：全局变量message = ', message )

print( "---------- 分割线 ----------" )
print( '函数体外：全局变量message = ', message )

def f_demo3():
    global message
    message = '命运给予我们的不是失望之酒，而是机会之怀。'
    print( '函数体内：全局变量message = ', message )

f_demo3()
print( '函数体外：全局变量message = ', message )
