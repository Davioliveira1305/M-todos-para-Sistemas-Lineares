import numpy as np

#Algoritmo que calcula a norma
def calcula_norma(n,x,v):
    normaNum = 0;
    normaDen = 0;
    for i in range(0,n):
        t = abs(v[i] - x[i]);
        if t > normaNum:
            normaNum = t;
        if abs(v[i]) > normaDen:
            normaDen = abs(v[i]);
        x[i] = v[i]
    norma = normaNum/normaDen
    return norma;


#Algoritmo de Gauss_Seidel
def Gauss_Seidel(A,b,epsilon,itermax):
    n = len(A);
    x = [0 for x in range(len(b))];
    v = [0 for v in range(len(b))];
    #Construção da matriz do vetor de iterações
    for i in range(0,n):
        r = 1/A[i][i];
        for j in range(0,n-1):
            if i != j:
                A[i][j] = A[i][j] * r;
        b[i] = b[i] * r;
        x[i] = b[i];
        k = 0;
        while(True):
            k = k+1;
            for i in range(0,n):
                soma = 0;
                for j in range(0,n):
                    if i != j:
                        soma = soma + A[i][j] * x[j];
                v[i] = x[i];
                x[i] = b[i] - soma;
            norma = calcula_norma(n,v,x);
            print(f"Iteração:{k},x={x},norma={norma}");
            if norma <= epsilon or k >= itermax:
                break;
    return x,k;

A = [[5,1,1],[3,4,1],[3,3,6]]
b = [5,6,0]

print(Gauss_Seidel(A,b,0.1,10))


