###imports
import os, PySimpleGUI as sg

###variables
index_counteru = 0
index_counterp = 0



###functions
def get_list(x):
    get_list.names = []
    with open(x, 'r') as f:
        for name in f:
            get_list.names.append(name)

def check(x, y, z, v, iu, ip):
    for user_n in x:
        user = user_n[:-1]
        iu = iu + 1
        if user == z:
            cu = iu
            print('correct username', cu)
    for passs_n in y:
        passs = passs_n[:-1]
        ip = ip + 1
        if passs == v:
            cp = ip
            print('correct password', cp)
    try:
        if cp == cu:
            import main.py
            print('logged in')
    except:
        print('failed loggin')
    
    
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
        sg.Button('Login',enable_events=True,key='-LOG-'),
        sg.Button('new User',enable_events=True,key='-NEW-')
    ]
]


window = sg.Window('Window that stays open', layout)

###main event
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '-NEW-':
        import new_user.py

    if event == '-LOG-':
        username = values['-USR-']
        password = values['-PAS-']
        get_list('usernames.txt')
        usernames = get_list.names
        get_list('passwords.txt')
        passwords = get_list.names
        check(usernames, passwords, username, password, index_counteru, index_counterp)






