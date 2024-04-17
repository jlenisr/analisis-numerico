import numpy as np

def resolver_sistema_ecuaciones():
    # Solicitar los datos del sistema
    A = np.array(eval(input('Ingrese la matriz de coeficientes A: ')))
    b = np.array(eval(input('Ingrese el vector de términos independientes b: ')))
    x0 = np.array(eval(input('Ingrese el vector inicial de aproximación x0: ')))
    tol = float(input('Ingrese la tolerancia para el criterio de convergencia: '))
    max_iter = int(input('Ingrese el número máximo de iteraciones: '))

    # Mostrar el menú de métodos
    metodo = int(input('Seleccione el método iterativo:\n1. Gauss-Seidel\n2. Jacobi\n'))

    # Resolver el sistema según el método seleccionado
    if metodo == 1:
        solucion = gauss_seidel(A, b, x0, tol, max_iter)
    elif metodo == 2:
        solucion = jacobi(A, b, x0, tol, max_iter)
    else:
        print('Opción inválida')
        return None

    return solucion

def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    iter = 0
    error = float('inf')

    while error > tol and iter < max_iter:
        x_old = x.copy()
        for i in range(n):
            sum = 0
            for j in range(i):
                sum += A[i, j] * x[j]
            for j in range(i + 1, n):
                sum += A[i, j] * x_old[j]
            x[i] = (b[i] - sum) / A[i, i]
        error = np.max(np.abs(x - x_old))
        iter += 1

    if iter == max_iter:
        print(f"Advertencia: No se alcanzó la convergencia después de {max_iter} iteraciones.")

    return x

def jacobi(A, b, x0, tol, max_iter):
    n = len(b)
    x = x0.copy()
    iter = 0
    error = float('inf')

    while error > tol and iter < max_iter:
        x_old = x.copy()
        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += A[i, j] * x_old[j]
            x[i] = (b[i] - sum) / A[i, i]
        error = np.max(np.abs(x - x_old))
        iter += 1

    if iter == max_iter:
        print(f"Advertencia: No se alcanzó la convergencia después de {max_iter} iteraciones.")

    return x

# Ejemplo de uso
solucion = resolver_sistema_ecuaciones()
if solucion is not None:
    print('Solución:', solucion)