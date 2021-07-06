import csv

with open('file.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for line in csv_reader:
       print(line['email'])