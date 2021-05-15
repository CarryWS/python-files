import sys
import os
try:
    option = sys.argv[1]
except:
    print('gcc: fatal error: no input files\ncompilation terminated.')
    exit()
os.system('H:\\Dev-Cpp\\MinGW64\\bin\\g++.exe '+str(option)+' -o '+str(option)[:-4]+str('.exe'))
os.system(str(option)[:-4]+str('.exe'))
