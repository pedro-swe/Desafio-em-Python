a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços?', a.isspace())#Verifica se o que foi digitado só tem espaços
print('Só tem letra maiúscula?', a.isupper())
print('Só tem números?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Está tudo em minúsculo?', a.islower())
print('Está capitalizada?', a.istitle())