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

>bcftools query -f'%ID [%AN]\n' "/nfs/scistore17/robingrp/madamega/rotation4/VCF_files/Am_all_stitchRun1_Chr8.final.vcf.gz" > id_out.txt


VCF convertion: 




