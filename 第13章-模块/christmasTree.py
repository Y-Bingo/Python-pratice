# _*_ coding  : utf-8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/5   11:57
# 文件名称     ： christmasTree.PY
# 开发工具     ： PyCharm

pinetree = '我是一棵树'  # 定义一个全局变量

def fun_christmastree():
    """
        功能：一个梦
    :return: None
    """
    pinetree = '挂上彩灯，彩礼...我变成一颗圣诞树 @@@@~\n'
    print( pinetree )

# ****************************** 函数体外 ****************************** #
if __name__ == '__main__':
    print( '\n 下雪了....\n' )
    print( '================== 开始做梦了 ==================' )
    fun_christmastree()
    print( '================== 梦醒了... ==================' )
    pinetree = '我身上落满了雪花' + pinetree + '-_-'
    print( pinetree )
