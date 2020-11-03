import pyperclip, re

print('Welcome to StrongPass password checker. \n Your password in the clipboard will be processed...')

StrongPassword1 = re.compile(r'[QWERTYUIOPASDFGHJKLZXCVBNM]')
StrongPassword2 = re.compile(r'[qwertyuiopasdfghjklzxcvbnm]')
StrongPassword3 = re.compile(r'\d')

CheckedPassword = str(pyperclip.paste())

if len(CheckedPassword)>= 8:
    if StrongPassword1.findall(CheckedPassword)!= []:
        if StrongPassword2.findall(CheckedPassword) != []:
            if StrongPassword3.findall(CheckedPassword) != []:
                print('Strong password')
            else:
                print('Not strong password')
        else:
            print('Not strong password')
    else:
        print('Not strong password')
else:
    print('Not strong password')

print('\nFeel free to copy something new to your clipboard and check again')
end = input()
