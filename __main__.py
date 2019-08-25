
import os
from Translete import Translete_Elemint






def main():
	if not 'Photo' in os.listdir(os.getcwd()):
		os.makedirs('Photo')
	if not 'Data' in os.listdir(os.getcwd()):
		os.makedirs('Data')

	Translete_Elemint()




if __name__ == '__main__':
	main()