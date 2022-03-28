def fun1(name='felixu'):
    return 'Hi, ' + name


print(fun1())


func_1 = fun1

del fun1

print(func_1())