import os
import re

# this script is to build parent -> child relationship file

with open("gmt.RXN.tmp") as f:
    for line in f:
        tmp_line=line.split()
        for i in range(3,len(tmp_line)):
            new_line=tmp_line[1]+'\t'+tmp_line[i]
            with open('parent.child.rxn.txt', 'a') as f1:
                f1.write(new_line + os.linesep)
