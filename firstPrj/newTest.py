import fibonacci2

if __name__ == '__main__':
    fib = fibonacci2.Fib(100)
    # print(fib)
    # print(fib.b)
    print(fib.__class__)
    print(fib.__doc__)
    print(fib.max)
    # print(fib.a)
    for a in fib:
        print(a)
