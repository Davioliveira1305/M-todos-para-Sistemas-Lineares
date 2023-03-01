import numpy as np;
from gauss import gauss;
from gauss_PP import gauss_PP;
from gauss_jacobi import gauss_jacobi;
from Fatoracao_LU import fatoracao_LU;
from Fatoracao_LU import fatoracao_LU_PP;
from gauss_jordan import gauss_jordan;
from gauss_jordan import gauss_jordan_det;

def main():
    escolha = int(input("\n Digite 1 para executar o método de Gauss ; \n Digite 2 para executar o método de Gauss_Jacobi; \n Digite 3 para executar o método da Fatotação LU \n Digite 4 para executar o método de Gauss_Jordan;\nOpção:"))
    if (escolha < 0 or escolha > 4):
        print("Digite um número válido!!!!!!!!!");
        return main();
    #Variável que recebe a ordem da matriz
    n = abs(int(input("Digite a ordem da sua matriz A: ")));
    
    #Criação da matriz pelo usuário
    A = [];
    for i in range(0,n):
        l = [];
        for j in range(0,n):
            a = int(input(f"Digite o elemento A[{i+1}{j+1}] da matriz: "));
            l.append(a);
        A.append(l);

    #Função que verifica se a matriz possui inversa
    if (np.linalg.det(A)==0):
        print("A matriz A não possui inversa!!!!!");
        return main();    

    #Criação do vetor pelo usuário
    b = []
    for i in range(0,n):
        a = int(input(f"Digite o {i+1}° elemento do seu vetor: "));
        b.append(a);
    
    #Executa o método de Gauss normal     
    if (escolha == 1):
        escolha_2 = int(input("Digite 1 para executar Gauss sem pivoteamento parcial e 2 para executar com pivoteamento parcial: "));
        if (escolha_2 == 1):
            print(gauss(A,b));
        elif(escolha_2 == 2):
            print(gauss_PP(A,b));
        else:
            print("Digite uma opção válida!!!!!!!")
            return main();

    #Executa o método de Gauss_Jacobi
    elif (escolha == 2):
        epsilon = float((input("Digite a precisão do método de Gauss_Jacobi: ")))
        x_inicial = [];
        for i in range(0,n):
          a = int(input(f"Digite o {i+1}° elemento do seu vetor inicial: "));
          x_inicial.append(a);      
        print(gauss_jacobi(A,b,epsilon,x_inicial));

    #Executa o método da Fatoração LU
    elif(escolha == 3):
        escolha_3 = int(input("Digite 1 para executar a Fatoração LU sem pivoteamento parcial e 2 para executar com pivoteamento parcial: "))
        if (escolha_3 == 1):
            print(fatoracao_LU(A,b));
        elif(escolha_3 == 2):
            print(fatoracao_LU_PP(A,b));
        else:
            print("Digite uma opção válida!!!!!!!");
            return main();
    
    #Executa o método de Gauss_Jordan
    else:
        escolha_4 = int(input("Digite 1 para executar o método de Gauss_Jordan normal ou 2 para executar o método de Gauss_Jordan para encontrar o determinante da matriz: "))
        if(escolha_4 == 1):
            print(gauss_jordan(A,b));
        elif(escolha_4 == 2):
            print(gauss_jordan_det(A));
        else:
            print("Digite um número válido!!!!!!!")
            return main();
    

while(True):
    main();
    if(int(input("Quer parar? 1 para sim e 2 para não: "))==1):break;

    
      

        
    
