#!/usr/bin/python

import os

def createDirs():
    print("Creating the directories...");
    os.makedirs('src/asmLib');
    os.makedirs('src/bootloader');
    os.makedirs('bin/bootloader');
    os.makedirs('bin/asmLibs');
    os.makedirs('bin/kernel');
    os.makedirs('bin/kernelLib');
