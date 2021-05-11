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
    x5=list()
    x6=list()
    x7=list()
    x8=list()
    x9=list()
    x10=list()
    y5=list()
    y6=list()
    y7=list()
    y8=list()
    y9=list()
    y10=list()

    for line in range (0,entries):
        
        fig, ax = plt.subplots()
        if final_array[line, 0] == '05':
            x5.append(final_array[line, 1])
            y5.append(final_array[line, 4])
            ax.plot(x5[line], y5[line])
            ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 5th temperature/dew point spread')
            ax.grid()
            plt.savefig('May5th.png')
            plt.show()
        elif final_array[line, 0] == '06':
            x6.append(final_array[line, 1])
            y6.append(final_array[line, 4])
            ax.plot(x6[line], y6[line])
            ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 65th temperature/dew point spread')
            ax.grid()
            plt.savefig('May6th.png')
            plt.show()
        elif final_array[line, 0] == '07':
            x7.append(final_array[line, 1])
            y7.append(final_array[line, 4])
            ax.plot(x7[line], y7[line])
            ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 7th temperature/dew point spread')
            ax.grid()
            plt.savefig('May7th.png')
            plt.show()
        elif final_array[line, 0] == '08':
            x8.append(final_array[line, 1])
            y8.append(final_array[line, 4])
            ax.plot(x8[line], y8[line])
            ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 8th temperature/dew point spread')
            ax.grid()
            plt.savefig('May8th.png')
            plt.show()
        elif final_array[line, 0] == '09':
            x9.append(final_array[line, 1])
            y9.append(final_array[line, 4])
            ax.plot(x9[line], y9[line])
            ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 9th temperature/dew point spread')
            ax.grid()
            plt.savefig('May9th.png')
            plt.show()
        else:
            x10.append(final_array[line, 1])
            y10.append(final_array[line, 4])
            ax.plot(x5[line], y5[line])
            ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 10th temperature/dew point spread')
            ax.grid()
            plt.savefig('May10th.png')
            plt.show()

    ax = plt.subplots()
    ax.plot(x5, y5)
    ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 5th temperature/dew point spread')
    ax.grid()
    plt.savefig('May5th.png')
    plt.show()
    plt.figure()
    ax = plt.subplots()
    ax.plot(x6, y6)
    ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 6th temperature/dew point spread')
    ax.grid()
    plt.savefig('May6th.png')
    plt.show()

    plt.figure()
    ax = plt.subplots()
    ax.plot(x7, y7)
    ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 7th temperature/dew point spread')
    ax.grid()
    plt.savefig('May7th.png')
    plt.show()

    plt.figure()
    ax = plt.subplots()
    ax.plot(x8, y8)
    ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 8th temperature/dew point spread')
    ax.grid()
    plt.savefig('May8th.png')
    plt.show()

    plt.figure()
    ax = plt.subplots()
    ax.plot(x9, y9)
    ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 9th temperature/dew point spread')
    ax.grid()
    plt.savefig('May9th.png')
    plt.show()

    plt.figure()
    ax = plt.subplots()
    ax.plot(x10, y10)
    ax.set(xlabel = 'Time of day', ylabel = 'Temperature/dew point spread', title = 'May 10th temperature/dew point spread')
    ax.grid()
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

# make_charts(final_array, number_of_entries)

x = np.arange(0,2400,1)
y = final_array[:4]
import sys
original_stdout = sys.stdout #save original
with open('f_array.txt', 'w') as f:
    sys.stdout = f #change to write file
    print (final_array)
    sys.stdout = original_stdout
print (final_array)

#row = 0
#date = '05'
#while row < number_of_entries:
#    while final_array[row,0] == date:
fig, ax = plt.subplots()
ax.plot (x,y)
ax.set(xlabel='Time of day', ylabel='Temperature/dewpoint spread',title='120 hour temperature dewpoint spread data')
ax.grid()
fig.savefig("May5th.png")
plt.show()
#    date = '06'
#    row += 1
