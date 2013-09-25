import sys

reader = open('Pitching.csv', 'r')
line = reader.readline()
line = reader.readline()

while line != '':
    row = line.split(',')
    value = row[12]
    total_ipouts += float(value)
    count += 1
    line = reader.readline()
reader.close()


print "total_ipouts: " + str(total_ipouts)
print "count: " + str(count)
print "average: " + int(total_ipouts/count)



