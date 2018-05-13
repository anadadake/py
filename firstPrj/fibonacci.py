def fib(max):
    a, b = 0, 1
    while a < max:
        print('a:' + str(a))
        yield  a
        a, b = b, a + b



'''doc string'''



if __name__ == '__main__':
    print('####')
    print('####')
    p = fib(1000)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)
    next(p)


    # for n in fib(1000):
    #     print(n, end=' ')