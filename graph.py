import os
import re
import sys
from os import walk
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np




from matplotlib.ticker import MaxNLocator

ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

def getInfoFiles(dir):
    solution_files = []
    for (dirpath, dirnames, filenames) in walk(os.path.abspath(dir)):
        solution_files.extend(filenames)
        break
    solution_files = list(filter((lambda x: re.search(r'(LBS)*[0-9]+_[0-9]+\.param\.info$', x)),solution_files))

    return solution_files

def getArr(dir, file):
    details = {}
    name = file
    if("LBS" in file):
        split_name = file.split("S", 1)[1].split("_", 1)
        details["size"] = int(split_name[0])
        details["seed"] = int(split_name[1].split(".", 1)[0])
    else:
        split_name = name.split("_", 1)
        details["seed"] = int(split_name[0])
        details["size"] = int(split_name[1].split(".", 1)[0])
    file = open(dir+"/"+ file, 'r') 
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


def plotSolution(sol, symbol, field):
    # if(satisfied == sol["satisfied"]) :
    if(sol["satisfied"]):
        color = "#00ff00"
    else:
        color = "#FF0000"
    plt.plot(sol["size"], sol[field], symbol, color=color, alpha=0.45)
    plt.title(field)
    plt.ylabel(field)
    plt.xlabel("Number of Cards")
    # plt.legend(numpoints=1)

def main():

    if(len(sys.argv) == 4):
        key = sys.argv[3]
    else:
        key = sys.argv[2]
    files1 = getInfoFiles(sys.argv[1])

    info_files1 = []
    for file in files1:
        info_files1.append(getArr(sys.argv[1], file))

    info_files1.sort(key = lambda x: x["size"])
    for f in info_files1:
        if(key in f):
            plotSolution(f, "o", key)


    # secodn dir if exists
    if(len(sys.argv) == 4):
        files2 = getInfoFiles(sys.argv[2])
        info_files2 = []
        for file in files2:
            info_files2.append(getArr(sys.argv[2], file))

        info_files2.sort(key = lambda x: x["size"])
        for f in info_files2:
            if(key in f):
                plotSolution(f, "x", key)

    plt.show()
    # plt.figure()
    # for f in info_files:
    #     if(key in f):
    #         plotSolution(f, True, key)
    # plt.show()






main()