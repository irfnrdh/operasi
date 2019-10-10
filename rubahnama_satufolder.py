# by @irfnrdh 04/10/19

import os
from os import listdir
from os.path import isfile, join


dir_path = os.path.dirname(os.path.realpath(__file__))

onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

onlyfiles.remove('rubahnama.py');        

list = onlyfiles

calc= 0
i = 1
print("Jumlah file :" , format(len(list)))
print("Berikut files yang akan dirubah nama...")
    
    
while int(calc) < len(list):
    dst ="photo" + str(calc) + ".jpg"
    print(list[calc])
    os.rename(list[calc],dst)
    calc = calc + 1
    
print ("Nama telah berhasil dirubah sebanyak ", format(len(list)))
