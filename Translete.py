import requests
from tkinter import *
import pyperclip
import os
import win32api
import tkinter.scrolledtext as ScrolledText
import inspect
import time
from pynput import mouse
import win32api
import win32gui
 

import mss
import mss.tools
import cv2
import numpy



######################################################
#https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # выбрать файл куда устоновилсья
######################################################





#------------------------------------#
def test_token(token):
	respons0 = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={"key":token,
			'text':'Привет мир !','format':'plain','lang':'en'})
	if respons0.json()['code'] == 401:
		lab0['text'] = ' - Token False -'
		Отладик_задач()
		return 0
	else:
		radio()
		transelte()

def transelte():
	def transelte_func (text,lang,token):
		if text != '':
			global Check

			respons0 = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={"key":token,'text':str(text),'format':'plain','lang':lang})
			lab0['text'] = '||| ||| ||| ||| ||| ||| ||| ||| ||| ||| |||'
			resiut = respons0.json()['text']
			Check=text

			return resiut

	global Check
	global token

	a = text_box.get(1.0, 'end-1c')
	b = text_box1.get(1.0, END)
	lab0['text'] = '--- --- --- --- --- --- --- --- --- --- ---'


	if a  != Check:
		if Переключатели.get() == '0':
			lang = 'ru'

		if Переключатели.get() == '1':
			lang = 'en'

		resiut = transelte_func(a,lang,token)

		if resiut != None:
			text_box1.delete(1.0, END)
			text_box1.insert(INSERT,str(resiut[0]))

		else :
			text_box1.delete(1.0, END)

		root1.after(500, transelte)

	else :
		root1.after(1000, transelte)

def spl():

	def Spelling(text):
		Chhelk = []
		if Переключатели.get() == '0':
			lang = 'en'
		if Переключатели.get() == '1':
			lang = 'ru'

		texts = text.split(' ')

		text_str=''
		i= len(texts)
		io = 0
		for y in texts:
			if i == io+1:
				text_str+=y
			else:
				text_str+=y+' '
			io+=1

		respons_Spelling= requests.get('https://speller.yandex.net/services/spellservice.json/checkText?', params={'text':text_str,'lang':lang})
		if respons_Spelling.json() !=[]:
			Chhelk.append(respons_Spelling.json()[0]['word'])
			Chhelk.append(respons_Spelling.json()[0]['s'])
			return Chhelk


	lab0['text'] = '\\/ \\/  \\/  \\/  \\/  \\/'
	bat_Spelling.grid_forget()
	bat_token.grid_forget()
	dont_bat_Spelling.grid(columnspan=4,row=7,column=0)
	Chhelk = Spelling(text_box.get(1.0, 'end-1c'))

	try:
		dont_bat_Spelling['text']=Chhelk[0]
		global text_dont_bat_Spelling
		for x in range(6):
			try:
				text_dont_bat_Spelling.append(Chhelk[1][x])
			except IndexError:
				text_dont_bat_Spelling.append('-')

		text_dont_bat_Spelling.append(Chhelk[0])
		bat_t_Sp0['text']=text_dont_bat_Spelling[0]
		bat_t_Sp1['text']=text_dont_bat_Spelling[1]
		bat_t_Sp2['text']=text_dont_bat_Spelling[2]
		bat_t_Sp3['text']=text_dont_bat_Spelling[3]
		bat_t_Sp4['text']=text_dont_bat_Spelling[4]
		bat_t_Sp5['text']=text_dont_bat_Spelling[5]

					
		bat_t_Sp0.grid(sticky=W,columnspan=3,row=9,column=0)
		bat_t_Sp1.grid(columnspan=3,row=9,column=0)
		bat_t_Sp2.grid(sticky=E,columnspan=3,row=9,column=1)
		bat_t_Sp3.grid(sticky=W,columnspan=3,row=10,column=0)
		bat_t_Sp4.grid(columnspan=3,row=10,column=0)
		bat_t_Sp5.grid(sticky=E,columnspan=3,row=10,column=1)

		Chhelk.clear()

	except TypeError:
		spl_dont()
def spl_dont():
	lab0['text'] = '/\\  /\\  /\\  /\\  /\\  /\\'
	global text_dont_bat_Spelling
	text_dont_bat_Spelling.clear()
	dont_bat_Spelling.grid_forget()
	bat_t_Sp0.grid_forget()
	bat_t_Sp1.grid_forget()
	bat_t_Sp2.grid_forget()
	bat_t_Sp3.grid_forget()
	bat_t_Sp4.grid_forget()
	bat_t_Sp5.grid_forget()
	bat_Spelling.grid(columnspan=4,row=5,column=0)

def radio():
	if Переключатели.get() == '0':
		win32api.LoadKeyboardLayout("00000409",1)

	if Переключатели.get() == '1':
		win32api.LoadKeyboardLayout("00000419",1)

	global Check
	Check=' '

#------------------------------------#
def STOP():
	text_token.grid_forget()
	
	import_texst.grid_forget()

	text_box.grid_forget()

	bat_copy.grid_forget()

	bat_clear.grid_forget()

	bat_past.grid_forget()

	text_box1.grid_forget()

	lab0.grid_forget ()

	bat_token.grid_forget()

	radio1.grid_forget()

	radio2.grid_forget()

	bat.grid_forget()

	bat_Spelling.grid_forget()

	dont_bat_Spelling.grid_forget()

	bat_t_Sp0.grid_forget()
	bat_t_Sp1.grid_forget()
	bat_t_Sp2.grid_forget()
	bat_t_Sp3.grid_forget()
	bat_t_Sp4.grid_forget()
	bat_t_Sp5.grid_forget()

	skrin_shot_batton.grid_forget()




	#____________________________________________#
	bat1.grid(row=0,column=0)
def START():

	bat.grid(columnspan=3,row=0,column=0)

	bat_past.grid(sticky=W,columnspan=3,row=1,column=0)

	bat_clear.grid(columnspan=3,row=1,column=0)

	bat_copy.grid(sticky=E,columnspan=3,row=1,column=1)

	radio1.grid(sticky=W,columnspan=3,row=3,column=0)

	lab0.grid(columnspan=3,row=3,column=0)

	radio2.grid(sticky=E,columnspan=3,row=3,column=1)

	text_box.grid(columnspan=4,row=2,column=0)

	text_box1.grid(columnspan=6,row=4,column=0)

	bat_Spelling.grid(columnspan=4,row=5,column=0)

	skrin_shot_batton.grid(columnspan=4,row=6,column=0)

	bat_token.grid(columnspan=4,row=7,column=0)



	text_box.delete(1.0, END)

	text_box1.delete(1.0, END)

	bat1.grid_forget()

	#____________________________________________#
	try:

		with open('token_Y.txt','r') as file:
			token_r = file.read()
			global token
			token.append(token_r)

		test_token(token)

	except FileNotFoundError:
		lab0['text'] = ' - Token False -'
		Отладик_задач()
#------------------------------------#

def paste():
	a = pyperclip.paste()
	text_box.insert(INSERT,str(a))
	pass
def copy():
	pyperclip.copy(text_box1.get(1.0, END))
	pass
def clear():
	STOP()
	START()
def save_text():
	if text_token.get(1.0, 'end-1c') == "  Введите Token Яндекс Api переводчик":
		text_token.delete(1.0, END)

	elif text_token.get(1.0, 'end-1c') == "               Token не работает":
		text_token.delete(1.0, END)

	else:
		test = test_token(text_token.get(1.0, 'end-1c'))
		if test != 0:
			file = open('token_Y.txt','w')
			file.write(text_token.get(1.0, 'end-1c'))
			file.close()
			STOP()
			START()
		else:
			text_token.delete(1.0, END)
			text_token.insert(INSERT,"               Token не работает")

def Отладик_задач():
	bat_token.grid_forget()
	skrin_shot_batton.grid_forget()
	text_token.grid(columnspan=4,row=5,column=0)
	text_token.insert(INSERT,"     Введите Token Яндекс Api переводчик")
	import_texst.grid(columnspan=4,row=6,column=0)
#------------------------------------#
def sending_text(text_sennd,NAME_TEXT):

	a = (text_box.get(1.0, 'end-1c')).split(' ')
	cash_text= a
	i = -1
	for x in a:
		i+=1
		if x == NAME_TEXT:
			cash_text.pop(i)
			cash_text.insert(i,text_sennd)

	text=''
	i= len(cash_text)
	io = 0
	for y in cash_text:
		if i == io+1:
			text+=y
		else:
			text+=y+' '
		io+=1

	text_box.delete(1.0, END)
	text_box.insert(INSERT,text)
	spl_dont()
	spl()
def input_text0():
	global text_dont_bat_Spelling
	sending_text(text_dont_bat_Spelling[0],text_dont_bat_Spelling[6])
def input_text1():
	global text_dont_bat_Spelling
	sending_text(text_dont_bat_Spelling[1],text_dont_bat_Spelling[6])
def input_text2():
	global text_dont_bat_Spelling
	sending_text(text_dont_bat_Spelling[2],text_dont_bat_Spelling[6])
def input_text3():
	global text_dont_bat_Spelling
	sending_text(text_dont_bat_Spelling[3],text_dont_bat_Spelling[6])
def input_text4():
	global text_dont_bat_Spelling
	sending_text(text_dont_bat_Spelling[4],text_dont_bat_Spelling[6])
def input_text5():
	global text_dont_bat_Spelling
	sending_text(text_dont_bat_Spelling[5],text_dont_bat_Spelling[6])
#------------------------------------#



def skrinshot():
	def кординаты_мыши():
		def on_click(x, y, button, pressed):
			#####################
			nonlocal  mouse_kl
			f = x,y
			mouse_kl.append(f)
			if not pressed:
				return False
			#####################
		mouse_kl = []
		with mouse.Listener(on_click=on_click) as listener:
		    listener.join()
		return mouse_kl

	def отчитска(mouse_kl):
		#####################
		mouse_REQ = []
		#####################
		x0 = mouse_kl[0][0]
		x_max = mouse_kl[1][0]
		X =  x0-x_max
		if X < 0:
			X *= -1
		else:
			b  = x0
			x0 = x_max
			x_max = b
		f = x0,x_max,X
		mouse_REQ.append(f)
		#####################
		y0 = mouse_kl[0][1]
		y_max = mouse_kl[1][1]
		Y =  y0-y_max
		if Y < 0:
			Y *= -1
		else:
			b  = y0
			y0 = y_max
			y_max = b
		g = y0,y_max,Y
		mouse_REQ.append(g)
		#####################
		return mouse_REQ

	def заливка(JND):
		# Helpers
		# mss.tools.to_png(sct.grab(monitor).rgb, sct.grab(monitor).size, output="1.png")
		# cv2.imwrite('2.png', фото)
		# print(pytesseract.image_to_string(Image.open('1.png')))

		dc = win32gui.GetDC(0)
		red = win32api.RGB(78, 81, 216)
		x0 = JND[0][0]
		y0 = JND[1][0]

		for x in range(JND[0][2]):
			win32gui.SetPixel(dc,x0+x,y0,red) # UP
			win32gui.SetPixel(dc,x0+x,JND[1][1],red) # UP

		for y in range(JND[1][2]):
			win32gui.SetPixel(dc,x0,y0+y,red) # UP
			win32gui.SetPixel(dc,JND[0][1],y0+y,red) # UP


		with mss.mss() as sct:
			monitor = {"top": JND[1][0], "left": JND[0][0], "width": JND[0][2], "height":JND[1][2]}
			img = numpy.array(sct.grab(monitor))
			фото = cv2.resize(img,(0,0),fx=10,fy=10)
			фото = cv2.GaussianBlur(фото,(11,11),0)

			try:
				a = pytesseract.image_to_string(фото)
				if a != '':
					skrin_shot_batton['text'] = '[+]'
					text_box.delete(1.0, END)
					text_box.insert(INSERT,str(a))
					try:
						os.remove('except_photo.png')
					except FileNotFoundError:
						pass
				else:
					skrin_shot_batton['text'] = '[-]'
					cv2.imwrite('except_photo.png', фото)


			except pytesseract.pytesseract.TesseractNotFoundError:
				text_box.delete(1.0, END)
				text_box.insert(INSERT,'Для работы этой функции необходимо устоновить tesseract по ссылки\nhttps://github.com/UB-Mannheim/tesseract/wiki\nУкажите при устоновки следующий путь\nC:\\Program Files\\Tesseract-OCR')

	skrin_shot_batton['text'] = '[0]'
	заливка(отчитска(кординаты_мыши()))

	

	



Background ='#4E51D8'
Text_color='#FFFFFF'
root1=Tk()
try:
	root1.iconbitmap('icos.ico')
except:
	root1.iconbitmap()

root1.title('Translete')
root1["bg"] = Background
root1.resizable(width=False, height=False)

Check = []
Переключатели = StringVar()
Переключатели.set('1') 
token = []
text_dont_bat_Spelling=[]


############################################################################################################
#____________________________________________________________________________#
text_box = ScrolledText.ScrolledText(root1,width=43, height=15)
text_box1= ScrolledText.ScrolledText(root1,width=43, height=15)
#____________________________________________________________________________#
lab0= Label(root1,width =25,bg  = Background,fg = '#00FFFF',font = ( "Helvetica" , 10))
#____________________________________________________________________________#
radio1=Radiobutton(root1, text='RU',selectcolor = Background, bg  = Background,fg = Text_color,value='0',variable=Переключатели,command = radio) # переключатель 
radio2=Radiobutton(root1, text='ENG',selectcolor = Background , bg  = Background,fg = Text_color, value='1',variable=Переключатели, command = radio) # переключатель 
#____________________________________________________________________________#
bat = Button(root1, text='STOP', width=52,fg = Text_color,bg  = Background, command = STOP) # кнопка
bat_copy = Button(root1,width =16, text='COPY',fg = Text_color,bg  = Background, command = copy) # кнопка
bat_clear= Button(root1,width =17, text='X_X',fg = Text_color,bg  = Background, command = clear) # кнопка
bat_past = Button(root1,width =16,text='PASTE',fg = Text_color,bg  = Background, command = paste) # кнопка
bat_token = Button(root1, text='API Яндекс.Переводчик', width=52, command = Отладик_задач,bg  = Background, fg = Text_color) # кнопка
bat_Spelling=Button(root1,width =52,text='\\/', fg = Text_color,bg  = Background, command = spl) # кнопка
dont_bat_Spelling=Button(root1,width =52,text='/\\',fg = Text_color,bg  = Background, command = spl_dont) # кнопка
#____________________________________________________________________________#
bat1 = Button(root1, text='START', width=15, command = START,bg  = Background, fg = Text_color, font = 'BOLD' ) # кнопка
bat1.grid(row=0,column=0)
#____________________________________________________________________________#
text_token= Text(root1,width=45, height=1)
import_texst = Button(root1,width =50,text='Save Token',fg = Text_color,bg  = Background, command = save_text) # кнопка
#____________________________________________________________________________#

bat_t_Sp0= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text0) # 
bat_t_Sp1= Button(root1,width=20,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text1) # 
bat_t_Sp2= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text2) # 
bat_t_Sp3= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text3) # 
bat_t_Sp4= Button(root1,width=20,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text4) # 
bat_t_Sp5= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text5) # 
#____________________________________________________________________________#
skrin_shot_batton = Button(root1, text='[O]', width=52, command = skrinshot,bg  = Background, fg = Text_color) # кнопка
#____________________________________________________________________________#

START()
root1.wm_attributes('-topmost',1)
root1.mainloop()
############################################################################################################
