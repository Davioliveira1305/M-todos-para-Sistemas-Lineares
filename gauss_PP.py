from gauss import retroativa
import numpy as np

#Função que escolhe o melhor pivô para uma linha i
def escolhe_pivo(k,A,b):
    trocou = False;
    n = len(A);
    pivo = A[k][k];
    linha_pivo = k;
    for i in range(k+1,n):
        if abs(A[i][k]) > abs(pivo):
          pivo = A[i][k];
          linha_pivo = i;
    if k!=linha_pivo:
        A[k],A[linha_pivo] = A[linha_pivo],A[k];
        b[k],b[linha_pivo] = b[linha_pivo],b[k];
        trocou = True;
    return trocou;


def gauss_PP(A,b):
    #Tamanho da matriz
    n = len(A);
    for k in range(0,n-1):
        for i in range(k+1,n):
            escolhe_pivo(k,A,b);
            m = -A[i][k]/A[k][k];
            for j in range(k+1,n):
                A[i][j]=m*A[k][j]+A[i][j];
            b[i]=m*b[k]+b[i];
            A[i][k]=0;
    x = retroativa(A,b);
    return f"Solução x*={np.around(x,1)}";


