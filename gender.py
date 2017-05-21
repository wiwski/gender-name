import csv

#Dict as {name: gender}
nameDb = {}
result = [['firstname', 'gender']]

print('Loading names...')
with open('names.csv', 'r') as namecsv:
    data = csv.reader(namecsv, delimiter=',')
    for row in data:
        nameDb[row[1].lower()] = row[2]
print('Names loaded')

print('Path to file:')
name_to_file = input()
print('Match in progress...')
with open(name_to_file, 'r') as namecsv:
    data = csv.reader(namecsv, delimiter=',')
    for row in data:
        if(row[0].lower() in nameDb):
            result.append([row[0], [nameDb[row[0].lower()]]])
        else:
            result.append([row[0], 'NN'])
print('Match done... Writting to file')
with open('result.csv', 'w') as resultfile:
    for row in result:
        resultfile.write('{}, {}\n'.format(row[0], row[1]))
print('Done')


    