lectures = int(input("no of lecture: "))

awake = 0

if lectures in range(1,100000):
    i = input("is there a coffee machine: ")
    for j in range(len(i)):
        if i[j] == "1": awake += 2

    if awake <= lectures:
        print(awake)
    else:
        print(lectures)
else:
    print("invalid number of lecture")