
import sys
import os

if os.path.basename(__file__) == 'Translate.py':
	import custom_libraries
	custom_libraries.mainCL()

import json
from tkinter import *
import tkinter.scrolledtext
from re import findall,compile

import requests
import pyperclip

if sys.platform == 'win32':
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
I_killed_PEP_8 = True
############################################################################################################
#---------------- Translator --------------------#

def SAVE_OZ_Text(ТEXT,RESAU=False):
	if scale.get()==2:
		lab0['text'] = '<NO OFLAIN>'
		return False

	

	if RESAU == False:
		try:
			with open('Saved_replies.json','r',encoding='utf-8') as JSon_R:
				Jsons = json.load(JSon_R)
				if not ТEXT in Jsons:
					return False
				elif ТEXT in Jsons:
					text_box1.delete(1.0, END)
					text_box1.insert(INSERT,Jsons[ТEXT])
					lab0['text'] = '|+| |+| |+| {}kb |+| |+| |+|'.format(os.path.getsize('Saved_replies.json')//1024)
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

		elif scale.get()==1:
			lab0['text'] = '<NO SAVE>'
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
		Check=a
		lab0['text'] = '--- --- --- --- --- --- --- --- --- --- ---'
		if a !='':
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

		else :
			text_box1.delete(1.0, END)

		root1.after(300, transelte)
	root1.after(1000, transelte)

def radio():
	global Check
	if Switches_radio.get() == '0':
		win32api.LoadKeyboardLayout("00000409",1)
		Check=' '
		text_box.insert(INSERT,' ')
	elif Switches_radio.get() == '1':
		win32api.LoadKeyboardLayout("00000419",1)
		Check=' '
		text_box.insert(INSERT,' ')

#-------------- STOP - START ----------------------#
def STOP():
	global globalF3
	globalF3=[]
	frame0.pack_forget()
	frame1.pack_forget()
	frame2.pack_forget()
	frame3.pack_forget()
	text_token.pack_forget()
	import_texst.pack_forget()
	text_box.pack_forget()
	bat_copy.pack_forget()
	scale.pack_forget()
	bat_clear.pack_forget()
	bat_past.pack_forget()
	text_box1.pack_forget()
	lab0.pack_forget ()
	bat_token.pack_forget()
	radio1.pack_forget()
	radio2.pack_forget()
	bat.pack_forget()
	bat_Spelling.pack_forget()
	dont_bat_Spelling.pack_forget()
	frame2.pack_forget()
	bat_t_Sp0.pack_forget()
	bat_t_Sp1.pack_forget()
	bat_t_Sp2.pack_forget()
	frame21.pack_forget()
	bat_t_Sp3.pack_forget()
	bat_t_Sp4.pack_forget()
	bat_t_Sp5.pack_forget()
	skrin_shot_batton.pack_forget()
	skrin_shot_batton_AV.pack_forget()
	skrin_shot_batton_COMBO.pack_forget()
	bat1.pack(fill=BOTH,expand=True)
	root1.geometry('145x32')
	# root1.update()
	# print(root1.winfo_width(),root1.winfo_height())
	#____________________________________________#

def START():
	bat1.pack_forget()
	root1.geometry('384x666')
	bat.pack(fill=BOTH,expand=True)

	frame0.pack(fill=BOTH,expand=True)
	bat_past.pack(side='left',fill=BOTH,expand=True)
	bat_clear.pack(side='left',fill=BOTH,expand=True)
	bat_copy.pack(side='left',fill=BOTH,expand=True)

	text_box.pack(side='top',fill=BOTH,expand=True)

	frame1.pack(fill=BOTH,expand=True)
	radio2.pack(side='left',fill=BOTH,expand=True)
	lab0.pack(side='left',fill=BOTH,expand=True)
	radio1.pack(side='left',fill=BOTH,expand=True)

	scale.pack(fill=BOTH,expand=True)
	text_box1.pack(side='top',fill=BOTH,expand=True)
	bat_Spelling.pack(fill=BOTH,expand=True)

	frame3.pack(fill=BOTH,expand=True)
	skrin_shot_batton.pack(side='left',fill=BOTH,expand=True)
	skrin_shot_batton_AV.pack(side='left',fill=BOTH,expand=True)
	skrin_shot_batton_COMBO.pack(side='left',fill=BOTH,expand=True)

	bat_token.pack(fill=BOTH,expand=True)
	#____________________________________________#
	text_box.delete(1.0, END)
	text_box1.delete(1.0, END)
	Token_test()
	lab0['text'] = '--- --- ESA - Translate  --- ---'
	transelte()
#---------------- Utilities  --------------------#

def paste():
	text_box.insert(INSERT,str(pyperclip.paste()))
	spl_dont()
	spl()
		
def copy():
	pyperclip.copy(text_box1.get(1.0, 'end-1c'))
	pass
	
def clear():
	text_box.delete(1.0, END)
	text_box1.delete(1.0, END)

#--------------- TOKEN ---------------------#

def Token_test():
	global token
	try:
		with open('token_Y.txt','r') as tokens_txt:
			token = tokens_txt.read()
	except FileNotFoundError:
		Debugging_tasks()

def Debugging_tasks():
	bat_token.pack_forget()
	frame3.pack_forget()
	skrin_shot_batton.pack_forget()
	skrin_shot_batton_AV.pack_forget()
	bat_Spelling.pack_forget()

	text_token.pack(fill=BOTH,expand=True)
	text_token.insert(INSERT,"     Введите Token Яндекс Api переводчик")
	import_texst.pack(fill=BOTH,expand=True)

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

#------------------- Spelling -----------------#

def spl():
	def Spelling(text):
		if Switches_radio.get() == '0':
			lang = 'en'
		if Switches_radio.get() == '1':
			lang = 'ru'


		text = ' '.join(re.findall(re.compile('[A-Za-z0-9а-яА-Я]+'), text))
		respons_Spelling= requests.get('https://speller.yandex.net/services/spellservice.json/checkText?', params={'text':text,'lang':lang}).json()
		if respons_Spelling != []:
			Chhelk=[respons_Spelling[0]['word']]
			Chhelk.append(respons_Spelling[0]['s'])
			return Chhelk


	lab0['text'] = '\\/ \\/  \\/  \\/  \\/  \\/'

	frame3.pack_forget()
	bat_Spelling.pack_forget()
	bat_token.pack_forget()
	dont_bat_Spelling.pack(fill=BOTH,expand=True)


	Chhelk = Spelling(text_box.get(1.0, 'end-1c'))


	try:
		global text_dont_bat_Spelling
		dont_bat_Spelling['text']=Chhelk[0]
		for x in range(6):
			try:
				text_dont_bat_Spelling.append(Chhelk[1][x])
			except IndexError:
				text_dont_bat_Spelling.append('-')

		text_dont_bat_Spelling.append(Chhelk[0])
		bat_t_Sp0['text'],bat_t_Sp1['text'],bat_t_Sp2['text']=text_dont_bat_Spelling[0],text_dont_bat_Spelling[1],text_dont_bat_Spelling[2]
		bat_t_Sp3['text'],bat_t_Sp4['text'],bat_t_Sp5['text']=text_dont_bat_Spelling[3],text_dont_bat_Spelling[4],text_dont_bat_Spelling[5]

		frame2.pack(fill=BOTH,expand=True)
		bat_t_Sp0.pack(side='left',fill=BOTH,expand=True)
		bat_t_Sp1.pack(side='left',fill=BOTH,expand=True)
		bat_t_Sp2.pack(side='left',fill=BOTH,expand=True)

		frame21.pack(fill=BOTH,expand=True)
		bat_t_Sp3.pack(side='left',fill=BOTH,expand=True)
		bat_t_Sp4.pack(side='left',fill=BOTH,expand=True)
		bat_t_Sp5.pack(side='left',fill=BOTH,expand=True)

		Chhelk.clear()

	except TypeError:
		spl_dont()

def spl_dont():
	lab0['text'] = '/\\  /\\  /\\  /\\  /\\  /\\'
	global text_dont_bat_Spelling
	text_dont_bat_Spelling.clear()
	dont_bat_Spelling.pack_forget()

	frame2.pack_forget()
	frame21.pack_forget()
	bat_t_Sp0.pack_forget()
	bat_t_Sp1.pack_forget()
	bat_t_Sp2.pack_forget()
	bat_t_Sp3.pack_forget()
	bat_t_Sp4.pack_forget()
	bat_t_Sp5.pack_forget()
	bat_Spelling.pack(fill=BOTH,expand=True)
	frame3.pack(fill=BOTH,expand=True)

def sending_text(text_sennd,NAME_TEXT):
	#############TEST##################
	# умнек мир приве                 #
	# умнек! мир приве                #
	# Првие. умнек как дила,          #
	# Приве. умнек\ как дила0         #
	# 10 # . Приве0 как дила, умнек0  #
	# 3Умнек 10приве1 Приве1. 10умнек\#
	#cd Ge UL aaa don't bat UL aaa Spelling  #
	###################################


	a = text_box.get(1.0, 'end-1c')
	cash_text = re.findall(re.compile('[A-Za-zа-яА-Я]+'), a)
	cash_comma = re.findall(re.compile('[^A-Za-zа-яА-Я]+'), a)

	else_no_t=True
	for x in re.findall(re.compile('[A-Za-zа-яА-Я]+'), a):
		if x == NAME_TEXT:
			i=cash_text.index(x)
			cash_text.pop(i)
			cash_text.insert(i,text_sennd)
			else_no_t=False


	if else_no_t:

		op = re.findall(re.compile('[A-Za-zа-яА-Я]+'), a)
		i = len(NAME_TEXT.split(' '))
		NAME_TEXT = ''.join(NAME_TEXT.split(' '))
		io=0
		poi=[]
		for x in range(len(op)):

			for y in range(i):
				try:
					poi.append(op[x+io])
					io+=1
				except IndexError:
					break

			if ''.join(poi) == NAME_TEXT:
				ihh=cash_text.index(poi[0])
				for yu in range(i):
					cash_text.pop(ihh)
				cash_text.insert(ihh,text_sennd)

			poi=[]
			io=0


	for x in cash_comma:
		split_x = x.split(' ')
		for y in split_x:
			if y in re.findall(re.compile('[0-9]+'), x):

				i = cash_comma.index(x)
				try:
					if split_x[0]!='':
						cash_comma.pop(i)
						cash_comma.insert(i,' {} '.format(y))

					elif split_x[0]=='' and split_x[2] != '':
						pass

				except IndexError:
					cash_comma.pop(i)
					cash_comma.insert(i,'{} '.format(y))


	try:
		b = ' '.join(a.split(' ')[0])[0]
		if not b in re.findall(re.compile('[A-Za-zа-яА-Я]+'), b):
			cash_text.insert(0,'-')

	except IndexError:
		cash_text.insert(0,'-')

	i=1
	for x in cash_comma:
		cash_text.insert(i,x)
		i+=2


	text_box.delete(1.0, END)
	text_box.insert(INSERT,''.join(cash_text))
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

#---------------- ORC --------------------#

def skrinshot_s(AVTO_S=0):

	def exit_func(event=0):
		nonlocal all_cord_mnogo
		nonlocal Auto_capture
		root1.unbind('<B1-Motion>')
		root1.unbind('<ButtonRelease-1>')
		root1.unbind('<F2>')


		if Auto_capture == 1:
			global globalF3
			paint.pack_forget()
			bat1.pack()
			root1.geometry('145x32+{}+{}'.format(location_window[0],location_window[1]))
			root1.update()
			root1.overrideredirect(0)
			root1.update()
			START()
			lab0['width']=25
			text_box.delete(1.0, END)
			text_box1.delete(1.0, END)
			globalF3 = all_cord_mnogo
			Tracking_S()
			# root1.bind('F1',skrinshot_bid)
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



		paint.pack_forget()
		bat1.pack()
		root1.geometry('145x32+{}+{}'.format(location_window[0],location_window[1]))
		root1.update()
		root1.overrideredirect(0)
		root1.update()
		START()
		lab0['width']=25
		text_box.delete(1.0, END)
		text_box1.delete(1.0, END)
		# root1.bind('F1',skrinshot_bid)


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
						text_box.insert(INSERT,'\n\\/-------------{}-------------------\\/\n{} '.format(i+1,a))

					
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



	# root1.unbind('F1')
	# root1.unbind('F3')
	# root1.unbind('F4')
	STOP()
	bat1.pack_forget()
	frame1.pack()
	lab0.pack()
	lab0['width']=45
	lab0['text']='-------- [F2] --------'
	root1.update()

	with mss.mss() as sct:
		monitor = {"top":0, "left": 0, "width": win32api.GetSystemMetrics(0), "height":win32api.GetSystemMetrics(1)}
		mss.tools.to_png(sct.grab(monitor).rgb, sct.grab(monitor).size, output='photo_t.png')
	lab0.pack_forget()
	frame1.pack_forget()
	root1.overrideredirect(1)

	global imgas
	imgas = ImageTk.PhotoImage(Image.open('photo_t.png'))
	paint.create_image(0,0, anchor=NW,image=imgas)
	location_window = (root1.winfo_x(),root1.winfo_y())
	paint.pack()
	root1.geometry('{}x{}+0+0'.format(root1.winfo_screenwidth(),root1.winfo_screenheight()))
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
	pass

#------------- ORC AVTO -----------------------#

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
	pass

#------------- COMBO ORC -----------------------#9

def overlay_tk(text_n,t,l,w,h):
	global token
	a =  requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params={"key":token,'text':str(text_n),'format':'plain','lang':'ru'}).json()
	if a['code'] == 200 and a !=' ':

		jk = 0
		ok = []
		for x in list(a['text'][0]):
			if jk >= w:
				ok.append('\n')
				jk=0
			if x == '\n':
				ok.append(' ')
			else:
				jk+=10
				ok.append(x)

		hj = 0
		for x in ok:
			if x == '\n':
				hj+=30


		if h <= hj:
			h=hj


		root1.update()
		windo_tk=Toplevel()
		windo_tk.overrideredirect(1) 
		windo_tk.geometry('{}x{}+{}+{}'.format(w,h,l,t))
		vbat = Button(windo_tk,text = ''.join(ok),command=lambda:windo_tk.destroy())
		vbat.pack(fill=BOTH,expand=True)
		windo_tk.wm_attributes('-topmost',1)

def skrinshot_bid_Combo():
	def exit_func(event=0):
		nonlocal all_cord_mnogo
		root1.unbind('<B1-Motion>')
		root1.unbind('<ButtonRelease-1>')
		root1.unbind('<F2>')


		imags = []
		cords = []
		for x in all_cord_mnogo:

			if x[2] == 0 and x[3] == 0:
				continue

			with mss.mss() as sct:
				cords.append(x[0])
				cords.append(x[1])
				cords.append(x[2])
				cords.append(x[3])
				monitor = {"top":x[0], "left": x[1], "width": x[2], "height":x[3]}
				try:
					img = cv2.resize(numpy.array(sct.grab(monitor)),(0,0),fx=10,fy=10)
					img = cv2.GaussianBlur(img,(11,11),0)
					imags.append(img)

				except cv2.error:
					continue

		paint.pack_forget()
		bat1.pack()
		root1.geometry('145x32+{}+{}'.format(location_window[0],location_window[1]))
		root1.update()
		root1.overrideredirect(0)
		root1.update()
		START()
		lab0['width']=25
		# root1.bind('F4',skrinshot_bid)


		i=0
		try:
			for y in imags:
				a = pytesseract.image_to_string(y,lang='eng')
				if a != '':
					overlay_tk(a,cords[i],cords[i+1],cords[i+2],cords[i+3])
				i+=4

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


	# root1.unbind('F1')
	# root1.unbind('F3')
	# root1.unbind('F4')
	STOP()
	bat1.pack_forget()
	frame1.pack()
	lab0.pack()
	lab0['width']=45
	lab0['text']='-------- [F2] --------'
	root1.update()

	with mss.mss() as sct:
		monitor = {"top":0, "left": 0, "width": win32api.GetSystemMetrics(0), "height":win32api.GetSystemMetrics(1)}
		mss.tools.to_png(sct.grab(monitor).rgb, sct.grab(monitor).size, output='photo_t.png')
	lab0.pack_forget()
	frame1.pack_forget()
	root1.overrideredirect(1)

	global imgas
	imgas = ImageTk.PhotoImage(Image.open('photo_t.png'))
	paint.create_image(0,0, anchor=NW,image=imgas)
	location_window = (root1.winfo_x(),root1.winfo_y())
	paint.pack()
	root1.geometry('{}x{}+0+0'.format(root1.winfo_screenwidth(),root1.winfo_screenheight()))
	root1.update()



	x=y=0
	all_cord_mnogo = []

	root1.bind('<B1-Motion>',one)
	root1.bind('<ButtonRelease-1>',one)
	root1.bind('<F2>',exit_func)

def skrinshot_bid_COMBO(event):
	skrinshot_bid_Combo()
	pass

#------------------------------------------------#


###################################################################################################################
def ignorsd():
	lab0['text'] = 'COMAND IN WINDOWS'
	pass

def General_settings():
	try:
		global Background
		global Text_color
		global dimensions
		with open('General_settings.txt','r') as Files:
			fils = Files.read().split('\n')
			Background=fils[0]
			Text_color=fils[1]
			dimensions.append(fils[2])
			dimensions.append(fils[3])
	
	except FileNotFoundError:
		with open('General_settings.txt','w') as Files:
			Files.write('#4E51D8\n')
			Files.write('#FFFFFF\n')

			if sys.platform == 'win32':
				if win32api.GetSystemMetrics(1) <= 780:
					Files.write('10\n')
					Files.write('10\n')

				elif win32api.GetSystemMetrics(1) >= 780:
					Files.write('15\n')
					Files.write('15\n')
			
			else:
				Files.write('10\n')
				Files.write('10\n')


		General_settings()

############################################ Total ################################################################

Background =''
Text_color=''
token = ''
Check = []
text_dont_bat_Spelling=[]
globalF3 = []
dimensions = []
General_settings()


root1=Tk()
try:
	root1.iconbitmap('icos.ico')
except:
	root1.iconbitmap()

root1.title('Translete')
root1["bg"] = Background
Switches_radio = StringVar()
Switches_radio.set('1')
#####################################################################################################################
############################################## TKINTER ##############################################################
text_box = tkinter.scrolledtext.ScrolledText(root1,width=43, height=dimensions[0])
text_box1= tkinter.scrolledtext.ScrolledText(root1,width=43, height=dimensions[1])
#__________________________________________________________________________________________________________#
frame0 = Frame(root1)
bat_copy = Button(frame0,width=6, text='COPY', fg = Text_color,bg  = Background, command = copy)
bat_clear= Button(frame0,width=6, text='X_X',  fg = Text_color,bg  = Background, command = clear)
bat_past = Button(frame0,width=6, text='PASTE',fg = Text_color,bg  = Background, command = paste)
#__________________________________________________________________________________________________________#
frame1 = Frame(root1)
lab0= Label(frame1,width =15,bg  = Background,fg = '#00FFFF',font = ( "Helvetica" , 10))
radio1=Radiobutton(frame1, text='RU',selectcolor = Background, bg  = Background,fg = Text_color,value='0',variable=Switches_radio,command = radio)
radio2=Radiobutton(frame1, text='ENG',selectcolor = Background , bg  = Background,fg = Text_color, value='1',variable=Switches_radio, command = radio)
#__________________________________________________________________________________________________________#
bat_token = Button(root1,width=42, text='API Яндекс.Переводчик',fg = Text_color, bg  = Background, command = Debugging_tasks)
bat_Spelling      = Button(root1,width=42, text='\\/', fg = Text_color, bg  = Background, command = spl)
dont_bat_Spelling = Button(root1,width=42, text='/\\', fg = Text_color, bg  = Background, command = spl_dont)
#__________________________________________________________________________________________________________#
bat  = Button(root1,width=42, text='STOP', fg = Text_color,bg  = Background, command = STOP)
bat1 = Button(root1, width=15,text='START',  command = START,bg  = Background, fg = Text_color, font = 'BOLD' )
bat1.pack()
#__________________________________________________________________________________________________________#
text_token = Text(root1,width=35, height=1)
import_texst = Button(root1,width =40,text='Save Token',fg = Text_color,bg  = Background, command = save_text)
#__________________________________________________________________________________________________________#
frame2 = Frame(root1)
bat_t_Sp0 = Button(frame2,width=9,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text0)
bat_t_Sp1 = Button(frame2,width=9,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text1)
bat_t_Sp2 = Button(frame2,width=9,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text2)
#__________________________________________________________________________________________________________#
frame21 = Frame(root1)
bat_t_Sp3 = Button(frame21,width=9,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text3)
bat_t_Sp4 = Button(frame21,width=9,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text4)
bat_t_Sp5 = Button(frame21,width=9,text='-',fg = Text_color,bg  = Background,font = ( "Helvetica" , 8),command=input_text5)
#__________________________________________________________________________________________________________#


frame3 = Frame(root1)
skrin_shot_batton      = Button(frame3, text='[F1]', width=7,bg = Background, fg = Text_color, command = skrinshot_s)
skrin_shot_batton_AV   = Button(frame3, text='[F3]', width=7,bg = Background, fg = Text_color, command = skrinshot_bid_AVS)
skrin_shot_batton_COMBO= Button(frame3, text='[F4]', width=7,bg = Background, fg = Text_color, command = skrinshot_bid_Combo)

if sys.platform != 'win32':
	skrin_shot_batton['command'] = ignorsd
	skrin_shot_batton_AV['command'] = ignorsd
	skrin_shot_batton_COMBO['command'] = ignorsd
#__________________________________________________________________________________________________________#
paint = Canvas(root1,width=root1.winfo_screenwidth(), height=root1.winfo_screenheight())
scale = Scale(root1, length=367,width=15,orient=HORIZONTAL,troughcolor=Background,activebackground=Background,relief=FLAT ,showvalue=0,sliderlength=52,from_=0, to=2,highlightbackground=Background,bg  = Background)
#__________________________________________________________________________________________________________#
root1.bind('<F1>',skrinshot_bid)
root1.bind('<F3>',skrinshot_bid_AV)
root1.bind('<F4>',skrinshot_bid_COMBO)
#__________________________________________________________________________________________________________#
START()
root1.wm_attributes('-topmost',1)
root1.mainloop()
############################################################################################################
############################################################################################################