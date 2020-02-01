# -*- conding:utf8 -*-
# _python_ 学习与练习
#     作者： YBingo
# 开发时间： 2020/1/20   1:21
# 文件名称： 01.PY
# 开发工具： PyCharm

print( "\n手机店正在打折，活动进行中...." )
strWeek = input( "请输入中文星期几（如：星期一）：" )
intTime = int( input( "请输入时间中的小时（范围：0~23）：" ) )

if (strWeek == "星期二" and 10 <= intTime <= 12
        or (strWeek == "星期五" and 14 <= intTime <= 15)):
    print( "恭喜您，获得了折扣活动参与资格！" )
else:
    print( "对不起，您来晚了一步" )
