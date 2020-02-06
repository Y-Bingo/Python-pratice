# _*_ coding  : utf-8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/5   12:02
# 文件名称     ： main.PY
# 开发工具     ： PyCharm

import christmasTree

print( '全局变量：', christmasTree.pinetree )

# 引入自定义的包
print( "---------- 分割线 ----------" )

import setting.test

setting.test.func_test()

print( "---------- 分割线 ----------" )
import setting.size

if __name__ == "__main__":
    print( '宽度：', setting.size.width )
    print( '高度：', setting.size.height )

print( "---------- 分割线 ----------" )
from setting import size

if __name__ == "__main__":
    print( '宽度：', size.width )
    print( '高度：', size.height )

print( "---------- 分割线 ----------" )
from setting.size import width, height

if __name__ == "__main__":
    print( '宽度：', width )
    print( '高度：', height )
