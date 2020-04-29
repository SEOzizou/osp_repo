#!/usr/bin/python


def binary_to_dec(binary):
    #10진법
    DEC = 0
    i = 0
    while(binary > 0):
        DEC = DEC + (2**i) * (binary%10)
        binary = binary//10
        i += 1 

    return DEC

def binary_to_oct(binary):
    #8진법
    OCT = 0
    i = 0
    while(binary > 0):
        b = binary%1000
        OCT = OCT + ((b//100)*(2**2) + ((b%100)//10)*(2**1) + (b%10)*(2**0))*(10**i)
        binary = binary//1000
        i += 1
    return OCT 


def binary_to_hex(binary):

    HEX = ''
    i = 0

    while(binary > 0):
        b = binary%10000
        s = (b//1000)*(2**3)+((b%1000)//100)*(2**2)+((b%100)//10)*(2**1)+(b%10)*(2**0)
        if s<10: HEX = str(s) + HEX
        elif s == 10:  HEX = 'A' + HEX
        elif s == 11:  HEX = 'B' + HEX 
        elif s == 12:  HEX = 'C' + HEX 
        elif s == 13:  HEX = 'D' + HEX 
        elif s == 14:  HEX = 'E' + HEX
        elif s == 15:  HEX = 'F' + HEX 
        binary = binary//10000

    return HEX
