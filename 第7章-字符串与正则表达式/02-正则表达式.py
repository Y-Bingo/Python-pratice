# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/1   11:56
# 文件名称     ： 02.PY
# 开发工具     ： PyCharm

import re

pattern = r'mr_\w+'  # 模式字符串
string = '项目名称MR_SHOP mr_SHOP'
match = re.match( pattern, string, re.I )  # 匹配字符串，忽略大小写
print( match )
string = 'MR_SHOP mr_SHOP'  # 要匹配的字符串
match = re.match( pattern, string, re.I )  # 匹配字符串，忽略大小写
print( match )

print( "---------- 分割线 ----------" )

print( "匹配的起始位置：", match.start() )
print( "匹配的结束位置：", match.end() )
print( "匹配位置的元祖：", match.span() )
print( "匹配的字符串：", match.string )
print( "匹配的数据：", match.group() )

# 使用search() 方法进行匹配
# search 作用域整个字符串，搜索第一个匹配的值，返回match对象
print( "---------- 分割线 ----------" )
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.search( pattern, string, re.I )  # 搜索字符串，不区分大小
print( match )
string = '项目名称MR_SHOP mr_shop'
match = re.search( pattern, string, re.I )
print( match )

# 使用findall() 方法进行匹配
# findall 方法作用于整个字符串，搜索所有符合正则表达式的字符串，并以列表的形式返回
print( "---------- 分割线 ----------" )
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.findall( pattern, string, re.I )
print( match )
string = '项目名臣MR_SHOP mr_shop'
match = re.findall( pattern, string, re.I )
print( match )

print( "---------- 分割线 ----------" )
pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
string = '127.0.0.1 192.168.1.66'
match = re.findall( pattern, string )
for item in match:
    print( item, item[ 0 ] )

# 替换字符串
print( "---------- 分割线 ----------" )
pattern = r'1[34578]\d{9}'
string = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub( pattern, '1xxxxxxxxxx', string )
print( result )

# 使用正则表达式分割字符串
print( "---------- 分割线 ----------" )
pattern = r'[?|&]'
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split( pattern, url )
print( result )
