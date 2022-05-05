from sympy import *
import numpy as np
init_printing(use_unicode=False, wrap_line=False, no_global=True)

x, y, z = symbols('x, y, z')
X = Matrix([[5, 7, -5], [0, -2, 2], [-4, -8, -7], [1, 1, 2], [2, -1, 2], [4, 1, 4]])
b = Matrix([-47, 10, 63, -1, -4, -2])
a = Matrix([x, y, z])
Xa = (X * a - b)


def mse_calc(equals):
    MSE = sum(equal ** 2 for equal in equals)
    return MSE / (len(equals) -1 )

MSE = mse_calc(Xa)

MSE_x = diff(MSE, x)
MSE_y = diff(MSE, y)
MSE_z = diff(MSE, z)

i, j, k = 0, 0, 0
while MSE.subs({x: i, y: j, z: k}) > 55:
    D_MSE = np.array([MSE_x.subs({x: i, y: j, z: k}), MSE_y.subs({x: i, y: j, z: k}), MSE_z.subs({x: i, y: j, z: k})]) * - 0.01
    i += D_MSE[0]
    j += D_MSE[1]
    k += D_MSE[2]
print('MSE = ',  MSE.subs({x: i, y: j, z: k}))
print(f'x= {i}, y= {j}, z= {k}')