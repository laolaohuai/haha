#百鸡百钱

a=5#公鸡
b=3#母鸡
c=1/3#小鸡

def func1(a,b,c):
    for a1 in range(0,100//a+1):
        for b1 in range(0,(100-a*a1)//b+1):
            c1=100-a1-b1
            if a*a1+b*b1+c*c1==100:
                print("公鸡%d,母鸡%d,小鸡%d"%(a1,b1,c1))

#斐波那契数列
def func2():
    a=[1,1]
    for i in range(3,21):
        a.append(a[-1]+a[-2])
    print(a)

#完美数
def func3():
    for i in range(1,10001):
        s=0
        for j in range(1,i):
            if i%j==0:
                s+=j
        if s==i:
            print(i)

#100内所有素数
def func4():
    for i in range(2,101):
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
                break
        if flag:
            print(i)


if __name__=="__main__":
    #func1(a,b,c)
    func2()
    #func3()
    #func4()