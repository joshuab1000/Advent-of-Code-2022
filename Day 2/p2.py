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
    # X = Lose      A = Rock
    # Y = Draw      B = Paper
    # Z = Lose      C = Scissors

    if me == 'X':
        if opponent == 'A':
            score += 3
        elif opponent == 'B':
            score += 1
        else:
            score += 2
    elif me == 'Y':
        if opponent == 'A':
            score += 1
        elif opponent == 'B':
            score += 2
        else:
            score += 3
        score += 3
    else:
        if opponent == 'A':
            score += 2
        elif opponent == 'B':
            score += 3
        else:
            score += 1
        score += 6
        
    total += score
    
print(total)   
