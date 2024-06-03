# GWAS with GEMMA

GEMMA github page: https://github.com/genetics-statistics/GEMMA?tab=readme-ov-file#installation

## Tutorial

Following tutorial from: https://github.com/rcc-uchicago/genetic-data-analysis-2/blob/master/slides.pdf

# Input
``` slurm
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

### Filter IDs on excel:

Slurm script: "/nfs/scistore17/robingrp/madamega/rotation4/VCF_files/filter_IDs.sh"
``` ruby
#!/bin/bash
#
#----------------------------------------------------------------
# running a multiple independent jobs
#----------------------------------------------------------------
#
#  Defining options for slurm how to run
#----------------------------------------------------------------
#
#SBATCH --job-name=filger
#SBATCH --output=filter.log
#        %A and %a are placeholders for the jobid and taskid, resp.
#
#Number of CPU cores to use within one node
#SBATCH -c 5
#
#Define the number of hours the job should run. 
#Maximum runtime is limited to 10 days, ie. 240 hours
#SBATCH --time=240:00:00

#SBATCH --mail-user=madamega@ist.ac.at
#SBATCH --mail-type=ALL
#SBATCH --array=1-8
#18
#IMPORTANT NUMBER OF FILES TO BE PROCESSED
#number of files in a directory: ls -1 | wc -l
#for this job: ls /nfs/scistore18/vicosgrp/madamega/artemiaImprinting/analysis/F1C1KS/*1.fastq -1 | wc -l = 11

#Define the amount of RAM used by your job in GigaBytes
#In shared memory applications this is shared among multiple CPUs
#SBATCH --mem=99G
#
#Do not requeue the job in the case it fails.
#SBATCH --no-requeue
#
#Do not export the local environment to the compute nodes
#SBATCH --export=NONE
#SBATCH --reservation=vicosgrp_75
unset SLURM_EXPORT_ENV

#module load 
module load bcftools

#IMPORTANT DO NOT LOAD JAVA 
# Search all the fastq files from the "data" directory and generate the array
dir='/nfs/scistore17/robingrp/madamega/rotation4/VCF_files/rename_Am_all_stitchRun1_Chr'


file=$(ls ${dir}*.vcf.gz | sed -n ${SLURM_ARRAY_TASK_ID}p)
base=$(basename $file ".vcf.gz")
echo ${base}

bcftools view -S IDs.txt ${base}.vcf.gz > filtered_vcf/filt_chr${SLURM_ARRAY_TASK_ID}.vcf
```

/nfs/scistore17/robingrp/madamega/rotation4/VCF_files/filtered_vcf/*

VCF convertion: 




