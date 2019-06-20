import os
import sys

def check_lib_win32():

    if not 'General_settings.txt' in os.listdir():

        a = input('Похоже вы запустили программу впервый раз, хотите установить все необходимые бибилиотеки для работы программы?[+\\-]\
            \nIt looks like you ran the program the first time want to install all the required libraries for the program?[+\\-] ')

        if a == '+':
            os.system('python -m pip install --upgrade pip')
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
  
            try:
                import pytesseract
            except:
                os.system('pip3 install pytesseract')

            try:
                #https://github.com/UB-Mannheim/tesseract/wiki
                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # выбрать файл с Tesseract-OCR
                with mss.mss() as sct:
                    monitor = {"top":1, "left": 1, "width": 1, "height":1}
                    a = pytesseract.image_to_string(numpy.array(sct.grab(monitor)),lang='eng')
            except pytesseract.pytesseract.TesseractNotFoundError:
                if 'tesseract-ocr.exe' in os.listdir():
                    os.system('tesseract-ocr.exe')

def mainCL():
    if sys.platform == 'win32':
        check_lib_win32()

    # elif sys.platform == 'linux':
    #   check_lib_win32()

    # elif sys.platform == 'darwin':
    #   check_lib_win32()


if __name__ == '__main__':
    mainCL()
