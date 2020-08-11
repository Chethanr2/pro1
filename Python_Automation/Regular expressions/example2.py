import re

RegXVar = re.compile(r'Bat(man|mobile|woman)')
mo = RegXVar.search('Batmobile is in the street of sanfrancisco')
print(mo.group())