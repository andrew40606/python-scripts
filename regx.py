import re

message = 'call me 415-555-1011 tomorrow, or 415-555-9999'

phonenum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenum.findall(message)
print(mo)
