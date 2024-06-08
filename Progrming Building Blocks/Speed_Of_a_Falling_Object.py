#team 9

print('Welcome to the velocity calculator. Please enter the following:')

#data
mass= int(input("Mass (in kg): "))
gravity= float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): " ))
time= float (input("Time (in seconds): "))
d_fluid= float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
c_area= float(input("Cross sectional area (in m^2): "))
d_constant= float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#formula
import math
c=(0.5 * float(d_fluid)) * float(c_area) * float(d_constant)
v= math.sqrt(mass * gravity/c) * (1-math.exp((- math.sqrt(mass * gravity * c)/ mass) * time))


#result

print('The inner value of c is: ')
print("The velocity after 10.0 seconds is:")