# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/5   9:58
# 文件名称     ： 01-面向对象.PY
# 开发工具     ： PyCharm

class Geese:
    """大雁类"""
    # 类属性
    neck = '脖子较长'
    wing = '振翅膀频率高'
    leg = '腿位于身份的中心支点，行走自如'
    
    def __init__( self, beak, wing, claw ):
        # 实例属性
        self.neck = '实例：脖子较长'
        self.wing = '实例：振翅膀频率高'
        self.leg = '实例：腿位于身份的中心支点，行走自如'
        print( "我是大雁类！" )
        print( Geese.neck )
        print( Geese.wing )
        print( Geese.leg )
        print( self.leg )
        print( self.wing )
        print( self.leg )

beak_1 = "喙的基部比较高，长度和头部的长度几乎相等"
wing_1 = '翅膀长而尖'
claw_1 = "爪子是蹼状的"
wildGoose = Geese( beak_1, wing_1, claw_1 )

# 访问限制
print( "---------- 分割线 ----------" )

class Swan:
    """天鹅类"""
    __neck_swan = '天鹅的脖子很长'
    
    def __init__( self ):
        print( "__init__():", Swan.__neck_swan )

swan = Swan()
swan._Swan__neck_swan = "23"
print( "加入类名：", swan._Swan__neck_swan )
print( '直接访问：', swan.__neck_swan )
