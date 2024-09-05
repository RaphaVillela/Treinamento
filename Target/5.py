frase = 'aditrevni gnirtS'
invertida =  ''

for i in range (len(frase), 0, -1):
    invertida += frase[i-1]

print(invertida)