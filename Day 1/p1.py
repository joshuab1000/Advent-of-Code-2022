with open("list.txt") as f:
    cal_list = f.readlines()

cal_list = [number.strip() for number in cal_list]

from itertools import groupby
cal_list = [list(g) for k, g in groupby(cal_list, key=bool) if k]


most_cal = 0

for elf in cal_list:
    total = sum([int(food) for food in elf])
    if total > most_cal:
        most_cal = total

print(most_cal)
