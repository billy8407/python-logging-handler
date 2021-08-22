from functools import wraps
import sys
import time
import traceback

from utility.log_handler import logger
from utility.thread_handler import close_thread, ThreadWithException, thread_list

test_dict = {
    'x': 'x is error'
}


def log_measure(func):
    log_dict = {'orignal_func': func.__name__}

    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            # logger.warning(test_dict[func.__name__], extra=log_dict)
            
            return result
        except:
            # string traceback
            log_dict['traceback'] = traceback.format_exc()

            # Prevent no key error in logger print 
            if func.__name__ in test_dict.keys():
                logger.error(test_dict[func.__name__], extra=log_dict)
            else:
                logger.error('', extra=log_dict)

            # Close threads if existed
            close_thread(func.__name__)
            
            sys.exit(1)
    
    return wrap