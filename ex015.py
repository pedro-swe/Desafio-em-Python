#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preço = float(input('Qual o preço do produto? R$'))
novo = preço - (preço * 5 / 100) #Não utilizar simbolo de porcentagem, que serve pra resto de divisão
print('O preço do produto que custava R${:.2f}, com o desconto vai passar a custar R${:.2f}'.format(preço, novo))