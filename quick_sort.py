#快速排序说明
#1.从数组中随意选取一个中值（可以是第一个数，也可以取在中间的数，还可以取末尾的数或随机选取一个数）。
#2.准备三个空数组，将比中值小的数放到第一个数组，将等于中值的数放到第二个数组（不需要再排序）,将比中值大的数放到第三个数组。
#3.对1和2的过程进行递归，直到数组长度小于2。

#优化思路：

#中值的选择：如果每次取中值时能取到接近当前数组的中位数，那么运行效率会提高。在数据量很大的时候中值要考虑(选中值的时间代价<节省出来的时间)。
#数据混乱程度：如果数据只在很多小范围内有序，整体无序，那快速排序很好，但如果数据大部分都是有序的，只是某几个小部分无序，那快速排序就很渣。
#数据重复度：数据重复量越大，数据分布越窄，快排越不如桶排。
#复合排序：数据量很大的时候,数据分布相对数据量本身来说一定是很窄的，所以先做桶排序分块，然后再用快排细分。


#快速排序1
def quick_sort(data):
    if len(data) >= 2:
        mid = data[len(data)//2]
        left, right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data



#快速排序2(仅5行代码)
#当数据重复量很多时，这种比上面的要快很多，因为它会将与中值相等的数一次性排好。
#用了filter和lambda函数等奇技淫巧，代码看起来略难懂，但看懂后其实和上面一样。
def quick_sort2(data):
    if len(data) > 1:
        return quick_sort2(list(filter(lambda a:a<data[0], data))) + list(filter(lambda a:a==data[0], data)) + quick_sort2(list(filter(lambda a:a>data[0], data)))
    else:
        return data



#桶排+快排
import functools as fu
import math
def bucket_sort(data):
    #根据对数据的初步了解来确定桶的个数，具体问题具体分析，
    #一般设置为数据分布数+1的平方根向上取整。
    #例如：最小的数为21，最大的数为120，那么就应该得准备math.sqrt(120-21+1),也就是10个桶。
    #数据比较连续和紧密时，一般采用整数除法来"分桶"(实际场景一般用位运算右移)，简单粗暴，一步到位。
    #数据量很大且分布很窄时，先桶排+后快排是非常强大的组合。
    #也可以二次或多次"分桶"，但算法相对复杂，而且多次分桶效率不如桶排+快排。
    min_num,max_num=data[0],data[0]
    for i in data:
    	min_num,max_num=min(min_num,i),max(max_num,i)
    b_num=math.ceil(math.sqrt(max_num-min_num+1))#通过数据分布算出桶的个数
    bucket=[]
    for i in range(0,b_num):
    	bucket.append([])
    for i in data:
        bucket[(i-1)//b_num].append(i)#通过一定简单算法(比如整数除法)将数据分装在每个桶内
    print(bucket)
    for i in range(0,b_num):
    	bucket[i]=quick_sort2(bucket[i])#对每个桶内部快排
    return fu.reduce(lambda c,d:c+d, bucket)#组装在一起


array = [3,7,7,7,7,2,4,6,1,1,4,9,8,5]
#array2 = [5,5,5,5,5,5,5]
print(quick_sort2(array))
#[1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 7, 7, 8, 9]