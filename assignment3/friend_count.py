import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
    friend1 = record[0]
    # friend2 = record[1]
    mr.emit_intermediate(friend1, 1)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, sum(list_of_values)))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
