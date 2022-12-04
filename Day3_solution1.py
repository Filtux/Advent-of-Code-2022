with open('Day3_input') as file:
    input = file.read().splitlines()

runningTotal = 0

for line in input:
    compartment1, compartment2 = line[:len(line)//2], line[len(line)//2:]

    compartment1 = set([ord(char) for char in compartment1])
    compartment2 = set([ord(char) for char in compartment2])

    if (compartment1 & compartment2):
        value = compartment1 & compartment2
        value = value.pop()

        if value >= 97 and value <= 122: #Lower
            value = value - 96

        if value >= 65 and value <= 90: #Capital
            value = value - 38 #64 for Ascii and offset of 26 for alphabet (A = 27)

        runningTotal += value
        print(value)

print(runningTotal)