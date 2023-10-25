hour = int(input("Starting time l(hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

totMin = mins + dura
endHour = ((totMin // 60) + hour) % 24
endMins = totMin % 60

print(f"{endHour}:{endMins}")