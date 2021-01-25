import numpy as np
import matplotlib.pyplot as plt

def derivadam(x,y,m,b):
    derivada_m = 0
    for _x, _y in zip(x, y):
        derivada_m += 2 * ((m * _x) + b - _y) * _x
    return derivada_m

def derivadab(x,y,m,b):
    derivada_b = 0
    for _x, _y in zip(x, y):
        derivada_b += 2 * ((m * _x) + b - _y)
    return derivada_b
 
def regression_linear(m,x,b):
    result = []
    for p in x:
        result.append(m*p + b)
    return result

def modelo_regressao(x, y, color):
    m = 7
    b = 1
    L = 0.0001 #Taxa de aprendizagem
    for i in range(250000):
        m -= derivadam(x, y, m, b) * L
        b -= derivadab(x, y, m, b) * L
    xreg = np.arange(0, 0.5, 0.01)
    plt.plot(xreg, m * xreg + b, color = color)
    print()
    print("[    DADOS CALCULADO ABAIXO    ]")
    print("[CALCULADO] b = ", b)
    print("[CALCULADO] m = ", m)

def principal():
    x = [0.1001, 0.1001, 0.1001, 0.127, 0.127, 0.127, 0.2301, 0.2301, 0.2301, 0.3333, 0.3333, 0.3333,
        0.1001, 0.1001,0.1001, 0.127, 0.127, 0.127, 0.2301, 0.2301, 0.2301, 0.3333, 0.3333, 0.3333,
        0.1001, 0.1001,0.1001, 0.127, 0.127, 0.127, 0.2301, 0.2301, 0.2301, 0.3333, 0.3333, 0.3333]
    y = [14, 15, 12, 34, 34, 40, 61, 77, 72, 122, 129, 177,
        18, 9, 14, 47, 44, 43, 55, 71, 68, 113, 126, 62,
        11, 13, 9, 36, 36, 39, 98, 90, 96, 155, 137, 142]

    x_ = [0.1001, 0.1001, 0.1001, 0.127, 0.127, 0.127, 0.2301, 0.2301, 0.2301, 0.3333, 0.3333, 0.3333]
    y_1 = [18, 9, 14, 47, 44, 43, 55, 71, 68, 113, 126, 62]
    y_2 = [14, 15, 12, 34, 34, 40, 61, 77, 72, 122, 129, 177]
    y_3 = [11, 13, 9, 36, 36, 39, 98, 90, 96, 155, 137, 142]

    modelo_regressao(x, y, 'red')
    modelo_regressao(x_, y_1, 'grey')
    modelo_regressao(x_, y_2, 'green')
    modelo_regressao(x_, y_3, 'yellow')
    
    plt.scatter(x_, y_1, color = ['grey'])
    plt.scatter(x_, y_2, color = ['green'])
    plt.scatter(x_, y_3, color = ['yellow'])
    plt.grid(True)
    plt.show()
    
principal()