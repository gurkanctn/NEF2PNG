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
# *** Important Notes! ***
# 1) Check all tasks (denoted as TODO) in the code,
# 2) correct as required for your specific computer setup.

import os
import multiprocessing
import subprocess

NEFnames = []
myCount = 0
numberOfFiles = 1

def getNEFnames():
    """get NEF file names from current working directory"""
    files = [f for f in os.listdir('.') if (os.path.isfile(f))]
    NEFfiles = [ f for f in files if (".NEF" in f)]
    numberOfFiles = len(NEFfiles)
    return NEFfiles

def convertNEFtoPNG(fileList):
    """ Handle Conversion of each NEF file """
    if isinstance(fileList, list):
        for f in fileList:
            print("y", end = "")
            try:
                subprocess.run(['C:\Program Files (x86)\IrfanView\i_view32.exe', f, '/convert=', f,'.png'])
            except:
                print("ERROR: unable to run IrfanView! Verify that the command can be run at your machine before running NEF2PNG.")
    else:
        print("+", end = "", flush= True)
        try:
            subprocess.run(['C:\Program Files (x86)\IrfanView\i_view32.exe', fileList, '/convert=', fileList,'.png'])
        except:
            print("ERROR: unable to run IrfanView! Verify that the command can be run at your machine before running NEF2PNG.")

def printOut(NEFnames):
    """ Print some info and visual progress indicator    """
    if NEFnames:
        print("\n Starting Conversion: ... \n")
        for f in NEFnames:      # Print out list of NEF files
            # do something
            print(f, end = ';')  
        print("")
        for f in NEFnames:      # Generate a visual cue of number of files (to watch progress)
            # do something
            print("_", end = "", flush=True)
    else:
            print("Warning: No NEF files found!")
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