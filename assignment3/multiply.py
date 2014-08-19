import MapReduce
import sys
from collections import defaultdict

"""
Matrices are 5x5
"""

matrix_length = 5
mr = MapReduce.MapReduce()


def calcTuple(t):
    if len(t) < 2:
        return 0
    assert(len(t) == 2)
    return t[0] * t[1]


def mapper(record):
    matrix, i, j, value = record  # matrix is "a" or "b'
    order = j if matrix == "a" else i
    for r in range(matrix_length):
        if matrix == "a":
            mr.emit_intermediate((i, r), (order, value))
        else:
            mr.emit_intermediate((r, j), (order, value))


def reducer(key, list_of_values):
    d = defaultdict(list)
    print key, list_of_values
    for k, v in list_of_values:
        d[k] += [v, ]
    result = sum([calcTuple(x) for x in d.values()])
    i, j = key
    mr.emit((i, j, result))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
