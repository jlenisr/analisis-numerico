import sympy as sp
sp.init_printing(use_unicode = True)

class GaussJacobi():
    def __init__(self, A, b, x_0, iter, tol):
        self.A = A
        self.b = b
        self.x_0 = x_0
        self.iter = iter
        self.tol = tol


    def __infinityNorm(self, A):
        B = list()
        for i in range(0, len(A.col(0))):
            B.append(sum(abs(A.row(i))))
        return max(B)

    def __spectralRatio(self, A):
        eigA = map(lambda x: float(abs(x)), list(A.eigenvals().keys()))
        return max(eigA)

    def __defineMatrix(self, A, b, x_0):
        Asp = sp.Matrix(A)
        bsp = sp.Matrix(b)
        x_i = sp.Matrix(x_0)
        D = sp.diag(*Asp.diagonal())
        print("D = ")
        sp.pprint(D)
        print("\n")
        U = D - Asp.upper_triangular()
        print("U = ")
        sp.pprint(U)
        print("\n")
        L = D - Asp.lower_triangular()
        print("L = ")
        sp.pprint(L)
        print("\n")
        return (D, L, U, Asp, bsp, x_i)

    def jacobi(self):
        D, L, U, Asp, bsp, x_i = self.__defineMatrix(self.A, self.b, self.x_0)
        Tj = D**-1*(L+U)
        print("Tj = ")
        sp.pprint(Tj)
        print("\n")
        cj = (D**-1)*bsp
        print("C = ")
        print(list(cj))
        print("\n")
        l = self.__spectralRatio(Tj)
        print("Spectral ratio: ", l)
        for i in range(0, self.iter):
            x = Tj * x_i + cj
            if Asp*x.evalf(6) == bsp or self.__infinityNorm(x-x_i)/self.__infinityNorm(x) < self.tol:
                print("X = ")
                sp.pprint(x.evalf(6))
                break
            x_i = x
            print(f"x_{i+1} = ", list(x.evalf(6)))

    def gauss(self):
        D, L, U, Asp, bsp, x_i = self.__defineMatrix(self.A, self.b, self.x_0)
        Tg = (D-L)**-1*U
        print("Tg = ")
        sp.pprint(Tg)
        print("\n")
        cg = (D-L)**-1*bsp
        print("C = ")
        print(list(cg))
        print("\n")
        l = self.__spectralRatio(Tg)
        print("Spectral ratio: ", l)
        for i in range(0, self.iter):
            x = Tg * x_i + cg
            if Asp*x.evalf(6) == bsp or self.__infinityNorm(x-x_i)/self.__infinityNorm(x) < self.tol:
                print("X = ")
                sp.pprint(x.evalf(6))
                break
            x_i = x
            print(f"x_{i+1} = ", list(x.evalf(6)))

def basicFilling():
    A = eval(input("Ingrese la matriz: "))
    b = eval(input("introduzca el vector b: "))
    x_0 = eval(input("ingrese el vector inicial: "))
    iter = int(input("ingrese el nùmero de iteraciones: "))
    tol = float(input("Ingrese la tolerancia: "))
    return (A, b, x_0, iter, tol)

while True:
    print("Metodo: \n")
    print("1. Jacobi \n")
    print("2. Gauss \n")
    print("3. Salir \n")
    option = int(input("Numero de metodo: "))
    if option == 1:
        A, b, x_0, iter, tol = basicFilling()
        GaussJacobi(A, b, x_0, iter, tol).jacobi()
    if option == 2:
        A, b, x_0, iter, tol = basicFilling()
        GaussJacobi(A, b, x_0, iter, tol).gauss()
    if option == 3:
        print("gracias por ejecutar ;)")
        break

