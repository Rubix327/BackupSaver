import os
import time

sources = []

# Entering paths where to copy files from

active = True
while active:
    queue = input('\n>> Enter the path you will copy the files from.\n(or \'q\' to exit queue): ')
    if queue == 'q':
        active = False
    else:
        sources.append(queue)

# Changing the main reservation catalog path (through the file mainCatalog.txt)

with open('backupSaver/mainCatalog.txt', 'r') as MC:
    mainCatalogPath = MC.read()

print('\nThe path of the main reservation catalog is: ' + mainCatalogPath)
changedPath = input('>> Enter new path if you want (or \'q\' if you don\'t want): ')
if changedPath == 'q':
    pass
else:
    mainCatalogPath = changedPath
    with open('backupSaver/mainCatalog.txt', 'w') as MC:
        MC.write(changedPath)
    
print('\nCatalog path now is: ' + mainCatalogPath + '\n')

# Setting up date and time

date = time.strftime('%d-%m-%Y')
time = time.strftime('%H-%M-%S')
datePath = mainCatalogPath + os.sep + date

# Setting up a comment

setComment = input('>> Enter the comment if you want (or \'q\' if you don\'t want): ')
if setComment == 'q':
    timeAndComment = time
else:
    timeAndComment = time + ' ' + setComment

# Creating the linked list of source files paths

dec = '\', \''
files = dec.join(sources)

# Creating the folders if they don't exist

if not os.path.exists(mainCatalogPath):
    os.mkdir(mainCatalogPath)
if not os.path.exists(datePath):
    os.mkdir(datePath)

# Setting up the zip command

savePath = mainCatalogPath + os.sep + date + os.sep + timeAndComment + '.zip'

zipCommand = 'powershell.exe Compress-Archive -Path ' + '\'' + files + '\'' + ' -DestinationPath ' + '\'' + savePath + '\''

if os.system(zipCommand) == 0:
    print('\nBackup successfully created at ' + savePath)
else:
    print('\nError while saving backup!')