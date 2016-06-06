#!/bin/sh

#------------------Script Usage--------------------
# > module load launcher
# > ls $TACC_LAUNCHER_DIR
# > cp $TACC_LAUNCHER_DIR/launcher.slurm .
# Edit script (this file) to set headers as follows:

#------------------Scheduler Options--------------------
#SBATCH -N 4
#SBATCH -n 96
#SBATCH -o msgpy-parametric.%N.%j.out
#SBATCH -e msgpy-parametric.%N.%j.err
#SBATCH -J Msgpy-Parametric
#SBATCH -p normal
#SBATCH -t 72:00:00
#SBATCH -A Groundwater-Decision

 #------------------General Options---------------------
 export TACC_LAUNCHER_PPN=48

 #------------------Script---------------------
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

#------------------Create paramlist File---------------------
# Example file:
# myprogram -i data1 -o output1 >& run1.out
# myprogram -i data2 -o output2 >& run2.out
# myprogram -i data3 -o output3 >& run3.out
# myprogram -i data4 -o output4 >& run4.out
# myprogram -i data5 -o output5 >& run5.out
# myprogram -i data6 -o output6 >& run6.out

#------------------Launch Script---------------------
# > sbatch launcher.slurm
