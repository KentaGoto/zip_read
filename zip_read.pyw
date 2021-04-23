# coding: utf-8

import sys
import zipfile
import re
import PySimpleGUI as sg

if __name__ == '__main__':
    sg.theme('Dark Blue 3')

    layout = [
        [sg.Text('Zip file:', size=(5, 1)),
         sg.InputText('', enable_events=True,),
         sg.FilesBrowse('Add a file', key='-FILES-',
                        file_types=(('Zip file', '*.zip'),))],
        [sg.Output(size=(80, 25), key='-RESULTS-')],
        [sg.Submit(button_text='Run')]
    ]

    window = sg.Window('Zip Read', layout)

    while True:
        event, values = window.read()

        # Exit with [x] in the window
        if event is None:
            break

        if event == 'Run':
            f = values[0]
            f = re.sub('^\"', '', f)
            f = re.sub('\"$', '', f)

            if f == '':
                sg.popup('Please specify a Zip file.')
                continue

            z = zipfile.ZipFile(f)
            fnames = []
            for i in z.infolist():
                name = i.orig_filename.encode('cp437').decode('cp932', errors="ignore")
                fnames.append(name)
            results = '\n'.join(fnames)
            window['-RESULTS-'].update(results)

    window.close()
    sys.exit()
