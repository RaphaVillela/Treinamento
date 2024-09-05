anterior = 0
atual = 1

alvo1 = 1000
alvo2 = 6765

while atual < alvo1:

    proximo = anterior + atual
    anterior = atual
    atual = proximo

if(atual == alvo1):
    print('O número ' + str(alvo1) + ' pertence a sequência')
else:
    print('O número ' + str(alvo1) + ' não pertence a sequência')

while atual < alvo2:

    proximo = anterior + atual
    anterior = atual
    atual = proximo

if(atual == alvo2):
    print('O número ' + str(alvo2) + ' pertence a sequência')
else:
    print('O número ' + str(alvo2) + ' não pertence a sequência')