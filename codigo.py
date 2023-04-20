import math
preco = float(input('digite o preço'))
origen = int(input('digite o codigo de origem'))

if origen == 1:
    print('{} = '.format(origen))
    print(str(preco) + ', origem sul')

elif origen == 2:

    print(str(preco) + ', origem norte')

elif origen == 3:
    print('{} = '.format(origen))
    print(str(preco) + ', origem leste')

elif origen == 4:
    print('{} = '.format(origen))
    print(str(preco) + ', origem oeste')

elif (origen > 6) and (origen < 10):
    print('{} = '.format(origen))
    print(str(preco) + ', origem sudeste')


elif (origen > 9) and (origen < 21):
    print('{} = '.format(origen))
    print(str(preco) + 'origem centro-oeste')


elif (origen > 4) and (origen < 31):
    print('{} = '.format(origen))
    print(str(preco) + 'origem Nordeste')
else:
    print('produto importado.')
