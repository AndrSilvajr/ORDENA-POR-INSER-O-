import openpyxl
import time

#n = int(input('tamanho'))



def insercao(A):
    n = len(A)
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] >= chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave


def selecao(A):
   for j in range(len(A)-1,0,-1):
       m=0
       for i in range(1,j+1):
           if A[i]>A[m]:
               m= i

       aux = A[j]
       A[j] = A[m]
       A[m] = aux

book = openpyxl.Workbook()
book.create_sheet('Dados')
dados_page = book['Dados']
dados_page.append(['Numero','Tempo'])
for n in range(1000,9000,1000):
	A = list(range(n,0,-1))
	print("tamanho :",n) 
	#print("Não ordenado: ", A)
	start = time.time()
	selecao(A)
	#print("Ordenado:", A)
	end = time.time()
	dados_page.append([n,end-start])
	print(end-start)
book.save('Dados.xlsx')
