import sys

#python blast-subset.py <file of list of ids to subset> <blastoutput>
#stores list of ids to subset by

l = []
for line in open(sys.argv[1]):
    l.append(line.rstrip())

#takes the blastoutput and subsets for gene ids in the list above
d = {}
for line in open(sys.argv[2]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    if hit in l:
        print line.rstrip()
