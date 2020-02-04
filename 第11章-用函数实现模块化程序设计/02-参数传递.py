# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/4   11:12
# 文件名称     ： 02-参数传递.PY
# 开发工具     ： PyCharm

# 定义函数
def demo( obj ):
    print( '原值：', obj )
    obj += obj

# 调用函数
print( '=========值传递=========' )
mot = '唯有在被追赶的时候，你才能真正地奔跑'
print( "函数调用前：", mot )
demo( mot )
print( '函数调用后：', mot )
print( '=========引用传递=========' )
list1 = [ '邓肯', '吉诺比利', '帕克' ]
print( '函数调用前：', list1 )
demo( list1 )
print( '函数调用后：', list1 )

# 可变参数

print( "---------- 分割线 ----------" )

## *parameter： 接受任意多个实际参数并将其放到一个元组中
def printplayer( *name ):
    print( '\n我喜欢的NBA球员有：' )
    for item in name:
        print( item )

printplayer( '邓肯' )
printplayer( '邓肯', '乔丹', '吉诺比利', '帕克' )
printplayer( '邓肯', '大卫罗宾逊' )

print( "---------- 分割线 ----------" )

## **parameter: 接受任意多个显示赋值的实际参数，并将其放到一个字典中。
def printsign( **sign ):
    print()
    for key, value in sign.items():
        print( '[' + key + ']的绰号是：' + value )

printsign( 邓肯 = '邓肯', 罗宾逊 = '罗宾逊' )
printsign( 吉诺比利 = '妖刀', 帕克 = '跑车', 鲍文 = '鲍三叔' )

dict1 = { '邓肯': '石佛', '罗宾逊': '海军上将', '吉诺比利': '妖刀' }
printsign( **dict1 )
