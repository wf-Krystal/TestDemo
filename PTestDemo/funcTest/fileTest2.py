#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
with open('user.txt', 'rb+') as f:
    str = f.read(10)
    print("前10个字符串为：", str)
    # 查找当前位置
    position = f.tell()
    print("当前位置是：", position)
    # 把指针再次重新定位到文件开头
    position = f.seek(0, 0)
    str = f.read(10)
    print("重新读取字符串：", str)
    position = f.seek(-20, 2)
    position = f.tell()
    print("当前位置是：", position)
    str = f.read(20)
    print("重新读取字符串：", str)
    print("filename:", f.name)
    print("is colosed?", f.closed)
    print("filemode:", f.mode)
    #print("softspace?", f.softspace)   python2.x的用法，python3已经没有


"""
position = f.seek(-10, 2)报错：can't do nonzero end-relative seeks
原因：在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常。
解决方案：filemode改为 'rb+'
'rb+'模式，不能指定文件编码格式为'gbk/utf-8',报错：binary mode doesn't take an encoding argument
"""