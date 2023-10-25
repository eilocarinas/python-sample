def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0)  year % 4 == 400:
        leap = True
    else:
        leap = False
    # Write your logic here

    return leap


year = int(input())
print(is_leap(year))