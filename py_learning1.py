#在123456789之间添加+-*/或不填，使其结果=100
import os

arr1=[1,2,3,4,5,6,7,8,9]

arr2=["","+","-","*","/"]

def func1(arr3):
    arr4=[1]
    for i in range(0,8):
        if arr3[i]==0:
            arr4[-1]=arr4[-1]*10+arr1[i+1]
        else:
            arr4.append(arr2[arr3[i]])
            arr4.append(arr1[i+1])
    #print(arr4)
    idx=1
    while idx<len(arr4):
        if arr4[idx]=="*":
            arr4[idx-1]=arr4[idx-1]*arr4[idx+1]
            arr4.pop(idx)
            arr4.pop(idx)
        elif arr4[idx]=="/":
            arr4[idx-1]=arr4[idx-1]/arr4[idx+1]
            arr4.pop(idx)
            arr4.pop(idx)
        else:
            idx=idx+2
    #print(arr4)
    idx=1
    while idx<len(arr4):
        if arr4[idx]=="+":
            arr4[idx-1]=arr4[idx-1]+arr4[idx+1]
            arr4.pop(idx)
            arr4.pop(idx)
        elif arr4[idx]=="-":
            arr4[idx-1]=arr4[idx-1]-arr4[idx+1]
            arr4.pop(idx)
            arr4.pop(idx)
        else:
            idx=idx+2

    return arr4[0]

def func2():
    s1=""
    for i1 in range(0,5):
        for i2 in range(0,5):
            for i3 in range(0,5):
                for i4 in range(0,5):
                    for i5 in range(0,5):
                        for i6 in range(0,5):
                            for i7 in range(0,5):
                                for i8 in range(0,5):
                                    if func1([i1,i2,i3,i4,i5,i6,i7,i8])==100:
                                        s2="1"+arr2[i1]+"2"+arr2[i2]+"3"+arr2[i3]+"4"+arr2[i4]+"5"+arr2[i5]+"6"+arr2[i6]+"7"+arr2[i7]+"8"+arr2[i8]+"9"
                                        print(s2)
                                        s1=s1+s2+"\n"
    f = open(os.getcwd()+"\\"+"100.txt", 'w')
    f.write(s1)
    f.close()
    return



if __name__=="__main__":
    func2()
