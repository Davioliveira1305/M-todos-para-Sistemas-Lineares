
#Cálculo da norma
def calculo_norma(v,x):
    n = len(v);
    normaNum = 0;
    normaDen = 0;
    for i in range(0,n):
        num = abs(v[i] - x[i]);
        if num > normaNum:
            normaNum = num;
        den = abs(v[i]);
        if den > normaDen:
            normaDen = den;
    
    norma = normaNum/normaDen;
    return round(norma,4);


def gauss_jacobi(A,b,epsilon,itermax):
    n = len(A);
    x = n * [0];
    v = n * [0];
    for linha in range(0,n):
        for coluna in range(0,n):
            if linha != coluna:
                A[linha][coluna] = A[linha][coluna]/A[linha][linha];
        b[linha] = b[linha]/A[linha][linha];
        x[linha] = b[linha];
        for k in range(1,itermax+1):
            for linha in range(0,n):
                s = 0;
                for coluna in range(0,n):
                    if linha != coluna:
                        s = s + A[linha][coluna] * x[coluna];
                v[linha] = b[linha] - s;
            d = calculo_norma(v,x);
            print(x,v,d)
            if d <= epsilon: 
                return v; 
            x = v[:];

A = [[10,2,1],[1,5,1],[2,3,10]]
b = [7,-8,6]
print(gauss_jacobi(A,b,0.05,100))