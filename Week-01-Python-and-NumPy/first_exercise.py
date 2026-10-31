#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 14:13:22 2026

@author: mariem
"""

#1. Write a program that prints out your full name.
print("your full name")

'''
2. Write a program that assigns the value 5 to a variable m representing mass and a value 10 to a variable
v representing speed and then prints the kinetic energy.
'''
m=5
v=10
KE=0.5*m*(v**2)
print("the kinetic energy is equal to", KE,"J")

'''
3. What will be the value of the expression (2.0 + 3*(1/2)) / 5 ? Type this expression into the Python
shell to verify your answer (Python will give you an answer that is off by a very small amount; ignore
this). Now type this expression into your calculator. Why do we get a different answer than the one
you predicted? (If you don’t get a different answer, congratulations, you’re probably using Python 3!)
'''
value=(2.0+3*(1/2))/5
print ("the value of the expression is", value)
'''
 Write a program that prints a four by four matrix of x’s. It should look like:
* * * *
* * * *
* * * *
* * * *
You may find the ‘\t’ character useful. What does it do?
'''
for i in range(4):
    print("*\t*\t*\t*")

'''
6. Write a program that switches the values of two variables x and y (when you define the variables, you
may assign any values you want to them in order for the program to compile, but you may not use
these values anywhere else in the program). Note x=y, y=x will not work (why?).
'''
x=5
y=x
x+=1
print(y)
x = y
print(x)
y += x
x -= y
print(x, y)


