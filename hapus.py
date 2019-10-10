# by @irfnrdh 04/10/19

'''
Studi kasus ini menghapus semua file thumbnail hasil download photo dari telegram
'''

import os
from os import listdir
from os.path import isfile, join
import json

dir_path = os.path.dirname(os.path.realpath(__file__))

onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

def write_json(onlyfiles, filename='files.json'):
    with open(filename,'w') as f:
        json.dump(onlyfiles, f, indent=2,ensure_ascii=False)

onlyfiles.remove('hapus.py');        
#write_json(onlyfiles)       
#onlyfiles.remove('files.json');

list = onlyfiles

calc = 1
print("Jumlah file :" , format(len(list)))
print("Berikut files thumb yang dihapus...")

while int(calc) <= len(list):
    print(list[calc])
    os.remove(dir_path + "/" + list[calc])
    list.remove(list[calc])
    calc = int(calc) + 1
    
print("Jumlah file Setelah dihapus :" , format(len(list)))
#write_json(onlyfiles)  
