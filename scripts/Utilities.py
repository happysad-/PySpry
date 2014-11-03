#!/usr/bin/python

import subprocess
import sys
import os

userInput = "";

def getUsrPlatform():
    print("Getting your platform...");
    usrPlatform = sys.platform;
    print("Operating System: " + usrPlatform + "\n");
    return usrPlatform;

def mkFloppyImg(usrPlatform):
    print("Creating a floppy disk image...\n");
    print("Select the size of the floppy disk image:\n");
    print("\t 1 - 360KB");
    print("\t 2 - 720KB");
    print("\t 3 - 1.44MB (Recommended)");
    print("\t q - Quit");
    getUserInput();

    #ADD THE *NIX and XOS scripts.
    if userInput == '1':
        if usrPlatform == 'win32' or usrPlatform == 'win64':
            pathToLibWin = os.path.join('lib', 'win', '');
            subprocess.call([pathToLibWin + 'mkFloppyDiskImg.bat', '-360k']);
    elif userInput == '2':
        if usrPlatform == 'win32' or usrPlatform == 'win64':
            pathToLibWin = os.path.join('lib', 'win', '');
            subprocess.call([pathToLibWin + 'mkFloppyDiskImg.bat', '-720k']);
    elif userInput == '3':
        if usrPlatform == 'win32' or usrPlatform == 'win64':
            pathToLibWin = os.path.join('lib', 'win', '');
            subprocess.call([pathToLibWin + 'mkFloppyDiskImg.bat', '-1440k']);
    elif userInput == 'q':
        pass;
    else:
        print("ERROR: Not an option...");

def getUserInput():
    global userInput;
    userInput = input(">> ");

def cpBootToFloppyImg():
    print("Copying the bootloader to the first sector (512KB)...");
    print("Copying the secondary bootloader to the second sector...");
    print("\t ");
    pass;

def cpKernelToFloppyImg():
    pass;
