import csv
from errorHandler.error import Error
def remove_nonNumeric_lines(file):
    # specify the path to the CSV file
    csv_file = file
    new_header = ['seconds', 'mV']
    # open the CSV file and read the lines
    try:
        with open(csv_file, 'r') as file:
            lines = file.readlines()
    
        # find the first line containing numbers
        start_index = 0
        for i, line in enumerate(lines):
            if any(c.isdigit() for c in line):
                start_index = i
                break

        # modify the file in place
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(new_header)
            for line in lines[start_index:]:
                writer.writerow(line.strip().split(','))
        lines = open(csv_file).readlines()
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            data[1][1] = 0
            data[2][1] = 0
        # open the CSV file for writing
        with open(csv_file, 'w', newline='') as f:
            # create a writer object
            writer = csv.writer(f)
            # write the updated data to the CSV file
            writer.writerows(data)
    except:
        error_message = "Type of CSV file is bad."
        return Error(error_message,400)