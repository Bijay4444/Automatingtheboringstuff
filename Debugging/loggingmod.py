import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) #It disables the log prints to enable it commet out this code

logging.debug('Start of the program')


def factorial(n):
    logging.debug('Satrat of factorial(%s)' % (n))

    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' %(i, total))
    
    logging.debug('Return value is %s' %(total))
    return total

print(factorial(5))
logging.debug('End of program')