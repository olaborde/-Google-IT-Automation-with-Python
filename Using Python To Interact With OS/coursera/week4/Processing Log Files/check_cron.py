import re
import sys

logfile = sys.argv[1]

with open(logfile) as file:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(line.strinp())
        print(result[1])