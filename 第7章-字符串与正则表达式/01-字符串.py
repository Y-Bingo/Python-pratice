# _*_ coding    : utf8 -*-
# _python_ 学习与练习
# 开发人员      ： YBingo
# 开发时间      ： 2020/1/24  16:29
# 文件名称      ： 01.PY
# 开发工具      ： PyCharm

# 字符串拼接
mot_en = "Remembrance is a form of meeting, Frgetfulness is form of freedom."
mot_cn = "记忆是一种相遇，遗忘是一种自由。"
print( mot_en + "--" + mot_cn )

str1 = "今天我一共走了"  # 定义字符串
num = 12980  # 定义一个整数
str2 = "步"
print( str1 + str( num ) + str2 )

# 计算字符串长度
str1 = "人生苦短，我用Python！"
length = len( str1 )
print( "默认字符串长度：", length )

length = len( str1.encode() )  # 计算utf-8 编码的字符串长度
print( "使用UTF-8编码的字符串长度：", length )

# 截取字符串长度
print( "---------- 分割线 ----------" )
subStr1 = str1[ 1 ]  # 截取2个字符
subStr2 = str1[ 5: ]  # 从第六个字符开始截取
subStr3 = str1[ : 5 ]  # 从昨天开始截取5个字符
subStr4 = str1[ 2: 5 ]  # 截取第3个到第5个字符
print( "原字符：", str1 )
print( "str1[ 1 ] :", subStr1 )
print( "str1[ 5: ]:", subStr2 )
print( "str1[ : 5 ] :", subStr3 )
print( "sstr1[ 2: 5 ] :", subStr4 )

# 分割字符串
print( "---------- 分割线 ----------" )
str1 = "明 日 学 院 官 网 >>> www.mingrisoft.com"
print( "源字符串：", str1 )
list1 = str1.split()  # 默认分隔符
list2 = str1.split( ">>>" )  # 采用多个字符作为分隔符
list3 = str1.split( "." )  # 采用“.”进行啊分割
list4 = str1.split( " ", 4 )  # 采用空格进行分割，并且只分割前4个
list5 = str1.split( ">" )  # 采用“>”进行分割
print( "默认分隔符:", list1 )
print( "用多个字符作为分隔符:", list2 )
print( "采用“.”进行啊分割:", list3 )
print( "采用空格进行分割，并且只分割前4个:", list4 )
print( "采用“>”进行分割:", list5 )

# 字符串检索
print( "---------- 分割线 ----------" )
str1 = "@明日科技 @咋克伯格 @雷军"
print( "字符串中 ‘", str1, "’中包括", str1.count( "@" ), "个@符号" )
print( "字符串中 ‘", str1, "’中符号‘@’首次出现的位置索引为：", str1.find( "@" ) )
print( "字符串中 ‘", str1, "’中符号‘@’右边首次出现的位置索引为：", str1.rindex( "@" ) )
print( "字符串中 ‘", str1, "’中是否以‘@’开头，结果为：", str1.startswith( "@" ) )
print( "字符串中 ‘", str1, "’中是否以‘@’结尾，结果为：", str1.endswith( "@" ) )

# 大小写切换
print( "---------- 分割线 ----------" )
str1 = "WWW.Mingrisoft.com"
print( "源字符串：", str1 )
print( "转小写：", str1.lower() )
print( "转大写：", str1.upper() )

# 去除字符串中的空格和字符

## 移除左右两侧的空格和特殊字符串
print( "---------- 分割线 ----------" )
str1 = " \t http://www.mingrisoft.com \t\n\r"
print( "原字符串str1:", str1 )
print( "字符串：", str1.strip() )
str2 = "@明日@科技.@."
print( "原字符串str2：", str2 )
print( "字符串：", str2.strip( "@." ) )

## 移除左侧的空格和特殊字符串
print( "---------- 分割线 ----------" )
print( "原字符串：", str1 )
print( "字符串：" + str1.lstrip() )
print( "原字符串：", str2 )
print( "字符串：", str2.lstrip( "@" ) )

## 移除右侧的空格和特殊字符串
print( "---------- 分割线 ----------" )
print( "原字符串：", str1 )
print( "字符串：" + str1.rstrip() )
print( "原字符串：", str2 )
print( "字符串：", str2.rstrip( "@." ) )

# 格式化字符串
print( "---------- 分割线 ----------" )
template = "编号： %09d\t公司名称： %s \t官网：  http://www.%s.com"
context1 = (7, '百度', 'baidu')
context2 = (8, '明日学院', 'mingrisoft')
print( template % context1 )
print( template % context2 )

template = "编号： {:0>9d}\t公司名称： {:s}\t官网： http://wwww.{:s}.com"
print( template.format( 7, '百度', 'baidu' ) )
print( template.format( 8, '明日学院', 'mingrisoft' ) )
