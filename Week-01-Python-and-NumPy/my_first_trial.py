# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello world")
print(9//4, 9.0//4, 9.//4, 9/4, 9.0/4.0, 9%4, 9.%4, 1/2, 1//2, (3.0**2)//(2.0**2))

#** -> power , 
# calculating the speed of a projectile
v=12.5
g=9.8
h=v**2/(2*g)
print(h)
v=15 
print(h)
h = v**2/(2*g)
print("The height of the ball h =", h)


# calculating the activity of the radioactive decay

r=5.0
t12=30.0
deltat=10.0
frac=0.5**(deltat/t12)
print ('intial activity', r )
r=r*frac
print('activitynow', r)
r=r*frac
print('activitynow', r)
r=r*frac
print('activitynow', r)
