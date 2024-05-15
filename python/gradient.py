import sympy as sp

sp.init_printing(use_unicode = True)
def innerProduct(x, y):
    return x.T * y

def infinityNorm(A):
    B = list()
    for i in range(0, len(A.col(0))):
        B.append(sum(abs(A.row(i))))
    return max(B)

def gradient(A, b, x_i, v_i, iter, tol ):
    Asp = sp.Matrix(A)
    bsp = sp.Matrix(b)
    x_0 = sp.Matrix(x_i)
    v_1 = sp.Matrix(v_i)

    for i in range(0, iter):
        t = innerProduct(v_1, bsp-Asp*x_0)[0]/innerProduct(v_1, Asp*v_1)[0]
        x = x_0 + t*v_1
        print(f"x_{i+1} = ", list(x.evalf(6)))
        if Asp*x.evalf(6) == bsp or infinityNorm(x-x_0)/infinityNorm(x) < tol: 
            print("X = ")
            sp.pprint(x.evalf(6))
            break
        x_0 = x.evalf(6)
        v_1 = bsp - Asp*x.evalf(6)
gradient([[4,3,0], [3,4,-1], [0,-1,4]], [24,30,-24], [0,0,0], [1,0,0], 100, 1e-10)
