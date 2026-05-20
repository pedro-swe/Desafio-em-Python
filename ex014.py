#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m².
larg = float(input('Qual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
area = larg * alt
print('A dimensão da sua parede é de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('A quantidade de tinta necessária será de {} litros.'.format(tinta))