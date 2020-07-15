# !/usr/bin/env python3
#!"C:\Python33\python.exe"
import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


# cpu_percent() returns a float showing the current system-wide CPU use as a percentage
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERRORT!")
else:
    print("Optimal Health!")    


# for linux run chmod +x <name of the script>

