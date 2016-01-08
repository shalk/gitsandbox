def f1():
    x=88
    def f2(x=x):
        print x
    return f2

f=f1()
f()
