import os
import time

sources = []

# Entering paths where to copy files from

active = True
while active:
    queue = input('Enter the path you will copy the files from.\n(or \'q\' to exit queue): ')
    if queue == 'q':
        active = False
    else:
        sources.append(queue)

mainCatalogPath = 'C:\\Users\\Rubix327\\Desktop\\backups' ############# Изменить путь главного каталога!

# Changing the main reservation catalog path

changedPath = input('Enter new path of main reservation catalog:\n(or \'q\' if you don\'t want to): ')
if changedPath == 'q':
    pass
else:
    mainCatalogPath = changedPath

#
