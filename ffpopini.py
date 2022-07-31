#!/usr/bin/env python3
#

import os
import re

mozilla_ff_path = os.path.expanduser('~') + "/.mozilla/firefox"
ff_ini_path = mozilla_ff_path + "/profiles.ini"

dirs = [ f.path for f in os.scandir(mozilla_ff_path) if f.is_dir() ]

# Filter profiles

profiles = []
ini_str = ""

print("Start updating...\n")
i = 0
for d in dirs:
    if re.match(".*\..*\.", d):
        full_name = d
        dir_p = d.split("/")[-1]
        #print(dir_p)
        name = d.split(".")[2]
        print("%s profile found " % name)
        t = """[Profile%s]
Name=%s
IsRelative=1
Path=%s\n\n""" % (i, name, dir_p)
        ini_str += t
        i += 1


with open(ff_ini_path, "w") as f:
    f.write(ini_str)

print("\nFirefox profiles.ini updated.")
