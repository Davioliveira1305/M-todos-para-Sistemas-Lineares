import numpy as np
#Gauss_Jordan para sistemas Ax=b
def gauss_jordan(A,b):
    n = len(A);
    for linha in range(0,n):
        for coluna in range(linha+1,n):
            A[linha][coluna] = A[linha][coluna]/A[linha][linha];
        b[linha] = b[linha]/A[linha][linha];
        A[linha][linha] = 1;
        for i in range(0,n):
            if i != linha:
                for coluna in range(linha+1,n):
                    A[i][coluna] = A[i][coluna] - A[i][linha] * A[linha][coluna];
                b[i] = b[i] - A[i][linha] * b[linha];
                A[i][linha] = 0;
    return b


#Método de Gauss_Jordan para cálculo de determinantes, usando matriz diagonal
def gauss_jordan_det(A):
    n = len(A);
    for linha in range(0,n):
        for coluna in range(linha+1,n):
            A[linha][coluna] = A[linha][coluna]/A[linha][linha];
        for i in range(0,n):
            if i != linha:
                for coluna in range(linha+1,n):
                    A[i][coluna] = A[i][coluna] - A[i][linha] * A[linha][coluna];
                A[i][linha] = 0;
    
    #Coloca os pivôs dentro de um vetor x
    x = n*[0];
    for linha in range(0,n):
        for coluna in range(0,n):
            if A[linha][coluna]!=0 and A[linha][linha] != 0:
                x[linha] = A[linha][coluna];
    
    #Calculo do determinante
    det = 1
    for i in range(0,len(x)):
        det = det * x[i];

    return f"determinante = {det}";


#Método de Gauss_Jordan para calcular Inversa de matrizes
def gauss_jordan_inv(A):
    n = len(A);
    Inversa = np.identity(n,dtype=float)
    for linha in range(0,n):
        for coluna in range(linha+1,n):
            A[linha][coluna] = A[linha][coluna]/A[linha][linha];
            Inversa[linha][coluna] = Inversa[linha][coluna]/Inversa[linha][linha];
        A[linha][linha] = 1;
        for i in range(0,n):
            if i != linha:
                for coluna in range(linha+1,n):
                    A[i][coluna] = A[i][coluna] - A[i][linha] * A[linha][coluna];
                    Inversa[i][coluna] = Inversa[i][coluna] - Inversa[i][linha] * Inversa[linha][coluna];

                A[i][linha] = 0;
    return Inversa;

A=[[5,1],[2,2]]
print(gauss_jordan_inv(A))


