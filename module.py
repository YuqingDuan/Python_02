#python的模块相当于java的包
#python自带的模块在Lib目录

'''
#python模块的导入
#先导入文件夹再导入模块和模块中的函数
import urllib
from urllib.request import urlopen
#文件夹名称.模块文件名称.函数名
data1=urlopen("http://www.baidu.com").read()
print(len(data1))
'''

#另外一种导入方式
from urllib import request
data=request.urlopen("http://www.baidu.com").read()
print(len(data))
