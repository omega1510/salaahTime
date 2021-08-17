#!/usr/bin/env python3

# assumes a unix-like system, e.g. GNU/linux, macOS, BSD


import os
from format import colors

if os.name == "posix":
    output = os.popen(
        "curl -s https://saba-igc.org | grep Imsaak | grep -o '\([1-9]\:[0-5][0-9]\|1[0-2]\:[0-5][0-9]\) [a-z][a-z]'"
    ).read()

    output = str(output).splitlines()

    loop = 0

    labels = ["Imsaak", "Fajr", "Sunrise", "Zuhr", "Sunset", "Maghrib", "Midnight"]

    print(
        colors.bold
        + colors.underline
        + "Here are the prayer times for the San Francisco Bay Area:\n"
        + colors.reset
    )

    for time in output:
        print(colors.bold + colors.fg.green + labels[loop] + ": " + colors.reset + time)

        loop += 1
else:
    print("Incompatible operating system! Only posix systems are supported :(")
