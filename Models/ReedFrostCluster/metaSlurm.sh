#!/bin/bash
#SBATCH --partition=health,lts,hawkcpu,infolab,engi,eng
#--Request 1 hour of computing time
#SBATCH --time=48:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#--Give a name to your job to aid in monitoring
#SBATCH --job-name runner
#--Write Standard Output and Error
#SBATCH --output="myjob.%j.%N.out"
cd ${SLURM_SUBMIT_DIR} # cd to directory where you submitted the job
bash distributor.sh clust.sh iterations.CSV
exit
