#from utility.log_handler import logger
from utility.function_wrapper import log_measure


@log_measure
def x():
    xx = 2/0

x()