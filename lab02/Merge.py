import datetime
import math
class Product:
    def __init__(self, id, name, price, release_date, rating):
        self.id = id
        self.name = name
        self.price = price
        self.release_date = datetime.datetime.strptime(release_date, '%Y-%m-%d')
        self.rating = rating

    def __repr__(self):
        return '{}'.format(self.id)

def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # 创建临时数组
    L = [0] * (n1)
    R = [0] * (n2)

    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = a[l + i]

    for j in range(0, n2):
        R[j] = a[m + 1 + j]

        # 归并临时数组到 arr[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引
    print("Merge {} and {}".format(L, R))
    #print("Merge {} and {}".format(L, R))
    while i < n1 and j < n2:
        if L[i].rating >= R[j].rating:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
    # 拷贝 L[] 的保留元素
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    # 拷贝 R[] 的保留元素
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1
    #print("Merge {} and {}".format(a[l:r], a[r:r+1]))
    print("After merge: {}".format(a[l:r+1]))

def merge_sort(a, l, r):
    if l < r:
        m = math.ceil((l + (r - 1)) / 2)
        merge_sort(a, l, m)
        merge_sort(a, m + 1, r)
        merge(a, l, m, r)

database = [
    Product(1, 'A', 5000, '2019-10-24', 4.7),
    Product(2, 'B', 300, '2018-1-14', 3.1),
    Product(3, 'C', 1200, '2020-3-3', 5),
    Product(4, 'D', 10, '2019-7-19', 4.2),
    Product(5, 'E', 50, '2019-12-4', 3.5),
    Product(6, 'F', 180, '2021-3-8', 3.9)
]

merge_sort(database, 0, len(database)-1)
'''
arr = [13, 12, 11, 7, 6, 5]
n = len(arr)
print("给定的数组")
for i in range(n):
    print("%d" % arr[i]),

merge_sort(arr, 0, n - 1)
print("\n\n排序后的数组")
for i in range(n):
    print("%d" % arr[i])
'''