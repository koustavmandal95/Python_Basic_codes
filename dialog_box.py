@echo off
set /p t=what do you want the title to  be ?
cls
set /p body=what do you want the message to be?
ping localhost>nul
cls
echo x=msgbox("%body%",0,"%t%") >message.vbs
cls
echo Press a key to display your message box
start message.vbs
