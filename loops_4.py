def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fiboSeq = [0, 1]
    aux = 2
    while aux <= n:
        fiboSeq.append(fiboSeq[aux - 2] + fiboSeq[aux - 1])
        aux += 1
    return fiboSeq[n]


def main():
    m = int(input())
    d = int(input())
    i = 0
    cont = 1
    resposta = []

    while i < m:
        if fibonacci(cont) % d == 0:
            i += 1
            resposta.append(fibonacci(cont))
        cont += 1

    for item in resposta:
        print(item, )


main()