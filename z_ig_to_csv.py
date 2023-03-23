from data import open_filedata

filename = 'ig_order.txt'
with open(filename) as file:
    data = file.read()

print(data) 

data = '\n'.join([','.join(row.split(':')) for row in data.split('\n')])

print(data)

filename = 'ig_order.csv'
with open(filename, 'w') as file:
    file.write(data)


### LOL could also just replace all ':' with ','