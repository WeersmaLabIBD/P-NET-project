import os
import re

# this script is to build PWY -> gene list, because Humann database contains RXN -> gene list and PWY -> RNX, but no PWY -> gene list

with open("gmt.PWY.tmp") as f:
    for line in f:
        tmp_line=line.split()
        for i in range(3,len(tmp_line)):
            file = open("metacyc_reactions_level4ec_only.uniref", "r")
            for n in file:
                if re.search(tmp_line[3],n): 
                    tmp_gene=n.split()       
                    new_gene=tmp_gene[2:len(tmp_gene)]
                    pattern= r"\b{}\b".format(tmp_line[3])
                    new_line=re.sub(pattern,' '.join(str(x) for x in new_gene),' '.join(str(x) for x in tmp_line))
        with open('Test.txt', 'a') as f1:
            f1.write(new_line + os.linesep)
