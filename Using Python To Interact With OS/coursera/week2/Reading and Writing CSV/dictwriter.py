'''
DictReader() allows us to convert the data in a CSV file into a standard dictionary. DictWriter() \ allows us to write data from a dictionary into a CSV file. What’s one parameter we must pass in order for DictWriter() to write our dictionary to CSV format?
The fieldnames parameter of DictWriter() requires a list of keys
This will help DictWriter() organize the CSV rows properly.
'''


import csv
users  = [{'name': 'Sol Mansi', 'username': 'solm', 'department': 'IT Infrastructure'},
        {'name': 'Lio Nelson', 'username': 'lion', 'department': 'User Experience Research'},
        {'name': 'Charle Grey', 'username': 'greyc', 'department': 'Development'}]
keys = ['name', 'username', 'department']

with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users) 