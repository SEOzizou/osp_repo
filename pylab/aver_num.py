#!/usr/bin/python

N = int(input("How many input numbers are : "))

num_sum = 0
for i in range(0, N):
	number = float(input(f'number {i+1} : '))
	num_sum += number
avg_num = num_sum/N
print(f'average of input numbers : {avg_num}') 
