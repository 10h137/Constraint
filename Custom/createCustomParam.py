import os
import re
import sys
from os import walk

from random import seed
from random import randint

seed(1)
seeds = []

for i in range(0, 21):
    seeds.append(randint(0,10000000))

for i in range(11,16):
    for j in seeds:
        os.system("java LBSGen " + str(i) + " " + str(j) + " > " + str(j) + "_" + str(i) + ".param")