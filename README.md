# MSG.PY 
### Modflow Scalar Generation for Python

Version: **v.0.1.5** | 
Last Updated: **2016.06.14**

### What is msg.py?
Msg.py is a python script to regenerate specific selected scalar inputs for MODFLOW 96 scenarios.

The script takes the targeted GAM's baseline wells.dat file and an exported tablelink data file from the targeted GAM's shapefile and combines them with a set of pre-determined scalar input values for the Model to generate a new set of candidate solution input wel.dat files for use in MODFLOW 96.

### Directory Structure
The msg.py script expects the following directory structure to exist:

    |-- msgpy/
        |-- csv_input/
            |-- wells and tablelinks files
        |-- csv_data/
            |-- scalars file(s)
        |-- csv_output/
            |-- new files created here
        |-- csv_utils/
            |-- several script utilities to help prepare data for use.
        |-- refs/
            |-- several docs to look to for troubleshooting and post processing.
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

### Script Arguments
The msg.py script is configurable and accepts arguments for the following options:

    - -id (input directory)
    - -dd (data directory)
    - -od (output directory)
    - -w (wells file)
    - -t (tablelinks file)
    - -s (scalars file)
    - -th (tablelinks headers)
    - -sh (scalars headers)

**All directory paths MUST include the trailing slash.**
**The header arrays MUST be passed in as a string (surrounded by quotes).**

It is recommended that all arguments be passed in as strings using the following syntax:

    ./msg.py -id "/my/inputs/" -dd "/my/data/" -od "/my/outputs/" \
        -w "wellsFile.csv" -t "tablelinksFile.csv" -s "scalarsFile.csv" \
        -th "['Header1', 'Header2', 'Header3']" \
        -sh "['Header1', 'Header2', 'Header3', 'Header4']"

__Warning: While it is possible to pass in paths directly, it is not recommended.__

#### Default Argument Values
Default values are provided for simplicity of use.
They are as follows:

    - input directory = "/csv_input/"
    - data directory = "/csv_data/
    - output directory = "/csv_output/"
    - wells file = "wells.csv"
    - tablelinks file = "tablelinks.csv"
    - scalars file = "scalars.csv"
    - tablelinks headers = "['Row', 'Col', 'Kzone']"
    - scalars headers = "['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']"

### Script Execution
Assuming you are using the default values specified, you can run msg.py by executing the following commands:

    $ python msg.py

Alternatively (after running _$ chmod +x msg.py_):

    $ ./msg.py

If you have custom arguments to pass in, the complete syntax is as follows:

    $ ./msg.py -id "/my/inputs/" -dd "/my/data/" -od "/my/outputs/" \
        -w "wellsFile.csv" -t "tablelinksFile.csv" -s "scalarsFile.csv" \
        -th "['Header1', 'Header2', 'Header3']" \
        -sh "['Header1', 'Header2', 'Header3', 'Header4']"

You can omit any arguments for which you are using the default values.

#### **_Enjoy your tasty data!_**
:stew: :yum: :purple_heart:








