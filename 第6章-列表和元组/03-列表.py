# _*_ coding    : utf8 -*-
# _python_ 学习与练习
# 开发人员      ： YBingo
# 开发时间      ： 2020/1/23  12:57
# 文件名称      ： 03.PY
# 开发工具      ： PyCharm

# 列表定义
listname = [ "element 1", "element 2", "element 3", "element 4" ]
print( "列表的定义：", listname )

# 创建空列表
emptyList = [ ];
print( "使用list函数来创建列表：", list( range( 10, 20, 1 ) ) )

# 删除列表
# del listname
# print( "删除列表：", listname )

# 编列列表
for item in listname:
    print( "编列列表：", item )

for index, item in enumerate( listname ):
    print( "输出元素与索引：", index, item )

# 添加元素
listname.append( "element 5" )
print( "添加元素：", listname )
listname.extend( [ "element 5", "element 6" ] )
print( "扩展列表：", listname )

# 修改元素
listname[ 2 ] = "element 33"
print( "修改元素：", listname )

# 删除元素
del listname[ -1 ]
print( "删除元素：", listname )
listname.remove( "element 5" )
print( "删除元素：", listname )

# 列表统计
print( "列表统计：", listname.count( "element 5" ) )

# 获取列表首次出现的下标 不存在的对象会抛出异常
print( "获取element 3的下表：", listname.index( "element 33" ) )

# 队列表进行排序
listname.sort( reverse = True )
print( "排序（倒序）：", listname )
listname.sort( key = str.lower )
print( "排序：", listname )

# 使用内置函数sorted排序    不改变原来列表
tempList = sorted( listname, reverse = True )
print( "使用内置sorted排序（倒序）：", tempList )
tempList = sorted( listname, key = str.lower )
print( "使用内置sorted排序：", tempList )

# 列表推导式
import random

## 生成指定范围的数值列表
randomNumber = [ random.randint( 10, 100 ) for i in range( 10 ) ]
print( "生成水机列表：", randomNumber )

## 根据列表生成指定需求的列表
price = [ 1200, 5300, 22988, 6200, 1998, 8888 ]
sale = [ int( x * 0.5 ) for x in price ]
print( "原价格：", price )
print( "打五折价格：", sale )

## 从列表中选择符合条件的元素组成新的列表
sale = [ x for x in price if x > 5000 ]
print( "价格高于5000：", sale )
