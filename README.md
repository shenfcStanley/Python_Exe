# Python_Exe
1. Dir of file is changed after bundling
2. run command:

pyinstaller --onefile --add-data 'test:.' uncompiled2.py (for Unix)<br />
pyinstaller --onefile --add-data 'test;.' uncompiled2.py (for Win)<br />

for multiple files:<br />

pyinstaller --onefile --add-data 'test1:.' --add-data 'test2:.' uncompiled2.py (for Unix)<br />



https://stackoverflow.com/questions/13946650/pyinstaller-2-0-bundle-file-as-onefile<br />
https://stackoverflow.com/questions/9553262/pyinstaller-ioerror-errno-2-no-such-file-or-directory<br />
https://blog.csdn.net/buchunjiedexin/article/details/79764604<br />

3. Encrypt py file:<br />

pyinstaller -F --key xxxxx --onefile --add-data 'test:.' main.py ## import loadmodel in main.py<br />

https://zhuanlan.zhihu.com/p/109266820<br />
https://blog.luzy.top/posts/3136266189/<br />
install fails for numpy: https://github.com/numpy/numpy/issues/14747 <br />

4. Facing problem while using pyinstaller "No Module named xxxx", 'No Module named xxx._xxxx'. Solutions: <br />

pyinstaller -F --key xxxxx --onefile --hidden-import='xxxx' --hidden-import='xxx._xxxx' main.py <br />

5. Import .py as module <br />

https://blog.csdn.net/damotiansheng/article/details/43916881 <br />

6. VMware and VT-x enable <br />

https://www.cnblogs.com/mr-xiong/p/12468280.html <br />
https://www.howtogeek.com/213795/how-to-enable-intel-vt-x-in-your-computers-bios-or-uefi-firmware/ <br />
