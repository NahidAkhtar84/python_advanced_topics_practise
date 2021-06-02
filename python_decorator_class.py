
class decorator_class:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('It is now at the decorator class call method!')
        print(f'{args}')
        return self.func(*args, **kwargs)

@decorator_class
def display():
    print('Display function is here!')

@decorator_class
def sum_two_numb(a, b):
    print('sum: {}'.format(a+b))

sum_two_numb(14, 67)
display()