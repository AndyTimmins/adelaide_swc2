import sys

reader = open('pg76.txt', 'r')
line = reader.readline()
total_length = 0
line_count = 0

while line != '':
    total_length += len(line)
    line_count += 1
    line = reader.readline()
print total_length
print line_count

