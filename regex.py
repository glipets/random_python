import re
sentence = 'blah djsadfkl sadlfja'
pattern = re.compile(r'\d\d\d[-]\d\d\d\d')

with open('phone.txt','r') as file:
    contents = file.read()
    
    matches = pattern.findall(contents)
    
    for match in matches:
       # print(match.group(0))
       print(match)