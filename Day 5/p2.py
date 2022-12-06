with open ("data.txt") as f:
    instructions = f.readlines()

#Start at the first instruction, get rid of everything else
i = 0
while instructions[i][:4] != 'move':
    i += 1
instructions = instructions[i:]

#Extract the numbers from each line, that's all we need
instructions = [instruction.strip() for instruction in instructions]
for i in range(len(instructions)):
    newInstruction = instructions[i].split(' ')
    instructions[i] = [newInstruction[1], newInstruction[3], newInstruction[5]]

stack1 = ['D','H','N','Q','T','W','V','B']
stack2 = ['D','W','B']
stack3 = ['T','S','Q','W','J','C']
stack4 = ['F','J','R','N','Z','T','P']
stack5 = ['G','P','V','J','M','S','T']
stack6 = ['B','W','F','T','N']
stack7 = ['B','L','D','Q','F','H','V','N']
stack8 = ['H','P','F','R']
stack9 = ['Z','S','M','B','L','N','P','H']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

#Carry out each move
for instruction in instructions:
    amount = int(instruction[0])
    fromStack = int(instruction[1]) - 1
    toStack = int(instruction[2]) - 1
    
    stacks[toStack] = stacks[toStack] + stacks[fromStack][(len(stacks[fromStack]) - amount):]
    stacks[fromStack] = stacks[fromStack][:(len(stacks[fromStack]) - amount)]

finalTops = ""

for stack in stacks:
    finalTops = finalTops + stack[len(stack) - 1]

print(finalTops)
