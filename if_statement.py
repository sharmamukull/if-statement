# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 02:48:18 2021

@author: LENOVO
"""

Name = input("Your Name  :")
Roll_Number = input("Enter your roll number :")
a =int(input("Enter your  english marks :"))
b = int(input("Enter your maths marks : "))
c = int(input("Enter your hindi marks : "))
d = int(input("Enter your physics marks :"))
e = int(input("Enter your chemistry marks :"))
f = int(input("Enter your biology marks :"))
g = int(input("Enter your  geography marks :"))
h = int(input("Enter your social science marks :"))
i = int(input("Enter your history marks :"))

j = a+b+c+d+e+f+g+h+i
avg_valuve=j

if j >=900 :
    print("pass with distinction") 

elif j <=350 :
    print( "fail")
else :
       print("pass")