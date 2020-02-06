# _*_ coding  : utf-8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/5   10:42
# 文件名称     ： 02-属性.PY
# 开发工具     ： PyCharm

class TVShow:
    """节目类"""
    
    def __init__( self, show ):
        self._show = show
    
    # @property 将一个方法转换为属性，且改属性为只读
    @property
    def show( self ):
        return self._show

tvShow = TVShow( "正在播放《战狼2》" )
print( '默认：', tvShow.show )
