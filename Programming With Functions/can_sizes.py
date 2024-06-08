import math

def main():
    can_name= input("Enter can name: ")
    radius= float(input('insert radius: '))
    height = float(input('insert height: '))

    volume = compute_volume(radius, height)

    surface_area= compute_surface_area(radius, height) 

    storage_efficiency = volume / surface_area
    print (f"{can_name}: {storage_efficiency: .2f}")



def compute_volume(radius,height):
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius , height):
    surface_area= 2 * math.pi * (radius + height)
    return surface_area

main()

print()
