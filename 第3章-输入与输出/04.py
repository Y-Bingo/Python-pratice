# _python_ 学习与练习
#     作者： YBingo
# 开发时间： 2020/1/18   1:37
# 文件名称： 04.PY
# 开发工具： PyCharm

import datetime  # 调用模块

print( "当年年份：" + str( datetime.datetime.now().year ) )  # 输出当前年份，当前为2020，输出2020
# 输出当前日期和时间，如 2018-11-20 15:30:23 注意代码中单引号、字母大小写，不能写错
print( '当前日期：' + datetime.datetime.now().strftime( '%Y-%m-%d %H:%M:%S' ) )
