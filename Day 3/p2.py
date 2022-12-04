with open ("data.txt") as f:
    rucksacks = f.readlines()

rucksacks = [rucksack.strip() for rucksack in rucksacks]

ITEM_KEY = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
total = 0

for i in range(0, len(rucksacks), 3):
    for item in rucksacks[i]:
        if (item in rucksacks[i + 1]) and (item in rucksacks[i + 2]):
            shared_item = item

    shared_item_value = ITEM_KEY.index(shared_item) + 1
    total += shared_item_value
    
print(total)
