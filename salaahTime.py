#!/usr/bin/env python3

# assumes a unix-like system, e.g. GNU/linux, macOS, BSD

import os

output = os.popen(
    "curl -s https://saba-igc.org | grep Imsaak | grep -o '[0-9]\:[0-5][0-9]'"
).read()

output = str(output).splitlines()

loop = 0

for time in output:
    if loop == 0:
        print("Imsaak: %s am" % time)
    if loop == 1:
        print("Fajr: %s am" % time)
    if loop == 2:
        print("Sunrise: %s am" % time)
    if loop == 3:
        print("Zuhr: %s pm" % time)
    if loop == 4:
        print("Sunset: %s pm" % time)
    if loop == 5:
        print("Maghrib: %s pm" % time)
    if loop == 6:
        print("Midnight: %s am" % time)

    loop += 1
