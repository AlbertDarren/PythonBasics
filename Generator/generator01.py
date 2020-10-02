# Way 1
generator = (x * x for x in range(10))
print(generator.__next__())
print(next(generator))


# Way 2
def fib(length=1):  # 0,1,1,2,3 5,8
    n = 0
    a, b = 0, 1
    while n < length:
        yield a
        a, b = b, a + b
        n += 1
    # return '不能再生成元素了!'python3.6 的syntax


g = fib(2)
print(next(g))
print(next(g))
print(next(g))
