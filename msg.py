import os
import csv

print "Here we go! Calculating some tasty new scalar data!"

# MODULE VARIABLES
currentPath = os.getcwd()
csv_input_subdirectory = "/csv_input/"
csv_input_location = currentPath + csv_input_subdirectory
csv_output_subdirectory = "/csv_output/"
csv_output_location = currentPath + csv_output_subdirectory

# DATA INPUTS
csv_wells = csv_input_location + "wel.csv"
wells_headers = []
csv_scalars = csv_input_location + "scalars.csv"
scalars_headers = ['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']
scalars_data = []

# DATA OUTPUTS
wells_csv_output_filename = "NewWells.csv"
wells_output_headers = []
clean_wells_output_headers = []
scalars_csv_output_filename = "NewScalars.csv"
csv_tablelink = csv_input_location + "tablelink.csv"
tablelink_headers = ['Row', 'Col', 'Kzone']
tablelink_data = []
tablelink_csv_output_filename = "NewTablelink.csv"

# MODULE METHODS

# HANDLING LISTS
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
    print csv_file_path, csv_filename, csv_columns, data_list
    csv_file = csv_file_path + csv_filename
    columns = csv_columns
    data = data_list
    try:
        with open(csv_file, 'w') as csvfile:
            # writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONE)
            if columns:
                for header_row in columns:
                    writer.writerow(header_row)
            if data:
                for data_row in data:
                    writer.writerow(data_row)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return


def WriteWellsListToCSV(csv_file_path, csv_filename, csv_columns, data_list, wells_output_headers):
    # print csv_file_path, csv_filename, csv_columns, data_list, wells_output_headers
    csv_file = csv_file_path + csv_filename
    # print csv_file
    columns = csv_columns
    # print columns
    data = data_list
    # print data
    # print wells_output_headers

    try:
        with open(csv_file, 'w') as csvfile:
            # writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONE)
            if columns:
                writer.writerow(columns)
            for header_row in wells_output_headers:
                writer.writerow(header_row)
            for data_row in data:
                writer.writerow(data_row)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return


# HANDLING DICTS
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

    # ALGORITHM
    for scalar_series in scalars_data:
        # print scalar_series
        new_wells_data = []

        # get a ref to the sourcedata run hash.
        current_datasource = scalar_series["sourceFile"]

        # iterate over wells data.
        for wells_row in wells_data:
            # print wells_row

            # get the current cell Row/Col values.
            current_layer = int(wells_row[0])
            current_row = int(wells_row[1])
            current_col = int(wells_row[2])
            original_pumping = float(wells_row[3])
            new_scalar = 0
            # print current_row, current_col, original_pumping

            # iterate through tablelink for match in row.
            for tablelink_row in tablelink_data:
                # print tablelink_row, current_row, current_col, original_pumping

                # iterate through tablelink for match in col.
                if current_row == int(tablelink_row["Row"]):
                    # print current_row, tablelink_row["Row"]

                    # identify matches.
                    if current_col == int(tablelink_row["Col"]):
                        new_kzone = int(tablelink_row["Kzone"])
                        # print "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
                        # print current_col, tablelink_row["Col"]
                        # print "MATCH!"
                        # print "For the current cell at Row ", current_row, " in Col ", current_col, " the Kzone is ", new_kzone #int(tablelink_row["Kzone"])

                        # Lookup the KZone in the current scalar_series.
                        if new_kzone == 0:
                            new_scalar = 0
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 1:
                            new_scalar = scalar_series["CZ1"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 2:
                            new_scalar = scalar_series["CZ2"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 3:
                            new_scalar = scalar_series["CZ3"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone== 4:
                            new_scalar = scalar_series["CZ4"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 5:
                            new_scalar = scalar_series["CZ5"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 6:
                            new_scalar = scalar_series["CZ6"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 7:
                            new_scalar = scalar_series["CZ7"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 8:
                            new_scalar = scalar_series["CZ8"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 9:
                            new_scalar = scalar_series["CZ9"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 10:
                            new_scalar = scalar_series["CZ10"]
                            # print "The new scalar is ", new_scalar
                        elif new_kzone == 11:
                            new_scalar = scalar_series["CZ11"]
                            # print "The new scalar is ", new_scalar
                        else:
                            # print "No matching scalar value found."
                            break

            # Calculate the new pumping value.
            # print original_pumping, new_scalar
            new_pumping = float(original_pumping) * float(new_scalar)
            if (new_pumping == 0.0) or (new_pumping == -0.0):
                new_pumping = 0
            # print new_pumping

            # Append the new wels row data to a temp object for this scalar_series.
            new_wells_row = [current_layer, current_row, current_col, new_pumping]
            # print new_wells_row
            new_wells_data.append(new_wells_row)
            # print new_wells_data

        # Derive filename for new wells data object.
        cleaned_current_datasource = (current_datasource[:-4])
        # print cleaned_current_datasource
        new_wells_file_prefix = "wels_" + cleaned_current_datasource # + ".dat"
        # print new_wells_file_prefix
        new_wells_filename = new_wells_file_prefix + ".dat"

        # print new_wells_filename
        # verifying data types.
        # print type(csv_output_location), csv_output_location        # string
        # print type(new_wells_filename), new_wells_filename          # string
        # print type(wells_output_headers), wells_output_headers      # list
        # print type(wells_headers), wells_headers                    # list
        # print type(new_wells_data), new_wells_data                  # list

        # OUTPUT
        # print "Writing out new data..."
        # Write the final wells data object to the new file.
        WriteWellsListToCSV(csv_output_location, new_wells_filename, wells_headers, new_wells_data, clean_wells_output_headers)


# USE DATA INPUTS

# WELLS
wells_data = ReadCSVasList(csv_wells)
# print "Current wells Data: ", wells_data

# Cleanup wells data
# Push first two rows of wels data to new List for use when writing back out to file.
wells_output_headers.append(wells_data[0])
wells_output_headers.append(wells_data[1])
# print "Wells Output Headers: ", wells_output_headers

# Cleanup header data for writing later.
for header_row in wells_output_headers:
    # print header_row
    clean_wells_output_row = []

    for item in header_row:
        # print item
        # print type(item)
        if (type(item) == float):
            new_item = int(item)
            clean_wells_output_row.append(new_item)
        else:
            clean_wells_output_row.append(item)

    # print clean_wells_output_row
    clean_wells_output_headers.append(clean_wells_output_row)

# print clean_wells_output_headers

# Trim off first two rows for processing.
wells_data.pop(0)
# print "Wells data with one pop: ", wells_data
wells_data.pop(0)
# print "Wells data with two pops: ", wells_data
# We want to use this remaining data for calculating the scalars.

# SCALARS
ReadCSVasDict(csv_scalars, scalars_headers, scalars_data)
# print "Current scalars data: ", scalars_data

# TABLELINK
ReadCSVasDict(csv_tablelink, tablelink_headers, tablelink_data)
# print "Current tablelink data: ", tablelink_data

# RUN CALCULATIONS
CalculateScalarsPerRun(scalars_headers, scalars_data, wells_data, tablelink_headers, tablelink_data)

# TEST WRITE OUT NEW DATA.
# WriteWellsListToCSV(csv_output_location, wells_csv_output_filename, wells_headers, wells_data, wells_output_headers)
# WriteDictToCSV(csv_output_location, scalars_csv_output_filename, scalars_headers, scalars_data)
# WriteDictToCSV(csv_output_location, tablelink_csv_output_filename, tablelink_headers, tablelink_data)

# END OF MODULE.
print "MMM, Mmm, mmm! That WAS some tasty data!"
