with open ("data.txt") as f:
    pairs = f.readlines()
pairs = [pair.strip() for pair in pairs]

total = 0

for pair in pairs:
    #Split up assignment pairs
    assignments = pair.split(',')
    a1 = assignments[0]
    a2 = assignments[1]

    #Split individual assignments into two values
    a1 = a1.split('-')
    a2 = a2.split('-')
    a1_start = int(a1[0])
    a1_end = int(a1[1])
    a2_start = int(a2[0])
    a2_end = int(a2[1])

    if (a1_start >= a2_start and a1_end <= a2_end) or (a2_start >= a1_start and a2_end <= a1_end):
        total += 1

print(total)
