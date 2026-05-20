#Crie um programa que leia quanto dinheiro a pessoa tem na carteira e quantos dólares e euros ela pode comprar
#Considere US$1,00=R$5,01 e 1€=R$5,83
real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.01
euro = real / 5.83
print('Com R${:.2f} você pode comprar US${:.2f} e {:.2f}€.'.format(real, dolar, euro))