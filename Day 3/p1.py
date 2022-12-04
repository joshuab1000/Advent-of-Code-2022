with open ("data.txt") as f:
    rucksacks = f.readlines()

rucksacks = [rucksack.strip() for rucksack in rucksacks]

ITEM_KEY = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total = 0
for rucksack in rucksacks:
    #Divide rucksack into compartments
    compartment_length = len(rucksack)//2
    compartment1 = rucksack[:compartment_length]
    compartment2 = rucksack[compartment_length:]

    #Find the item that each compartment has in common
    shared_item = ""
    for item in compartment1:
        if item in compartment2:
            shared_item = item
            
    shared_item_value = ITEM_KEY.index(shared_item) + 1
    total += shared_item_value
    
print(total)
