import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime) -%(levelname)s - %(message)s")

logging.debug('Start of program')

def factorial(n):
    logging.debug('Starting factorial program %s' % (n))

    Total = 1

    for i in range(1, n + 1):
        Total *= i
        logging.debug('i is %s, total is %s' %(i, Total ))

    logging.debug('Return value of total %s' %Total)

print(factorial(5))

logging.debug('End of the program')