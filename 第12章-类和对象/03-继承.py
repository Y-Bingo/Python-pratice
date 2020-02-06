# _*_ coding  : utf-8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/5   10:46
# 文件名称     ： 03-继承.PY
# 开发工具     ： PyCharm


class Fruit:
    color = '绿色'
    
    def __init__( self, color = '绿色' ):
        Fruit.color = color
    
    def harvest( self, color ):
        print( '水果是：' + color + '的！' )
        print( '水果已经收获....' )
        print( '水果原来是：' + Fruit.color + "的！" )

class Orange( Fruit ):
    color = "橙色"
    
    def __init__( self ):
        print( '\n我是橘子' )
    
    def harvest( self, color ):
        print( '橘子是：' + color + '的！' )
        print( '橘子已经别收获了...' )
        print( '橘子原来是：' + Fruit.color + '的！' )

class Apple( Fruit ):
    def __init__( self ):
        super().__init__()
        print( "我是苹果！" )

orange = Orange()
orange.harvest( "橙色" )

apple = Apple()
