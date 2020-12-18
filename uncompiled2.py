import os, sys

filename = 'test'
if hasattr(sys, '_MEIPASS'):
    # PyInstaller >= 1.6
    os.chdir(sys._MEIPASS)
    filename = os.path.join(sys._MEIPASS, filename)
elif '_MEIPASS2' in environ:
    # PyInstaller < 1.6 (tested on 1.5 only)
    os.chdir(environ['_MEIPASS2'])
    filename = os.path.join(environ['_MEIPASS2'], filename)
else:
    os.chdir(dirname(sys.argv[0]))
    filename = os.path.join(dirname(sys.argv[0]), filename)


f = open(filename, "r")
print(f.read())
