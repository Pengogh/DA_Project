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
        for column in range (6,12):	# searches each 'possible' temperature column for temp/dew pt data
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
    time = final_array[:,1]
    diff = final_array[:,4]
    x5=[]
    x6=[]
    x7=[]
    x8=[]
    x9=[]
    x10=[]
    y5=[]
    y6=[]
    y7=[]
    y8=[]
    y9=[]
    y10=[]


    for line in range (0,entries):
        """These if-elif statements populate each day's x/y values"""
        if final_array[line, 0] == 5:
            x5.append(final_array[line, 1])
            y5.append(final_array[line, 4]) 
       
        elif final_array[line, 0] == 6:
            x6.append(final_array[line, 1])
            y6.append(final_array[line, 4])

        elif final_array[line, 0] == 7:
            x7.append(final_array[line, 1])
            y7.append(final_array[line, 4])

        elif final_array[line, 0] == 8:
            x8.append(final_array[line, 1])
            y8.append(final_array[line, 4])

        elif final_array[line, 0] == 9:
            x9.append(final_array[line, 1])
            y9.append(final_array[line, 4])

        elif final_array[line, 0] == 10:
            x10.append(final_array[line, 1])
            y10.append(final_array[line, 4])
 
    """These plot blocks create a chart for each day"""
    plt.plot(x5, y5)
    plt.title('Conway, AR airport - May 5th, 2021')
    plt.xlabel('Time of day - 24hr clock')
    plt.ylabel('Temperature/dew point spread\n(< 2 indicates fog probability)')
    plt.grid(True)
    plt.xlim([0,2400])
    plt.hlines(2, xmin=0, xmax= 2400, color='r')
    plt.show()
    plt.savefig('May5th.png')

    plt.figure()
    plt.plot(x6, y6)
    plt.title('Conway, AR airport - May 6th, 2021')
    plt.xlabel('Time of day - 24hr clock')
    plt.ylabel('Temperature/dew point spread\n(< 2 indicates fog probability)')
    plt.grid(True)
    plt.xlim([0,2400])
    plt.hlines(2, xmin=0, xmax= 2400, color='r')
    plt.show()
    plt.savefig('May6th.png')

    plt.figure()
    plt.plot(x7, y7)
    plt.title('Conway, AR airport - May 7th, 2021')
    plt.xlabel('Time of day - 24hr clock')
    plt.ylabel('Temperature/dew point spread\n(< 2 indicates fog probability)')
    plt.grid(True)
    plt.xlim([0,2400])
    plt.hlines(2, xmin=0, xmax= 2400, color='r')
    plt.show()
    plt.savefig('May7th.png')

    plt.figure()
    plt.plot(x8, y8)
    plt.title('Conway, AR airport - May 8th, 2021')
    plt.xlabel('Time of day - 24hr clock')
    plt.ylabel('Temperature/dew point spread\n(< 2 indicates fog probability)')
    plt.grid(True)
    plt.xlim([0,2400])
    plt.hlines(2, xmin=0, xmax= 2400, color='r')
    plt.show()
    plt.savefig('May8th.png')

    plt.figure()
    plt.plot(x9, y9)
    plt.title('Conway, AR airport - May 9th, 2021')
    plt.xlabel('Time of day - 24hr clock')
    plt.ylabel('Temperature/dew point spread\n(< 2 indicates fog probability)')
    plt.grid(True)
    plt.xlim([0,2400])
    plt.hlines(2, xmin=0, xmax= 2400, color='r')
    plt.show()
    plt.savefig('May9th.png')

    plt.figure()
    plt.plot(x10, y10)
    plt.title('Conway, AR airport - May 10th, 2021')
    plt.xlabel('Time of day - 24hr clock')
    plt.ylabel('Temperature/dew point spread\n(< 2 indicates fog probability)')
    plt.grid(True)
    plt.xlim([0,2400])
    plt.hlines(2, xmin=0, xmax= 2400, color='r')
    plt.show()
    plt.savefig('May10th.png')

    return()

#####
# Main program
#####

data_block = parse_ragged_array('KCXW-120hour-METAR.txt')

number_of_entries = np.size(data_block,0) - 1		# the minus1 will eliminate the header line later on

data_block = reverse_entries(data_block)

final_array=create_and_fill(data_block, number_of_entries)

make_charts(final_array, number_of_entries)

