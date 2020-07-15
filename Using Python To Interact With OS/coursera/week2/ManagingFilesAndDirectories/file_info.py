import os
import datetime
os.path.abspath('spider.txt')
os.getcwd() # get current working directory
os.mkdir('new_dir') # to create a new directory
os.chdir('new_dir') # to change directory
os.rmdir('new_dir')
os.listdir('dir')
print(os.path.getsize('C:\\Users\\OML00\\Desktop\\GoogleIT\\UsingPythonToInteract_OS\\coursera\\week2\\ReadingAndWritingFiles\\spider.txt'))

print(os.path.getmtime('spider.txt'))  # will give a Unix timestamp
timestamp = os.path.getmtime('spider.txt')

datetime.datetime.fromtimestamp(timestamp)
datetime.datetime(2020, 1, 6, 7, 2, 3, 899999)