
#Need to install requests package for python
import requests
from configparser import ConfigParser
import os.path
import logging
import ipaddress 

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        #print("IP address {} is valid. The object returned is {}".format(address, ip))
        return True
       
    except ValueError:
        #print("IP address {} is not valid".format(address))
        return False 
#def label_present(label):


def setup():

 file = 'config.txt'
 log_file = 'snow.log'
 api_file= 'api_results.txt'
 va_file= 'valabels.csv'
 # set log level
 logging.root.handlers = []
 logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO , filename=log_file)

# set up logging to console
 console = logging.StreamHandler()
 console.setLevel(logging.ERROR)
# set a format which is simpler for console use
 formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
 console.setFormatter(formatter)
 logging.getLogger("").addHandler(console)

 print(' ============= ')
 print(' Commensing script prechecks, you can check info inside ' + log_file)

 if os.path.exists(file):
    logging.info(' CHECK1: config file path ' + file + ' is there ')
 else:
    logging.error(' no path to config file' +file+ ' exists ')
    exit()

 if os.path.isfile(file):
    logging.info(' CHECK2: config file' + file + ' is actualy a file and not a directory ')
 else:
    logging.error(' your config file' + file+ ' is not a file ')
    exit()

 config = ConfigParser()
 config.read(file)
 if config.has_section('info'):
     logging.info(' CHECK 3: info section is present ')
 else:
    logging.error(' You do not have section labeled [info] in the ' + file)
    exit()

 url = config.get('info','url')
 user = config.get('info','user')
 pwd = config.get('info','pwd')
 return va_file, api_file, url, user, pwd


def main():
 va_file, api_file, url, user, pwd = setup() 
 # Set proper headers
 headers = {"Content-Type":"application/json","Accept":"application/json"}
 
 # Do the HTTP request
 response = requests.get(url, auth=(user, pwd), headers=headers )
 
 # Check for HTTP codes other than 200
 if response.status_code != 200:
     print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
     exit()
 else: 
    logging.info(' CHECK4: URL IS VALID ' + url)
    print(' ============= ')
 
 
 # Decode the JSON response into a dictionary and use the data
 if(response):
     try: 
         data =response.json()
     except:
          print(response.text)
          logging.error('Not getting json. Is the ServiceNow instance hibernating ?')
          exit()

#print(response.text)
#below is to see the json represantation of the output
#print(data)
#python3 test.py | python3 -m json.tool| less  


 output = open(api_file, "w")

 va = open(va_file, "w")
 va.write('Name,Type,Definition'+'\n')
 print(' API OUTPUT is in the ' + api_file + ' file')
 print(' vArmour labels are in the ' + va_file + ' file')
 #labels = []
 allLabels = {}
 for record in data['result']:
    #uncomment below if i want to see only names that have IP addresses
    #if len(record['ip_address']) > 0:
        output.write(record['name'] + ',' + record['ip_address'] +'\n')

        if not validate_ip_address(record['ip_address']):
          continue
        appname = "AppName=" + record['name']
        if appname in allLabels.keys():
          allLabels[appname].append (record['ip_address'])
        else:
          allLabels[appname] = [record['ip_address']] 

        appfunc = "AppFunc=" + record['name']
        if appfunc in allLabels.keys():
          allLabels[appfunc].append (record['ip_address'])
        else:
          allLabels[appfunc] = [record['ip_address']] 

        apprealm = "Realm=" + record['u_realm']
        if apprealm in allLabels.keys():
          allLabels[apprealm].append (record['ip_address'])
        else:
          allLabels[apprealm] = [record['ip_address']] 

        appregion = "Region=" + record['u_location_text']
        if appregion in allLabels.keys():
          allLabels[appregion].append (record['ip_address'])
        else:
          allLabels[appregion] = [record['ip_address']] 

 for key in allLabels:
   #print(key, allLabels[key])
   va.write("%s.Manual,%s\n"%(key," ".join(allLabels[key])))
 output.close()
 va.close()


if __name__ == "__main__":
    main()
