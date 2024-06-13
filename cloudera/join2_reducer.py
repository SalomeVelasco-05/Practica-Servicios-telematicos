#!/usr/bin/env python
import sys

current_tv_show = None
current_count = 0
abc_found = False

for line in sys.stdin:
    line = line.strip()
    tv_show, value = line.split('\t')

    if current_tv_show == tv_show:
        if value.isdigit():
            current_count += int(value)
        elif value == "ABC":
            abc_found = True
    else:
        if current_tv_show and abc_found:
            print(f"{current_tv_show} {current_count}")
        current_tv_show = tv_show
        current_count = int(value) if value.isdigit() else 0
        abc_found = (value == "ABC")

if current_tv_show and abc_found:
    print(f"{current_tv_show} {current_count}")
