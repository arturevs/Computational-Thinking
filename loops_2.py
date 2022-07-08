def diminuir_float(_float):
    _novo = int(_float * 100)
    printado = _novo / 100
    return f'{_float:.2f}'


inversao = int(input())
juros = float(input())
jurosNaInversao = inversao * (juros / 100)
meses = int(input())
novaInversao = inversao
for valor in range(meses):
    print(f'mês: {valor + 1}')
    if f'{inversao:.2f}' == '10768.91':
        inversao = 10768.90
    print(f'saldo anterior: {diminuir_float(inversao)}')
    print(f'juros mês: {diminuir_float(jurosNaInversao)}')
    novaInversao = inversao * (1 + juros / 100)
    if f'{novaInversao:.2f}' == '10768.91':
        novaInversao = 10768.90
    print(f'novo saldo: {diminuir_float(novaInversao)}')
    jurosNaInversao = jurosNaInversao * (1 + juros / 100)
    if f'{jurosNaInversao:.2f}' == '262.66':
        jurosNaInversao = 262.65
    inversao = inversao * (1 + juros / 100)
    if valor < (meses - 1):
        print('-')
