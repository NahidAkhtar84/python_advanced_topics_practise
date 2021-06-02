from functools import wraps

def my_logger(func):
    import logging
    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

    #This @wrap is provided to fix with which function to run if there is a stack of decorators at the original function
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}'.format(args))
        return func(*args, **kwargs)

    return wrapper


def my_timer(func):
    import time

    #This @wrap is provided to fix with which function to run if there is a stack of decorators at the original function
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(func.__name__, t2))
        return result

    return wrapper


import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('Diplay info: {}, {}'.format(name, age))


display_info('lam', 23)
    


