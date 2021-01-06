# -*- codeing = utf-8 -*-
# @Time : 2020/12/23 21:37
# @Author : Vanis
# @File : File.py
# @software:PyCharm

# Begin

'''
文件操作概念：
   就是把一些数据存放起来，可以让程序下一次执行的时候直接使用，而不必重新制作一份
'''

'''
文件的打开与关闭：   
   1.打开文件：使用open函数，可以打开一个已经存在的文件，或者创造一个新文件
             open(文件名，访问模式)  如： file = open('test.txt','w')  - 其中‘w’模式为写模式
     #当用open函数新建一个文件，默认在当前目录下创建文件
   2.关闭文件：使用close函数       
'''

'''
访问模式：
   1.r：以 只读 方式发开文件，文件的指针会放在文件的开头，这是默认模式；如果文件不存在，则会报错
   2.w：打开一个文件只用于 写入 ，如果文件存在则会覆盖；如果不存在，则会新建文件
   3.a：打开一个文件用于 追加 ，如果文件存在，则从文件末尾写入；否则新建文件
   4.rb、wb、ab：以 二进制格式 打开文件
   5.r+、w+、a+：打开一个文件用于 读写
   6.rb+、wb+、ab+：以 二进制格式 打开一个文件用于 读写
'''

'''
文件的写入：
   在打开文件后，使用.write函数  如：file = open('text.txt','w') 
                                file.write("hello world!")
                                file.close()
'''

'''
文件的读取：
   1.在打开文件后，使用.read函数，可读取指定数目字符串 如：
                              file = open('text.txt','r')
                              content = f.read(5) - 5代表读5个字符出来
                              print(content)
                              file.close()
   #.read函数只有在第一次时，指针才会在文件开头。如果.read方法使用多次，指针的位置会
    随着所读取字符串的变化而变化   
   2.在打开文件后，使用.readlines函数，可以多行字符串的方式读取全部文本，且以列表的形式打印出来，
     列表的每一个元素为一行 如：   file = open('text.txt','r')
                              content = f.readlines() 
                              print(content)
                              file.close()   
   3.在打开文件后，使用.readline函数，可以读取一行字符串 如：
                              file = open('text.txt','r')
                              content = f.readline() 
                              print(content)
                              file.close()  
   #.readline函数跟.read函数一样，在第一次使用时指针才会在文件开头，如果读取多次指针位置会有变化                
'''

file = open("test.txt","r")
content = file.read(5)
print(content)
content = file.read(5)
print(content)
file.close()

'''
文件的相关操作：
   1.文件的重命名：os模块中的rename()可以完成对文件的重命名 如：import os
                                                        os.rename(文件名前，文件名后)
   2.删除文件：os模块中的remove()可以完成对文件的删除 如：os.remove(文件名)
   3.创建文件夹：os.mkdir(文件夹名)
   4.获取当前目录：os.getcwd()
   5.改变默认目录：os.chdir("../")
   6.获取目录列表：os.listdir("./")
   7.删除文件夹：os.rmdir(文件夹名)
   8.文件指针：文件在读取之后，文件指针会停留在最后一次读取的末尾处，此时用.seek方法可以设置指针位置，如
            file.seek(offset[,where])  - offset指偏移量 where指指针状态，默认为0：从文件头部开始 此外还有 1：当前位置开始 2：文件末尾开始
'''

#End