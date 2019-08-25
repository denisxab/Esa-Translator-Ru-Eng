# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=C0301
# pylint: disable=R0902

import os
import tkinter


try:
    from win32api import GetSystemMetrics
    from PIL import Image, ImageTk
    from mss import mss
    import mss.tools
    from cv2 import resize, GaussianBlur, imwrite
    from numpy import array
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    ORC_check = True
except ModuleNotFoundError:
    ORC_check = False

import Translete


class ORC():
    def __init__(self):
        super(ORC, self).__init__()
        self.Auto_capture = 0
        self.x, self.y = 0, 0
        self.all_cord_mnogo = []
        self.location_window = 0, 0

    def skrinshot_s_class(self, self_import, AVTO_S=0):

        def exit_func(event):
            del event
            self_import.Windows.unbind('<B1-Motion>')  # pylint: disable=E1101
            self_import.Windows.unbind(
                '<ButtonRelease-1>')  # pylint: disable=E1101
            self_import.Windows.unbind('<F2>')  # pylint: disable=E1101

            imags, cords = [], []
            for x in self.all_cord_mnogo:
                if x[2] == 0 and x[3] == 0:
                    continue

                with mss.mss() as sct:
                    cords.append(x[0])
                    cords.append(x[1])
                    cords.append(x[2])
                    cords.append(x[3])
                    monitor = {"top": x[0], "left": x[1],
                               "width": x[2], "height": x[3]}
                    try:
                        img = resize(array(
                            sct.grab(monitor)), (0, 0), fx=10, fy=10)
                        img = GaussianBlur(img, (11, 11), 0)
                        imags.append(img)

                    except Exception:
                        continue

            self_import.paint.pack_forget()
            # self.bat1.pack()
            self_import.Windows.geometry(
                '145x32+{}+{}'.format(self.location_window[0], self.location_window[1]))
            self_import.Windows.update()
            self_import.Windows.overrideredirect(0)
            self_import.Windows.update()
            self_import.START()
            self_import.lab0['width'] = 25
            # self.Windows.bind('F4',skrinshot_bid)

            i = 0
            for y in imags:
                try:
                    a = pytesseract.image_to_string(y, lang='eng')
                    if a != '':
                        self_import.skrin_shot_batton['text'] = '[+]'
                        self_import.Switches_radio.set('0')

                        if i == 0:
                            self_import.text_box.insert(
                                tkinter.INSERT, '{} '.format(a))

                        else:
                            self_import.text_box.insert(
                                tkinter.INSERT, '\n\\/-------------{}-------------------\\/\n {} '.format(i+1, a))

                        i += 1

                        try:
                            os.remove('Photo\\except_photo{}.png'.format(i))
                        except FileNotFoundError:
                            pass
                    else:
                        self_import.skrin_shot_batton['text'] = '[-]'
                        imwrite('Photo\\except_photo{}.png'.format(i), y)

                except pytesseract.pytesseract.TesseractNotFoundError:
                    if 'tesseract-ocr.exe' in os.listdir(os.getcwd()):
                        os.system('tesseract-ocr.exe')
                        return

                    self_import.text_box.delete(1.0, tkinter.END)
                    self_import.text_box.insert(
                        tkinter.INSERT, 'Для работы этой функции необходимо устоновить tesseract по ссылки\nhttps://github.com/UB-Mannheim/tesseract/wiki\nУкажите при устоновки следующий путь\nC:\\Program Files\\Tesseract-OCR')
                    return

                except pytesseract.pytesseract.TesseractError:
                    self_import.text_box.delete(1.0, tkinter.END)
                    self_import.text_box.insert(
                        tkinter.INSERT, 'Выбраный язык не устоновлен - выберите этот язык при устоновки')
                    return

        def one(event):

            def paint_square(self, event=0):

                if self.x == 0 and self.y == 0:
                    self.x = event.x
                    self.y = event.y
                else:
                    self_import.paint.delete('circle')
                    self_import.paint.create_rectangle(
                        event.x, event.y, self.x, self.y, outline='blue', tag='circle')

            if event.num == 1:

                #########################################
                x0, x_max = self.x, event.x
                X = x0-x_max
                if X < 0:
                    X *= -1
                else:
                    x0, x_max = x_max, x0
                #########################################
                y0, y_max = self.y, event.y
                Y = y0-y_max
                if Y < 0:
                    Y *= -1
                else:
                    y0, y_max = y_max, y0
                #########################################
                self.x = self.y = 0

                if x0 == 0 and y0 == 0:
                    exit_func(self)
                    return

                rrr = (y0, x0, X, Y, x_max, y_max)
                self.all_cord_mnogo.append(rrr)
                self_import.paint.create_rectangle(
                    x_max, y_max, x0, y0, outline='blue', tag=str(x_max))

            else:
                paint_square(self, event)

        if not ORC_check:
            self_import.lab0['text'] = ' NO ORC '
            return False

        self_import.STOP()
        self_import.bat1.pack_forget()
        self_import.frame1.pack()
        self_import.lab0.pack()
        self_import.lab0['width'] = 45
        self_import.lab0['text'] = '-------- [F2] --------'
        self_import.Windows.update()

        with mss.mss() as sct:
            monitor = {"top": 0, "left": 0, "width": GetSystemMetrics(
                0), "height": GetSystemMetrics(1)}
            mss.tools.to_png(sct.grab(monitor).rgb, sct.grab(
                monitor).size, output='Photo\\photo_t.png')

        self_import.lab0.pack_forget()
        self_import.frame1.pack_forget()
        self_import.Windows.overrideredirect(1)

        global imgas  # pylint: disable=E1101
        imgas = ImageTk.PhotoImage(Image.open('Photo\\photo_t.png'))
        self_import.paint.create_image(0, 0, anchor=tkinter.NW, image=imgas)
        self.location_window = (
            self_import.Windows.winfo_x(), self_import.Windows.winfo_y())
        self_import.paint.pack()
        self_import.Windows.geometry(
            '{}x{}+0+0'.format(self_import.Windows.winfo_screenwidth(), self_import.Windows.winfo_screenheight()))
        self_import.Windows.update()

        self.Auto_capture = 0
        if AVTO_S == 1:
            self.Auto_capture = 1

        self_import.Windows.bind('<B1-Motion>', one)
        self_import.Windows.bind('<ButtonRelease-1>', one)
        self_import.Windows.bind('<F2>', exit_func)
