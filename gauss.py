import numpy as np

#Função que calcula as substituições retroativas
def retroativa(A,b):
    #tamanho da matriz A
    n = len(A)
    #Inicialização do vetor de retorno
    x = n*[0]

    for i in range(n-1,-1,-1):
        s=0
        for j in range(i+1,n):
            s = s+A[i][j]*x[j]
        x[i]=(b[i]-s)/A[i][i]
    return x

#Método de Gauss sem pivoteamento parcial
def gauss(A,b):
    #Tamanho da matriz
    n = len(A)
    for k in range(0,n-1):
        for i in range(k+1,n):
            m = -A[i][k]/A[k][k]
            for j in range(k+1,n):
                A[i][j]=m*A[k][j]+A[i][j]
            b[i]=m*b[k]+b[i]
            A[i][k]=0
    x = retroativa(A,b)
    return x




