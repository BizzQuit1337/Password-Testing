###imports
import os, PySimpleGUI as sg
import encode.py

###setup
layout= [
    [
        sg.Text('this is a fully realised page trust me...')
    ]
]


window = sg.Window('Window that stays open', layout)

###main event
while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break