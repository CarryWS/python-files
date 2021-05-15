import os
os.system('echo msgbox"哈哈哈哈",64,"提示">message.vbs')
while True:
    for i in range(10):
        os.system('start message.vbs')
    os.system('taskkill /im wscript.exe /f')
