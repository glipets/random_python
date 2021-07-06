import csv


with open('file.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('newfile.csv','w') as new_file:
        fieldnames = ['number','name','email']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        #if i want a header
        #csv_writer.writeheader()
        
        for line in csv_reader:
            #deletes email entries inside the file
            #del line['email']
            #print line int file
            #csv_writer.writerow(line)
            #prints line to stdout
            #print(line['email'])
            #print number 1 on every line and actual name from read file
            csv_writer.writerow({'number':'1', 'name':line['name']})