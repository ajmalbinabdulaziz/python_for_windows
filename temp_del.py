import subprocess
import os


os.chdir('C:/Windows')
p = subprocess.run('RD /s /q Temp', capture_output=True, shell=True)

os.chdir('C:/Users/AJMAL BIN ABDUL AZIZ/AppData/Local')
o = subprocess.run('RD /s /q Temp', capture_output=True, shell=True)
