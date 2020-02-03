# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/3   10:11
# 文件名称     ： 01.PY
# 开发工具     ： PyCharm

a = -9
b = a if a > 0 else -a
print( b )

# if...else
print( "---------- 分割线 ----------" )
number = 432678
print( "请输入你的6位奖票号码：", number )
if number == 432678:
    print( number, "恭喜你中奖了了！！！" )
else:
    print( number, "很遗憾， 你没有中奖！" )

# if...elif...else
print( "---------- 分割线 ----------" )
number = 490
print( "请输入商品7天销量：", number )
if number >= 1000:
    print( "销售量为A！" )
elif number >= 500:
    print( "销售量为：B！" )
elif number >= 300:
    print( "销售量为：C！" )
else:
    print( "销售量为：D！" )

# if 语句的嵌套
print( "---------- 分割线 ----------" )
number = 200
print( "请输入商品7天的销售量：", number )
if number >= 1000:
    print( "本商品7天销售量为A!" )
else:
    if number >= 500:
        print( "商品销售量为：B!!" )
    elif number >= 300:
        print( "商品销售量为：C！！" )
    else:
        print( "商品销售量为：D！！" )

# 使用and链接条件语句
print( "---------- 分割线 ----------" )
age = 33
print( "请输入您的年龄：", age )
if 18 <= age and age <= 70:
    print( "你可以申请小型汽车驾驶证!" )

# 使用or链接条件语句
print( "---------- 分割线 ----------" )
sales = 443
print( "请输入商品的销售量：", sales )
if sales < 10 or sales > 100:
    print( "该商品为重点关注商品" )

# 使用not关键字的选择语句
print( "---------- 分割线 ----------" )
data = None
if not data:
    print( "you lost" )
else:
    print( "you win！" )

print( "---------- 分割线 ----------" )
a = "6"
print( "请输入1位数字密码：", a )
b = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
if a not in b:
    print( "非法输入" )
