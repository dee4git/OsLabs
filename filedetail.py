import os
import datetime
import time

filename = 'text.txt'
print("File name: " + str(os.path.basename(filename)))
print("Size of file : " + str(os.path.getsize(filename)) + " byte")

# Last modified time
mod_time = os.path.getmtime(filename)
modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))
print(f"Last Modified Time : {modificationTime}")

# Creation Time
c_time = os.path.getctime(filename)
creationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(c_time))
print(f"Creation Time : {creationTime}")

# path
path = os.path.abspath(filename)
print(f'The path of the file: {path}')

# file type
print(f'File Type: {os.path.splitext(filename)}')
