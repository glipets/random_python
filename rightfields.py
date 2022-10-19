#! python3


import csv
import sys

n = len(sys.argv)
#print("Total arguments passed:", n)
if n != 2:
    print("Usage:rightfields.py <input_subnet_csv>")
    exit()
input_file=sys.argv[1]

output_file="data/output.csv"
with open(input_file, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # for line in csv_reader:
    #     print(line)
    with open(output_file, "w") as new_file:
        #fieldnames = ['\ufeffIP Address','MAC Address','Hostname','DHCP Client Name','System Name','Description', 'Contact','System Location', 'Vendor', 'Machine Type','Comments', 'Status', 'System Object ID', 'Type','Alias', 'Requestor','Subnet Display Name','Subnet Address','Subnet CIDR','Subnet Mask', 'AppName','AppFunc','Region']
        needed_fieldnames = ['\ufeffIP Address','Hostname','System Name', 'Contact','System Location', 'Vendor', 'Machine Type','Comments','Alias', 'AppName','AppFunc','Region']
        csv_writer = csv.DictWriter(new_file, fieldnames=needed_fieldnames,delimiter=',')
        csv_writer.writeheader()
        for row in csv_reader:
            
            #del line['MAC Address','DHCP Client Name','Description','Status', 'Status', 'Type', 'Requestor','Subnet Display Name','Subnet Address','Subnet CIDR','Subnet Mask']
            del row['MAC Address']
            del row['DHCP Client Name']
            del row['Description']
            del row['Status']
            del row['System Object ID']
            del row['Type']
            del row['Requestor']
            del row['Subnet Display Name']
            del row['Subnet Address']
            del row['Subnet CIDR']
            del row['Subnet Mask']
          

            csv_writer.writerow(row)
            
print("Output is in:" + output_file)   
