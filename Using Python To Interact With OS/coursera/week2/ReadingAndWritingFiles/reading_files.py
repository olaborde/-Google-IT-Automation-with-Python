

file = open("spyder.txt")


print(file.readline()) # read file one line at a time while remembers the last line 

print(file.read()) # read the whole text file\


file.close()

'''
Why close file?
 First, when a file is opening your script, your file system usually lock it down and so no other programs or scripts can use it until you're finished. 
 Second, there's a limited number of file descriptors that you can create before your file system runs out of them. Although this number might be high,
 it's possible to open a lot of files and deplete your file system resources.
 Third, leaving open files hanging around can lead to race conditions which occur when multiple processes try to modify and read from one resource at the same time and can cause all sorts of unexpected behavior. No one wins in a race condition.
'''