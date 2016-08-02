library(plyr)
library(reshape2)

## This R script takes the blast best hits and convert them to a count table: gene as rows, and metag id as columns
#```
#input: 4 column table output from blast-m8-parser-best_to_1_file.py
#    ```
#    16S_Ribosomal_RNA_Methyltransferase     4454769 GMS2XNS02G8AQD  HQ451074.1.gene23.p01   32.5    40      26      1       146     265
#     2       40      4.4e-04 27.7
#16S_Ribosomal_RNA_Methyltransferase     4459840 GMS2XNS02HWYKB  HQ451074.1.gene23.p01   37.2    43      27      0       205     77
#      59      101     4.5e-06 34.3
#16S_Ribosomal_RNA_Methyltransferase     4459843 GMS2XNS01AQG1Q  DQ345788.gene.p01       39.4    33      20      0       301     203
#     69      101     1.5e-04 28.9
#    ```
#output: a spread out sparse matrix, missing values are filled with NA
#```
# USAGE: Rscript convert_bests_to_counts.R <blast_best_hit> <cut-off e-value> <output_table>
args<-commandArgs(TRUE)

## all_best.txt 
data<-read.delim(args[1], sep="\t", header=F)
## subset by e-value
test<-subset(data, V13 < args[2])
## counting, V1 is the gene names, V2 is the metag id, V4 is the blast hit
test_long<-count(test, c("V1", "V2", "V4"))

## creating a sparse matrix formatted table
test_wide<-dcast(test_long, V1+V4 ~ V2, value.var="freq", fill = 0)
write.table(test_wide, args[3], sep="\t", quote=F, row.names=F)
