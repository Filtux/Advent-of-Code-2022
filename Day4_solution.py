with open ("Day4_input") as file:
    input = file.read().splitlines()

count = 0
countB = 0

for line in input:

    print(line)

    line = line.split(',')

    line[0] = line[0].partition('-')
    line[1] = line[1].partition('-')

    elfOneRange = range(int(line[0][0]), int(line[0][2]) + 1)
    elfTwoRange = range(int(line[1][0]), int(line[1][2]) + 1)

    elfOneStart = elfOneRange.start
    elfOneEnd = elfOneRange.stop - 1
    elfTwoStart = elfTwoRange.start
    elfTwoEnd = elfTwoRange.stop - 1

    if elfOneStart <= elfTwoStart and elfOneEnd >= elfTwoEnd:
        count += 1

    elif elfTwoStart <= elfOneStart and elfTwoEnd >= elfOneEnd:
        count += 1

    #Part 2

    if elfOneEnd >= elfTwoStart and elfOneStart <= elfTwoEnd:
        countB += 1

print(count)    
print(countB)