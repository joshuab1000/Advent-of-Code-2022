with open("list.txt") as f:
    cal_list = f.readlines()

cal_list = [number.strip() for number in cal_list]

from itertools import groupby
cal_list = [list(g) for k, g in groupby(cal_list, key=bool) if k]
total_cal_list = []
for elf in cal_list:
    total = sum([int(food) for food in elf])
    total_cal_list.append(total)

top_three_sum = sum(sorted(total_cal_list, reverse=True)[:3])
print(top_three_sum)
