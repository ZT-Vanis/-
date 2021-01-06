# -*- codeing = utf-8 -*-
# @Time : 2020/12/17 22:05
# @Author : Vanis
# @File : String.py
# @software:PyCharm

Begin

'''
String字符串：
   1.Python中的字符可以用 单引号、双引号、三引号（三单或三双）括起来，使用反斜杠\
     转移特殊字符
   #单引号类似单词，双引号类似句子，三引号类似段落（可以直接换行） 
   2.Python3源码文件默认以UTF-8编码，所有的字符都是Unicode字符串
   3.支持字符拼接、截取等多种运算
   #字符串的拼接用 + 号，如：print(str+",你好")  或是使用 * 号多次打印
   4.Python的字符串可以用 Variables[x:y:z] （x为起始位置，y为结束位置，z为步进数）
    来取出字符串里的字符，如：
    print(str[0:6:2]) -可取出str字符串里第一到第六个字符，步进2
   5.在字符串前添加 r 可以使字符串内的字符直接打印而不转义，如：print(r"hello\nworld")
   
'''

'''
字符串的常见方法：
   1.bytes.decode(encoding="utf-8",errors="strict"):Python3中没有decode方法，但
     我们可以使用bytes对象的decode()方法来解码给指定的bytes对象，这个bytes对象可以由
     str.encode()来编码返回
   2.encode(encoding="utf-8",errors='strict'):以encoding指定的编码格式编码字符串，
     如果出错默认报一个ValueError的异常，除非errors指定的是'igonre'或'replace'
   3.isalnum():如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False
   4.isalpha():如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
   5.isnumeric():  如果字符串只包含数字则返回True，否则返回False
     #isdigit():同isnumeric()方法一样，但面对罗马数字和汉字数字等情况时兼容不同
   6.join(seq):以指定字符串作为分隔符，将seq中所有的元素合并成一个新的字符串
   7.len(string):返回string字符串的长度
   8.lstrip()/rstrip():删除字符串左边/末尾的空格或指定字符
   9.split(str="",num=string.count(str)):以str作为分隔符分片字符串，
     如果num有指定值，则仅截取num+1个子字符串  
'''

End





