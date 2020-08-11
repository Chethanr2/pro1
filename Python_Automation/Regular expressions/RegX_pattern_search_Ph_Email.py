import re, pyperclip

EmailRegX = re.compile(r'''
# Search for email in the selected text
[a-zA-Z0-9_.+]+             # search for text
@                           # search for @
[a-zA-Z0-9_.+]+             # search for text
''', re.VERBOSE)

text = pyperclip.paste()

ExtractedEmailAddress = EmailRegX.findall(text)

print(ExtractedEmailAddress)