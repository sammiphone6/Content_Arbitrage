import shutil
import os


def clean_accsmarket_instagram_input(): ### LOL could also just replace all ':' with ','
    filename = 'accsmarket_input.txt'
    with open(filename) as file:
        data = file.read()

    print(data) 

    data = '\n'.join([','.join(row.split(':')) for row in data.split('\n')])

    print(data)

    filename = 'accsmarket_output.csv'
    with open(filename, 'w') as file:
        file.write(data)

def generate_instas_tuples(): #to copy and paster
    filename = 'accsmarket_input.txt'
    with open(filename) as file:
        data = file.read()

    data = '\n'.join(str(tuple(row.split(':')[:2]))+',' for row in data.split('\n'))

    print(data)

def copy_photos():
    orig_file = 'PFPs/kev.within.jpg'
    for i in range(66):
        new_file = f'PFPs/skjbdcoerinverweoir{i}.jpg'
        shutil.copy(orig_file, new_file)

generate_instas_tuples()
# clean_accsmarket_instagram_input()


