# -*- codeing = utf-8 -*-
# @Time : 2020/12/21 16:13
# @Author : Vanis
# @File : Dict.py
# @software:PyCharm

Begin

'''
Dict字典：
    1.字典是无序的对象集合，使用键-值（key-value）存储，具有极快的查找速度
    2.键（key）必须使用不可变类型
    3.同一个字典中，键（key必须是唯一的）
'''

'''
Dict字典的定义：
    用{}，如：info = {"name":"黄振韬","age":20}
Dict字典的访问：
    1.直接通过键的索引值 如：print(info["name"]) -此时print "黄振韬"
      #当访问一个不存在的键时，会报错，抛出KeyError异常
    2.用.get方法：如 print(info.get["gender"])
      #当用.get访问一个不存在的键时，会返回None
      #返回的默认值可设置，如 print(info.get["gender","Not"]) -此时未找到时会返回Not
'''

'''
Dict字典的常用操作：
    1.增：
        ·直接通过新的键新增键值对：info["id"] = 123
        ·通过.update合并两个字典：dict1.update(dict2)
    2.删：
        ·del -直接删除整个字典或键值对：如 del info["name"] -此时再访问indo["name"]会报错
        ·.clear() -清空整个字典 如 info.clear() -此时info字典成了空字典
    3.改：
        ·直接通过下标索引更改值：info["age"] = 21
    4.查：
        1）对键（key）的查找：
          ·拿到字典里所有的键：如 print（info.keys()） -此时会以list列表的形式打印出来
        2）对值（value）的查找：
          ·拿到字典里所有的值：如 print(info.values()) -此时会以list列表的形式打印出来
        3）对项（item）的查找：
          ·拿到字典里所有的项：如 print(info.items()) -此时会以list列表的形式打印出来，列表立立每一个元组就是一个项   
        #.keys() .values() .items()只会以列表的形式打印，如果要拿到单独的值还得用 for in 遍历 如：for keys in info.keys()
        #遍历所有键值对时，可以用 for in 可遍历多个元素的特点，如 for keys,values in info.items()
    5.其他类型对象转化成字典：dict（） -里面必须是元组形式 如 dict([(1,2),(2,3)])
'''

'''
Set集合：
    1.set和dict类似，也是一组key的集合，但不存储value。由于key在字典中是唯一的，所以在set中，没有重复的key
    2.set是无序的，重复元素在set中自动被过滤
    3.set集合也是以{}括起来，但是{}里仅仅只有数值，而不是跟字典那样的键值对
'''

'''
数据结构小结：
                    是否有序               是否可变类型
   ·List列表[]        有序                   可变类型
   ·Tuple元组()       有序                  不可变类型
   ·Dict字典{}        无序              key可变，value不可变
   ·Set集合{}         有序                可变类型（不重复） 
'''

End