# _*_ coding  : utf8 -*-
# _python_ 学习与练习
#     作者    : YBingo
# 开发时间     : 2020/2/4   11:39
# 文件名称     ： 03-返回值.PY
# 开发工具     ： PyCharm

def fun_checkout( name ):
    nickName = ""
    if name == '邓肯':
        nickName = '石佛'
    elif name == '吉诺比利':
        nickName = '妖刀'
    elif name == '罗宾逊':
        nickName = '海军上将'
    else:
        nickName = '无法找到你输入的信息'
    return nickName

# ********** 调用函数 *********** #
while True:
    name = input( '请输入你的NBA球员名称：' )
    nickname = fun_checkout( name )
    print( '球员：', name, '绰号：', nickname )
    if len( nickname ) <= 6:
        break
