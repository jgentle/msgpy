#!/usr/bin/env python
"""
MSG.PY
v.1.1.0
By John Gentle
Updated 2016.06.14

Python script to combine input files for MODFLOW 96 and regenerate the selected iputs.
See README for usage instructions.
"""

import sys
import getopt
import argparse
import os
import csv
from decimal import *

############################################################
"""
TODO: ARGUMENTS
Refactor argument inputs into a config file that can be maintained seperately.
Load as a Parameter Object instead of parsing args.
"""
############################################################

# ARGUMENTS CONFIG
__author__ = 'jgentle'
parser = argparse.ArgumentParser(description='This is the msg.py MODFLOW 96 scalar generation script.')

# note: set required to false in order to use set_defaults on an option.
parser.add_argument('-id','--inputdir', help='Input directory path for wells and tablelinks data. Defaults to /csv_input/ if no argument is provided.',required=False)
parser.add_argument('-dd','--datadir', help='Input directory path for scalars data. Defaults to /csv_data/ if no argument is provided.',required=False)
parser.add_argument('-od','--outputdir',help='Output directory path. Defaults to /csv_output/ if no argument is provided.', required=False)
parser.add_argument('-w','--wells', help='Input file for wells data. Defaults to wells.csv if no argument is provided.',required=False)
parser.add_argument('-t','--tablelinks', help='Input file for tablelinks data. Defaults to tablelinks.csv if no argument is provided.',required=False)
parser.add_argument('-s','--scalars', help='Input file for scalars data. Defaults to scalars.csv if no argument is provided.',required=False)
# parser.add_argument('-wh','--wellsheaders', help='Headers for wells input data. Defaults to [\'A\', \'B\', \'C\', \'D\'] if no argument is provided.',required=False)
parser.add_argument('-th','--tablelinksheaders', help='Headers for tablelinks input data. Defaults to [\'Row\', \'Col\', \'Kzone\'] if no argument is provided.',required=False)
parser.add_argument('-sh','--scalarsheaders', help='Headers for scalars input data. Defaults to [\'sourceFile\', \'CZ1\', \'CZ2\', \'CZ3\', \'CZ4\', \'CZ5\', \'CZ6\', \'CZ7\', \'CZ8\', \'CZ9\', \'CZ10\', \'CZ11\'] if no argument is provided.',required=False)

# Set some defaults for simplicity.
parser.set_defaults(inputdir="/csv_input/")
parser.set_defaults(datadir="/csv_data/")
parser.set_defaults(outputdir="/csv_output/")
parser.set_defaults(wells="wells.csv")
parser.set_defaults(tablelinks="tablelinks.csv")
parser.set_defaults(scalars="scalars.csv")
# parser.set_defaults(wellsheaders="['A', 'B', 'C', 'D']")
parser.set_defaults(tablelinksheaders="['Row', 'Col', 'Kzone']")
parser.set_defaults(scalarsheaders="['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']")

# Parse the cli args (which will supercede the defaults).
args = parser.parse_args()

# SCRIPT PATHS
csv_input_subdirectory = args.inputdir
csv_data_subdirectory = args.datadir
csv_output_subdirectory = args.outputdir

# SOURCE DATA INPUTS
csv_input_file_wells = args.wells
csv_input_file_tablelinks = args.tablelinks
csv_input_file_scalars = args.scalars
# wells_headers = args.wellsheaders
tablelink_headers = args.tablelinksheaders
scalars_headers = args.scalarsheaders


############################################################
# DO NOT EDIT BEYOND THIS POINT!!!
############################################################

# MODULE VARIABLES
currentPath = os.getcwd()
csv_input_location = currentPath + csv_input_subdirectory
csv_data_location = currentPath + csv_data_subdirectory
csv_output_location = currentPath + csv_output_subdirectory

# MODULE DATA INPUTS AND OUTPUTS
wells_headers = []
scalars_data = []
tablelink_data = []
wells_output_headers = []
clean_wells_output_headers = []
wells_run_subheader = []
clean_wells_run_subheader = []
csv_wells = csv_input_location + csv_input_file_wells
csv_scalars = csv_data_location + csv_input_file_scalars
csv_tablelink = csv_input_location + csv_input_file_tablelinks


# MODULE METHODS

# LOG ARGUMENTS & OPTIONS
def LogArguments():
    print ("msg.py script arguments:")
    print ("-------------------------------")
    # print ("First argument: %s" % str(sys.argv[1]))
    # print ("Second argument: %s" % str(sys.argv[2]))
    # print ("Third argument: %s" % str(sys.argv[3]))
    # for i in xrange(total):
    #     print ("Argument # %d : %s" % (i, str(sys.argv[i])))
    print ("The total numbers of args passed to the script: %d" % total)
    print ("Args list: %s" % cmdargs)
    print ("Script name: %s" % str(sys.argv[0]))
    print ("Wells file: %s" % str(sys.argv[1]))
    print ("Tablelinks file: %s" % str(sys.argv[2]))
    print ("Scalars filee: %s" % str(sys.argv[3]))
    print (" ")
    return

def LogArgsParser():
    print ("msg.py script arguments:")
    print ("-------------------------------")
    print ("Input directory: %s" % args.inputdir )
    print ("Data directory: %s" % args.datadir )
    print ("Output directory: %s" % args.outputdir )
    print ("Input wells file: %s" % args.wells )
    print ("Input tablelinks file: %s" % args.tablelinks )
    print ("Input scalars file: %s" % args.scalars )
    # print ("Wells file headers: %s" % args.wellsheaders )
    print ("Tablelinks file headers: %s" % args.tablelinksheaders )
    print ("Scalars file headers: %s" % args.scalarsheaders )
    print (" ")
    return


# LOG VARIABLES
def LogVariables():
    print ("msg.py script variables:")
    print ("-------------------------------")
    # print ("Input chunk file: %s" % csv_input_file_scalars_arg)
    print ("csv_input_subdirectory: %s" % csv_input_subdirectory)
    print ("csv_data_subdirectory: %s" % csv_data_subdirectory)
    print ("csv_output_subdirectory: %s" % csv_output_subdirectory)
    print ("csv_input_file_wells: %s" % csv_input_file_wells)
    print ("csv_input_file_tablelinks: %s" % csv_input_file_tablelinks)
    print ("csv_input_file_scalars: %s" % csv_input_file_scalars)
    print ("tablelink_headers: %s" % tablelink_headers)
    print ("scalar_headers: %s" % scalars_headers)
    print (" ")
    return


# CONFIGURATION LOGGING
def LogConfigs():
    print ("msg.py script configuration:")
    print ("-------------------------------")
    print ("currentPath: %s" % currentPath)
    print ("csv_input_location: %s" % csv_input_location)
    print ("csv_data_location: %s" % csv_data_location)
    print ("csv_output_location: %s" % csv_output_location)
    print ("wells_headers: %s" % wells_headers)
    print ("scalars_data: %s" % scalars_data)
    print ("tablelink_data: %s" % tablelink_data)
    print ("wells_output_headers: %s" % wells_output_headers)
    print ("clean_wells_output_headers: %s" % clean_wells_output_headers)
    print ("wells_run_subheader: %s" % wells_run_subheader)
    print ("clean_wells_run_subheader: %s" % clean_wells_run_subheader)
    print ("csv_wells: %s" % csv_wells)
    print ("csv_tablelink: %s" % csv_tablelink)
    print ("csv_scalars: %s" % csv_scalars)
    print (" ")
    return


# HANDLING LISTS
def ReadCSVasList(csv_file):
    try:
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, dialect='excel',
                                quoting=csv.QUOTE_NONNUMERIC)
            datalist = []
            datalist = list(reader)
            return datalist
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
        print " "
        # break
    return


# Generic Method for Reference - Unused by Module.
def WriteListToCSV(csv_file_path, csv_filename, csv_columns, data_list):
    # print csv_file_path, csv_filename, csv_columns, data_list
    csv_file = csv_file_path + csv_filename
    columns = csv_columns
    data = data_list
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='excel',
                                quoting=csv.QUOTE_NONE)
            if columns:
                for header_row in columns:
                    writer.writerow(header_row)
            if data:
                for data_row in data:
                    writer.writerow(data_row)
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
        print " "
        # break
    return


def WriteWellsListToCSV(csv_file_path, csv_filename, csv_columns, data_list, wells_output_headers):
    csv_file = csv_file_path + csv_filename
    columns = csv_columns
    data = data_list

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='excel',
                                quoting=csv.QUOTE_NONE)
            if columns:
                writer.writerow(columns)
            for header_row in wells_output_headers:
                writer.writerow(header_row)
            for data_row in data:
                writer.writerow(data_row)
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
        print " "
        # break
    return


# HANDLING DICTS
def ReadCSVasDict(csv_file, headers, data_target):
    try:
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_target.append(row)
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
        print " "
        # break
    return


# Generic Method for Reference - Unused by Module.
def WriteDictToCSV(csv_file_path, csv_filename, csv_columns, dict_data):
    csv_file = csv_file_path + csv_filename
    columns = csv_columns
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
        print " "
        # break
    return


# CLEAN HEADER DATA
def CleanHeaderData(dirty_output_headers, clean_output_headers):
    for header_row in dirty_output_headers:
        clean_output_row = []
        for item in header_row:
            if (type(item) == float):
                new_item = int(item)
                clean_output_row.append(new_item)
            else:
                clean_output_row.append(item)
        clean_output_headers.append(clean_output_row)

############################################################
"""
TODO: CALCULATE SCALARS
    Decouple the hardcoded header values from within the module.
    Should reference the header values defined in the variables section.
    Need to determine the impact of this change before implementing it.
"""
############################################################

# CALCULATE SCALARS.
def CalculateScalarsPerRun(scalars_headers, scalars_data, wells_data, tablelink_headers, tablelink_data):

    # ALGORITHM
    for scalar_series in scalars_data:
        new_wells_data = []

        # get a ref to the sourcedata run hash.
        current_datasource = scalar_series["sourceFile"]

        # iterate over wells data.
        for wells_row in wells_data:

            # Handle the individual run subheaders that are inerted between runs.
            if(wells_row == wells_run_subheader[0]):
                new_wells_data.append(clean_wells_run_subheader[0])
                continue

            # get the current cell Row/Col values.
            current_layer = int(wells_row[0])
            current_row = int(wells_row[1])
            current_col = int(wells_row[2])
            original_pumping = float(wells_row[3])
            new_scalar = 0

            # iterate through tablelink for match in row.
            for tablelink_row in tablelink_data:

                # iterate through tablelink for match in col.
                if current_row == int(tablelink_row["Row"]):

                    # identify matches.
                    if current_col == int(tablelink_row["Col"]):
                        new_kzone = int(tablelink_row["Kzone"])

                        # Lookup the KZone in the current scalar_series.
                        if new_kzone == 0:
                            new_scalar = 0
                        elif new_kzone == 1:
                            new_scalar = scalar_series["CZ1"]
                        elif new_kzone == 2:
                            new_scalar = scalar_series["CZ2"]
                        elif new_kzone == 3:
                            new_scalar = scalar_series["CZ3"]
                        elif new_kzone == 4:
                            new_scalar = scalar_series["CZ4"]
                        elif new_kzone == 5:
                            new_scalar = scalar_series["CZ5"]
                        elif new_kzone == 6:
                            new_scalar = scalar_series["CZ6"]
                        elif new_kzone == 7:
                            new_scalar = scalar_series["CZ7"]
                        elif new_kzone == 8:
                            new_scalar = scalar_series["CZ8"]
                        elif new_kzone == 9:
                            new_scalar = scalar_series["CZ9"]
                        elif new_kzone == 10:
                            new_scalar = scalar_series["CZ10"]
                        elif new_kzone == 11:
                            new_scalar = scalar_series["CZ11"]
                        else:
                            break

            # Calculate the new pumping value.
            # new_pumping = float(original_pumping) * float(new_scalar)
            new_pumping = Decimal(str(original_pumping)) * Decimal(str(new_scalar))
            if (new_pumping == 0.0) or (new_pumping == -0.0):
                new_pumping = 0

            # Append the new wels row data to a temp object for this
            # scalar_series.
            new_wells_row = [current_layer, current_row, current_col, new_pumping]
            new_wells_data.append(new_wells_row)

        # Derive filename for new wells data object.
        cleaned_current_datasource = (current_datasource[:-4])
        new_wells_file_prefix = "wells_" + cleaned_current_datasource
        new_wells_filename = new_wells_file_prefix + ".dat"

        # Write the final wells data object to the new file.
        WriteWellsListToCSV(csv_output_location, new_wells_filename, wells_headers, new_wells_data, clean_wells_output_headers)


# START MODULE.
print (" ")
print ("Starting msg.py...")
print("Gathering ingredients... ")
print (" ")

# LogArguments()
LogArgsParser()
LogVariables()
LogConfigs()

print "Here we go! Calculating some tasty new scalar data!"
print ("Cooking the data... ")
print (" ")

############################################################
# STOP SCRIPT
# Development Only.
sys.exit()

# LOAD DATA SOURCES.

# WELLS
wells_data = ReadCSVasList(csv_wells)

# Trim headers from wells data
# Push first rows of wells data to new List for use when writing back out to file.
wells_output_headers.append(wells_data[0])

# Cleanup header data for writing later.
CleanHeaderData(wells_output_headers, clean_wells_output_headers)

# Trim off first row of headers before processing remaining run data.
wells_data.pop(0)

# Get a reference to the per run subheader values needed to filter out during run processing.
wells_run_subheader.append(wells_data[0])
# print wells_run_subheader

# Cleanup subheader data for writing later.
CleanHeaderData(wells_run_subheader, clean_wells_run_subheader)
# print clean_wells_run_subheader

# SCALARS
ReadCSVasDict(csv_scalars, scalars_headers, scalars_data)

# TABLELINK
ReadCSVasDict(csv_tablelink, tablelink_headers, tablelink_data)

print ("Seasoning the data... ")
print ("Come and see what the python has cookin!")
print (" ")

############################################################
# STOP SCRIPT
# Development Only.
sys.exit()

# RUN CALCULATIONS
CalculateScalarsPerRun(scalars_headers, scalars_data, wells_data, tablelink_headers, tablelink_data)

# END MODULE.
print ("Completed msg.py.")
print ("MMM, Mmm, mmm! That WAS some tasty scalar data!")
print ("Have a nice day!")
print (" ")
