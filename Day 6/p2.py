with open ("data.txt") as f:
    signal = f.readlines()
signal = signal[0]

i = 2

startOfPacket = False
while not startOfPacket:
    marker = signal[i:i + 14]
    currGroup = ""
    for char in marker:
        if char not in currGroup:
            currGroup = currGroup + char    
    if len(currGroup) == len(marker):
        startOfPacket = True
    
    i += 1
    
print(i + 13)
