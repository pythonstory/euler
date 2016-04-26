# 반복문에 의한 계산
def func1(max):
    x, y, n = 1, 2, 1 + 2
    i = 3
    sum = 2

    while n < max:
        if n % 2 == 0:
            sum += n
        x = y
        y = n
        n = x + y

        i += 1

    return sum


# 수열의 공식에 의한 계산
def func2(x, y, L):
    while y < L:
        x, y = y, 4 * y + x

    return (x + y - 2) / 4


if __name__ == '__main__':
    print(func1(4000000))

    print(func2(0, 2, 4000000))
