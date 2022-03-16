import openpyxl
import time

def insercao(A):
    n = len(A)
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] >= chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave
book = openpyxl.Workbook()
book.create_sheet('Dados')
dados_page = book['Dados']
dados_page.append(['Numero','Tempo'])

for n in range(1000,20000,1000):
    A = list(range(n,0,-1))
    print("tamanho ",n)
    start = time.time()
    #print("Não ordenado: ", A)
    insercao(A)
    #print("Ordenado:", A)
    end = time.time()
    dados_page.append([n,end-start])
    print(end-start)


book.save('Dados.xlsx')
#print("x: ", x)
#print("y: ", y)
#print("Ordenado: ", A)


