#!/bin/bash

#SBATCH --partition=health,lts,hawkcpu,infolab,engi,eng

# Request 1 hour of computing time
#SBATCH --time=0:02:00
#SBATCH --ntasks=3 --nodes=1

# Give a name to your job to aid in monitoring
#SBATCH --job-name reedFrostNetworkModel

# Write Standard Output and Error
#SBATCH --output="reedFrost.%j.%N.out"
#cd ${SLURM_SUBMIT_DIR} # cd to directory where you submitted the job

export PYTHONPATH=$PYTHONPATH:$HOME/pythonPackages

python3 NetworkClusterFile.py --P=$P --Q=$Q

exit