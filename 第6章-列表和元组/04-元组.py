# _*_ coding    : utf8 -*-
# _python_ 学习与练习
# 开发人员      ： YBingo
# 开发时间      ： 2020/1/23  22:47
# 文件名称      ： 04-元组.PY
# 开发工具      ： PyCharm

# 元组的定义
tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = "一", "二", "三", "四"
print( "元组的定义：", tuple1 )
print( "元组的定义：", tuple2 )

# 元组类型检测
print( "元组类型检测：", type( tuple1 ) )

# 创建空元祖
emptyTuple = ();

# 创建数值元组
print( "创建随机数元组：", tuple( range( 10, 20, 2 ) ) )

# 删除元组
# del tuple1
# print( "删除元组：", tuple1 )

# 访问元组元素
print( "访问元组元素：", tuple1[ 1 ] )
print( "切片式访问元组元素：", tuple1[ :2 ] )

# 修改元组元素
tuple1 = (5, 4, 3, 2, 1)
print( "新元组：", tuple1 )

# 元组推导式
import random
# 元组推导式生成的是一个生成器对象 需要用tuple来转换
randomNumber = tuple( random.randint( 10, 100 ) for i in range( 10 ) )
print( "生成的元组为:", randomNumber )
