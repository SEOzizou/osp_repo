#!/usr/bin/python


n = int(input('fibonacci number? '))
F1 = F2 = 1
sum_num = 0

for i in range(0, n):
	if (i == 0) | (i == 1):
		print(F1, end = ', ')
		if (i == n -1) : print('\b\b ') #eliminate last comma
		continue

	print(F1+F2, end = ', ')
	if (i == n-1): print('\b\b ') #eliminate last comma

	if (i % 2) == 0:
		F1 = F1 + F2
	else:
		F2 = F1 + F2 
print(f'\nF{i+1} = {max(F1,F2)}')
