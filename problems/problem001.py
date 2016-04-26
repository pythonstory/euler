def func1(max):
    sum = 0
    for i in range(1, max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


# n 이하 d의 약수 합 계산
def func2(n, d):
    n //= d
    return d * n * (n + 1) // 2


if __name__ == '__main__':
    print(func1(10))
    print(func1(1000))

    L, a, b = 1000 - 1, 3, 5

    print(func2(L, a) + func2(L, b) - func2(L, a * b))
