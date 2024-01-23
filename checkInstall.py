import subprocess


def installPIL():
    print('正在幫您安裝')
    subprocess.run(
        ['pip', 'install', 'PIL'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('PIL庫已安裝')


try:
    import PIL
except ImportError:
    print('PIL庫未安裝')
    installPIL()
