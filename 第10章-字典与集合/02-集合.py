# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/3   12:10
# 文件名称     ： 02-集合.PY
# 开发工具     ： PyCharm

# 创建集合
set1 = { "石佛", "妖刀", "跑车" }
set2 = { 3, 1, 4, 5, 9, 2, 6 }
set3 = { 'python', ('人生苦短', '我用python'), 23 }
print( set1 )
print( set2 )
print( set3 )

## 使用setr()函数创建
## 创建空集合的时候，只能用set()来创建，因为“{}”表示的是一个空字典
print( "---------- 分割线 ----------" )
set1 = set( "命运给予我们的不是失望之酒，而是机会之杯" )
set2 = set( [ 1.234, 1.344, 3.2323, 322 ] )
set3 = set( ('人生苦短', '我用python') )
print( set1 )
print( set2 )
print( set3 )

# 集合的添加和删除
print( "---------- 分割线 ----------" )

## 向集合中添加元素
mr = set( [ '零基础学java', '零基础学Android', '零基础学C语言', '零基础学C#', '零基础学PHP' ] )
mr.add( '零基础学Python' )
print( mr )

## 从集合中删除元素
mr = set( [ '零基础学java', '零基础学Android', '零基础学C语言', '零基础学C#', '零基础学PHP', '零基础学Python' ] )
mr.remove( '零基础学Python' )
print( '使用remove()方法移除指定元素后：', mr )
mr.pop()
print( '使用pop()方法移除一个元素后：', mr )
mr.clear()
print( '使用clear()方法清空集合后：', mr )

# 集合的交集、并集和差集运算
print( "---------- 分割线 ----------" )
pf = set( [ '邓肯', '加内特', '马龙' ] )
print( '大前锋位置的球员有：', pf, '\n' )
cf = set( [ '邓肯', '奥尼尔', '姚明' ] )
print( '中锋位置的球员有：', cf, '\n' )
print( '交集运算：', pf & cf )
print( '并集运算：', pf | cf )
print( '差集运算：', pf - cf )
