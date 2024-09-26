import os
from metodos import *

def menu(): 
    
    matrix = np.array([[0.1,7.0,-0.3],
                       [3.0, -0.1, -0.2],
                       [0.3,-0.2,-10],])    

    b = np.array([[-19.3, 7.85,  71.40]]).T.astype(float)
    

    #Matrices y arrays de prueba y para ejemplos

    """
    matrix = np.array([
     [ 1.,     1.,     0.167,  0.5,  ],
 [ 0.,     0.,     5.67,   8.,   ],
 [ 0.,     0.,     2.83,   2.5,     ],
 [ 0.,    -5.,     1.33,  -4.,       ]
    ])

    b = np.array([[1/2, -1,  23/2, 4]]).T.astype(float)
    """

    index_list = []
    flag = False
    
    

    select = 0

    while select != 4:
        os.system('cls')
        print("\nSolucionador de sistemas de ecuaciones lineales\n\n")
        print("1. Cambiar matriz aumentada")
        print("2. Método de Gauss-Jordan")
        print("3. Método de Gauss-Seidel")
        print("4. Salir")

        print("\nMatriz aumentada actual:\n")
        print("",np.array2string(np.concatenate((matrix, b), 1))[1:-1])

        try: #try except para validar el input
            select = int(input("\nIntroduzca la opción a realizar: "))
            if (select <= 0 or select >= 5):
                print("Opción inválida")
                os.system("pause")
        except Exception as err:
            if (err == KeyboardInterrupt): raise KeyboardInterrupt #Permite usar ctrl+c para terminar en seco el programa
            print("Opción inválida")
            os.system("pause")
            select = 0

        while (select == 1): #Cambiar matriz
            os.system("cls")
            print("matriz aumentada actual: ")
            print("",np.array2string(np.concatenate((matrix, b), 1))[1:-1])
            try: 
                n_aux = int(input("\nintroduzca el valor del alto y el ancho de la matriz (n): "))
                aux_matrix = np.reshape(np.zeros(n_aux*n_aux), (n_aux, n_aux))
                aux_b = np.reshape(np.zeros(n_aux), (1, n_aux))
                for i in range(n_aux): 
                    row = np.array((input(f"Introduzca los coeficientes de la matriz aumentada de la fila {i+1} espaciados (solo usar decimales): ")).split(" "))
                    if (len(row) == n_aux+1): 
                        aux_matrix[i] = row[:-1]
                        aux_b[0][i] = row[-1]
                    else: raise ValueError("Valor inválido")
                select = 0 if (str(input("\nDeseas continuar? (y: sí): ")).lower() == 'y') else -1 #Si se introduce y, se guarda la función ingresada
                if (select == 0): 
                    matrix = np.copy(aux_matrix)
                    b = np.copy(aux_b.T)
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print(err)
                os.system("pause")
        
        while (select == 2): #Método Gauss-Jordan
            try:
                os.system("cls")
                print("Método Gauss-Jordan")
                if (np.linalg.det(matrix) == 0) : raise ValueError("La matriz no tiene soluciones únicas.")
                aumented_matrix = np.concatenate((matrix, b), 1)
                print(aumented_matrix)
                print("\n\n",gauss_jordan(aumented_matrix))
                os.system("pause")
                select = 0
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                else: print(err)
                os.system("pause")
                select = 0
        
        while (select == 3): #Método Gauss-Seidel
            os.system("cls")
            try:
                aux_list = range(matrix.shape[0])
                print("Método Gauss-Seidel\n")
                if (np.linalg.det(matrix) == 0) : raise ValueError("La matriz no tiene solución única")
                reorder_index = reorder_matrix(matrix)
                if (reorder_index.count(-1) != 0): raise ZeroDivisionError("No se pudo ordenar la matriz de tal forma que no se divida entre 0 y converja")
                print("Matriz utilizada: \n")
                print("",np.array2string(np.concatenate((matrix[reorder_index, :], b[reorder_index]), 1))[1:-1], "\n\n")
                gauss_seidel(matrix[reorder_index, :],b[reorder_index])
                select = 0
                os.system("pause")
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                else: print(err)
                select = 0
                os.system("pause")



menu() #Ejecuta el programa