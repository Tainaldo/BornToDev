import csv

def readCSV():
    with open('Lecture 87 employee_birthday.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')


def writeCSV():
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Tai Jaikla', 'CEO', 'March'])
        employee_writer.writerow(['Tai Jaikla', 'Data sicne', 'March'])
        employee_writer.writerow(['Wilawan', 'UX/UI', 'Arpil'])

writeCSV()