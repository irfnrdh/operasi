'''
	Mendapatkan semua file di dalam folder
'''
import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Kamu Sedang Berada di '%s'" % (cwd))
print("Isi File dalam folder  %s " % (files))