#!/bin/sh

#SBATCH -N 1
#SBATCH -n 48
#SBATCH -o msgpy.%N.%j.out
#SBATCH -e msgpy.%N.%j.err
#SBATCH -J msgpy_scalars
#SBATCH -p normal
#SBATCH -t 24:00:00
#SBATCH -A Groundwater-Decision

now=$(date)
echo ""
echo "Starting job at: $now"
echo ""

echo "Loading modules..."
module load intel
module load python
echo "Modules loaded."
echo ""

echo "Executing msg.py script..."
python msg.py
echo "Completed executing msg.py."
echo ""
