#!/usr/bin/python
import my_pkg.num_base_change as bs_ch  
import my_pkg.list_set 
import re

while(True):
	ans=input('Select menu: 1) conversion 2) union/intersection 3) exit? ')
	if ans == '1':
		binary = int(input('input binary number: '))
		print(f'=> OCT> {bs_ch.binary_to_oct(binary)}') 
		print(f'=> DEC> {bs_ch.binary_to_dec(binary)}')
		print(f'=> HEX> {bs_ch.binary_to_hex(binary)}')
	if ans == '2':
		first_list = input('1st list: ')
		second_list = input('2nd list: ')
		
		list_list={}
		for i, l in enumerate([first_list, second_list]):
			list_list[i] = [int(re.sub('[^0-9]','',x)) for x in l.split(',')] #정규 표현식 사용하여 숫자를 제외한 모든 문자 제거
		print(f'=> union {my_pkg.list_set.union_list(list_list[0],list_list[1])}')
		print(f'=> intersection {my_pkg.list_set.interset_list(list_list[0], list_list[1])}')
	if ans == '3':
		print('exit program...')
		break	

