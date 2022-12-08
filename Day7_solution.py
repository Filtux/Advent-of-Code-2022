with open ("Day7_input.txt") as file:
    input = file.read().splitlines()

commandList = []
directory = []
folders = []
index = 0

for command in input:
    commandList.append(command)

for command in commandList:
    #print(command)

    if "cd" in command and ".." not in command:
        #print(command)
        command = command[5:]
        #Perform regex to strip just folder name
        folders.append(command)

    if "dir" in command:
        command = command[4:]
        folders.append(command)

print(set(folders)) #List of every unorganised folder

while index < len(commandList):

    currentCommand = commandList[index]
    previousCommand = commandList[index - 1]

    if "cd" in currentCommand and ".." not in currentCommand:
        currentDirectory = currentCommand[5:]
        print(currentDirectory)

        directory.append(currentDirectory)





    index += 1

print(directory)

# for command in input:

    

# for command in input:

#     if "dir" in command:
#         command = command[4:]
#         indexOfFolder = folders.index(command)
        
#         print(indexOfFolder)
#         print(command)

#     if command.isalnum:
#         print(folders[indexOfFolder])
        




