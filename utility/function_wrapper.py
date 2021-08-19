from functools import wraps
import time
from utility.log_handler import logger

test_dict = {
    '1': 'This is a warning',
    '2': 'This is an error'
}


def log_measure(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.warning(test_dict['1'])
            return result
        except:
            logger.error(test_dict['2'], exc_info=True)
    return wrap