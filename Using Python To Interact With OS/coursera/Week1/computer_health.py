import shutil
import math
import psutil # cpu_percent returns a number showing how much of the cpu is being used


du = shutil.disk_usage("/")
print(du)
Per_of_disk_space = du.free / du.total * 100
print(Per_of_disk_space)
'''
The amount of CPU used at each instant can change a lot, 
since processes are starting and finishing all the time.
 So this function receives an interval of seconds 
and returns an average percentage of usage in that interval.
'''
cpu_usage = psutil.cpu_percent(0.1)
print(cpu_usage)