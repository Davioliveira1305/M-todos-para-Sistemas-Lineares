import numpy as np

#Função que retorna o critétio de parada do método de gauss-Jacobi
def modulo_jacobiano(vetor_A:list, vetor_B:list) -> float:
    modular = [];
    maximo_a = 0;
    for coluna in range(len(vetor_A)):
        modular.append(abs(vetor_A[coluna] - vetor_B[coluna]));
        if (abs(vetor_A[coluna])>maximo_a): maximo_a = abs(vetor_A[coluna]);
    return np.around(max(modular)/maximo_a, 4);

#Função que transforma A em Cx + g
def matrix_transformation(A:list, b:list):
    for linha in range(len(A)):
        for coluna in range(len(A[0])):
            if (linha==coluna): continue;
            A[linha][coluna]=A[linha][coluna]/-A[linha][linha];
        b[linha]=b[linha]/A[linha][linha];
            
        A[linha][linha]=0;
    
#Função que cálcula o próximo x
def calculo_xn1(A:list, b:list, x_inicial) -> list:
    
    x_jacobi = [0 for x in range(len(b))];

    for linha in range(len(A)):
        x_jacobi[linha] += float(b[linha]);
        for coluna in range(len(A[0])):
            x_jacobi[linha] += A[linha][coluna] * x_inicial[coluna];
    return np.around(x_jacobi,4);

#Função que executa o método de Gauss_Jacobi
def gauss_jacobi(A:list, b:list, epsilon:float,x_inicial:list) -> list:

    k = 0;
    epsilon_jacobi = epsilon*2;   
    matrix_transformation(A,b);
    while(epsilon_jacobi > epsilon):
        print(f"Interaçao {k+ 1 }");
        x_jacobi = calculo_xn1(A, b, x_inicial); print("x jacobi:", x_jacobi);
        epsilon_jacobi = modulo_jacobiano(x_jacobi, x_inicial); print(f"Epsilon jacobi: {epsilon_jacobi}\n");
        x_inicial = x_jacobi;
        k += 1;
    return f"Solução x*={x_inicial},com {k} iterações.";

    


