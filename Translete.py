import requests
from tkinter import *
import pyperclip
import os
import win32api
import tkinter.scrolledtext as ScrolledText
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
		#-----------------------------------------------------------------#
		texts = text.split(' ')
		for y in texts:
			respons_Spelling= requests.get('https://speller.yandex.net/services/spellservice.json/checkText?', params={'text':y,'lang':lang})
			if respons_Spelling.json() !=[]:
				Chhelk.append(respons_Spelling.json()[0]['word'])
				Chhelk.append(respons_Spelling.json()[0]['s'])
				return Chhelk

	
	lab0['text'] = '\\/ \\/  \\/  \\/  \\/  \\/'

	bat_Spelling.grid_forget()
	bat_token.grid_forget()
	lab01.grid(columnspan=4,row=7,column=0)
	text_box_spe0.grid(columnspan=4,row=8,column=0)
	dont_bat_Spelling.grid(columnspan=4,row=9,column=0)	

	Chhelk = Spelling(text_box.get(1.0, 'end-1c'))

	try:
		lab01['text'] = Chhelk[0]
		ux = ''
		for x in Chhelk[1]: 
			ux+=x+str(' ')
		text_box_spe0.insert(INSERT,str(ux))
		Chhelk.clear()

	except TypeError:
		spl_dont()

def spl_dont():
	lab0['text'] = '/\\  /\\  /\\  /\\  /\\  /\\'
	lab01.grid_forget()
	dont_bat_Spelling.grid_forget()
	text_box_spe0.grid_forget()
	text_box_spe0.delete(1.0, END)
	bat_Spelling.grid(columnspan=4,row=6,column=0)

def radio():
	if Переключатели.get() == '0':
		win32api.LoadKeyboardLayout("00000409",1)

	if Переключатели.get() == '1':
		win32api.LoadKeyboardLayout("00000419",1)

	global Check
	Check=' '

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

	lab01.grid_forget()

	text_box_spe0.grid_forget()

	dont_bat_Spelling.grid_forget()
	#____________________________________________#
	bat1.grid(row=0,column=0)

def START():

	bat.grid(columnspan=4,row=0,column=0)

	bat_past.grid(row=1,column=0)

	bat_clear.grid(row=1,column=1)

	bat_copy.grid(row=1,column=2)

	text_box.grid(columnspan=4,row=2,column=0)

	lab0.grid(row = 3,column = 1)

	radio1.grid(row=3,column=0)

	radio2.grid(row=3,column=2)

	text_box1.grid(columnspan=6,row=4,column=0)

	bat_Spelling.grid(columnspan=4,row=5,column=0)

	bat_token.grid(columnspan=4,row=6,column=0)

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
	text_token.grid(columnspan=4,row=5,column=0)
	text_token.insert(INSERT,"     Введите Token Яндекс Api переводчик")
	import_texst.grid(columnspan=4,row=6,column=0)
#------------------------------------#
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
#____________________________________________________________________________#
text_box = ScrolledText.ScrolledText(root1,width=43, height=15)
text_box1= ScrolledText.ScrolledText(root1,width=43, height=15)


text_box_spe0 = ScrolledText.ScrolledText(root1,width=43, height=1)
#____________________________________________________________________________#

lab0= Label(root1,width =25,bg  = Background,fg = '#00FFFF',font = ( "Helvetica" , 10))


lab01= Label(root1,width =10,bg  = Background,fg = Text_color,font = ( "Helvetica" , 8))
#____________________________________________________________________________#
radio1=Radiobutton(root1, text='Русский', selectcolor = Background, bg  = Background,fg = Text_color,value='0',variable=Переключатели,command = radio) # переключатель 
radio2=Radiobutton(root1, text='Английский',  selectcolor = Background , bg  = Background,fg = Text_color, value='1',variable=Переключатели, command = radio) # переключатель 
#____________________________________________________________________________#
bat = Button(root1, text='STOP', width=50,fg = Text_color,bg  = Background, command = STOP) # кнопка

bat_copy = Button(root1,width =10, text='COPY',fg = Text_color,bg  = Background, command = copy) # кнопка
bat_clear= Button(root1,width =27, text='X_X',fg = Text_color,bg  = Background, command = clear) # кнопка
bat_past = Button(root1,width =7,text='PASTE',fg = Text_color,bg  = Background, command = paste) # кнопка

bat_token = Button(root1, text='API Яндекс.Переводчик', width=60, command = Отладик_задач,bg  = Background, fg = Text_color, font = ( "Helvetica" , 7) ) # кнопка

bat_Spelling=Button(root1,width =60,text='\\/',fg = Text_color,bg  = Background, command = spl,font = ( "Helvetica" , 7)) # кнопка
dont_bat_Spelling=Button(root1,width =60,text='/\\',fg = Text_color,bg  = Background, command = spl_dont,font = ( "Helvetica" , 7)) # кнопка

#____________________________________________________________________________#

bat1 = Button(root1, text='START', width=15, command = START,bg  = Background, fg = Text_color, font = 'BOLD' ) # кнопка
bat1.grid(row=0,column=0)

#____________________________________________________________________________#

text_token= Text(root1,width=45, height=1)
import_texst = Button(root1,width =50,text='Save Token',fg = Text_color,bg  = Background, command = save_text) # кнопка

#____________________________________________________________________________#
START()
#____________________________________________________________________________#
root1.wm_attributes('-topmost',1)
root1.mainloop()
