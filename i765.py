#!/usr/bin/env python3
# 

import bs4, requests, sys
from bs4.builder import HTML


try: 
    file = open('case.txt') 
    file.close
except FileNotFoundError:
    print("case.txt doesn't exist in the current directory")
    sys.exit()


with open('case.txt','r') as rf:
        for case in rf:
            case = case.strip()
            print(case)
            DATA = 'changeLocale=&appReceiptNum=' + case + '&initCaseSearch=CHECK+STATUS'
            HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}
            r = requests.post('https://egov.uscis.gov/casestatus/mycasestatus.do', data = DATA, headers=HEADERS)

            soup = bs4.BeautifulSoup(r.content, features="lxml")
            match = soup.find('div', class_='rows text-center')
            headline = match.h1.text
            status = match.p.text
            print("===========================")
            print(headline)
            print("===========================")
            print(status)
            print("======================================================")


