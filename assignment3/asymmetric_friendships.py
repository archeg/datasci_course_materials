import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
    friend1 = record[0]
    friend2 = record[1]
    if (friend1 > friend2):
        mr.emit_intermediate(friend1 + " " + friend2, 1)
    else:
        mr.emit_intermediate(friend2 + " " + friend1, -1)
    # if friend1 > friend2:
    #     mr.emit_intermediate(friend1 + " " + friend2, 1)
    # else:
    #     mr.emit_intermediate(friend2 + " " + friend1, 1)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    friend1, friend2 = key.split()
    if (sum(list_of_values) != 0):
        mr.emit((friend1, friend2))
        mr.emit((friend2, friend1))
    # mr.emit((friend2, friend1))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
