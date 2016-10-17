@echo off
Echo Build Exe of Projekt KaSi
copy main.pyw main.py
C:\Python34\Scripts\pyinstaller.exe --onefile --icon=lib\icon\icon.ico --name=Projekt_KaSiServer_64Bit main.py
del *.spec
rmdir /s /q build\
C:\Python34_32Bit\Scripts\pyinstaller.exe --onefile --icon=lib\icon\icon.ico --noconsole --name=Projekt_KaSiServer_32Bit main.py
del *.spec
del main.py
rmdir /s /q build\
echo "Build finished"
