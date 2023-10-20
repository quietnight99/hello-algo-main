"""
File: recursion.py
Created Time: 2023-08-24
Author: Krahets (krahets@163.com)
"""
import time


# def recur(n: int) -> int :
#     """递归"""
#     # 终止条件
#     if n == 1 :
#         return 1
#     # 递：递归调用
#     res = recur(n - 1)
#     # 归：返回结果
#     return n + res
# print(recur(3))

# 递归
# def hello(n) :
#     print("当前n为：%s" % n)
#     if n == 1 :
#         return 1
#     res = hello(n - 1)
#     print("当前res为：%s" % res)
#     print("当前res + n为：%s" % (res + n))
#     return res + n
# hello(5)


# # for循环求和
# def for_num(n : int):
#     res = n
#     for i in range(n):
#         res = res + i
#     print(res)
# for_num(3)

# # while循环求和
# def while_num(n : int):
#     i = 1
#     res = 0
#     while i <= n:
#         res += i
#         i = i + 1
#     print(res)
# while_num(10)

# def formula(n):
#     s = (n*(n+1))/2
#     return s
#
# a = jisuan(n = 3)
# print(a)


def for_loop_recur(n: int) -> int :
    """使用迭代模拟递归"""
    # 使用一个显式的栈来模拟系统调用栈
    stack = []
    res = 0
    # 递：递归调用
    for i in range(n, 0, -1) :
        # 通过“入栈操作”模拟“递”
        stack.append(i)
    # 归：返回结果
    while stack :
        # 通过“出栈操作”模拟“归”
        res += stack.pop()
    # res = 1+2+3+...+n
    return res


# def tail_recur(n, res) :
#     print(n, res)
#     """尾递归"""
#     # 终止条件
#     if n == 0 :
#         print(res)
#         return res
#     # 尾递归调用
#     return tail_recur(n - 1, res + n)
# tail_recur(5,0)



def fib(n: int) -> int :
    """斐波那契数列：递归"""
    # 终止条件 f(1) = 0, f(2) = 1
    if n == 1 or n == 2 :
        return n - 1
    # 递归调用 f(n) = f(n-1) + f(n-2)
    res = fib(n - 1) + fib(n - 2)
    # 返回结果 f(n)
    return res


"""Driver Code"""


# if __name__ == "__main__":
#     n = 4
#     res = recur(n)
#     print(f"\n递归函数的求和结果 res = {res}")

# res = for_loop_recur(n)
# print(f"\n使用迭代模拟递归求和结果 res = {res}")
#
# res = tail_recur(n, 0)
# print(f"\n尾递归函数的求和结果 res = {res}")
#
# res = fib(n)
# print(f"\n斐波那契数列的第 {n} 项为 {res}")


def creat_arry() :
    import random
    # 生成一个固定长度的列表
    random_list = [random.randrange(100000) for _ in range(10000)]
    # print(random_list)
    # print(random_list)
    return random_list


# 冒泡排序
def bubble_sort(random_list) :
    arry = random_list
    n = len(arry)
    for i in range(n - 1) :
        flag = True
        for j in range(n - 1 - i) :  # 每轮找到最大数值 或者用 for j in range(i+1, n)
            # print(i, j+1)
            # print(j, j + 1)
            if arry[j] > arry[j + 1] :
                arry[j], arry[j + 1] = arry[j + 1], arry[j]
                flag = False
        if flag :
            break
    return arry
    # print(arry)
    # print('\n')


# bubble_sort()

# 插入排序
def insert_sort(random_list) :
    data1 = random_list
    n = len(data1)
    for i in range(n - 1) :
        m = i
        for j in range(i + 1, n) :
            # print(i,j)
            if data1[j] < data1[m] :
                m = j
        data1[i], data1[m] = data1[m], data1[i]
    # print(data1)
    return data1


# insert_sort()


def quick_sort(lst) :
    n = len(lst)
    if n <= 1 :
        return lst
    baseline = lst[0]
    left = [lst[i] for i in range(1, len(lst)) if lst[i] < baseline]
    right = [lst[i] for i in range(1, len(lst)) if lst[i] >= baseline]
    return quick_sort(left) + [baseline] + quick_sort(right)

#
#
#
# for i in range(1):
#     array = creat_arry()
#     start_time = time.time()
#     res = quick_sort(array)
#     end_time = time.time()
#     a = end_time - start_time
#     print("快速排序耗时：{}".format(end_time - start_time))
#
#     start_time = time.time()
#     res1 = insert_sort(array)
#     end_time = time.time()
#     b = end_time - start_time
#     print("插入排序耗时：{}".format(end_time - start_time))
#
#     start_time = time.time()
#     res2 = bubble_sort(array)
#     end_time = time.time()
#     c = end_time - start_time
#     print("冒泡排序耗时：{}".format(end_time - start_time))
#     print('\n')
#
#     base = b
#
#     ab_ratio = a / base
#     ac_ratio = c / base
#     bc_ratio = b / base
#
#     print(ab_ratio, ac_ratio, bc_ratio)
