# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/3   10:53
# 文件名称     ： 01.PY
# 开发工具     ： PyCharm

# 字典的创建与删除
print( "---------- 分割线 ----------" )

dictionary = { "key1": 'value1', "key2": 'value2', "key3": 'value3' }
print( dictionary )

## 通过映射函数创建字典
print( "---------- 分割线 ----------" )
name = [ "邓肯", "吉诺比利", "帕克" ]
sign = [ "石佛", "妖刀", "跑车" ]
dictionary = dict( zip( name, sign ) )
print( dictionary )

## 通过给定的“关键字参数”创建字典
print( "---------- 分割线 ----------" )
dictionary = dict( 邓肯 = "石佛", 吉诺比利 = '妖刀', 帕克 = '跑车' )
print( dictionary )

### 使用fromkeys()方法创建值为空的字典
name_list = [ "邓肯", "吉诺比利", "帕克" ]
dictionary = dict.fromkeys( name_list )
print( dictionary )

### 使用元组和列表来创建字典
name_tuple = ("邓肯", "吉诺比利", "帕克")  # 作为键的元组
sign = [ "石佛", "妖刀", "跑车" ]
dict1 = { name_tuple: sign }
print( dict1 )

# 删除字典
print( "---------- 分割线 ----------" )
# del dictionary
# dictionary.clear()
# dict1.pop( name_tuple )
dict1.popitem()
print( dictionary )
print( dict1 )

# 通过键值访问字典
print( "---------- 分割线 ----------" )
print( "罗宾逊的绰号是：", dictionary[ '罗宾逊' ] if '罗宾逊' in dictionary else "我的字典里没有此人" )
print( '吉诺比利的绰号是：', dictionary.get( '吉诺比利' ) )
print( '罗宾逊的绰号是：', dictionary.get( '罗宾逊', "我的字典里没有此人" ) )

# 遍历字典
print( "---------- 分割线 ----------" )
dictionary = { 'qq': '84978981', '明日科技': '84978981', '无语': '0431-84978981' }
for item in dictionary.items():
    print( item )

for key, value in dictionary.items():
    print( key, '联系电话：', value )

# 添加、修改和删除字典
print( "---------- 分割线 ----------" )
dictionary = dict( (('邓肯', '石佛'), ('吉诺比利', '妖刀'), ('帕克', '跑车')) )
dictionary[ '罗宾逊' ] = '海上将军'
dictionary[ '帕克' ] = '法国跑车'
if '帕克' in dictionary:
    del dictionary[ '帕克' ]
print( dictionary )

# 字典推导式
import random

randomdict = { i: random.randint( 10, 100 ) for i in range( 1, 5 ) }
print( "生成的字典为：", randomdict )
