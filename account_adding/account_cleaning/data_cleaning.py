import shutil
import os
import pandas as pd
import time

output_filename = 'output.csv'

def clean_accsmarket_instagram_input(): ### LOL could also just replace all ':' with ','
    data = generate_instas_tuples()

    filename = output_filename
    with open(filename, 'w') as file:
        file.write(data)

def generate_instas_tuples(delim = ':'): #to copy and paster
    filename = 'accsmarket_input.txt'
    with open(filename) as file:
        data = file.read()

    num_commas = 9 # Number of commas after password
    data = '\n'.join(f"{row.split(delim)[0]},{row.split(delim)[1]}{','*num_commas}" for row in data.split('\n') if delim in row)

    print(data)
    return data

def copy_photos():
    orig_file = 'PFPs/kev.within.jpg'
    for i in range(66):
        new_file = f'PFPs/skjbdcoerinverweoir{i}.jpg'
        shutil.copy(orig_file, new_file)


def clean_fbs(filename = 'new.xlsx'):
    # Read and store content
    # of an excel file 
    read_file = pd.read_excel (filename)
    
    # Write the dataframe object
    # into csv file
    read_file.to_csv (output_filename, 
                    index = None,
                    header=True)
    
    # time.sleep(10)
    filename = output_filename
    with open(filename) as file:
        data = file.read()

    rows = data.split('\n')
    for i in range(len(rows)):
        rows[i] += ','*6

    data = '\n'.join(rows)

    print(data)

    with open(filename, 'w') as file:
        file.write(data)


#### generate_instas_tuples(':')


# clean_accsmarket_instagram_input()
clean_fbs()


