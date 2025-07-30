import pyperclip, re

text = str(pyperclip.paste())
matches = []

# My Regexes
phoneRegex = re.compile(r'(\d{3})|\(\d{3}\)?(\s|-|\.)\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2, 5})?', re.VERBOSE)
ukNumRegex = re.compile(r'(\+44|0(7\d{3}\s?\d{6}))')

#emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-](\.[a-az-Z]{2,4}))', re.VERBOSE)
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
   )''', re.VERBOSE)

# Easier version of the above
emailRegex2 = re.compile(r'((.*)@(.*)(\.[a-zA-Z]{2,4}))', re.VERBOSE)

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[2], groups[3]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex2.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email adresses found...')
mo1 = ukNumRegex.search('07711946746')

mo3 = emailRegex2.search('sgrant25@gmail.com')
print(mo3.groups())
print(mo1.groups())