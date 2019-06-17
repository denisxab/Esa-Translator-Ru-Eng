import requests
from tkinter import *
import pyperclip
import os
import tkinter.scrolledtext

import win32api
import win32gui


from PIL import Image,ImageTk
import mss
import mss.tools
import cv2
import numpy

######################################################
#https://github.com/UB-Mannheim/tesseract/wiki
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # выбрать файл с Tesseract-OCR
######################################################
import sys
import json
############################################################################################################
#------------------------------------#


def Token_test():
	global token
	try:
		with open('token_Y.txt','r') as tokens_txt:
			token = tokens_txt.read()
	except FileNotFoundError:
		Debugging_tasks()


def SAVE_OZ_Text(ТEXT,RESAU=False):
	if scale.get()==2:
		lab0['text'] = '<NO OFLAIN>'
		return

	elif scale.get()==1:
		lab0['text'] = '<NO SAVE>'
		return


	elif RESAU == False:
		try:
			with open('Saved_replies.json','r',encoding='utf-8') as JSon_R:
				Jsons = json.load(JSon_R)
				if not ТEXT in Jsons:
					return False
				elif ТEXT in Jsons:
					text_box1.delete(1.0, END)
					text_box1.insert(INSERT,Jsons[ТEXT])
					return True

		except FileNotFoundError:
			with open('Saved_replies.json','w',encoding='utf-8') as JSon_W:
				json.dump({},JSon_W,sort_keys=False,ensure_ascii=False)


	elif RESAU != False:
		if scale.get()==0:
			with open('Saved_replies.json','r',encoding='utf-8') as JSon_R:
				Jsons = json.load(JSon_R)
				if not ТEXT in Jsons:
					Jsons[ТEXT]=RESAU[0]
					JSon_R.close()
					with open('Saved_replies.json','w',encoding='utf-8') as JSon_W:
						json.dump(Jsons,JSon_W,sort_keys=False,ensure_ascii=False)
					return False


			 





def transelte():
	def transelte_func (text,lang,token):
		if text != '':
			try:
				a =  requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={"key":token,'text':str(text),'format':'plain','lang':lang}).json()
				if a['code'] == 200:
					return a['text']
				elif a['code'] == 401:
					return '#401##401#'

			except requests.exceptions.ConnectionError:
				return 'ER1*1*1*1*1'



	global Check
	global token

	
	a = text_box.get(1.0, 'end-1c')




	if a != Check:
		lab0['text'] = '--- --- --- --- --- --- --- --- --- --- ---'
		if a !='':
			Check=a
			OTV = SAVE_OZ_Text(a)
			#_____________________________________________________$
			if not OTV:
				if Switches_radio.get() == '0':
					lang = 'ru'
				elif Switches_radio.get() == '1':
					lang = 'en'


				resiut = transelte_func(a,lang,token)


				if resiut == 'ER1*1*1*1*1':
					lab0['text']='NO INTERNET'
					return
				elif resiut == '#401##401#':
					lab0['text'] = "НЕВЕРНЫЙ ТОКЕН"
					Debugging_tasks()
					return

				elif resiut != None:
					text_box1.delete(1.0, END)
					text_box1.insert(INSERT,str(resiut[0]))
					lab0['text'] = '||| ||| ||| ||| ||| ||| ||| ||| ||| ||| |||'
					SAVE_OZ_Text(a,resiut)

			#_____________________________________________________$
			elif OTV:
				lab0['text'] = '|+| |+| |+| {}kb |+| |+| |+|'.format(os.path.getsize('Saved_replies.json')//1024)


		else :
			text_box1.delete(1.0, END)



		root1.after(500, transelte)


	root1.after(1000, transelte)









def spl():
	def Spelling(text):
		Chhelk = []
		if Switches_radio.get() == '0':
			lang = 'en'
		if Switches_radio.get() == '1':
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
	bat_Spelling.grid(columnspan=4,row=6,column=0)

def radio():
	if Switches_radio.get() == '0':
		win32api.LoadKeyboardLayout("00000409",1)

	if Switches_radio.get() == '1':
		win32api.LoadKeyboardLayout("00000419",1)

	global Check
	Check=' '

#------------------------------------#
def STOP():
	global globalF3
	globalF3=[]
	text_token.grid_forget()
	import_texst.grid_forget()
	text_box.grid_forget()
	bat_copy.grid_forget()
	scale.grid_forget()
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
	skrin_shot_batton_AV.grid_forget()
	bat1.grid(row=0,column=0)
	#____________________________________________#

def START():
	bat.grid(columnspan=3,row=0,column=1)
	bat_past.grid(sticky=W,columnspan=3,row=1,column=1)
	bat_clear.grid(columnspan=3,row=1,column=1)
	bat_copy.grid(sticky=E,columnspan=3,row=1,column=2)
	text_box.grid(columnspan=4,row=2,column=1)
	radio1.grid(sticky=W,columnspan=3,row=3,column=1)
	lab0.grid(columnspan=3,row=3,column=1)
	radio2.grid(sticky=E,columnspan=3,row=3,column=2)
	scale.grid(columnspan =3,row=4,column=0)
	text_box1.grid(columnspan=6,row=5,column=1)
	bat_Spelling.grid(columnspan=4,row=6,column=1)
	skrin_shot_batton.grid(sticky=W,columnspan=4,row=8,column=1)
	skrin_shot_batton_AV.grid(sticky=E,columnspan=4,row=8,column=1)
	bat_token.grid(columnspan=4,row=9,column=1)
	text_box.delete(1.0, END)
	text_box1.delete(1.0, END)
	bat1.grid_forget()
	#____________________________________________#
	Token_test()
	transelte()


#------------------------------------#
def paste():
	text_box.insert(INSERT,str(pyperclip.paste()))
	
def copy():
	pyperclip.copy(text_box1.get(1.0, 'end-1c'))
	
	
def clear():
	STOP()
	START()
	
def save_text():
	if text_token.get(1.0, 'end-1c') == "     Введите Token Яндекс Api переводчик":
		text_token.delete(1.0, END)

	elif text_token.get(1.0, 'end-1c') == "              Token не работает":
		text_token.delete(1.0, END)

	
	else:
		test = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={"key":text_token.get(1.0, 'end-1c'),'text':'Привет','format':'plain','lang':'ru'}).json()
		if test['code'] == 200:
			with open('token_Y.txt','w') as file:
				file.write(text_token.get(1.0, 'end-1c'))
			STOP()
			START()

		elif test['code'] == 401:
			text_token.delete(1.0, END)
			text_token.insert(INSERT,"              Token не работает")



def Debugging_tasks():
	bat_token.grid_forget()
	skrin_shot_batton.grid_forget()
	skrin_shot_batton_AV.grid_forget()
	text_token.grid(columnspan=4,row=5,column=0)
	text_token.insert(INSERT,"     Введите Token Яндекс Api переводчик")
	import_texst.grid(columnspan=4,row=6,column=0)


#------------------------------------#
def sending_text(text_sennd,NAME_TEXT):
	a = (text_box.get(1.0, 'end-1c')).split(' ')
	cash_text = a

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
def skrinshot_s(AVTO_S=0):

	def exit_func(event=0):
		nonlocal all_cord_mnogo
		nonlocal Auto_capture
		root1.unbind('<B1-Motion>')
		root1.unbind('<ButtonRelease-1>')
		root1.unbind('<F2>')


		if Auto_capture == 1:
			global globalF3
			paint.grid_forget()
			lab0.grid()
			root1.geometry('+{}+{}'.format(location_window[0],location_window[1]))
			root1.update()
			root1.overrideredirect(0)
			root1.update()
			START()
			lab0['width']=25
			text_box.delete(1.0, END)
			globalF3 = all_cord_mnogo
			Tracking_S()
			root1.bind('F1',skrinshot_bid)
			return


		imags = []
		for x in all_cord_mnogo:

			if x[2] == 0 and x[3] == 0:
				continue

			with mss.mss() as sct:
				monitor = {"top":x[0], "left": x[1], "width": x[2], "height":x[3]}
				try:
					img = cv2.resize(numpy.array(sct.grab(monitor)),(0,0),fx=10,fy=10)
					img = cv2.GaussianBlur(img,(11,11),0)
					imags.append(img)

				except cv2.error:
					continue





		paint.grid_forget()
		lab0.grid()
		root1.geometry('+{}+{}'.format(location_window[0],location_window[1]))
		root1.update()
		root1.overrideredirect(0)
		root1.update()
		START()
		lab0['width']=25
		text_box.delete(1.0, END)


		i=0
		for y in imags:
			try:
				a = pytesseract.image_to_string(y,lang='eng')
				if a != '':
					skrin_shot_batton['text'] = '[+]'
					Switches_radio.set('0')

					
					if i == 0:
						text_box.insert(INSERT,'{} '.format(a))

					else:
						text_box.insert(INSERT,'\n\\/-------------{}-------------------\\/\n {} '.format(i+1,a))

					
					i+=1


					try:
						os.remove('except_photo{}.png'.format(i))
					except FileNotFoundError:
						pass
				else:
					skrin_shot_batton['text'] = '[-]'
					cv2.imwrite('except_photo{}.png'.format(i), y)

			except pytesseract.pytesseract.TesseractNotFoundError:
				if 'tesseract-ocr.exe' in os.listdir():
					os.system('tesseract-ocr.exe')
					return

				else:
					text_box.delete(1.0, END)
					text_box.insert(INSERT,'Для работы этой функции необходимо устоновить tesseract по ссылки\nhttps://github.com/UB-Mannheim/tesseract/wiki\nУкажите при устоновки следующий путь\nC:\\Program Files\\Tesseract-OCR')
					return

			except pytesseract.pytesseract.TesseractError:
				text_box.delete(1.0, END)
				text_box.insert(INSERT,'Выбраный язык не устоновлен - выберите этот язык при устоновки')
				return


		spl()

		root1.bind('F1',skrinshot_bid)



	def one(event):

		def paint_square(event):
			nonlocal x,y
			if x == 0 and y == 0:
				x = event.x
				y = event.y
			else:
				paint.delete('circle')
				paint.create_rectangle(event.x, event.y, x, y, outline = 'blue',tag='circle')


		if event.num == 1:

			nonlocal x,y
			nonlocal location_window
			nonlocal all_cord_mnogo
			#########################################
			x0,x_max = x,event.x
			X =  x0-x_max
			if X < 0:
				X *= -1
			else:
				x0,x_max = x_max,x0
			#########################################
			y0,y_max= y,event.y
			Y =  y0-y_max
			if Y < 0:
				Y *= -1
			else:
				y0,y_max = y_max,y0
			#########################################
			x=y=0

			if x0 == 0 and y0 == 0:
				exit_func()
				return


			rrr = (y0,x0,X,Y,x_max,y_max)
			all_cord_mnogo.append(rrr)
			paint.create_rectangle(x_max,y_max, x0, y0, outline = 'blue',tag = str(x_max))



		else:
			paint_square(event)



	root1.unbind('F1')
	STOP()
	bat1.grid_forget()
	lab0.grid()
	lab0['width']=45
	lab0['text']='-------- [F2] --------'
	root1.update()

	with mss.mss() as sct:
		monitor = {"top":0, "left": 0, "width": win32api.GetSystemMetrics(0), "height":win32api.GetSystemMetrics(1)}
		mss.tools.to_png(sct.grab(monitor).rgb, sct.grab(monitor).size, output='photo_t.png')
	lab0.grid_forget()
	root1.overrideredirect(1)

	global imgas
	imgas = ImageTk.PhotoImage(Image.open('photo_t.png'))
	paint.create_image(0,0, anchor=NW,image=imgas)
	location_window = (root1.winfo_x(),root1.winfo_y())
	paint.grid()
	root1.geometry('+0+0')
	root1.update()


	Auto_capture = 0
	if AVTO_S == 1:
		Auto_capture = 1


	x=y=0
	all_cord_mnogo = []
	root1.bind('<B1-Motion>',one)
	root1.bind('<ButtonRelease-1>',one)
	root1.bind('<F2>',exit_func)


def skrinshot_bid(event):
	skrinshot_s()



#------------- AVTO -----------------------#


def Tracking_S():
	global globalF3

	text_box.delete(1.0, END)


	imags = []

	for xss in globalF3:

		if xss[2] == 0 and xss[3] == 0:
			continue


		dc = win32gui.GetDC(0)
		red = win32api.RGB(78, 81, 216)

		for x in range(xss[2]):
			win32gui.SetPixel(dc,xss[1]+x,xss[0],red) # UP
			win32gui.SetPixel(dc,xss[1]+x,xss[5],red) # UP

		for y in range(xss[3]):
			win32gui.SetPixel(dc,xss[1],xss[0]+y,red) # UP
			win32gui.SetPixel(dc,xss[4],xss[0]+y,red) # UP



		with mss.mss() as sct:
			monitor = {"top":xss[0], "left": xss[1], "width": xss[2], "height":xss[3]}
			try:
				img = cv2.resize(numpy.array(sct.grab(monitor)),(0,0),fx=10,fy=10)
				img = cv2.GaussianBlur(img,(11,11),0)
				imags.append(img)

			except cv2.error:
				continue


	i=0

	for y in imags:

		try:
			a = pytesseract.image_to_string(y,lang='eng')
			if a != '':
				skrin_shot_batton['text'] = '[+]'
				Switches_radio.set('0')

				
				if i == 0:
					text_box.insert(INSERT,'{} '.format(a))

				else:
					text_box.insert(INSERT,'\n\\/-------------{}-------------------\\/\n {} '.format(i+1,a))

				
				i+=1


				try:
					os.remove('except_photo{}.png'.format(i))
				except FileNotFoundError:
					pass
			else:
				skrin_shot_batton['text'] = '[-]'
				cv2.imwrite('except_photo{}.png'.format(i), y)

		except pytesseract.pytesseract.TesseractNotFoundError:
			if 'tesseract-ocr.exe' in os.listdir():
				os.system('tesseract-ocr.exe')
				return

			else:
				text_box.delete(1.0, END)
				text_box.insert(INSERT,'Для работы этой функции необходимо устоновить tesseract по ссылки\nhttps://github.com/UB-Mannheim/tesseract/wiki\nУкажите при устоновки следующий путь\nC:\\Program Files\\Tesseract-OCR')
				return

		except pytesseract.pytesseract.TesseractError:
			text_box.delete(1.0, END)
			text_box.insert(INSERT,'Выбраный язык не устоновлен - выберите этот язык при устоновки')
			return


		spl()




def skrinshot_bid_AVS():
	global globalF3
	if globalF3 == []:
		skrinshot_s(1)
	else:
		Tracking_S()



def skrinshot_bid_AV(event):
	skrinshot_bid_AVS()





#------------------------------------------#
############################################################################################################



############################################################################################################
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
Switches_radio = StringVar()
Switches_radio.set('1')
token = ''
text_dont_bat_Spelling=[]
globalF3 = []
############################################################################################################



############################################################################################################
#____________________________________________________________________________#
text_box = tkinter.scrolledtext.ScrolledText(root1,width=43, height=15)
text_box1= tkinter.scrolledtext.ScrolledText(root1,width=43, height=15)
#____________________________________________________________________________#
lab0= Label(root1,width =25,bg  = Background,fg = '#00FFFF',font = ( "Helvetica" , 10))
#____________________________________________________________________________#
radio1=Radiobutton(root1, text='RU',selectcolor = Background, bg  = Background,fg = Text_color,value='0',variable=Switches_radio,command = radio)
radio2=Radiobutton(root1, text='ENG',selectcolor = Background , bg  = Background,fg = Text_color, value='1',variable=Switches_radio, command = radio)
#____________________________________________________________________________#
bat = Button(root1, text='STOP', width=52,fg = Text_color,bg  = Background, command = STOP)
bat_copy = Button(root1,width =16, text='COPY',fg = Text_color,bg  = Background, command = copy)
bat_clear= Button(root1,width =18, text='X_X',fg = Text_color,bg  = Background, command = clear)
bat_past = Button(root1,width =16,text='PASTE',fg = Text_color,bg  = Background, command = paste)
bat_token = Button(root1, text='API Яндекс.Переводчик', width=52, command = Debugging_tasks,bg  = Background, fg = Text_color)
bat_Spelling=Button(root1,width =52,text='\\/', fg = Text_color,bg  = Background, command = spl)
dont_bat_Spelling=Button(root1,width =52,text='/\\',fg = Text_color,bg  = Background, command = spl_dont)
#____________________________________________________________________________#
bat1 = Button(root1, text='START', width=15, command = START,bg  = Background, fg = Text_color, font = 'BOLD' )
bat1.grid(row=0,column=0)
#____________________________________________________________________________#
text_token= Text(root1,width=45, height=1)
import_texst = Button(root1,width =50,text='Save Token',fg = Text_color,bg  = Background, command = save_text)
#____________________________________________________________________________#

bat_t_Sp0= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text0)
bat_t_Sp1= Button(root1,width=20,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text1)
bat_t_Sp2= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text2)
bat_t_Sp3= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text3)
bat_t_Sp4= Button(root1,width=20,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text4)
bat_t_Sp5= Button(root1,width=19,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text5)
#____________________________________________________________________________#
skrin_shot_batton = Button(root1, text='[F1]', width=26, command = skrinshot_s,bg  = Background, fg = Text_color)
skrin_shot_batton_AV= Button(root1, text='[F3]', width=26, command = skrinshot_bid_AVS,bg  = Background, fg = Text_color)

#____________________________________________________________________________#
paint = Canvas(root1,width=root1.winfo_screenwidth(), height=root1.winfo_screenheight())
scale = Scale(root1, length=367,width=15,orient=HORIZONTAL,troughcolor=Background,activebackground=Background,relief=FLAT ,showvalue=0,sliderlength=52,from_=0, to=2,highlightbackground=Background,bg  = Background)
#____________________________________________________________________________#
root1.bind('<F1>',skrinshot_bid)
root1.bind('<F3>',skrinshot_bid_AV)
#____________________________________________________________________________#
START()
root1.wm_attributes('-topmost',1)
root1.mainloop()
############################################################################################################
