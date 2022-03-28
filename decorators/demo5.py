def decorator(func):
    def _func():
        print('before')
        func()
        print('after')

    return _func


def decorated():
    print('I will decorated by decorator')


decorated()

decorated = decorator(decorated)

decorated()
