import os
import csv
from decimal import *


# INPUT VARS - EDIT THESE
csv_input_subdirectory = "/csv_input/"
csv_output_subdirectory = "/csv_output/"

# TEST DATA
# csv_input_file_wells = "wel.csv"
# csv_input_file_scalars = "scalars.csv"
# csv_input_file_tablelink = "tablelink.csv"

# REAL DATA
csv_input_file_wells = "wel_0.csv"
csv_input_file_tablelink = "tablelink_0.csv"
csv_input_file_scalars = "scalars_0.csv"

# TEST DATA Configs
scalars_headers = ['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']
tablelink_headers = ['Row', 'Col', 'Kzone']

# DO NOT EDIT BEYOND THIS POINT!!!

# MODULE VARIABLES
currentPath = os.getcwd()
csv_input_location = currentPath + csv_input_subdirectory
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
csv_scalars = csv_input_location + csv_input_file_scalars
csv_tablelink = csv_input_location + csv_input_file_tablelink


# MODULE METHODS
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
# print "Here we go! Calculating some tasty new scalar data!"

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

# RUN CALCULATIONS
CalculateScalarsPerRun(scalars_headers, scalars_data, wells_data, tablelink_headers, tablelink_data)

# END MODULE.
# print "MMM, Mmm, mmm! That WAS some tasty data!"
