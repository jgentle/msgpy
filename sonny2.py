import csv
import copy
import numpy


# OPTION 1 - read files directly.

# print " "
# print "Well Data:"
# print " "
# wel = open('wel.csv', 'rb')
# weldata = csv.reader(wel)
# weldata = [row for row in wel]
# print weldata
# # for row in weldata:
# #     print row
# print " "

# print "Scalar Data:"
# print " "
# scl = open('scalars.csv', 'rb')
# scldata = csv.reader(scl)
# scldata = [row for row in scl]
# print scldata
# # for row in scldata:
# #     print row
# print " "

# print "Tablelink Data:"
# print " "
# tab = open('tablelink.csv', 'rb')
# tabdata = csv.reader(tab)
# tabdata = [row for row in tab]
# print tabdata
# # for row in tabdata:
# #     print row
# print " "

# OPTION 2 - make lists of the 3 files.

print "Well Data:"
print " "
wells_list = []
with open('wel.csv') as wel:
    reader = csv.reader(wel)
    next(reader)
    next(reader)
    for row in reader:
        # print row
        wells_list.append(row)  # or copy.deepcopy if inner lists exist
print wells_list
print " "
print "-------------------"


print "Tablelink Data:"
print " "
tablelink_list = []
with open('tablelink.csv') as tab:
    reader = csv.reader(tab)
    next(reader)
    for row in reader:
        # print row
        tablelink_list.append(row)
print tablelink_list
print " "
print "-------------------"


print "Scalar Data:"
print " "
scalars_list = []
with open('scalars.csv') as tab:
    reader = csv.reader(tab)
    next(reader)
    for row in reader:
        # print row
        scalars_list.append(row)
print scalars_list
print " "
print "-------------------"


# Processing Algorithm

# Step 1: Make copy of wells data.
wells_list_new = copy.deepcopy(wells_list)
# print "wells_list_new:"
# print wells_list_new


# Step 2: Lookup Kzone for each well(cell).
for row in wells_list_new:
    current_kzone = None
    current_kzone_index = []
    current_kzone_row = row[1]
    current_kzone_column = row[2]
    # Need to convert the original_scalar from string into float properly.
    original_scalar = row[3]
    print original_scalar
    # original_scalar = -float(original_scalar.translate(None, "(),"))
    # original_scalar = -float(original_scalar.replace('-', ''))
    original_scalar = original_scalar.replace('-', '')
    # original_scalar = float(original_scalar)
    print original_scalar
    print type(original_scalar)
    current_scalar = None
    # print current_kzone_row
    # print current_kzone_column
    # Get the row and column index for each Kzone.
    for row in tablelink_list:
        if row[0] == current_kzone_row:
            if row[1] == current_kzone_column:
                # print "Match found:"
                # print current_kzone_row
                # print current_kzone_column
                # print row
                # print " "
                # Assign the correct KZone value.
                current_kzone = row[2]
                # print "Current KZone:"
                # print current_kzone
                # print " "
                # Lookup the correct scalar value in sclars_list with the KZone value.
                # Calculate the correct index based on the Kzone.
                current_kzone_index = int(current_kzone)
                # print "Current KZone Index:"
                # print current_kzone_index
                # print " "
                # Iterating through the candidate scalar runs.
                index = 0
                # Need to skip first row of scalars.
                # Look at incsv and islice.
                iter_scalars_list = iter(scalars_list)
                next(iter_scalars_list)
                for row in scalars_list:
                    # print "row in scalars_list[index]"
                    # print index
                    # print "scalars_list[index][0]"
                    # print scalars_list[index][0]
                    # print "scalars_list[index][current_kzone_index]"
                    # print scalars_list[index][current_kzone_index]
                    # Need to convert the current_scalar from string into float properly.
                    current_scalar = scalars_list[index][current_kzone_index]
                    current_scalar = float(current_scalar)
                    print "current scalar value:"
                    print current_scalar
                    print type(current_scalar)
                    index += 1
                    print " "
                    # Calculate new scalar value
                    print "Original scalar value:"
                    print original_scalar
                    print type(original_scalar)
                    new_scalar = None
                    # STOPPAGE ISSUE 1
                    # Need to use numeric conversion ofthese values to get new scalar calculation.
                    # new_scalar = float(original_scalar) * float(current_scalar)
                    print new_scalar
                    # Write new line to new sourcefile.wells.dat object with new scalar value.
                    # # STOPPAGE ISSUE 2
                    # When done, write object to disc.
                    # Verify output.
                    # SEPARATE TASK
                    # Now run the files through modflow (separate script from this one).
