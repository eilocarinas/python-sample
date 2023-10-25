from math import *
text = "RosesAreRedVioletsAreBlue"
strlen = int(sqrt(len(text)))
print(strlen)
arr1 = []
for j in range(strlen):
    for i in range(len(text)):
    #arr0.append(text[i])
        arr1.append(text[i])
print(arr1)
