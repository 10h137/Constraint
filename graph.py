import os
import re
import sys
from os import walk
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


def getInfoFiles(dir):
    solution_files = []
    for (dirpath, dirnames, filenames) in walk(os.path.abspath(dir)):
        solution_files.extend(filenames)
        break
    print(len(solution_files))
    solution_files = list(filter((lambda x: re.search(r'[0-9]+_[0-9]+\.param\.info$', x)),solution_files))
    print(len(solution_files))

    return solution_files

def getArr(file):
    details = {}
    split_name = file.split("_", 1)
    details["seed"] = int(split_name[0])
    details["size"] = int(split_name[1].split(".", 1)[0])
    file = open(file, 'r') 
    lines = file.readlines()

    for line in lines:
        value = float(line.split(":", 1)[1])
        if("SavileRowTotalTime" in line):
            details["savile_time"] = value;
        elif("SolverNodes" in line):
            details["nodes"] = value;
        elif("SolverTotalTime" in line):
            details["solver_time"] = value;
        elif("SolverSatisfiable" in line):
            details["satisfied"] = bool(value);
        elif("SATClauses" in line):
            details["clauses"] = value;

    return details


def plotSolution(sol, satisfied, field):
    if(satisfied == sol["satisfied"]) :
        plt.plot(sol["size"], sol[field], "o")
        plt.title(field + " - Solved = " + str(satisfied) )
        plt.ylabel(field)
        plt.xlabel("Number of Cards")
    # plt.legend(numpoints=1)

def main(key):
    files = getInfoFiles(sys.argv[1])
    info_files = []
    for file in files:
        info_files.append(getArr(file))
    print(info_files)
    info_files.sort(key = lambda x: x["size"])
    for f in info_files:
        if(key in f):
            plotSolution(f, False, key)
    plt.show()
    plt.figure()
    for f in info_files:
        if(key in f):
            plotSolution(f, True, key)
    plt.show()






main(sys.argv[2])