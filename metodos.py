"""

Instalar numpy con el siguiente comando:

pip install numpy


"""

import numpy as np

def gauss_jordan(matrix):
    flag = True
    for i in range(matrix.shape[0]):
        if (matrix[i,i] == 0): 
            flag = reorder_matrix_zero(matrix, i)
            if (flag == False): raise ZeroDivisionError("No se encontró un elemento pivote no nulo válido en algún momento de la iteración")
            print("\nCambio de filas\n")
            print("\n",np.round(matrix, decimals= 2), "\n\n")
        matrix[i] /=  matrix[i,i]
        for j in range(matrix.shape[0]): matrix[j] += matrix[i]*matrix[j,i]*-1 if i != j else 0
        print(f"\nIteración {i+1}: \n\n",np.round(matrix, decimals= 2))
    return matrix[:,-1]

def reorder_matrix_zero(matrix, index):
    for i in range(index+1, matrix.shape[0]):
        if (matrix[i][index] != 0):
            aux = np.copy(matrix[i])
            matrix[i] = np.copy(matrix[index])
            matrix[index] = np.copy(aux)
            return True
    return False
    
def gauss_seidel(matrix,b):
    x =  np.zeros(matrix.shape[0])
    xant = np.zeros(matrix.shape[0])
    err = np.ones(matrix.shape[0])
    iter = 0
    while ((err > 0.001).any() and iter <= 100):
        for i in range(matrix.shape[0]): x[i] = (np.sum(matrix[i,np.arange(matrix[i].size) != i]*x[np.arange(len(x)) != i])*-1 + b[i])/ matrix[i][i]
        err = np.abs(x-xant)
        for i in range(matrix.shape[0]): print(f"x{i},{iter} = {x[i]}\nError = {err[i]}")
        print("\n\n")
        xant = np.copy(x)
        iter += 1
    if (iter > 100): print("\n\nSe alcanzó el limite de iteraciones (100). Puede que el resultado no sea el correcto")
    return x

def reorder_matrix(matrix):
    n = matrix.shape[0]
    index_list = [0]*n
    index = -1
    counter_list = [0]*n
    aux_array = np.arange(n)
    for i in range(n): index_list[i] = [j for j in range(n) if i in aux_array[np.abs(matrix[j]) == np.max(np.abs(matrix[j]))].tolist()] +[-1]
    max_counter_list = [len(index)-1 for index in index_list]
    better_result = [-1]*n
    while True:
        result = [index_list[i][counter_list[i]] for i in range(n)]
        if (len(result) == len(set(result)) and result.count(-1) == 0): return result
        elif (better_result.count(-1) > result.count(-1)):
            aux = [num for num in better_result if num != -1]
            if (len(aux) == len(set(aux))): better_result = result.copy()
        if (sum(counter_list) == sum(max_counter_list)): break
        while True:
            if (counter_list[index] == max_counter_list[index]):
                counter_list[index] = 0
                index -= 1
            else:
                counter_list[index] += 1
                index = -1
                break
    print("\nLa matriz no se puede ordenar de tal forma que se cumpla la condición de convergencia. El resultado podría no ser el correcto. \n")
    for i in range(n): #Rellenar los -1 que quedaron con filas al azar y que no tengan 0 de coeficiente en la variable a despejar
        if (better_result.count(-1) == 0): break
        if((i in result) == False and matrix[result.index(-1), result.index(-1)] != 0): result[result.index(-1)] = i
    return result
    

    




    
    
        


