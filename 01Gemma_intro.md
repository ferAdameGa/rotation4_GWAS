# GWAS with GEMMA

GEMMA github page: https://github.com/genetics-statistics/GEMMA?tab=readme-ov-file#installation

## Tutorial

Following tutorial from: https://github.com/rcc-uchicago/genetic-data-analysis-2/blob/master/slides.pdf

# Input
```
GEMMA requires four main input files containing genotypes, phenotypes, relatedness matrix and
(optionally) covariates. Genotype and phenotype files can be in two formats, either both in the
PLINK binary ped format or both in the BIMBAM format
```
# Prepare data for GWAS:

## Format for GEMMA:

#### format.genotypes.for.gemma.R

> install.packages("stringr", repos='http://cran.us.r-project.org')
>

### BIMBAM format

IDs must match

IDs excel (from python code):

C:\Users\madamega\Documents\ISTA\Rotations\4\IDs.txt

Check IDs of VCF:

> bcftools query -l "/nfs/scistore17/robingrp/madamega/rotation4/VCF_files/Am_all_stitchRun1_Chr1.final.vcf.gz" > id_vcf.txt

Different format:

```
10x2-13_Am_Pla_pb1196_v3.5
10x2-14_Am_Pla_pb1008_v3.5
10x2-15_Am_Pla_pb1253_v3.5
10x2-16_Am_Pla_pb1682_v3.5
10x2-17_Am_Pla_pb2190_v3.5
10x2-18_Am_Pla_pb1687_v3.5
10xNEW-Plate10-10_Am_Pla_pb0952_v3.5
10xNEW-Plate10-11_Am_Pla_pb0960_v3.5
10xNEW-Plate10-12_Am_Pla_pb1085_v3.5
10xNEW-Plate10-13_Am_Pla_pb1088_v3.5
10xNEW-Plate10-14_Am_Pla_pb1092_v3.5
10xNEW-Plate10-15_Am_Pla_pb1093_v3.5
10xNEW-Plate10-16_Am_Pla_pb1164_v3.5
10xNEW-Plate10-17_Am_Pla_pb1166_v3.5
10xNEW-Plate10-18_Am_Pla_pb1172_v3.5
10xNEW-Plate10-19_Am_Pla_pb1179_v3.5
```

Replace IDs file:

```
file = open("id_vcf.txt", "r")
vcf_id=file.readlines()
file.close()

ids=[]
for name in vcf_id:    
    splited=name.split("Am_")
    final=splited[1].split("_")
    ids.append(final[1])
    

with open('replace_id.txt','w') as tfile:
	tfile.write('\n'.join(ids))
```
SLURM script: "/nfs/scistore17/robingrp/madamega/rotation4/VCF_files/change_IDs.sh"


VCF convertion: 




