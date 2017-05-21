import csv

print('File:')
name_of_file = input()

names = []
firstname, lastname = ['firstname'], ['lastname']

name_column_index = -1

with open(name_of_file, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in data:
        #Find in which column is the name field
        if(i == 0):
            j = 0
            for column in row:
                if(column == 'name'):
                    name_column_index = j
                j += 1
            if(name_column_index == -1):
                exit('No name column found')
            print('Name column found at index  {}'.format(str(name_column_index + 1)))
        #Extract names and Separate firstname from lastname
        else:
            name = row[name_column_index].split(' ')
            '''
            if(len(name) == 2):
                firstname.append(name[0])
                lastname.append(name[1])
            elif(len(name) == 3):
                firstname.append(name[0])
                lastname.append(' '.join(name[1:]))
            elif(len(name) == 4):
                firstname.append(' '.join(name[0:2]))
                lastname.append(' '.join(name[2:]))
            '''
            firstname.append(name[0])
            lastname.append(' '.join(name[1:]))
        i += 1

with open('names.txt', 'w') as txtfile:
    i = 0
    for fs in firstname:
        txtfile.write('{},{}\n'.format(firstname[i], lastname[i]))
        i += 1




