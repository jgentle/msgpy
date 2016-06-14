# MSG.PY 
### Modflow Scalar Generation for Python

Version: **v.1.1.0** | 
Updated: **2016.06.14** | 
Author: **John Gentle** | 
Contact: **jgentle@tacc.utexas.edu**


### What is msg.py?
Msg.py is a python script to regenerate specific selected scalar inputs for MODFLOW 96 scenarios.

The script takes the targeted GAM's baseline wells.dat file and an exported tablelink data file from the targeted GAM's shapefile and combines them with a set of pre-determined scalar input values for the Model to generate a new set of candidate solution input wel.dat files for use in MODFLOW 96.

### Directory Structure
The msg.py script expects the following directory structure to exist:

    |-- msgpy/
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

The msg.py script expects to find specific files in these locations.

### Script Inputs
The input files required are as follows:

    - wells         (the base wells.dat file used by MODFLOW 96 for the scenario)
    - tablelinks    (the linkage table data extracted from GAM shape file to connect wells with cells by zone)
    - scalars       (the input values for multiplying well values in corresponding cells)

### Script Configs
You must edit the headers for the SCALAR and TABLELINK files to match your input data structure.
By default, they are defined as follows:

    scalars_headers = ['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']
    tablelink_headers = ['Row', 'Col', 'Kzone']

### Script Arguments
The msg.py script is configurable and expects arguments (in this specific order) for:

    - wells
    - tablelinks
    - scalars

### Script Execution
To run the msg.py script you can execute either of the following commands:

    $ python msg.py WELLS.CSV TABLELINKS.CSV SCALARS.CSV

Alternatively (after running _$ chmod +x msg.py_):

    $ ./msg.py WELLS.CSV TABLELINKS.CSV SCALARS.CSV

#### Enjoy your tasty data!






