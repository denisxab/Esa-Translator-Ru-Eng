# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=C0301
# pylint: disable=R0902
"""
Переводчик
"""
import sys
import os
import json
import tkinter
import tkinter.scrolledtext
import requests
import pyperclip  # sudo apt-get install xsel
from t9 import Text_T9
import Orc


class Translete_Elemint:
    """docstring for Translete"""

    def __init__(self):
        super(Translete_Elemint, self).__init__()

        self.Windows = tkinter.Tk()
        self.Windows.title('Translete')
        try:
            self.Windows.iconbitmap('Data/icos.ico')
        except tkinter.TclError:
            self.Windows.iconbitmap()

        self.Background = '#4E51D8'
        self.Text_color = '#FFFFFF'
        self.Check = ''

        self.Windows["bg"] = self.Background
        self.Switches_radio = tkinter.StringVar()
        self.Switches_radio.set('1')

        #__________________________________________________________________________________________________________#
        self.frame1 = tkinter.Frame(self.Windows)

        self.text_box = tkinter.scrolledtext.ScrolledText(
            self.Windows, width=1, height=13)
        self.text_box1 = tkinter.scrolledtext.ScrolledText(
            self.Windows, width=1, height=13)

        self.frame0 = tkinter.Frame(self.Windows)

        self.bat_copy = tkinter.Button(self.frame0,
                                       width=1,
                                       text='COPY',
                                       fg=self.Text_color,
                                       bg=self.Background,
                                       command=self.copy)

        self.bat_clear = tkinter.Button(self.frame0,
                                        width=1,
                                        text='X_X',
                                        fg=self.Text_color,
                                        bg=self.Background,
                                        command=self.clear)

        self.bat_past = tkinter.Button(self.frame0,
                                       width=1,
                                       text='PASTE',
                                       fg=self.Text_color,
                                       bg=self.Background,
                                       command=self.paste)

        self.lab0 = tkinter.Label(self.frame1,
                                  width=1,
                                  bg=self.Background,
                                  fg='#00FFFF',
                                  font=("Helvetica", 10))

        self.radio1 = tkinter.Radiobutton(self.frame1,
                                          text='RU',
                                          selectcolor=self.Background,
                                          bg=self.Background,
                                          fg=self.Text_color,
                                          value='0',
                                          variable=self.Switches_radio,
                                          command=self.radio)

        self.radio2 = tkinter.Radiobutton(self.frame1,
                                          text='ENG',
                                          selectcolor=self.Background,
                                          bg=self.Background,
                                          fg=self.Text_color,
                                          value='1',
                                          variable=self.Switches_radio,
                                          command=self.radio)

        self.bat_token = tkinter.Button(self.Windows,
                                        width=1,
                                        text='API Яндекс.Переводчик',
                                        fg=self.Text_color,
                                        bg=self.Background,
                                        command=self.Token_test)

        self.bat_Spelling = tkinter.Button(self.Windows,
                                           width=1,
                                           text='\\/',
                                           fg=self.Text_color,
                                           bg=self.Background,
                                           command=self.spl)

        self.dont_bat_Spelling = tkinter.Button(self.Windows,
                                                width=1,
                                                text='/\\',
                                                fg=self.Text_color,
                                                bg=self.Background,
                                                command=self.spl_dont)

        self.T9 = Text_T9(self.Windows,
                          self.text_box, 'ru',
                          self.Background,
                          self.Background,
                          self.Text_color)

        self.bat = tkinter.Button(self.Windows,
                                  width=1,
                                  text='STOP',
                                  fg=self.Text_color,
                                  bg=self.Background,
                                  command=self.STOP)

        self.bat1 = tkinter.Button(self.Windows,
                                   width=1,
                                   text='START',
                                   command=self.START,
                                   bg=self.Background,
                                   fg=self.Text_color,
                                   font='BOLD')

        self.bat1.pack()

        self.text_token = tkinter.Text(self.Windows, width=1, height=1)
        self.import_texst = tkinter.Button(self.Windows,
                                           width=1,
                                           text='Save Token',
                                           fg=self.Text_color,
                                           bg=self.Background,
                                           command=self.save_text)

        self.frame3 = tkinter.Frame(self.Windows)

        self.skrin_shot_batton = tkinter.Button(self.frame3,
                                                text='[F1]',
                                                width=1,
                                                bg=self.Background,
                                                fg=self.Text_color,
                                                command=lambda: self.skrinshot_s(0))

        self.skrin_shot_batton_AV = tkinter.Button(self.frame3,
                                                   text='[F3]',
                                                   width=1,
                                                   bg=self.Background,
                                                   fg=self.Text_color,
                                                   command=lambda: self.skrinshot_bid_AVS(0))

        self.skrin_shot_batton_COMBO = tkinter.Button(self.frame3,
                                                      text='[F4]',
                                                      width=1,
                                                      bg=self.Background,
                                                      fg=self.Text_color,
                                                      command=lambda: self.skrinshot_bid_Combo(0))

        self.paint = tkinter.Canvas(self.Windows,
                                    width=self.Windows.winfo_screenwidth(),
                                    height=self.Windows.winfo_screenheight())

        self.scale = tkinter.Scale(self.Windows,
                                   length=367,
                                   width=15,
                                   orient=tkinter.HORIZONTAL,
                                   troughcolor=self.Background,
                                   activebackground=self.Background,
                                   relief=tkinter.FLAT,
                                   showvalue=0,
                                   sliderlength=52,
                                   from_=0,
                                   to=2,
                                   highlightbackground=self.Background,
                                   bg=self.Background)

        #__________________________________________________________________________________________________________#
        self.Windows.bind('<F1>', self.skrinshot_s)
        self.Windows.bind('<F3>', self.skrinshot_bid_AVS)
        self.Windows.bind('<F4>', self.skrinshot_bid_Combo)

        self.START()
        self.token = self.Token_test()
        self.transelte()

        self.Windows.wm_attributes('-topmost', 1)
        self.Windows.mainloop()

    def copy(self):
        """
        Копирывание
        """
        Key_assistant.copy(self)

    def clear(self):
        """
        Отчитска
        """
        Key_assistant.clear(self)

    def paste(self):
        """
        Вставить текст
        """
        Key_assistant.paste(self)

    def transelte(self):
        Translate_text.transelte(self)

    def spl(self):
        self.bat_token.pack_forget()
        self.frame3.pack_forget()
        self.bat_Spelling.pack_forget()
        self.dont_bat_Spelling.pack(fill=tkinter.BOTH, expand=True)
        self.T9.pack()
        self.T9.Getting_text()
        self.Windows.geometry('384x690')

    def spl_dont(self):
        self.T9.pack_forget()
        self.dont_bat_Spelling.pack_forget()
        self.bat_Spelling.pack(fill=tkinter.BOTH, expand=True)
        self.bat_token.pack(fill=tkinter.BOTH, expand=True)
        self.frame3.pack(fill=tkinter.BOTH, expand=True)

    def STOP(self):
        Start_stop.Stop(self)

    def START(self):
        Start_stop.Start(self)
        self.Saved_replies = Save_load_Right('r', {})

    def Token_test(self):
        return Token_class.Token_test(self)

    def save_text(self):
        Token_class.save_text(self)

    def radio(self):
        Translate_text.radio_class(self)

    def skrinshot_s(self, event):
        Orc.ORC().skrinshot_s_class(self)

    def skrinshot_bid_AVS(self, event):
        Orc.ORC().skrinshot_s_class(self)

    def skrinshot_bid_Combo(self, event):
        Orc.ORC().skrinshot_s_class(self)


class Token_class(Translete_Elemint):

    def Token_test(self):
        try:
            with open('Data/token_Y.txt', 'r') as tokens_txt:
                token = tokens_txt.read()
                return token

        except FileNotFoundError:
            self.START()
            Token_class.Debugging_tasks(self)

    def Debugging_tasks(self):
        self.bat_token.pack_forget()
        self.frame3.pack_forget()
        self.skrin_shot_batton.pack_forget()
        self.skrin_shot_batton_AV.pack_forget()
        self.bat_Spelling.pack_forget()
        self.text_token.pack(fill=tkinter.BOTH, expand=True)
        self.text_token.insert(
            tkinter.INSERT, "     Введите Token Яндекс Api переводчик")
        self.import_texst.pack(fill=tkinter.BOTH, expand=True)

    def save_text(self):
        if self.text_token.get(1.0, 'end-1c') == "     Введите Token Яндекс Api переводчик":
            self.text_token.delete(1.0, tkinter.END)

        elif self.text_token.get(1.0, 'end-1c') == "              Token не работает":
            self.text_token.delete(1.0, tkinter.END)

        else:
            test = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={
                                "key": self.text_token.get(1.0, 'end-1c'), 'text': 'Привет', 'format': 'plain', 'lang': 'ru'}).json()
            if test['code'] == 200:
                with open('Data/token_Y.txt', 'w') as file:
                    file.write(self.text_token.get(1.0, 'end-1c'))

                self.START()
                self.STOP()
                self.token = self.text_token.get(1.0, 'end-1c')

            elif test['code'] == 401:
                self.text_token.delete(1.0, tkinter.END)
                self.text_token.insert(
                    tkinter.INSERT, "              Token не работает")


class Translate_text(Translete_Elemint):

    def transelte(self):

        def SAVE_OZ_Text(self, ТEXT, RESAU=False):

            if self.scale.get() == 2:
                self.lab0['text'] = '<NO OFLAIN>'
                return False

            if not RESAU:
                if ТEXT in self.Saved_replies:
                    self.text_box1.delete(1.0, tkinter.END)
                    self.text_box1.insert(
                        tkinter.INSERT, self.Saved_replies[ТEXT])
                    self.lab0['text'] = '|+| |+| |+| {}kb |+| |+| |+|'.format(
                        os.path.getsize('Data/Saved_replies.json')//1024)  # linux
                    return True

            elif RESAU:
                if self.scale.get() == 0:
                    if not ТEXT in self.Saved_replies:
                        self.Saved_replies[ТEXT] = RESAU[0]
                        Save_load_Right('w', self.Saved_replies)
                        return False

                elif self.scale.get() == 1:
                    self.lab0['text'] = '<NO SAVE>'
                    return False

            return False

        def iterant_requst(self, Text, lang, token):
            if Text != '':
                try:
                    a = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate',
                                     params={
                                         "key": token,
                                         'text': str(Text),
                                         'format': 'plain',
                                         'lang': lang}).json()

                    self.Windows.update()
                    if a['code'] == 200:
                        return a['text']
                    return False

                except requests.exceptions.ConnectionError:
                    raise Exception("NO INTERNET")
            return None

        Text_translate = self.text_box.get(1.0, 'end-1c')

        if Text_translate != self.Check:
            self.Check = Text_translate
            if Text_translate:
                self.Windows.update()
                self.lab0['text'] = '--- --- --- --- --- --- --- --- --- --- ---'

                OTV = SAVE_OZ_Text(self, Text_translate)

                if not OTV:

                    if self.Switches_radio.get() == '0':
                        lang = 'ru'
                    elif self.Switches_radio.get() == '1':
                        lang = 'en'

                    resiut = iterant_requst(
                        self, Text_translate, lang, self.token)

                    if resiut:
                        self.text_box1.delete(1.0, tkinter.END)
                        self.text_box1.insert(tkinter.INSERT, str(resiut[0]))
                        self.lab0['text'] = '||| ||| ||| ||| ||| ||| ||| ||| ||| ||| |||'
                        SAVE_OZ_Text(self, Text_translate, resiut)

                    elif not resiut:
                        self.lab0['text'] = "НЕВЕРНЫЙ ТОКЕН"

            elif not Text_translate:
                self.text_box1.delete(1.0, tkinter.END)

            self.Windows.after(300, self.transelte)
        self.Windows.after(1000, self.transelte)

    def radio_class(self):
        if self.Switches_radio.get() == '0':
            self.Check = ' '
            self.text_box.insert(tkinter.INSERT, ' ')
        elif self.Switches_radio.get() == '1':
            self.Check = ' '
            self.text_box.insert(tkinter.INSERT, ' ')


class Key_assistant(Translete_Elemint):

    def copy(self):
        # sudo apt-get install xsel
        pyperclip.copy(self.text_box1.get(1.0, 'end-1c'))

    def clear(self):
        self.text_box.delete(1.0, tkinter.END)
        self.text_box1.delete(1.0, tkinter.END)

    def paste(self):
        self.text_box.insert(tkinter.INSERT, str(pyperclip.paste()))
        self.T9.Getting_text()


class Start_stop(Translete_Elemint):

    def Start(self):
        self.bat1.pack_forget()
        self.Windows.geometry('384x666')
        self.bat.pack(fill=tkinter.BOTH, expand=True)
        self.frame0.pack(fill=tkinter.BOTH, expand=True)
        self.bat_past.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.bat_clear.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.bat_copy.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.text_box.pack(side='top', fill=tkinter.BOTH, expand=True)
        self.frame1.pack(fill=tkinter.BOTH, expand=True)
        self.radio2.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.lab0.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.radio1.pack(side='left', fill=tkinter.BOTH, expand=True)
        self.scale.pack(fill=tkinter.BOTH, expand=True)
        self.text_box1.pack(side='top', fill=tkinter.BOTH, expand=True)
        self.bat_Spelling.pack(fill=tkinter.BOTH, expand=True)
        self.frame3.pack(fill=tkinter.BOTH, expand=True)
        self.skrin_shot_batton.pack(
            side='left', fill=tkinter.BOTH, expand=True)
        self.skrin_shot_batton_AV.pack(
            side='left', fill=tkinter.BOTH, expand=True)
        self.skrin_shot_batton_COMBO.pack(
            side='left', fill=tkinter.BOTH, expand=True)
        self.bat_token.pack(fill=tkinter.BOTH, expand=True)
        self.text_box.delete(1.0, tkinter.END)
        self.text_box1.delete(1.0, tkinter.END)
        self.lab0['text'] = '--- --- ESA - Translate  --- ---'

    def Stop(self):
        self.frame0.pack_forget()
        self.frame1.pack_forget()
        self.frame3.pack_forget()
        self.text_token.pack_forget()
        self.import_texst.pack_forget()
        self.text_box.pack_forget()
        self.bat_copy.pack_forget()
        self.scale.pack_forget()
        self.bat_clear.pack_forget()
        self.bat_past.pack_forget()
        self.text_box1.pack_forget()
        self.lab0.pack_forget()
        self.bat_token.pack_forget()
        self.radio1.pack_forget()
        self.radio2.pack_forget()
        self.bat.pack_forget()
        self.bat_Spelling.pack_forget()
        self.dont_bat_Spelling.pack_forget()
        self.T9.pack_forget()
        self.skrin_shot_batton.pack_forget()
        self.skrin_shot_batton_AV.pack_forget()
        self.skrin_shot_batton_COMBO.pack_forget()
        self.bat1.pack(fill=tkinter.BOTH, expand=True)
        self.Windows.geometry('145x32')


def Save_load_Right(reg: str, Right_words: dict):
    """
    Делает:
    1) Кэширует в self.Right_words

    Нужно:
    0) json
    1) self.Saved_replies
    """
    name = 'Data/Saved_replies.json'  # linix

    if reg == 'r':
        try:
            with open(name, 'r', encoding='utf-8') as JSR:
                Right = json.load(JSR)
        except FileNotFoundError:
            with open(name, 'w', encoding='utf-8') as JSW:
                json.dump({}, JSW, sort_keys=False,
                          ensure_ascii=False)
            with open(name, 'r', encoding='utf-8') as JSR:
                Right = json.load(JSR)
        return Right

    with open(name, 'r', encoding='utf-8') as JSR:
        Right = json.load(JSR)
        Right.update(Right_words)
    with open(name, 'w', encoding='utf-8') as JSW:
        json.dump(Right, JSW, sort_keys=False, ensure_ascii=False)

    return True


if __name__ == '__main__':
    Translete_Elemint()
