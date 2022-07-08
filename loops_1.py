lista_entrada = []
entrada = 0
tempo_minimo = float(input())
while True:  # Inputs iniciais
  if entrada == -1.0:
    break
  entrada = float(input())
  lista_entrada.append(entrada)
lista_entrada.pop(-1)
lista_aptos = []
for corredor in lista_entrada:  # Adicionando os corredores aptos
    if corredor <= tempo_minimo:
        lista_aptos.append(corredor)
numero_de_corredores = len(lista_aptos)
if numero_de_corredores != 0:
    print(numero_de_corredores)
    print((numero_de_corredores // 8) + 1)
else:
    print('0\n0')
