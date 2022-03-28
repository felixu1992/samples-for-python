def func4():
    return 'Hi, felixu'


def before(func):
    print("before")
    print(func())


before(func4)
