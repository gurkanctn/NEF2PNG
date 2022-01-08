# NEF2PNG
# G.Çetin, 2021 
#
# https://github.com/gurkanctn/NEF2PNG
# 
# Python script that uses multiprocessing to convert all NEF files in a folder to PNG format
# 
# Requires: 
# 1) IrfanView to do the conversion
# 2) more than one core to get a better performance than simply using Irfanview
#  

import os
import multiprocessing
import subprocess

NEFnames = []
myCount = 0
numberOfFiles = 1

def getNEFnames():
    #get NEF file names from current working directory
    files = [f for f in os.listdir('.') if (os.path.isfile(f))]
    NEFfiles = [ f for f in files if (".NEF" in f)]
    numberOfFiles = len(NEFfiles)
    return NEFfiles

def convertNEFtoPNG(fileList):
    if isinstance(fileList, list):
        for f in fileList:
            print("y", end = "")
            subprocess.run(['C:\Program Files (x86)\IrfanView\i_view32.exe', f, '/convert=', f,'.png'])
    else:
        print("+", end = "", flush= True)
        subprocess.run(['C:\Program Files (x86)\IrfanView\i_view32.exe', fileList, '/convert=', fileList,'.png'])

def printOut(NEFnames):
    for f in NEFnames:
        # do something
        print(f, end = ';')
    print("\n Starting Conversion: ... ")
    for f in NEFnames:
        # do something
        print("_", end = "", flush=True)
    print("")

def main():
    """ main function.
    """
    NEFnames = getNEFnames()
    printOut(NEFnames)

    p = multiprocessing.Pool()
    for f in NEFnames:
        # launch a process for each file (ish).
        # The result will be approximately one process per CPU core available.
        p.apply_async(convertNEFtoPNG, [f]) 

    p.close()
    p.join() # Wait for all child processes to close.

    
if __name__ == '__main__':
    main()