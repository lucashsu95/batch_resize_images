import subprocess


def installTkinter():
    print('正在幫您安裝')
    subprocess.run(
        ['pip', 'install', 'tkinter'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('tkinter庫已安裝')


try:
    import tkinter
except ImportError:
    print('tkinter庫未安裝')
    installTkinter()
