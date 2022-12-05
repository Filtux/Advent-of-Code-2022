with open ("Day5_input.txt") as file:
    input = file.read().splitlines()

    instructionArray = []
    
    stackArray = [["B", "S", "V", "Z", "G", "P", "W"],
    ["J", "V", "B", "C", "Z", "F"],
    ["V", "L", "M", "H", "N", "Z", "D", "C"],
    ["L", "D", "M", "Z", "P", "F", "J", "B"],
    ["V", "F", "C", "G", "J", "B", "Q", "H"],
    ["G", "F", "Q", "T", "S", "L", "B"],
    ["L", "G", "C", "Z", "V"],
    ["N", "L", "G"],
    ["J", "F", "H", "C"]]

    for line in input:

        if line.startswith("move"):

            line = line.split(" ")

            line = line[1], line[3], line[5]

            instructionArray.append(line)

    for instruction in instructionArray:

        popAmount = int(instruction[0])
        fromCol = int(instruction[1]) - 1
        toCol = int(instruction[2]) - 1

        for amount in range(1, popAmount + 1):

            toPut = stackArray[fromCol].pop()
            stackArray[toCol].append(toPut)

answer = ""

for i in stackArray:
    answer += i[-1]

print(answer)