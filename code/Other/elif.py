n = int(input("Enter number: "))

if n % 2 != 0 or n in range(6,21):
    print("Weird")
else:
    if n in range(2,6) or n > 20: print("Not Weird")
