import time

n = int(input('tamanho'))
start = time.time()
def insercao(A):
    n = len(A)
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] >= chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave


A = list(range(n,0,-1))

#print("Não ordenado: ", A)
insercao(A)
#print("Ordenado:", A)

end = time.time()
print(end-start)