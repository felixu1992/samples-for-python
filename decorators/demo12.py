from functools import wraps


def decorator1(func):
    @wraps(func)
    def _func():
        print('before1')
        func()
        print('after1')

    return _func


def decorator2(func):
    @wraps(func)
    def _func():
        print('before2')
        func()
        print('after2')

    return _func


@decorator1
@decorator2
def decorated():
    print('I will decorated by decorator')


decorated()
print(decorated.__name__)
