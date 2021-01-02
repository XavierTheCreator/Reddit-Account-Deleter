from typing import Sized
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, InputText
import time

sg.theme('TanBlue')
done = False


layout = [[sg.Text('USERNAME', size=(15,1)),sg.InputText(k= '-USERNAME-')],
          [sg.Text('PASSWORD', size=(15,1)),sg.InputText(k= '-PASSWORD-')],
          [sg.Text(size=(50,2),key ='-OUTPUT-')],
          [sg.Button('Delete Account'),sg.Button('Delete Comments'),sg.Button('Delete Posts')],
          ]


window = sg.Window('Reddit Manager',layout)

while True:
    event,values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    if event == 'Delete Account':
        try:
            pass
        
        except:
            pass
    
    if event == 'Delete Comments':
        try:
            pass
        
        except:
            pass
    
    if event == 'Delete Posts':
        try:
            pass
        
        except:
            pass
    
    while not done:
        sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, 'Downloading', time_between_frames=30)
        time.sleep(.3)
        sg.popup_animated(image_source=None)
        #window['-OUTPUT-'].update(title + '\nis finished downloading')

window.close()