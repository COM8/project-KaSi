@echo off
Echo Build Exe of Projekt KaSi
C:\Python34_64Bit\Scripts\pyinstaller.exe --onefile --icon=lib\icon\icon.ico --name=Projekt_KaSi_64Bit main.py
C:\Python34_32Bit\Scripts\pyinstaller.exe --onefile --icon=lib\icon\icon.ico --name=Projekt_KaSi_32_Bit main.py
C:\Python34_32Bit\Scripts\pyinstaller.exe --onefile --noconsole --icon=lib\icon\icon.ico --name=ConfigEditor editConfig.py
del *.spec
rmdir /s /q build\
echo "Build finished"