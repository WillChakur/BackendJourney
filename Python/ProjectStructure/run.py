#We are going to use this py file to trigger the entire project
import constants as c
from functions import *

def run():
    primes = calculatePrimes(start=c.START, finish=c.FINISH)
    print(primes)

"""
We need to use if __name__ == "__main__": because when we import a file, it execute
the code that within it. By using this line of code, we prevent the code from running
when the file is imported.
"""

if __name__ == "__main__":
    run()