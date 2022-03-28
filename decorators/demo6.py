def decorator(func):
    def _func():
        print('before')
        func()
        print('after')

    return _func


@decorator
def decorated():
    print('I will decorated by decorator')


decorated()
print(decorated.__name__)