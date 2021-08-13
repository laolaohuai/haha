test_l1=lambda a:a*a
print(test_l1(5))
test_l2=lambda a,b:a*b
print(test_l2(2,3))
test_l3=lambda a,b,c,d,e:a+b-c*d/e
print(test_l3(10,20,30,40,50))



list1=[1,2,3,4,5]
list2=[5,4,3,2,1]

print(map(test_l1,list1))
print(map(test_l2,list1,list2))


print(filter(lambda a:a<4,list1))
print(filter(lambda a:a<4,list2))


print(reduce(lambda a,b:a+b,list1))
