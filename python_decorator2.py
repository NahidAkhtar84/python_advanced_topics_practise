

def decorator_func(func):
    def inner_func(*args, **kwargs):
        print('In the decorattor wrapper function !')
        print('The variables values are: {}, {}'.format(a, b))
        return func()
    return inner_func


@decorator_func
def display():
    print('This is the display function !')

@decorator_func
def sum_two_numb(a, b):
    print('sum: {}'.format(a+b))


