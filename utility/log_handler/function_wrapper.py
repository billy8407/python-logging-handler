from functools import wraps
import sys
import time
import traceback

from utility.log_handler.logging_handler import logger
from utility.log_handler.thread_handler import close_thread, ThreadWithException, thread_list

function_log = {
    'x': 'x is error'
}


def log_measure(func):

    # Used in logging.Formmater
    formatter = {'orignal_func': func.__name__}

    @wraps(func)
    def wrap(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            # logger.warning(test_dict[func.__name__], extra=log_dict)

            return result
        except:
            # string traceback
            formatter['traceback'] = traceback.format_exc()

            # Prevent no key error in logger print
            if func.__name__ in function_log.keys():
                logger.error(function_log[func.__name__], extra=formatter)
            else:
                logger.error('', extra=formatter)

            # Close threads if existed
            close_thread(func.__name__)

            sys.exit(1)

    return wrap
