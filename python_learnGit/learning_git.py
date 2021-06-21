#!/usr/bin/env python3
import os
import sys

def check_reboot():
    return os.path.exists('/run/reboot-required')

def main():
    pass

if __name__ == '__main__':
    print(check_reboot())
    sys.exit(1)
