import numpy as np
#Função que calcula as substuições retroativas
from gauss import retroativa
#Função que escolhe os melhores pivôs para uma determinada matriz A
from gauss_PP import escolhe_pivo

#Função que calcula as substituições sucessivas
def sucessiva(A,b):
    #tamanho da matriz A
    n = len(A);
    #Inicialização do vetor de retorno
    x = n*[0];

    for linha in range(0,n):
        s=0;
        for coluna in range(0,n):
            s = s+A[linha][coluna]*x[coluna];
        x[linha]=(b[linha]-s)/A[linha][linha];
    return x;

def fatoracao_LU(A:list,b:list) -> list:
    #tamanho da matriz A
    n = len(A);
    L = np.identity(len(A),dtype = float);
    for linha in range(0,n-1):
        for coluna in range(linha+1,n):
            m = -A[coluna][linha]/A[linha][linha];
            for j in range(linha+1,n):
                A[coluna][j]=m*A[linha][j]+A[coluna][j];
            L[coluna][linha] = -m;
            A[coluna][linha]=0;
    #Cálculo do Ly = b
    y =  sucessiva(L,b);
    #Cálculo do Ux = y
    x = retroativa(A,y);
    return x;
A =[[3,-2,1],[1,-3,4],[9,4,-5]]
b=[8,6,11]
#print(fatoracao_LU(A,b))

def fatoracao_LDP(A, b):
    #tamanho da matriz A
    n = len(A);
    L = np.identity(len(A),dtype = float);
    D = np.identity(len(A), dtype = float);
    P =  np.identity(len(A), dtype = float);
    R = np.identity(len(A), dtype = float);

    for linha in range(0,n-1):
        for coluna in range(linha+1,n):
            m = -A[coluna][linha]/A[linha][linha];
            for j in range(linha+1,n):
                A[coluna][j]=m*A[linha][j]+A[coluna][j];
            L[coluna][linha] = -m;
            A[coluna][linha]=0;
    #Obtenção das Matrizes P e D a partir da matriz A(U) escalonada
    #Nessa parte também é obtida uma matriz R que é o resultado da multiplicação da matriz D pela a diagonal de P
    for i in range(0,n):
        for j in range(0,n):
            P[i][j] = A[i][j];
            P[i][i] = 1;
            R[i][j] = A[i][j];
            if (i==j):
              D[i][j] = A[i][j];
              R[i][j] = P[i][j] * D[i][j];
    
    #Cálculo do Ly = b
    y =  sucessiva(L,b);
    #Cálculo do Rx = y
    x = retroativa(R,y);
    return x;
print(fatoracao_LDP(A,b))


def fatoracao_LU_PP(A:list,b:list) -> list:
    #tamanho da matriz A
    n = len(A);
    L = np.identity(len(A),dtype = float);
    for linha in range(0,n-1):
        for coluna in range(linha+1,n):
            #Função que escolhe o melhor pivô para uma linha
            escolhe_pivo(linha,A,b);
            m = -A[coluna][linha]/A[linha][linha];
            for j in range(linha+1,n):
                A[coluna][j]=m*A[linha][j]+A[coluna][j];
            L[coluna][linha] = -m;
            A[coluna][linha]=0;
    #Cálculo do Ly = b
    y =  sucessiva(L,b);
    #Cálculo do Ux = y
    x = retroativa(A,y);
    return f"Solução x*={x}";


