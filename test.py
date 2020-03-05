import os
import re
import sys
from os import walk
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


def getSolutionFiles(dir):
    solution_files = []
    for (dirpath, dirnames, filenames) in walk(os.path.abspath(dir)):
        solution_files.extend(filenames)
        break
    print(len(solution_files))
    solution_files = list(filter((lambda x: re.search(r'[0-9]_[0-9]\.solution$', x)),solution_files))
    return solution_files

def getArr(file):
    split_name = file.split("_", 1)
    seed = int(split_name[0])
    size = int(split_name[1].split(".", 1)[0])
    file = open(file, 'r') 
    lines = file.readlines()
    time = float(lines[2].split(":", 1)[1])
    result = [seed, size, time]
    return result


def plotSolution(sol):
    markers = ['o', 's', 'd', 'x']
    plt.plot(sol[1], sol[2], markers[int(sol[0])],
             label=sol[1])
    # plt.legend(numpoints=1)
    plt.show()

def main():
    files = getSolutionFiles(sys.argv[1])
    numbers = []
    for file in files:
        numbers.append(getArr(file))
    print(numbers)
    plotSolution(numbers[0])





main()