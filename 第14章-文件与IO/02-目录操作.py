# _*_ coding  : utf-8 -*-
# _python_ 学习与练习
#     作者    :  YBingo
# 开发时间     : 2020/2/6   14:12
# 文件名称     ： 02-目录操作.PY
# 开发工具     ： PyCharm

import os

with open( r'demo/message.txt', 'r' ) as file:
    string = file.read()
    print( string )

directory = 'demo'
path = r'demo/message.txt'
root = os.getcwd()
print( "目标路径：", path )
print( '相对路径：', path )
print( '绝对路径：', os.path.abspath( path ) )
print( '路径拼接：', os.path.join( root, path ) )
print( '判断demo目录是否存在：', os.path.exists( os.path.join( root, directory ) ) )

print( '=' * 20, '创建目录', "=" * 20 )

if not os.path.exists( path ):
    os.mkdir( os.path.join( root, directory ) )
    print( '目录创建成功' )
else:
    print( '该目录已经存在' )

print( '=' * 20, '创建多级目录', "=" * 20 )
if not os.path.exists( os.path.join( root, 'test/test-child' ) ):
    os.makedirs( os.path.join( root, 'test/test-child' ) )
    print( '目录创建成功' )
else:
    print( '该目录已经存在' )

print( '=' * 20, '删除目录', "=" * 20 )
if os.path.exists( os.path.join( root, 'test/test-child' ) ):
    os.rmdir( os.path.join( root, 'test/test-child' ) )
    print( '删除目录成功！' )
else:
    print( '目录已经不存在了' )

print( '=' * 20, '目录遍历', "=" * 20 )
tuples = os.walk( root )
for tuple1 in tuples:
    print( tuple1 )

# print( '=' * 20, '删除文件', "=" * 20 )
# if os.path.exists( path ):
#     os.remove( path )
#     print('文件删除完毕！')
# else:
#     print( "文件不存在了" )

print( '=' * 20, '重命名', "=" * 20 )
src = 'test'
dst = 'test2'
if os.path.exists( src ):
    if not os.path.exists( dst ):
        os.rename( src, dst )
        print( '目录重命名完毕' )
    else:
        print( '重命名目录已存在' )
else:
    print( '目录不存在' )

print( '=' * 20, '文件信息', "=" * 20 )
if os.path.exists( path ):
    fileinfo = os.stat( path )
    print( '文件的完整路径：', os.path.abspath( path ) )
    print( '文件大小：', fileinfo.st_size, '字节' )
    print( '最后一次修改时间：', fileinfo.st_mtime )
