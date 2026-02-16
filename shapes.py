<<<<<<< HEAD
import math

def main():
    FindArea('circle', 4)
    FindArea('rectangle', height=6, width=4)
    FindArea('square', 4)
    FindArea('sqaure', side=4)

def FindArea(shape = 'none', radius = 0, height = 0, width = 0, side = 0):
    area = 0
    if shape == 'circle':
        area = math.pi * radius * radius
        print(f'The Area of {shape} is: {area:.2f}')

    elif shape == 'square':
        area = side ** 2
        print(f'The Area of {shape} is: {area}')

    elif shape == 'rectangle':
        area = width * height
        print(f'The Area of {shape} is: {area}')

    else:
        print('Invalid Shape')

main()
=======
import math

def main():
    FindArea('circle', 4)
    FindArea('rectangle', height=6, width=4)
    FindArea('square', 4)
    FindArea('sqaure', side=4)

def FindArea(shape = 'none', radius = 0, height = 0, width = 0, side = 0):
    area = 0
    if shape == 'circle':
        area = math.pi * radius * radius
        print(f'The Area of {shape} is: {area:.2f}')

    elif shape == 'square':
        area = side ** 2
        print(f'The Area of {shape} is: {area}')

    elif shape == 'rectangle':
        area = width * height
        print(f'The Area of {shape} is: {area}')

    else:
        print('Invalid Shape')

main()
>>>>>>> d2ba29fbfd3c554d05834d91472d14f729dcb33b
