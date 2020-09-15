#! /usr/bin/python
# coding=utf-8
# -*- coding:utf8 -*-
import os,re,string
def test(path,ex,calc,para):
	#path根目录
	#ex扩展名过滤,填*则不过滤
	#calc操作函数
	#para操作函数参数
        pathlist=[path]
        index=0
        while (index<len(pathlist)):
                #print(pathlist[index])
                if os.path.isdir(pathlist[index]):
                        filelist=os.listdir(pathlist[index])
                        for i in filelist:
                                #print(pathlist[index]+"\\"+i)
                                pathlist.append(pathlist[index]+"\\"+i)
                else:
                        if ex=="*" or ex==string.split(pathlist[index],".")[-1]:
                                calc(pathlist[index],para,index)
                index+=1

def test2(path,para,index):
        #输出文件名
	print(path)

def test3(path,para,index):
        #输出文件内容
        f = open(path, 'r')
        txt = f.read()
        f.close()
        print(txt)

def test4(path,para,index):
        #用正则表达式对文件中的内容进行替换
        f = open(path, 'r')
        txt = f.read()
        f.close()
        txt = re.sub(para[0], para[1], txt)
        f = open(path, 'w')
        f.write(txt)
        f.close()

def test5(path,para,index):
        #重命名文件(非常危险,慎用)
        new_name="\\".join(string.split(path,"\\")[:-1])+"\\"+para[0]+str(index)+"."+string.split(path,".")[-1]
        print(path+">>"+new_name)
        #os.rename(path,new_name)


#test(os.getcwd(),"lua",test3,[])
test("E:\\haha-master\\1","*",test4,[r'.',"a"])
