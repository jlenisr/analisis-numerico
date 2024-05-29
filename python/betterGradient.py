
import sympy as sp

sp.init_printing(use_unicode = True)
def innerProduct(x, y):
    return x.T * y

def infinityNorm(A):
    B = list()
    for i in range(0, len(A.col(0))):
        B.append(sum(abs(A.row(i))))
    return max(B)

def gradient(A, b, x_i,  iter, tol ):
    Asp = sp.Matrix(A)
    bsp = sp.Matrix(b)
    x_0 = sp.Matrix(x_i)
    r_0 = bsp - Asp*x_0
    v_1 = r_0

    for i in range(0, iter):
        t = innerProduct(r_0, r_0)[0]/innerProduct(v_1, Asp*v_1)[0]
        x = x_0 + t*v_1
        print(f"x_{i+1} = ", list(x.evalf(6)))
        if Asp*x.evalf(6) == bsp or infinityNorm(x-x_0)/infinityNorm(x) < tol: 
            print("X = ")
            sp.pprint(x.evalf(6))
            break
        r_1 = r_0 - t*Asp*v_1
        s = innerProduct(r_1, r_1)[0]/innerProduct(r_0,r_0)[0]
        r_0 = r_1
        x_0 = x.evalf(6)
        v_1 = r_0 + s*v_1
        
A = eval(input("Ingrese la matriz: "))
b = eval(input("introduzca el vector b: "))
x_0 = eval(input("ingrese el vector inicial: "))
iter = int(input("ingrese el nùmero de iteraciones: "))
tol = float(input("Ingrese la tolerancia: "))
gradient(A, b, x_0,  iter, tol)
