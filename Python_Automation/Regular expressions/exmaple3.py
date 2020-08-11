import re
import pyperclip


SearchREGxVar = re.compile(r'(ha){3}')
mo = SearchREGxVar.search('He said haha')
print(mo.group())