import math
from datetime import datetime



w = int(input('Enter the width of the tire in mm (ex 205): '))
r = int(input('Enter the aspect ratio of the tire (ex 60):' ))
d = int(input('Enter the diameter of the wheel in inches (ex 15):' ))
now= datetime.now()
w_square= w * w
v = math.pi * w_square * r *( w * r + 2540 * d)/10000000000

print("")
#print(f"{now:%Y-%m-%d}\n")
print("The approximate volume is", round(v,2), "liters\n")

with open('volumes.txt', 'at') as volumes:
    print(f"{now:%Y-%m-%d}, {w}, {r}, {d}, {round(v, 2)}",file=volumes)
    







    
