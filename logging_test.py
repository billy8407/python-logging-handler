from utility.function_wrapper import log_measure
from utility.thread_handler import close_thread, ThreadWithException, thread_list 


@log_measure
def x():
    xx = 2/0

x()