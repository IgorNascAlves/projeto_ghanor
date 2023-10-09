@echo off
setlocal

:: Specify the path to your Python virtual environment
set VENV_PATH=C:\Users\Igor\Desktop\projeto_ghanor\venv

:: Activate the virtual environment
call "%VENV_PATH%\Scripts\activate"

:: Navigate to the directory where your Python script is located
cd /d "C:\Users\Igor\Desktop\projeto_ghanor"

:: Run the Python script
python main_script.py

:: Deactivate the virtual environment (optional)
:: deactivate

:: Pause to keep the command prompt window open (optional)
:: pause

:: Exit the batch file
exit
