divisores = []
num = int(input())
for valor in range(int(num/2) + 1):
    if valor == 0:
        continue
    if num % valor == 0:
        divisores.append(valor)
if sum(divisores) == num:
    print('número perfeito')
else:
    print('número não é perfeito')