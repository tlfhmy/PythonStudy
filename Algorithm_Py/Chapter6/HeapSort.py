from random import randint

# ----------------------------------
# |  Error Code  |       意义       |
# ----------------------------------
# |     1        |   参数传递错误    |
# ----------------------------------


def RightSon(i):
    if type(i) == int:
        return 2*i + 1
    else:
        print("Error Code 1.")


def LeftSon(i):
    if type(i) == int:
        return 2*i + 2
    else:
        print("Error Code 1.")


def Parent(i):
    if type(i) == int:
        return (i-1) // 2
    else:
        print("Error Code 1.")


def Max_Heap_Maintence(p, size, i):
    if (type(p) == list or type(p) == tuple)\
        and type(size) == int\
        and type(i) == int:

        l = LeftSon(i)
        r = RightSon(i)
        largest = i
        if l <= size-1 and p[l] > p[i]:
           largest = l
        else:
            largest = i
        if r <= size-1 and p[r] > p[largest]:
            largest = r
        if largest != i:
            tmp = p[i]
            p[i] = p[largest]
            p[largest] = tmp
            Max_Heap_Maintence(p, size, largest)

    else:
        print("Error Code 1.")

def Build_Max_Heap(p, size):
    if (type(p) == list or type(p) == tuple)\
        and type(size) == int:
        for i in range(size//2 - 1, -1, -1):
            Max_Heap_Maintence(p, size, i)

    else:
        print("Error Code 1.")

def Heap_Sort(p, size):
    if (type(p) == list or type(p) == tuple)\
        and type(size) == int:
        Build_Max_Heap(p, size)
        for i in range(size-1, -1, -1):
            tmp = p[0]
            p[0] = p[i]
            p[i] = tmp
            Max_Heap_Maintence(p, i, 0)

    else:
        print("Error Code 1.")


n = int(input("请输入待排序随机数的个数："))
a = []
for i in range(0, n):
    a.append(randint(0, 2*n))

print(a)

Heap_Sort(a, n)

print(a)