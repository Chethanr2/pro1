import re

phoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumber.search('I am going out, call me to 666-884-0909 or if not reachable call to 234-564-9098')
print(mo.group())