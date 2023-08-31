n1 = int(input('Dígite um número:'))
print(n1)
import random
lista = (1,2,3,4,5)
escolhido = random.choice(lista)
if n1 == escolhido:
    print('You win!')
else: print('You lose!')
print('o número escolhido foi {}'. format(escolhido))
if n1 != escolhido: 
    print(''' [ 1 ] Continuar jogando 
          [ 2 ] Sair do jogo''')
    opcao = int(input('qual opção'))
print('Fim do jogo! Volte sempre !')