#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1],'r+') as file:
    for line in file.readlines():
        newline = line.strip().replace('jane','jdoe')
        subprocess.run(
            ["mv", ".."+line.strip(), ".."+newline]
        )
file.close()
