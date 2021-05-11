import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

#####
# Function Definitions
#####

def parse_ragged_array(file):
    """This function fills in missing values in a ragged array to make a rectangular array for numpy usage"""
    new_array = list()
    lengths_of_lines = list()
    with open(file, 'r') as data_block:
        for line in data_block:
            each_line = line.split(' ')
            new_array.append(each_line)
            lengths_of_lines.append(len(each_line))
    limit = np.max(lengths_of_lines)
    for line in new_array:
        while len(line) < limit:
            line.append('nodata')
    return np.array(new_array,dtype=str)

def reverse_entries(data):
    """This function reverses a newest-first array into oldest_first array"""
    return data[::-1]

def create_and_fill(old_data, entries):
    """This function creates and fills new array with the required data and calls other functions to process"""
    final_array = np.arange(entries * 5, dtype=int)
    final_array.shape = (entries,5)
    final_array = get_date(final_array, old_data, entries)	# contains no header/footer line
    final_array = get_time(final_array, old_data, entries)
    final_array = get_temp_dewpt(final_array, old_data, entries)
    final_array = calculate_difference(final_array, old_data, entries)
    return final_array

def get_date(new_data, old_data, total):
    """This function inserts the date in the first column of the returned array"""
    for line in range (0, total):
        element = old_data[line,1]
        element = element[0:2]		# peels off 1st 2 numbers that are the day of the month
        new_data[line,0] = int(element)
    return new_data

def get_time(new_data, old_data, total):
    """This function inserts the time in the second column of the returned array"""
    for line in range (0, total):
        element = old_data[line,1]
        element = element[2:6]
        new_data[line,1] = int(element)
    return new_data

def get_temp_dewpt(new_data, old_data, total):
    """This function inserts the temperature in the third column of the returned array"""
    for line in range (0, total):	# examines each line
        for column in range (6,12):	# searches each possible column for temp/dew pt data
            element = old_data[line, column]
            if element[2:3] == '/':
                new_data[line,2] = int(element[0:2])	# assigns temperature value
                new_data[line,3] = int(element[3:5])	# assigns dew point value
    return new_data

def calculate_difference(new_data, old_data, total):
    """This funcion inserts the temp/dew point spread into the fifth column of the returned array"""
    for line in range (0, total):
        new_data[line, 4] = new_data[line, 2] - new_data[line, 3]
    return new_data

def make_charts(final_array,entries):
    """This function creates charts for temp-dew point spread for May 5th-10th from data"""
    time = final_array[:1]
    diff = final_array[:4]
    x5, x6, x7, x8, x9, x10 = list()
    y5, y6, y7, y8, y9, y10 = list()

    for line in range (0,entries):

        if final_array[line, 0] == '05':
            x5.append(final_array[line, 1])
            y5.append(final_array[line, 4])
        elif final_array[line, 0] == '06':
            x6.append(final_array[line, 1])
            y6.append(final_array[line, 4])
        elif final_array[line, 0] == '07':
            x7.append(final_array[line, 1])
            y7.append(final_array[line, 4])
        elif final_array[line, 0] == '08':
            x8.append(final_array[line, 1])
            y8.append(final_array[line, 4])
        elif final_array[line, 0] == '09':
            x9.append(final_array[line, 1])
            y9.append(final_array[line, 4])
        else:
            x10.append(final_array[line, 1])
            y10.append(final_array[line, 4])

    fig, ax = plt.subplots()
    ax.plt(x5, y5)
    ax.set(xlabel = 'Time of day', ylable = 'Temperature/dew point spread', title = 'May 5th temperature/dew point spread')
    ax.grid()
    plt.savefig('May5th.png')
    plt.show()

    fig, ax2 = plt.subplots()
    ax2.plt(x6, y6)
    ax2.set(xlabel = 'Time of day', ylable = 'Temperature/dew point spread', title = 'May 6th temperature/dew point spread')
    ax2.grid()
    plt.savefig('May6th.png')
    plt.show()

    fig, ax3 = plt.subplots()
    ax3.plt(x7, y7)
    ax3.set(xlabel = 'Time of day', ylable = 'Temperature/dew point spread', title = 'May 7th temperature/dew point spread')
    ax3.grid()
    plt.savefig('May7th.png')
    plt.show()

    fig, ax4 = plt.subplots()
    ax4.plt(x8, y8)
    ax4.set(xlabel = 'Time of day', ylable = 'Temperature/dew point spread', title = 'May 8th temperature/dew point spread')
    ax.grid()
    plt.savefig('May8th.png')
    plt.show()

    fig, ax5 = plt.subplots()
    ax5.plt(x9, y9)
    ax4.set(xlabel = 'Time of day', ylable = 'Temperature/dew point spread', title = 'May 9th temperature/dew point spread')
    ax.grid()
    plt.savefig('May9th.png')
    plt.show()

    fig, ax6 = plt.subplots()
    ax6.plt(x10, y10)
    ax6.set(xlabel = 'Time of day', ylable = 'Temperature/dew point spread', title = 'May 10th temperature/dew point spread')
    ax6.grid()
    plt.savefig('May10th.png')
    plt.show()

    return 

#####
# Main program
#####

data_block = parse_ragged_array('KCXW-120hour-METAR.txt')

number_of_entries = np.size(data_block,0) - 1		# the minus1 will eliminate the header line later on

data_block = reverse_entries(data_block)

final_array=create_and_fill(data_block, number_of_entries)

make_charts(final_array, number_of_entries)
