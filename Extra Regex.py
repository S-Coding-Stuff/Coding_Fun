import re, pyperclip

dateForm = re.compile(r'(\d{2}[/.-]\d{2}[/.-](\d{4}|\d{2}))')
date1 = dateForm.search('19/04/2003')

websiteURLForm = re.compile(r'((http://|https://)?(www.)?(.*)(\.[a-zA-Z]{2,4}))')
website = websiteURLForm.search('www.google.com')

def passwordCheck(password):
    if re.fullmatch(r'[a-zA-Z0-9@#.$%^&+=]{8,}', password):
        print('Password Accepted')
    else:
        print('Invalid Password')


print(date1.groups())
print(website.groups())
passwordCheck('JeremyClarkson.90988')