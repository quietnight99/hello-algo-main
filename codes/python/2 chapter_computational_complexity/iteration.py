"""
File: iteration.py
Created Time: 2023-08-24
Author: Krahets (krahets@163.com)
"""


def for_loop(n: int,a:str) -> int :
    """for 循环"""
    print(a)
    res = 0
    # 循环求和 1, 2, ..., n-1, n
    for i in range(1, n + 1) :
        res += i
    return res


# a = for_loop(3,'4')
# print(a)


def while_loop(n: int) -> int :
    """while 循环"""
    res = 0
    i = 1  # 初始化条件变量
    # 循环求和 1, 2, ..., n-1, n
    while i <= n :
        res += i
        i += 1  # 更新条件变量
    return res

# a = while_loop(3)
# print(a)

def while_loop_ii(n: int) -> int :
    """while 循环（两次更新）"""
    res = 0
    i = 1  # 初始化条件变量
    # 循环求和 1, 4, ...
    while i <= n :
        res += i
        # 更新条件变量
        i += 1
        i *= 2
    return res
a = while_loop_ii(3)
print(a)

def nested_for_loop(n: int) -> str :
    """双层 for 循环"""
    res = ""
    # 循环 i = 1, 2, ..., n-1, n
    for i in range(1, n + 1) :
        # 循环 j = 1, 2, ..., n-1, n
        for j in range(1, n + 1) :
            res += f"({i}, {j}), "
    return res


"""Driver Code"""
# if __name__ == "__main__":
#     n = 12
#     res = for_loop(n)
#     print(f"\nfor 循环的求和结果 res = {res}")
#
#     res = while_loop(n)
#     print(f"\nwhile 循环的求和结果 res = {res}")
#
#     res = while_loop_ii(n)
#     print(f"\nwhile 循环（两次更新）求和结果 res = {res}")
#
#     res = nested_for_loop(n)
#     print(f"\n双层 for 循环的遍历结果 {res}")
