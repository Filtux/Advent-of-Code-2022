totalCalories = 0
calorieArray = []

with open ('Day1_input.py') as file:
    input = file.readlines()

    for line in input:

        if line == "\n":
            calorieArray.append(totalCalories)
            totalCalories = 0

        else:
            totalCalories += int(line)
            
calorieArray.sort()

print(calorieArray[-1]) #Answer 1

print(calorieArray[-1] + calorieArray[-2] + calorieArray[-3]) #Answer 2

    