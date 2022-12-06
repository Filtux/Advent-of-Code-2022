with open("Day6_input.txt") as file:
    input = file.read()

index = 0
uniqueCount = 0
overallCount = 0
success = 0

while index < (len(input) - 4) and success < 1:

    rangeOfLetters = input[index : (index + 4)]

    if len(set(rangeOfLetters)) == len(rangeOfLetters):

        print(index + 4)
        success += 1
                
    index += 1

# Part B

index = 0
success = 0

while index < (len(input) - 14) and success < 1:

    rangeOfLetters = input[index : (index + 14)]

    if len(set(rangeOfLetters)) == len(rangeOfLetters):
        
        print(index + 14)
        success += 1
                
    index += 1