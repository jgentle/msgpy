import os
import csv
# import copy


print "Awwwwww SNAP! Time to make this data taste better!"


# VARIABLES
currentPath = os.getcwd()
csv_input_subdirectory = "/csv_input"
csv_input_location = currentPath + csv_input_subdirectory
csv_output_subdirectory = "/csv_output"
csv_output_location = currentPath + csv_output_subdirectory

# METHODS

# LISTS
def ReadCSVasList(csv_file):
    try:
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            datalist = []
            datalist = list(reader)
            return datalist
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return


def WriteListToCSV(csv_file_path, csv_filename, csv_columns, data_list):
    csv_file = csv_file_path + csv_filename
    # print csv_file
    columns = csv_columns
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            if columns:
                writer.writerow(columns)
            for data in data_list:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return


def WriteWellsListToCSV(csv_file_path, csv_filename, csv_columns, data_list, wells_output_headers):
    csv_file = csv_file_path + csv_filename
    # print csv_file
    columns = csv_columns
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            if columns:
                writer.writerow(columns)
            for data in wells_output_headers:
                writer.writerow(data)
            for data in data_list:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return


# DICTS
def ReadCSVasDict(csv_file, headers, data_target):
    try:
        with open(csv_file) as csvfile:
            # print "The current file is: ", csv_file
            # print " "
            reader = csv.DictReader(csvfile)
            # if headers:
                # print "Data Headers: ", headers
            # print "Row Data: "
            for row in reader:
                # print row
                data_target.append(row)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
            print " "
    # print " "
    return


def WriteDictToCSV(csv_file_path, csv_filename, csv_columns, dict_data):
    csv_file = csv_file_path + csv_filename
    # print csv_file
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
    return


# CALCULATE SCALARS.
def CalculateScalarsPerRun(scalars_headers, scalars_data, wells_data, tablelink_headers, tablelink_data):
    print "Here we go! Calculating some tasty scalar data!"
    print " "

    # SCALAR DATA
    # print "============================="
    # print "Scalar Data:"
    # print " "
    # # print scalars_headers
    # # print scalars_data
    # for scalar_series in scalars_data:
    #     print "sourceFile: ", scalar_series["sourceFile"]
    #     print "CZ1: ", scalar_series["CZ1"]
    #     print "CZ2: ", scalar_series["CZ2"]
    #     print "CZ3: ", scalar_series["CZ3"]
    #     print "CZ4: ", scalar_series["CZ4"]
    #     print "CZ5: ", scalar_series["CZ5"]
    #     print "CZ6: ", scalar_series["CZ6"]
    #     print "CZ7: ", scalar_series["CZ7"]
    #     print "CZ8: ", scalar_series["CZ8"]
    #     print "CZ9: ", scalar_series["CZ9"]
    #     print "CZ10: ", scalar_series["CZ10"]
    #     print "CZ11: ", scalar_series["CZ11"]
    #     print " "

    # WELLS DATA
    # print "============================="
    # print "Wells Data:"
    # print " "
    # # print wells_data
    # for wells_row in wells_data:
    #     # print wells_row
    #     print "Layer: ", wells_row[0]
    #     print "Row: ", wells_row[1]
    #     print "Col: ", wells_row[2]
    #     print "Pumping: ", wells_row[3]
    #     print " "

    # TABLELINK DATA
    # print "============================="
    # print "Tablelink Data:"
    # print " "
    # # print tablelink_headers
    # # print tablelink_data
    # for tablelink_row in tablelink_data:
    #     print "Row: ", tablelink_row["Row"]
    #     print "Col: ", tablelink_row["Col"]
    #     print "Kzone: ", tablelink_row["Kzone"]
    #     print " "

    # Need to refactor this using new var names.
    # for row in wells_data:
    #     current_kzone = None
    #     current_kzone_index = []
    #     current_kzone_row = row[1]
    #     current_kzone_column = row[2]
    #     original_scalar = row[3]
    #     current_scalar = None
    #     # Need to check that the values are floats.
    #     print "Current Wells Data:"
    #     print "Row: " , current_kzone_row
    #     print type(current_kzone_row)
    #     print "Col: " , current_kzone_column
    #     print type(current_kzone_column)
    #     print "Original Scalar: " , original_scalar
    #     print type(original_scalar)
    #     print "Current Scalar: " , current_scalar
    #     print " "
    #     # Get the row and column index for each Kzone.
    #     for row in tablelink_data:
    #         print "Current Tablelink Data:"
    #         print row
            # print row['Kzone']
            # if row[0] == current_kzone_row:
            #     if row[1] == current_kzone_column:
            #         print "Match found:"
            #         print current_kzone_row
            #         print current_kzone_column
            #         print row
            #         print " "
            #         # Assign the correct KZone value.
            #         current_kzone = row[2]
            #         print "Current KZone:"
            #         print current_kzone
            #         print " "
            #         # Lookup the correct scalar value in sclars_list with the KZone value.
            #         # Calculate the correct index based on the Kzone.
            #         current_kzone_index = int(current_kzone)
            #         print "Current KZone Index:"
            #         print current_kzone_index
            #         print " "
                    # Iterating through the candidate scalar runs.
    #                 index = 0
    #                 # Need to skip first row of scalars.
    #                 # Look at incsv and islice.
    #                 iter_scalars_list = iter(scalars_list)
    #                 next(iter_scalars_list)
    #                 for row in scalars_list:
    #                     # print "row in scalars_list[index]"
    #                     # print index
    #                     # print "scalars_list[index][0]"
    #                     # print scalars_list[index][0]
    #                     # print "scalars_list[index][current_kzone_index]"
    #                     # print scalars_list[index][current_kzone_index]
    #                     # Need to convert the current_scalar from string into float properly.
    #                     current_scalar = scalars_list[index][current_kzone_index]
    #                     print "current scalar value:"
    #                     print current_scalar
    #                     print type(current_scalar)
    #                     index += 1
    #                     print " "
    #                     # Calculate new scalar value
    #                     print "Original scalar value:"
    #                     print original_scalar
    #                     print type(original_scalar)
    #                     new_scalar = None
    #                     # STOPPAGE ISSUE 1
    #                     # Need to use numeric conversion ofthese values to get new scalar calculation.
    #                     # new_scalar = float(original_scalar) * float(current_scalar)
    #                     print new_scalar
    #                     # Write new line to new sourcefile.wells.dat object with new scalar value.
    #                     # # STOPPAGE ISSUE 2
    #                     # When done, write object to disc.
    #                     # Verify output.
    #                     # SEPARATE TASK
    #                     # Now run the files through modflow (separate script from this one).

    # ALGORITHM
    for scalar_series in scalars_data:
        # get a ref to the sourcedata run hash.
        current_datasource = scalar_series["sourceFile"]
        # iterate over wells data.
        for wells_row in wells_data:
            # get the current cell Row/Col values.
            current_row = wells_row[1]
            current_col = wells_row[2]
            current_scalar = wells_row[3]
            # print "* * * * * * * * * * * * * * *"
            # print current_row, current_col, current_scalar
            # print " "
            # iterate through tablelink for match in row.
            for tablelink_row in tablelink_data:
                # print "============================="
                # print tablelink_row, current_row, current_col, current_scalar
                # print " "
                # iterate through tablelink for match in col.
                if current_row == int(tablelink_row["Row"]):
                    # print "----------------------------------"
                    # print current_row, tablelink_row["Row"]
                    # print " "
                    # identify matches.
                    if current_col == int(tablelink_row["Col"]):
                        print "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
                        print current_col, tablelink_row["Col"]
                        print "MATCH!"
                        print "For the current cell at Row ", current_row, " in Col ", current_col, " the Kzone is ", tablelink_row["Kzone"]
                        # Lookup the KZone in the current scalar_series.
                        # Calculate the new scalar value.
                        # Append the new wels row data to a temp object for this scalar_series.
                        # Write the final wels data object out after completing iteration of scalars_series.
                        # print scalar_series
                        if int(tablelink_row["Kzone"]) == 0:
                            print "The new scalar is null."
                        elif int(tablelink_row["Kzone"]) == 1:
                            print "The new scalar is ", scalar_series["CZ1"]
                        elif int(tablelink_row["Kzone"]) == 2:
                            print "The new scalar is ", scalar_series["CZ2"]
                        elif int(tablelink_row["Kzone"]) == 3:
                            print "The new scalar is ", scalar_series["CZ3"]
                        elif int(tablelink_row["Kzone"]) == 4:
                            print "The new scalar is ", scalar_series["CZ4"]
                        elif int(tablelink_row["Kzone"]) == 5:
                            print "The new scalar is ", scalar_series["CZ5"]
                        elif int(tablelink_row["Kzone"]) == 6:
                            print "The new scalar is ", scalar_series["CZ6"]
                        elif int(tablelink_row["Kzone"]) == 7:
                            print "The new scalar is ", scalar_series["CZ7"]
                        elif int(tablelink_row["Kzone"]) == 8:
                            print "The new scalar is ", scalar_series["CZ8"]
                        elif int(tablelink_row["Kzone"]) == 9:
                            print "The new scalar is ", scalar_series["CZ9"]
                        elif int(tablelink_row["Kzone"]) == 10:
                            print "The new scalar is ", scalar_series["CZ10"]
                        elif int(tablelink_row["Kzone"]) == 11:
                            print "The new scalar is ", scalar_series["CZ11"]
                        else:
                            print "No matching scalar value found"


    print " "
    print "That WAS some tasty data!"


# INPUTS

# WELLS
csv_wells = csv_input_location + "/wel.csv"
wells_headers = None
wells_data = ReadCSVasList(csv_wells)
# print "Current wells Data: "
# print wells_data
# print " "
wells_csv_output_filename = "/NewWells.csv"

# Cleanup wells data
# Push first two rows of wels data to new List for use when writing back out to file.
wells_output_headers = []
wells_output_headers.append(wells_data[0])
wells_output_headers.append(wells_data[1])
# print "Wells Output Headers: "
# print wells_output_headers
# print " "
# Trim off first two rows for processing.
wells_data.pop(0)
# print "Wells data with one pop: "
# print wells_data
# print " "
wells_data.pop(0)
# print "Wells data with two pops: "
# We want to use this data for calculating the scalars.
# print wells_data
# print " "


# SCALARS
csv_scalars = csv_input_location + "/scalars.csv"
# print csv_scalars
# ReadCSVasDict(csv_scalars)
scalars_headers = ['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']
scalars_data = []
ReadCSVasDict(csv_scalars, scalars_headers, scalars_data)
# print "Current scalars data: "
# print scalars_data
# print " "
scalars_csv_output_filename = "/NewScalars.csv"


# TABLELINK
csv_tablelink = csv_input_location + "/tablelink.csv"
# print csv_tablelink
# ReadCSVasDict(csv_tablelink)
tablelink_headers = ['Row', 'Col', 'Kzone']
tablelink_data = []
ReadCSVasDict(csv_tablelink, tablelink_headers, tablelink_data)
# print "Current tablelink data: "
# print tablelink_data
# print " "
tablelink_csv_output_filename = "/NewTablelink.csv"


# RUN CALCULATIONS

# Step 1: Make copy of wells data.
# Is this necessary?? I don't think it is...
# wells_data_new = copy.deepcopy(wells_data)
# print "wells_list_new:"
# print wells_list_new

CalculateScalarsPerRun(scalars_headers, scalars_data, wells_data, tablelink_headers, tablelink_data)


# OUTPUT
print " "
print "Writing out new data..."

# Testing.
# WriteListToCSV(csv_output_file, test_csv_columns, csv_data_list)
# WriteDictToCSV(csv_output_location, csv_output_filename, csv_columns, dict_data)

# Using Data.
# WriteListToCSV(csv_output_location, wells_csv_output_filename, wells_headers, wells_data)
WriteWellsListToCSV(csv_output_location, wells_csv_output_filename, wells_headers, wells_data, wells_output_headers)
WriteDictToCSV(csv_output_location, scalars_csv_output_filename, scalars_headers, scalars_data)
WriteDictToCSV(csv_output_location, tablelink_csv_output_filename, tablelink_headers, tablelink_data)

print " "
print "Say WRITE THE DATA again! I dare you!"

