# -*- codeing = utf-8 -*-
# @Time : 2020/12/25 23:43
# @Author : Vanis
# @File : Exception.py
# @software:PyCharm

# Begin

'''
错误与异常：代码所产生的错误一般是难以预料的，但是异常却是可以避免的，可对可能发生的异常
          进行提前处理，避免系统报错，对异常的处理，叫做 捕获
'''

'''
捕获异常：try：
            所可能发生异常的代码段
        except 异常类型：
            对捕获到的异常进行的操作，或用 pass 不执行任何操作
        
        #如果想要捕获多钟异常，可以用逗号隔开，但捕获了第一个异常后，往后的异常不会再捕获
        #异常问题想要被捕获，需要异常类型与错误的类型一致    
捕获所有异常：except Exception:
'''

'''
获取错误描述：except(异常类型) as result:
           print(result)     -会把未捕获时的标红报错转换成字符串打印出来
'''

'''
try.....finally 和 嵌套
   1.finally：无论如何都会执行的代码段 #finally需要放在except后面
   2.try...finally的嵌套：try语句里可以再嵌套try语句 如：
       try:
           f = open("123.txt","r")
           
           try:
               while True:
                   content = f.readline()
                   if len(content) == 0:
                      break
                      
                   time.sleep(2)
                   print(content)
            
           finally:
              f.close()
              print("文件关闭")
              
       except Exception:
           print("发生异常")
   3.finally在执行文件操作时，可保证文件不管发生什么都能够正确关闭，以让下一次的
     文件能够顺利打开
'''

# 小作业1：应用文件操作的相关知识，通过Python新建一个文件gushi.txt,选择一首古诗写入其中

#创建一个文件，其内容是古诗
file = open("gushi.txt","w")

#将古诗写入
file.write("        春晓      \n"
            "春眠不觉晓，处处闻啼鸟；\n"
            "夜来风雨声，花落知多少。")

#文件关闭
file.close()


# 小作业2；另外写一个函数，读取指定文件gushi.txt,将内容复制到copy.txt中，并在控制台输出复制完毕
# 提示：分别定义两个函数，完成读文件和写文件的操作，尽可能完善代码，添加异常处理

#定义一个复制文本模块
def copy(file1,file2):
    #定义复制文本变量
    copy_txt = ""

    #检测是否存在文件，如果没有将提示文件未找到
    try:
        file1 = open(file1, "r")

        try:
            #将第一个文件的文本内容写入复制文本
            copy_txt = file1.readlines()

            #直接创建第二个文件
            file2 = open(file2, "w+")

            #将复制文本的内容写入第二个文件
            for word in copy_txt:
                file2.write(word)

            #判断是否复制成功
            if len(copy_txt) != 0:
                print("复制完毕")

            else:
                print("无内容可复制")

        finally:
            file1.close()
            file2.close()

    #如果需要复制的文件不存在，则输出提示信息
    except IOError:
        print("%s文件未找到，无法复制"%file1)

copy("gushi.txt","copy.txt")
