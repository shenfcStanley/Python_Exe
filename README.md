# Python_Exe
1. Dir of file is changed after bundling
2. run command:

pyinstaller --onefile --add-data 'test:.' uncompiled2.py (for Unix)
pyinstaller --onefile --add-data 'test;.' uncompiled2.py (for Win)

https://stackoverflow.com/questions/13946650/pyinstaller-2-0-bundle-file-as-onefile
https://stackoverflow.com/questions/9553262/pyinstaller-ioerror-errno-2-no-such-file-or-directory
https://blog.csdn.net/buchunjiedexin/article/details/79764604
