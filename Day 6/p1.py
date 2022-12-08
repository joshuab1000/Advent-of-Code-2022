with open ("data.txt") as f:
    signal = f.readlines()
signal = signal[0]

i = 2

startOfPacket = False
while not startOfPacket:
    marker = signal[i:i + 4]
    
    m1 = marker[0]
    m2 = marker[1]
    m3 = marker[2]
    m4 = marker[3]
    
    if (m1 != m2) and (m1 != m3) and (m1 != m4) and (m2 != m3) and (m2 != m4) and (m3 != m4):
        startOfPacket = True
    i += 1
    
print(i + 3)
