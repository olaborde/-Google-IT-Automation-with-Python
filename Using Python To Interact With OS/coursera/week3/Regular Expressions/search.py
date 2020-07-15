import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: Error Peforming package upgrade"

'''
Alternate solution
index = log.index("[")
print(log[index+1:index+6])
'''
# Optimized solution
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(result[1])