from utility.code_measure import time_measure
from utility.function_wrapper import log_measure
from utility.thread_handler import close_thread, ThreadWithException, thread_list


@time_measure
@log_measure
def x():

    # @time_measure only calculates when function runs successfully 
    xx = 2/2


x()
