with open ("data.txt") as f:
    rounds = f.readlines()

rounds = [round.strip() for round in rounds]

score = 0
total = 0

for round in rounds:
    score = 0
    opponent = round[0]
    me = round[2]

    # Me:           Opponent:
    # X = Rock      A = Rock
    # Y = Paper     B = Paper
    # Z = Scissors  C = Scissors

    if me == 'X':
        if opponent == 'A':
            score += 3
        elif opponent == 'C':
            score += 6
        score += 1
    elif me == 'Y':
        if opponent == 'B':
            score += 3
        elif opponent == 'A':
            score += 6
        score += 2
    else:
        if opponent == 'C':
            score += 3
        elif opponent == 'B':
            score += 6
        score += 3

    total += score

print(total)   
