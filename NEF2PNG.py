import time

import multiprocessing
import os
import subprocess

NEFnames = []

def getNEFnames():
    #get NEF file names from current working directory
    files = [f for f in os.listdir('.') if (os.path.isfile(f))]
    NEFfiles = [ f for f in files if (".NEF" in f)]
    return NEFfiles

def convertNEFtoPNG(fileList):
    if isinstance(fileList, list):
        for f in fileList:
            print(f)
            # os.system('C:\Program Files (x86)\IrfanView\i_view32.exe', f, '/convert=', f ,'.png')
            subprocess.run(['C:\Program Files (x86)\IrfanView\i_view32.exe', f, '/convert=', f,'.png'])
    else:
        subprocess.run(['C:\Program Files (x86)\IrfanView\i_view32.exe', fileList, '/convert=', fileList,'.png'])

def printOut(NEFnames):
    for f in NEFnames:
        # do something
        print(f)

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