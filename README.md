# contrução de algoritmo
Construa um algoritmo que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilindricos, de combustivel, em que são fornecidos a altura  e o raio desse cilidro. Sabendo que:
- a lata de tinta custa de $50
- cada lata cotém 5 litros
- cada litro de tinta pinta 3 metros quadrados.
- dados de entradas: altura (H) e raio (R).
- dados de saida: custo (C) e quantidade (QTDE).
# Utilizando o planejamento reverso sabemos que
- o custo é dado pela quantidade de latas $50
- a quantidades de latas é dada pela quantidade total de litros/5.
- a quantidade total de litros é dada pela area do cilindro/3.
- a área do cilindro é dada pela área da base + área lateral.
- a área da base é(PI * pot(R,2))
- a área lateral é altura * comprimento: (2 * PI *R * H)
- sendo que R(raio) e H(altura) são dados de entrada e PI é uma constante de valor conhecido: 3,14. 
