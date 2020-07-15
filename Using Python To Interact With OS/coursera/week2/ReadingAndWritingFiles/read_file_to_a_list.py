file = open('spider.txt')  # open the file
lines = file.readlines()   #read all the lines
file.close()               # close the file

lines.sort()
print(lines)