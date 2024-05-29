import sympy as sp
sp.init_printing(use_unicode = True)
def optimizeW(L, U, D):
    Tj = (D**-1)*(L+U) 
    EigTj = map(lambda x: float(abs(x).expand(complex = True)), list(Tj.eigenvals().keys()))
    TjRatio = max(EigTj)
    w = 2/(1 + sp.sqrt(1 - TjRatio**2))
    return w

def infinityNorm(A):
    B = list()
    for i in range(0, len(A.col(0))):
        B.append(sum(abs(A.row(i))))
    return max(B)
    
    
def sor(A, b, x_0, iter, tol):
    Anp = sp.Matrix(A)
    bnp = sp.Matrix(b)
    x_i = sp.Matrix(x_0)
    D = sp.diag(*Anp.diagonal())
    print("D = ")
    sp.pprint(D)
    print("\n")
    U = D - Anp.upper_triangular()
    print("U = ")
    sp.pprint(U)
    print("\n")
    L = D-Anp.lower_triangular()
    print("L = ")
    sp.pprint(L)
    print("\n")
    wCut = '{:.4f}'.format(optimizeW(L, U , D))
    w = float(wCut)
    Tw = ((D-w*L)**-1)*((1-w)*D + w*U)
    print("Tw = ")
    sp.pprint(Tw)
    print("\n")
    Cw = w*((D-w*L)**-1)*bnp
    print("Cw = ")
    sp.pprint(Cw)
    print("\n")
    print("spectral ratio:", w - 1)
    print("w = ", w)
    for i in range(0, iter):
        x = Tw*x_i + Cw
        if Anp*x.evalf(6) == bnp or infinityNorm(x-x_i)/infinityNorm(x) < tol:
            print(" X = ")
            sp.pprint(x.evalf(6))
            break 
        x_i = x
        print(f"x_{i+1} = ", list(x.evalf(6)))
A = eval(input("Ingrese la matriz: "))
b = eval(input("introduzca el vector b: "))
x_0 = eval(input("ingrese el vector inicial: "))
iter = int(input("ingrese el nùmero de iteraciones: "))
tol = float(input("Ingrese la tolerancia: "))
sor(A, b, x_0, iter, tol)
