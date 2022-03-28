def func2(name='felixu'):
    print('begin func2 function')

    def inner1():
        return 'inner1 function'

    def inner2():
        return 'inner2 function'

    print(inner1())
    print(inner2())
    print('end func2 function')


func2()
