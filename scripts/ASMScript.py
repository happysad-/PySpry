#!/usr/bin/python

import subprocess
import glob
import os

def assemble():

    counter = 0;    # General counter to see if all files assembled.

    path = os.path.join('src', 'bootloader');   # Working dir for this script

    os.chdir(path);

    pathToLib = os.path.join(os.pardir, os.pardir, 'lib', '');  # Dir to libraries
    pathToBin = os.path.join(os.pardir, os.pardir, 'bin', 'bootloader', '');    # Dir to binaries

    print("Attempting to assemble the bootloader...");
    print();
    
    for file in glob.glob("*.asm"):
        print("Assembling " + file);
        tmp = file[:-4];    # Remove the .ASM file extension for later use
        subprocess.call([pathToLib + 'nasm.exe', '-f', 'bin', file, '-o', pathToBin + tmp + '.bin']);
        counter += 1;

    print();
    if counter == len(os.listdir(path=pathToBin)):
        print("Everything was assembled!");
        print("However, please check the size of binaries to make sure...");
    else:
        print("Something went wrong... Not all files were assembled. Check your ASM files...");
    print();
