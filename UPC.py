#Projectile Calculator v1.0
import time
import math
import os

#Throwing Graphics
def throw():
	print('')
	time.sleep(0.5)
	for number in range(20):
		print('-', end='', flush='True')
		time.sleep(0.075)
	print('o',end='')
	print('#')
	time.sleep(0.5)

#varibles
v = 0.0
status = 'on'
height = 0.0
weight = 0.0
power = 0.0
mass = 0.0
fudge_factor = 0.0
g = 0.0
pro_area = 0.0
air_density = 0.0
drag = 0.0
vt = 0.0
rnge = 0.0
v_part_one = 0.0
v_part_two = 0.0
u_input = 0
cd = 0.0
units = 1
v_mph = 0.0
f_rnge = 0.0
u_input_two = 0.0
u_input = 0

#intro
os.system('clear')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('+                                                      +')
print('+            Ultimate Projectile Calculator            +')
print('+               By Huck Richardson v1.0                +')
print('+     Open Source Theoretical Projectile Calculator    +')
print('+                                                      +')
print('+     1:Scientist  2:Normal  3:Orc  4:Home  5:Quit     +')
print('+                                                      +')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')



while status == 'on':
	u_input = float(input())
	
	#Scientist Mode
	if u_input == 1:
		os.system('clear')
		print('')
		print('+++++++++++++++++++++++++')
		print('+       Scientist       +')
		print('+++++++++++++++++++++++++')
		print('')
		height = float(input('Please enter your height (m)'))
		weight = float(input('Please enter your weight (kg)'))
		fudge_factor = weight/1000
		mass = float(input('Please enter the mass of the projectile (kg)'))
		power = float(input('Please enter your power output (watts per kilogram)'))
		#Calculates Velocity
		v_part_one = float(3*height*weight*power)
		v_part_two = float(mass+fudge_factor)
		v = v_part_one/v_part_two
		v = v ** (1/3)
		g = float(input('Please enter the acceleration due to gravity (m/s)'))
		air_density = float(input('Please enter the air density (k/m3)'))
		pro_area = float(input('Please enter the cross-sectional-area of the projectile (m)'))
		#Calulates Drag Coefficent
		cd = float((2*mass*g)/(air_density*(v**2)*pro_area))
		#Calculates Terminal Velocity
		vt = float((((2*mass*g)/(pro_area*air_density*cd)))**(1/2))
		#Calculates Range
		rnge = float((v*vt*math.cos(45)/g))
		throw()
		print('You can throw the projectile '+ str(rnge) + ' meters with a top speed of ' + str(v) + ' mps')
		print('Enter "4" to go to the main menu')

	#Normal Mode
	elif u_input == 2:
		os.system('clear')
		print('')
		print('+++++++++++++++++++++++++')
		print('+         Normal        +')
		print('+++++++++++++++++++++++++')
		print('')
		height = float(input('Please enter your height (m)'))
		weight = float(input('Please enter your weight (kg)'))
		fudge_factor = weight/1000
		mass = float(input('Please enter the mass of the projectile (kg)'))
		#Simplifies the power output 
		print('Please enter your athletic skill')
		print('1:Jelly Man')
		print('2:Average Guy')
		print('3:Fitness Trainer')
		print('4:Pro Althlete')
		u_input = float(input())
		
		if u_input == 1:
			power = 5
		
		if u_input == 2:
			power = 10
			
		if u_input == 3:
			power = 15
			
		if u_input == 4:
			power == 20
		#Calculates Velocity
		v_part_one = float(3*height*weight*power)
		v_part_two = float(mass+fudge_factor)
		v = v_part_one/v_part_two
		v = v ** (1/3)
		g = float(9.8)
		air_density = float(1.225)
		pro_area = float(input('Please enter the cross-sectional-area of the projectile (m)'))
		#Calulates Drag Coefficent
		cd = float((2*mass*g)/(air_density*(v**2)*pro_area))
		#Calculates Terminal Velocity
		vt = float((((2*mass*g)/(pro_area*air_density*cd)))**(1/2))
		#Calculates Range
		rnge = float((v*vt*math.cos(45)/g))
		throw()
		print('You can throw the projectile '+ str(round(rnge,1)) + ' meters with a top speed of ' + str(round(v,1)) + ' mps')
		print('Enter "4" to go to the main menu')
	
	#Orc Mode
	elif u_input == 3:
		os.system('clear')
		print('')
		print('+++++++++++++++++++++++++')
		print('+           Orc         +')
		print('+++++++++++++++++++++++++')
		print('')
		height = float(input('Please enter your height (m)'))
		weight = float(input('Please enter your weight (kg)'))
		fudge_factor = float( weight/1000)
		#Simplifies the power output
		print('Please enter your athletic skill')
		print('1:Jelly Man')
		print('2:Average Guy')
		print('3:Fitness Trainer')
		print('4:Pro Althlete')
		u_input = float(input())
		
		if u_input == 1:
			power = 5
		
		if u_input == 2:
			power = 10
			
		if u_input == 3:
			power = 15
		
		if u_input == 4:
			power = 20
		
		fudge_factor = weight/1000
		#Simplifies the whole thing
		print('Select the projectile you wish to throw')
		print('1:Baseball')
		print('2:Meter Wide Iron Cube')
		print('3:Stapler')
		print('4:Websters Dictonary')
		u_input = float(input())
			
		if u_input == 1:
			mass = .14
			pro_area = 0.01
		
		if u_input == 2:
			mass = 78
			pro_area = 1
		
		if u_input == 3:
			mass = 0.37
			pro_area = .1
			
		if u_input == 4:
			mass = 0.425
			pro_area = .68
		
		v_part_one = float(3*height*weight*power)
		v_part_two = float(mass+fudge_factor)
		v = v_part_one/v_part_two
		v = v ** (1/3)
		g = float(9.8)
		air_density = float(1.225)
		pro_area = float(0.01)
		cd = float((2*mass*g)/(air_density*(v**2)*pro_area))
		vt = float((((2*mass*g)/(pro_area*air_density*cd)))**(1/2))
		rnge = float((v*vt*math.cos(45)/g))
		throw()
		print('You can throw the projectile '+ str(round(rnge,0)) + ' meters with a top speed of ' + str(round(v,0)) + ' mps')
		print('Enter "4" to go to the main menu')
	
	
	
	elif u_input == 4:
		os.system('clear')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		print('+                                                      +')
		print('+            Ultimate Projectile Calculator            +')
		print('+               By Huck Richardson v1.0                +')
		print('+     Open Source Theoretical Projectile Calculator    +')
		print('+                                                      +')
		print('+      1:Scientist  2:Normal  3:Orc  4:Home  5:Quit    +')
		print('+                                                      +')
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
	
	
	
#Settings may be added later, I don't know
	
			
	elif u_input == 5:
		quit()
		
	else:
		print('Thats not a valid input. See README, or the Starting Screen for help')
		
		
		