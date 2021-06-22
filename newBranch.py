#!/usr/bin/env python3
import sys

def cal():
    if 2+3==5:
        return True

if __name__ == '__main__':
    if cal():
        sys.exit(0)
    sys.exit(1)
