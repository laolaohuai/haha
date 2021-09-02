#切割/组合字符串
a="1,2,3,4,5,6,7,8"
b=a.split(",")
print(b)
c="+".join(b)
print(c)

#输出元属性
d={1:"123"}
print(dir(d))
print(d.__class__)