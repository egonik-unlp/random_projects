#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import csv
import sys
import os
csv.field_size_limit(sys.maxsize)

np.random.seed(42)

def go_short(input_file, sieve):
    with open(f'{input_file[:-4]}_{sieve}_random.csv', 'w') as f:
        with open(input_file, 'r') as file:
            header = next(file)
            f.write(header)
            for line in file:
                rn = np.random.uniform()
                if rn < 1/sieve:
                    f.write('\n')
                    f.write(line)        

 


if __name__ == '__main__':
    if len(sys.argv) == 3:
        go_short(sys.argv[1], int(sys.argv[2]))
    else:
        print('Parametros erroneos')
