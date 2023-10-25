from math import *
sampletext = "RosesAreRedVioletsAreBlue"
col = []
row = []
k = 0
lenstr = int(sqrt(len(sampletext)))
for i in range(lenstr):
    for j in range(lenstr):
        row.append(sampletext[k])
        k = k + 1
    col.append(row)
    row = []
for i in range(lenstr):
    for j in range(lenstr):
        row.append(col[j][i])
    print(row[::-1])
    row = []