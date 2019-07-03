#!/usr/bin/python

import numpy as np
import sys

mul = []
for line in sys.stdin:
    line = line.strip().split(',')
    line = [float(item) for item in line]
    x = line[0:-1]
    y = line[-1]

    xy = [i*y for i in x]
    xx = np.dot(np.array(x).reshape(-1,1), np.array(x).reshape(1, -1)).tolist()
    xx += [xy]
    mul.append(xx)

mul = np.array(mul)
summul = mul.sum(axis=0)
sumlist = summul.tolist()
print(sumlist)
