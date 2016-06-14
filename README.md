# MSG.PY 
### Modflow Scalar Generation for Python
> Version: v.1.1.0

> Updated 2016.06.14

> Author: John Gentle 

> Contact: jgentle@tacc.utexas.edu

## What is msg.py?
Python script to combine input files for MODFLOW 96 and regenerate the selected iputs.

## Target use case
For use in generating new wel.dat input files based on predetermined scalar values.

## General Usage

### Organization
The msg.py script expects the following directory structure to exist:

    | msg.py_root/
        |-- csv_input/
            |-- wells and tablelink file(s)
        |-- csv_data/
            |-- scalar file(s)
        |-- csv_output/
            |-- new files created here
        |-- csv_utils/
            |-- several script utilities to help prepare data for use.
        |-- refs/
            |-- several docs to look to for troubleshooting and usage patterns.
        |-- msg.py  
        |-- msgpy-slurm-sbatch.sh
        |-- msgpy-parametric-launcher.slurm
        |-- paramslist
        |-- README.md
        |-- .gitignore

### Script Inputs
The msg.py script expects to find specific files in these locations.
The input files required are as follows:

    - wells         (the base wells.dat file used by MODFLOW 96 for scenario)
    - tablelinks    (the linkage table data extracted from GAM shape file to connect wells with cells by zone)
    - scalars       (the input values for multiplying well values in corresponding cells)

### Script Arguments
The msg.py script is configurable and expects arguments (in this specific order) for:
    - wells
    - tablelinks
    - scalars

### Script Configs
You must edit the headers for the SCALAR and TABLELINK files to match your input data structure.
By default, they are defined as follows:

    scalars_headers = ['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']
    tablelink_headers = ['Row', 'Col', 'Kzone']

### Script Execution
To run the msg.py script you can execute either of the following commands:

    $ python msg.py WELLS.CSV TABLELINKS.CSV SCALARS.CSV

    OR

    $ ./msg.py WELLS.CSV TABLELINKS.CSV SCALARS.CSV

#### Enjoy your tasty data!






