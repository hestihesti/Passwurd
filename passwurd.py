import random
import os
import sys
from termcolor import colored

p1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z',
	'!','@','#','$','%','^','&','*','(',')','-','_','=','+','[','{',']','}','|',',','<','>','.','?']

icon = '''

                                                                            ===011010110001001111010100100001011010101000110100100101
                                                                          /    \ 1010111100010101001011010001110101011101100100100101
     _____  ______  _____ _____   _   _    __  __  ______    ___         ||    ||1000110010110010111001010110101001101001101010000110
    /    / /     / / ___// ___/  / | / |  / / / / /     /   /   \      __||____||__10101010010001111110101010111010010101011001000100
   /    / /     / / /__ / /___  / _//  / / / / / /   __/   /     \     |          |11001001010100010111010101101010101110100000011010
  / ___/ / __  / /__  //___  / / /  / / / / / / / /\ \    /       |    |    ||    |10100100000110101101010100111011101010110110111010
 / /    / / / / ___/ / ___/ / /  /|  / / /_/ / / /  \ \  /        /    |    ||    |10100111000101100111001010101111101010101011010010
/_/    /_/ /_/ /____/ /____/ /__/ |_/ /_____/ /_/   /_/ /________/     |   ====   |01101001010010111010100101110100110101100100101001
								       |__________|10101000000110011110101011110101001001100110011011
'''

print(colored(icon, 'yellow'))



def ps():
	chr = ''
	while chr != 'q':
		print(colored('PRESS "q" TO QUIT!', 'red'))
		chr = int(input('How Many Charectors Do You Want The Password:\n>  '))
		password = ''
		for x in range(chr):
			password = password + random.choices(p1)[0]

		site = input('What Site Is The Password For:\n>  ')

		form = f'{site}  :  {password}\n \n'
		file = input('Name Of Password File:\n>  ')
		file2 = file + '.txt'
		print(form)

		with open(file2, 'a') as f:
			f.write(form)

		encrypt = input('Would You Like To Encrypt Your PWDS.txt file <y/n>:\n>  ')
		if encrypt == 'y':
			gpg = 'gpg -e ' + file2
			os.system(gpg)
			rm = 'rm ' + file2
			os.system(rm)

		elif encrypt == 'n':
			pass
		else:
			print('Something Went Wrong')

		if chr == 'q':
			break
		else:
			continue

ps()

