#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) == 2:
        tv_show = parts[0]
        value = parts[1]
        if value.isdigit():
            print(f"{tv_show}\t{value}")
        elif value == "ABC":
            print(f"{tv_show}\tABC")
