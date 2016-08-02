import sys

if len(sys.argv) == 1:
	sys.exit("USAGE: python %s <blast_m8_file> > <output>" % sys.argv[0])

# This script parses blast m8 table ouput and prints out the best hit for each query.
#```
#input: blast m8 output (tab delimited). It also reads in file name (in the format of: GENE.x.METAGID.*.m8)
#output: tab delimited file in the format of 
#GENE	METAGID	"blast best hit"
#
#to use with multiple *.m8.besthit files:
#	for i in *.m8.besthit; do python blast-m8-parser-best_to_1_file.py $i; done > all_best.txt
#```

f = sys.argv[1]
metag = f.split('.')[0]

for line in open(f):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
	print query + "\t" + str(metag) + "\t" + line,
       # print line, 
