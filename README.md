# P-NET-project


### step1. Humann database prepare

```
Humann provides severl useful files: 
 (1)  map_uniref90_name.txt; map_metacyc-rxn_name.txt; map_metacyc-pwy_name.txt (the biological full names of Uniref90 genes, reactions and pathways)
 (2)  metacyc_pathways (pathway -> reaction list)
 (3)  metacyc_reactions_level4ec_only.uniref (reactions -> gene list)
 
P-NET database structure contains three main files, ReactomePathway.gmt format (all the terms and their gene lists), ReactomePathway.txt (annotation file, terms and genes, and their full names) and ReactomePathwayRelation.txt (parent -> child file, namely PWY -> RXN, RXN -> Uniref90 gene)

Note, metacyc_pathways and  metacyc_reactions_level4ec_only.uniref  are not equal: not all RXN in metacyc_pathways can be found in metacyc_reactions_level4ec_only.uniref

```
