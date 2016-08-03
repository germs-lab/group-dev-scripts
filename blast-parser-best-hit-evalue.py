import sys

d = {}

for line in open(sys.argv[1]):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    evalue = float(data[10])
    if evalue < 1e-5:
        if d.has_key(query):
            continue
        else:
            d[query] = hit
            print line,
