import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
    tableName = record[0]
    orderId = record[1]
    fields = record[2:]

    mr.emit_intermediate(orderId, (tableName, fields))


def reducer(key, list_of_values):
    orderId = key

    orderRecords = [x[1] for x in list_of_values if x[0] == "order"]
    itemRecords = [x[1] for x in list_of_values if x[0] == "line_item"]

    print itemRecords

    for orderRecord in orderRecords:
        for itemRecord in itemRecords:
            result = ["order", orderId, ] + orderRecord + ["line_item", orderId, ] + itemRecord
            assert(len(result) == 27)
            mr.emit(result)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
