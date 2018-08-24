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
                                calc(pathlist[index],para)
                index+=1

def test2(path,para):
	print(path)

def test3(path,para):
        f = open(path, 'r')
        txt = f.read()
        f.close()
        print(txt)
        #f = open(path, 'w')
        #f.write(txt)
        #f.close()

#test(os.getcwd(),"txt",test3,[])
