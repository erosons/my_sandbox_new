import math
import os
import random
import re
import sys
from collections import Counter
import logging


def sockMerchant(n: any):
    pairs_count = []
    try:
        n = input()
        if n.isalpha():
            int(n)
            ar = [random.randrange(1, n, 1) for i in range(n)]
            sorted_ar = sorted(ar)
            """
                The random array of stock file group together
                """
            group_pairs = Counter(sorted_ar)
            print(group_pairs)
            for values in group_pairs.values():
                if values % 2 == 0:
                    no_of_pairs = values/2
                    pairs_count.append(no_of_pairs)
                else:
                    odd_pairs = values//2
                    pairs_count.append(odd_pairs)
            return sum(pairs_count)

        else:
            if n.isdigit():
                ar = [random.randrange(1, int(n), 1) for i in range(int(n))]
                sorted_ar = sorted(ar)
                """
                The random array of stock file group together
                """
                group_pairs = Counter(sorted_ar)
                print(group_pairs)
                for values in group_pairs.values():
                    if values % 2 == 0:
                        no_of_pairs = values/2
                        pairs_count.append(no_of_pairs)
                    else:
                        odd_pairs = values//2
                        pairs_count.append(odd_pairs)
                return sum(pairs_count)

    except ValueError as v:
        logging.basicConfig(filename='pairs.log',
                            encoding='utf-8', filemode='w', level=logging.DEBUG)
        logging.debug('Invalid Parameter inputted')
