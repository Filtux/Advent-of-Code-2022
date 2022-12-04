with open('Day3_input') as file:
    input = file.read().splitlines()

runningTotal = 0
count = 0
groupOfThree = []

for line in input:

    count += 1

    if count < 3:
        
        line = set([ord(char) for char in line])
        groupOfThree.append(line)

    else:

        line = set([ord(char) for char in line])
        groupOfThree.append(line)

        if (groupOfThree[0] & groupOfThree[1] & groupOfThree[2]):
            value = groupOfThree[0] & groupOfThree[1] & groupOfThree[2]
            value = value.pop()
            print(chr(value))

        if value >= 97 and value <= 122: #Lower
            value = value - 96

        if value >= 65 and value <= 90: #Capital
            value = value - 38 #64 for Ascii and offset of 26 for alphabet (A = 27)

        runningTotal += value
        groupOfThree = []
        count = 0

print(runningTotal)