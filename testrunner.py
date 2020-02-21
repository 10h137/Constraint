import os
import re
import sys
from os import walk


files = []
for (dirpath, dirnames, filenames) in walk(os.path.abspath(sys.argv[1])):
    files.extend(filenames)
    break

files_to_delete = list(filter((lambda x: not re.search(r'(_|[A-z0-9])*\.param$', x)),files))
for f in files_to_delete:
    os.remove(os.path.join(sys.argv[1], f))

param_files = list(filter((lambda x: re.search(r'(_|[A-z0-9])*\.param$', x)),files))
for i in param_files:
    os.system("./" + sys.argv[2] + " " +  "prac.eprime " + os.path.abspath(sys.argv[1]) + "/" +  i + " -run-solver")


solution_files = []
for (dirpath, dirnames, filenames) in walk(os.path.abspath(sys.argv[1])):
    solution_files.extend(filenames)
    break
solution_files = list(filter((lambda x: re.search(r'(_|[A-z0-9])*\.solution$', x)),solution_files))

print(str(len(solution_files)) + " Solutions generated")
if(len(param_files) == len(solution_files)) :
    print("All solutions generated")
elif (len(solution_files == 0)):
    print("No solutions generated")