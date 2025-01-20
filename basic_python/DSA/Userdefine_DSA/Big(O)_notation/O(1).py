"""
Indexing over list
"""

# Time is constant for indexing the list irrespective of length or size

from time import time


def pricesearch(pricelist: list, price: str):
    return pricelist[price]


"time =  c"


start_time = time()

pricesearch([x for x in range(50)], '10')

end_time = time()

execution_time = end_time-start_time
