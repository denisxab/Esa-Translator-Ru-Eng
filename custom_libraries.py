import os
def check_lib():

    if not 'General_settings.txt' in os.listdir():
        # os.system('python -m pip install --upgrade pip')
        try:
            import requests
        except:
            os.system('pip3 install requests')
        try:
            import pyperclip
        except:
            os.system('pip3 install pyperclip')
        try:
            import win32api
        except:
            os.system('pip3 install pypiwin32')
        try:
            import win32gui
        except:
            os.system('pip3 install win32gui')
        try:
            from PIL import Image,ImageTk
        except:
            os.system('pip3 install Pillow')
        try:
            import mss
            import mss.tools
        except:
            os.system('pip3 install mss')
        try:
            import cv2
        except:
            os.system('pip3 install opencv-python')
        try:
            import numpy
        except:
            os.system('pip3 install numpy')

        #https://github.com/UB-Mannheim/tesseract/wiki
        try:
            import pytesseract
            pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # выбрать файл с Tesseract-OCR
        except:
            os.system('pip3 install pytesseract')

if __name__ == '__main__':
    check_lib()