import math
H = float(input('Por favor digite o altura '))
print('{}'.format(H))
R = float(input('Por favor digite o raio '))
print('{}'.format(R))

area = (math.pi * R**2) + (2 * math.pi * R * H)

litro = area/3

qtde = litro/5

c = qtde * 50

print('A área do quadrado é de ', area)

print('O litro é ', litro)

print('a quatidade de latas é de ', qtde)

print('O custo é de ', c)
