def func3(name='felixu'):
    def inner1():
        return 'inner1 function'

    def inner2():
        return 'inner2 function'

    if name == 'felixu':
        return inner1
    else:
        return inner2


func3_1 = func3()

print(func3_1)
print(func3_1())
print(func3()())
