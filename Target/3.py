import json

caminho_arquivo = 'dados.json'

try:
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except json.JSONDecodeError:
    print("Erro ao decodificar o JSON.")

menor = 0.0
maior = 0.0
total = 0.0
somatorio = 0.0

for dia in dados:

    if float(dia['valor']) == 0:
        continue

    if((menor == 0.0)):
        menor = float(dia['valor'])

    total += 1
    somatorio += float(dia['valor'])

    if(float(dia['valor']) < menor):
       menor = float(dia['valor'])
    
    if(float(dia['valor']) > maior):
       maior = float(dia['valor'])

media = somatorio/total
total_dias = 0

for dia in dados:

    if float(dia['valor']) == 0:
        continue

    if(float(dia['valor']) > media):
        total_dias += 1

print('Menor faturamento do mês: ' + str(menor))
print('Maior faturamento do mês: ' + str(maior))
print('Número de dias com faturamento maior que média: ' + str(total_dias))
