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

        # ウィンドウの[x]で終了
        if event is None:
            break

        if event == 'Run':
            f = values[0]

            # 行頭と行末にダブルクォーテーションがあったら削除
            f = re.sub('^\"', '', f)
            f = re.sub('\"$', '', f)

            if f == '':
                sg.popup('Please specify a Zip file.')
                continue

            z = zipfile.ZipFile(f)
            fnames = []
            for i in z.namelist():
                # Windows環境ではこのようにエンコード・デコードしないと
                # 文字化けした。
                name = i.encode('cp437').decode('cp932')
                fnames.append(name)
            results = '\n'.join(fnames)
            window['-RESULTS-'].update(results)

    window.close()
    sys.exit()
