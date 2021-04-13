# -*- coding: UTF-8 -*-

fileName = input("请输入文件名:")
content = input("请输入文件内容:")

file = open(fileName, "w")
file.write(content)
print(file.name)
print(file.mode)
file.close()