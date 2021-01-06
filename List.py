# -*- codeing = utf-8 -*-
# @Time : 2020/12/17 23:14
# @Author : Vanis
# @File : List.py
# @software:PyCharm

Begin

'''
List列表：
   1.列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串
     甚至可以包含列表（所谓嵌套）
   2.列表是写在方括号[]之前、用 逗号, 分隔开的元素列表
   3.列表索引值以0为开始值，-1为末尾的开始位置
   4.列表可以使用+操作符进行拼接，使用*表示重复  
'''

'''
列表的定义：
   1.定义一个空列表：list = []
   2.定义一个有内容的列表：list = ["a",123,"123"] #此时123为int类型 -列表可以定义混合类型数据
   #列表的下标从0开始
'''

'''
列表的遍历：
   1.使用 for...in 循环可以遍历出列表中的每一个元素，如：
      for name in namelist:         -将namelist列表中的每一个元素
          print(name)                遍历出来并储存在name变量中
     #使用枚举函数enumerate()可以同时拿到列表的下标和值 如：
      for i,x in enumerate(namelist):
          print(i,x)
   2.或是用len()函数得到列表的长度，再用while循环遍历，如：
      length = len(namelist)        -虽然不如 for...in 循环方便
      i=0                            但可以通过下标的变化拿到列表元素里
      while i<length:                具体的某一项
         print(namelist[i])         -但需要下标时，可以考虑用此方法 
         i += 1             
'''

'''
列表的常用操作：
   1.访问：通过下标直接访问 如：pring(list[1])
   2.切片：使用[: :] 如：list[2:5:2] #[开头:结尾:步进]
   3.遍历：使用for或while循环
   4.增：
        ·新增数据到列表尾部:使用append方法 如：list.append(5)  -append一个列表时，会将一整个列表当成一个元素增加
        ·列表的追加:使用extend方法 如：list.extend(list2)     -extend一个列表时，会将列表内的元素逐一追加
        ·列表数据插入：使用insert方法 如：list.insert(1,3)     -第一个变量表示插入的下标位置，第二个变量表示插入的元素对象
   5.删：
        ·列表的删除：del方法 -通过索引删除指定位置的元素 如：del list[0]
                   remove方法 -移除列表中指定值的第一个匹配值，如果没找到会抛出异常
                      如：list.remove(1)  
                   #del方法是通过下标删除 remove是直接删除指定内容   
        ·弹出列表尾部元素：使用pop方法 如：list.pop()     
   6.改：
        ·直接通过下标重新赋值来修改元素内容 如：list[1] = "小王"
   7.查：
        ·是否存在：通过 in 或 not in 方法来判断是否存在元素 如：if name in namelist...
        ·查找位置：通过index方法来寻找指定内容在列表里的下标位置 如：a.index("a",1,4) 
                 -表示 a字符串 是否在列表里下标1到下标4的范围内出现，如果有，则返回 a字符串的下标位置，否则报错
        ·统计指定元素出现次数：使用count方法 如：print(list.count("a"))
   8.排：
        ·反转列表：使用reverse方法 如 a.reverse()
        ·排序：使用sort方法 如：a.sort（） -默认升序，a.sort(reverse=True)可降序排列
   9.嵌套:
        ·定义时直接嵌套 如：list = [[],[],[]] -嵌套的列表，列表元素数量可以各不相同
         #嵌套列表的访问类似二维数组 如：print(list[0][0])                       
'''

#列表小作业：将8个老师随机分配到三个办公室中：
import random

office = [[],[],[]]
teacher = ["a","b","c","d","e","f","g","h",]


def distribution(teacher,office):
    x = len(office)
    for name in teacher:
        num=random.randint(0,x-1)
        office[num].append(name)


    i=0
    while i<=x-1:
        print("第%s个办公室有：%s个老师；分别是%s\t"%(i+1,len(office[i]),office[i]))
        i += 1

fenpei = distribution(teacher,office)
fenpei


End