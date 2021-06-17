#!/usr/bin/env python3

import re
import operator
from collections import defaultdict
import csv

error = {}
per_user = {}

with open('python_course2_final/syslog.log', 'r+') as logFile:
    for line in logFile:
        # Analyze type of Errors
        foundType = re.findall(r'ERROR ([\w \']+) ',line.strip())
        if foundType:
            error[foundType[0]] = error.get(foundType[0],0)+1

        # Analyze user Error and Info usage
        foundName_info = re.findall(r'INFO[^\(]+\(([\D .]+)\)',line.strip())
        foundName_error = re.findall(r'ERROR[^\(]+\(([\D .]+)\)',line.strip())
        if foundName_info:
            per_user[foundName_info[0]] = per_user.get(foundName_info[0],'')+'0'
        if foundName_error:
            per_user[foundName_error[0]] = per_user.get(foundName_error[0],'')+'1'
logFile.close()

# Handle per_user
for key,value in per_user.items():
    per_user[key] = [value.count('0'),value.count('1')]
# Error sort
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
# per_user sort
per_user = sorted(per_user.items(), key=operator.itemgetter(0))

'''------------------------------------------------------------------------------------'''
# Dictionary tranform to CSV
with open('error_message.csv', 'w+') as f:
    file = csv.writer(f, delimiter=',')
    file.writerow(['Error','Count'])
    for index in error:
        file.writerow(index)

with open('user_statistics.csv', 'w+') as f:
    file = csv.writer(f, delimiter=',')
    file.writerow(["Username", "INFO", "ERROR"])
    for index in per_user:
        file.writerow([index[0],index[1][0],index[1][1]])
