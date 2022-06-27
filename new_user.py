###imports
import os, random, PySimpleGUI as sg

###variables
index_counter = 0




###funct
def save(x, y):
    with open('usernames.txt', 'a')as f:
        f.write(x + '\n')
    with open('passwords.txt', 'a')as f:
        try:
            f.write(y + '\n')
        except:
            print("Koichi's bug")
            f.write('bugged\n')

def encode():
    import encode.py



###setup
layout= [
    [
        sg.Text('Username: '),
        sg.In(size=(20,5),enable_events=True,key='-USR-')
    ],
    [
        sg.Text('Password: '),
        sg.In(size=(20,5),enable_events=True,key='-PAS-',password_char='*')
    ],
    [
        sg.Button('Save',enable_events=True,key='-SAV-'),
    ]
]


window = sg.Window('Window that stays open', layout)

###main event
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '-SAV-':
        username = values['-USR-']
        password = values['-PAS-']
        encode()
        epassword = str_encrypt.password
        save(username, epassword)