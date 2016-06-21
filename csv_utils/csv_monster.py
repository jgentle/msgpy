# I haven't used csv in this class yet, but I am planning to integrate it in soon.
# since csv is just text file the class works fine with default IO functions.
import csv
import sys


class CSV_Monster:
    # current filename, file handle, index, whether to maintain headers when merging
    current_filename = ""
    file_h = None
    i = None
    with_headers = False


    def __init__(self, base_name, last_i, first_i=0, save_name="final-csv-output{}.csv", 
                 skips=set(), zero_index_name=None):
        """
        Prepare to write the files. Open the save name and wait for run() to be called on the 
        utility

        :base_name str: The common file path and name of csv files to parse
        :last_i int: The highest integer found in file names. such as base/name-csv-file (30).csv
        :first_i int: My files start without a number so 1 is default.
        :save_name str: The base name of the final output .csv if there is 1 singular file (merging)
        :skips set: A set of indexes which should be skipped
        :zero_index_name None|str: Pass in a starting name if there is a file to begin with which doesn't fit 
                                   convention in base_name
        """
        self.base_name = base_name
        self.save_name = save_name
        self.last_i = last_i
        self.i = first_i
        # --- Skips are file numbers which should be ignored for any reason .
        self.skips = skips
        self.zero_index_name = zero_index_name

        # --- Open up the output file for writing
        print("Preparing to write to file: {}".format(self.save_name.format('')))
        self.output_file = open(self.save_name.format(''), 'w')


    def open(self, filename=None):
        """Open the self.current_filename for reading As of now this method is overkill,
        there is no way to explicitly tell the class to append a file which isn't named 
        using the self.base_name convention. But I would like to extend the object to 
        be able to allow the user to pass in specific names.

        :filename str: Pass filename to explicitly open. Default - self.current_filename
        :{return} file_handler:
        """
        if filename is not None:
            self.current_filename = filename
        self.file_h = open(self.current_filename, 'r')
        print("opening up file: {}".format(self.current_filename))
        return self.file_h


    def next(self):
        """Setup the next file to be read then return file handler by calling self.open()
        #Todo: next() should be able to consume a list as a generator I think.

        :{return} file_handler:
        """
        if self.i > self.last_i:
            return False
        # Check that this isn't a skip index
        if self.skips and len(self.skips):
            while self.i in self.skips:
                self.i += 1

        if self.zero_index_name is not None:
            self.current_filename = self.zero_index_name
            self.zero_index_name = None
            self.with_headers = True
        else:
            self.current_filename = self.base_name.format(self.i)
            self.with_headers = False

        # incriment for the next file
        self.i += 1
        return self.open()


    def run(self):
        """Roll through each file and append lines to the output.
        """
        while self.next():
            # should skip the headers unless self.with_headers is True
            if not self.with_headers:
                self.file_h.next()
            # Append each line in current file to the output file
            for line in self.file_h:
                self.output_file.write(line)
            self.file_h.close()
        print("Closing the main file... {}".format(self.save_name.format('')))
        self.output_file.close()


    def check_headers(self):
        # TODO: Add header checks
        pass


    def split(self, chunk_size=500):
        """Split the current file into files of row size n where n is chunk_size
        First use self.open() to open a file to read from and then call self.split()

        :chunk_size int: How many lines per file.
        """
        line_num = 0
        file_num = 1
        if self.file_h is None:
            # If no file_h Split assumes to split the base_name file.
            self.open(self.base_name)
        for line in self.file_h:
            line_num += 1
            if line_num == 1 or file_headers is None:
                file_headers = line
            if int(line_num) % int(chunk_size) == 1:
                if self.output_file is not None:
                    self.output_file.close()
                    del self.output_file
                next_filename = self.save_name.format(file_num)
                print("About to write next {0} lines into file: {1}".format(chunk_size, next_filename))
                self.output_file = open(next_filename, 'w+')
                file_num += 1
                # Write the file headers as the first line of each file
                self.output_file.write(file_headers)
                if line_num == 1:
                    # continue because we dont' want to write headers 2 times.
                    continue

            self.output_file.write(line)
        self.file_h.close()
        self.output_file.close()


# EXAMPLE USAGE:
# if __name__ == '__main__':
#     # Make split_mode True to split files (for examples).
#     split_mode = True

#     if split_mode is True:
#         # Splitting files example
#         csv_monster = CSV_Monster("large-files/all-orders.csv", 1, save_name="orders-chunk-{}.csv")
#         csv_monster.split(400)

#     elif __name__ == '__main__' and split_mode is not True:
#         # Merging files example
#         csv_monster = CSV_Monster("split-files/orders-{}.csv", 34, first_i=1, save_name="orders-completed.csv", 
#                                   skips=set((2, 9, 10, 22, 27, 28, 29, 33)))
#         csv_monster.run()

csv_source_filename = "../csv_input/scalars.csv"

# Splitting files for MSG.PY
# 
# When running script across multiple nodes and cores, you need to split the input file at each nth line.
# The split value determines the number of chunks based on the number of lines in the scalars.csv file.
# 
# Formula:
# 1) NUMBER_NU * NUMBER_CORES = NUMBER_CHUNKS_NEEDED
# 2) NUMBER_SCALARS / NUMBER_CHUNKS_NEEDED = SPLIT_LINE_VALUE 
#
# Example for 9382 Scalars:
# 
# 4 NUs:
# csv_split_line = 98           # 96 chunks   
# csv_output_filename = "../csv_data_96chunks/scalar-inputs-chunk-{}.csv"
#
# 8 NUs:
# csv_split_line = 49           # 192 chunks 
# csv_output_filename = "../csv_data_192chunks/scalar-inputs-chunk-{}.csv"
#
# 10 NUs:
csv_split_line = 40           # 235 chunks NOTE: 39 resultes in a small remainder over 240, thus is too small a division.
csv_output_filename = "../csv_data_240chunks/scalar-inputs-chunk-{}.csv"

csv_monster = CSV_Monster(csv_source_filename, 1, save_name=csv_output_filename)
csv_monster.split(csv_split_line)
