import os
import re
import sys
from os import walk


files = []
for (dirpath, dirnames, filenames) in walk(os.path.abspath(sys.argv[1])):
    files.extend(filenames)
    break

param_files = list(filter((lambda x: re.search(r'(_|[A-z0-9])*\.param', x)),files))

for i in param_files:
    os.system("./" + sys.argv[2] + " " +  "prac.eprime " + os.path.abspath(sys.argv[1]) + "/" +  i + " -run-solver")
