#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:48:08 2026

@author: mariem
"""

#from numpy import e, sin, cos, pi
from numpy import pi, cos  #* will import all the functions in numpy
#print(e, sin(pi), cos(pi/2), pi)

# Activity(3) : calculating the distance between two satelites
m=input("enter the mass of the planet in kg")
m=float(m)
r1=input("enter the redius orbit of the first satellite")
r1=float(r1)
r2=input("enter the redius orbit of the secoond satellite")
r2=float(r2)
time=input("enter the time in days")
time=float(time)
time_sec= time*24*60*60
#gravitational constant in mks units
G = 6.67300e-11 # m3 kg-1 s-2
t1= ((4*pi**2)*r1**3/(G*m))**0.5
t2=((4*pi**2)*r2**3/(G*m))**0.5
delta_theta=2*pi*time_sec*((1/t1)-(1/t2))

#For output purposes, calculate periods in years.
T1_years = t1/time_sec
T2_years = t2/time_sec
#Use the "%" operator to make the angle fall between 0 and 360 degrees.
delta_theta_degrees = delta_theta*180.0/pi
delta_theta_degrees = delta_theta_degrees%360
#the distance between the two plets
delta_r=(r1**2+r2**2-(2*r1*r2*cos(delta_theta)))**0.5

print('You set M =', m, 'kg, r1 =', r1, 'm, r2 =', r2, 'm, t =',time,'days.')
print( 'Orbital period 1 is', T1_years, 'years. Orbital period 2 is', T2_years, 'years.')
print( 'Angular separation is', delta_theta_degrees, 'degrees.')

print("the distance between the two satellitess",delta_r/1000,"km")