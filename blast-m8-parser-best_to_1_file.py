import sys

if len(sys.argv) == 1:
	sys.exit("USAGE: python %s <blast_m8_file> > <output>" % sys.argv[0])

# This script parses blast m8 table ouput and prints out the best hit for each query.
#```
#input: blast m8 output (tab delimited). It also reads in file name (in the format of: GENE.x.METAGID.*.m8)
#output: tab delimited file in the format of 
#GENE	METAGID	"blast best hit"
#
#to use with multiple *.m8 files:
#	for i in *.m8; do python blast-m8-parser-best_to_1_file.py $i; done > all_best.txt
#```

f = sys.argv[1]
arg = f.split('.x.')[0].split('.')[0]
metag = f.split('.x.')[1].split('.')[0]

d = {}

for line in open(f):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    if d.has_key(query):
        continue
    else:
        d[query] = hit
	print arg + "\t" + str(metag) + "\t" + line,
       # print line, 
