import csv
import os


def ReadCSVasDict(csv_file, headers):
    try:
        with open(csv_file) as csvfile:
            print "The current file is: ", csv_file
            print " "
            reader = csv.DictReader(csvfile)
            if headers:
                print "Data Headers: ", headers
            print "Row Data: "
            for row in reader:
                print row
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
            print " "
    print " "
    return


def WriteDictToCSV(csv_file, csv_columns, dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
            print " "
    return


currentPath = os.getcwd()


csv_wells = currentPath + "/wel.csv"
# print csv_wells
# ReadCSVasDict(csv_wells)
wells_headers = []
wells_data = ReadCSVasDict(csv_wells, None)
# print wells_data


csv_scalars = currentPath + "/scalars.csv"
# print csv_scalars
# ReadCSVasDict(csv_scalars)
scalars_headers = ['sourceFile', 'CZ1', 'CZ2', 'CZ3', 'CZ4', 'CZ5', 'CZ6', 'CZ7', 'CZ8', 'CZ9', 'CZ10', 'CZ11']
scalars_data = ReadCSVasDict(csv_scalars, scalars_headers)
# print scalars_data


csv_tablelink = currentPath + "/tablelink.csv"
# print csv_tablelink
# ReadCSVasDict(csv_tablelink)
tablelink_headers = ['Row', 'Col', 'Kzone']
tablelink_data = ReadCSVasDict(csv_tablelink, tablelink_headers)
print tablelink_data


# tablelink_data_csv_target = currentPath + "/tablelink_data_export.csv"
# WriteDictToCSV(tablelink_data_csv_target, tablelink_headers, tablelink_data)
