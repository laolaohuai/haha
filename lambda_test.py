import functools as fu

la1=lambda a:a**3
#print(la1(5))
la2=lambda a,b:a*b
#print(la2(2,3))
test_la3=lambda a,b,c,d,e:a+b-c*d/e
#print(test_la3(10,20,30,40,50))


list1=[1,2,3,4,5,6]
list2=[5,4,3,2,1,0]

print(list(map(la1,list1)))
print(list(map(la2,list1,list2)))


print(list(filter(lambda a:a<4,list1)))
print(list(filter(lambda a:a<4,list2)))


print(fu.reduce(lambda a,b:a+b,list1))

#位运算
print(~6)#取反等于取相反数后再-1
print(3&6)#011 & 110 = 010
print(3|6)#011 | 110 = 111
print(3^6)#011 ^ 110 = 101

#数组操作
a=[111,333]
a.insert(1,222)
print(a)
print(a.pop())
print(a)