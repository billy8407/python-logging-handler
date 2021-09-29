from functools import wraps
import time


def time_measure(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('func %s duration time: %s' % (func.__name__, end - start))
        return result

    return wrap
