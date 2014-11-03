@echo off
echo Navigating to the /lib folder
cd lib/

if "%~1"=="-360k" goto mk360k
if "%~1"=="-720k" goto mk720k
if "%~1"=="-1440k" goto mk1440k

:mk360k
echo Creating a floppy image of size 360KB (0.36MB)
echo.
dd if=/dev/zero of="../bin/floppyImage.img" bs=360k count=1
echo.
echo Floppy disk image was saved in the bin folder.
goto end

:mk720k
echo Creating a floppy image of size 720KB (0.72MB)
echo.
dd if=/dev/zero of="../bin/floppyImage.img" bs=720k count=1
echo.
echo Floppy disk image was saved in the bin folder.
goto end

:mk1440k
echo Creating a floppy image of size 1440KB (1.44MB)
echo.
dd if=/dev/zero of="../bin/floppyImage.img" bs=1440k count=1
echo.
echo Floppy disk image was saved in the bin folder.
goto end

:end