# -*- coding: cp936 -*-
def quick_sort(data):
    """��������"""
    if len(data) >= 2:  # �ݹ���ڼ�����
        mid = data[len(data)//2]  # ѡȡ��׼ֵ��Ҳ����ѡȡ��һ�������һ��Ԫ��
        left, right = [], []  # �����׼ֵ����������б�
        data.remove(mid)  # ��ԭʼ�������Ƴ���׼ֵ
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data

# ʾ����
array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quick_sort(array))
# ���Ϊ[1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9, 9, 10, 12, 15, 15, 17]
