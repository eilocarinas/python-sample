def main(num):
    row = []
    store = []
    rangoli = []
    line = ""
    for i in range(num):
        size = i * 2 + 1
        center = size //2
        for j in range (size):
            if j == center:
                char = chr(96 + num - i)
            elif j > center:
                char = chr(96 + num - i +(j-center))
            elif j < center:
                char = chr(96 + num - i +(center - j))
            row.append(char)
        store.append(row)
        row = []
    for i in range(num):
        length = (num - 1) * 2 +(num*2-1)
        center = length//2
        for j in range(length):
            if j % 2 == 0 and center - (i * 2) <= j <= center + (i * 2):
                line += store[i][len(store[i])-1]
                store[i].pop()
            else:
                line +="-"
        rangoli.append(line)
        line = ""
    for i in range(num):
        print(rangoli[i])
    for i in range(num-2, -1, -1):
        print(rangoli[i])
while True:
    num = int(input("Enter the size of rangoli: "))
    if num < 3 or num > 26:
        continue
    main(num)
