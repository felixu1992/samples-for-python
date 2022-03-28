from functools import wraps


def decorator(func):
    def begin(args):
        pass

    def end(args):
        pass

    @wraps(func)
    def _func(*args, **kwargs):
        print('before')
        begin(args)
        ll = []
        for s in args:
            ll.append(s + '111111')
        if len(ll) == 0:
            func('sb', '108')
        else:
            func(*ll, **kwargs)
        end(args)
        print('after')

    return _func


@decorator
def decorated(name, age):
    print('I will decorated by decorator ' + name)


# decorated('felixu', '18')
decorated()
