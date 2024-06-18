import numpy as np
from scipy.sparse import csr_matrix, random, vstack, hstack
from multiprocessing import Pool, cpu_count


def generate_sparse_matrix(rows, cols):
    density = 0.01  
    return random(rows, cols, density=density, format='csr')


rows = 1000
cols = 1000
A = generate_sparse_matrix(rows, cols)
B = generate_sparse_matrix(rows, cols)


def multiply_row(i):
    row_A = A.getrow(i)
    result_row = row_A.dot(B)
    return result_row

def multiply_parallel_rows():
    num_processes = cpu_count()  
    pool = Pool(processes=num_processes)
    result_rows = pool.map(multiply_row, range(rows))
    pool.close()
    pool.join()

  
    result_matrix = vstack(result_rows)
    return result_matrix


def multiply_column(j):
    col_B = B.getcol(j)
    result_col = A.dot(col_B)
    return result_col

def multiply_parallel_columns():
    num_processes = cpu_count() 
    pool = Pool(processes=num_processes)
    result_columns = pool.map(multiply_column, range(cols))
    pool.close()
    pool.join()


    result_matrix = hstack(result_columns)
    return result_matrix


result_by_rows = multiply_parallel_rows()


result_by_columns = multiply_parallel_columns()


print("Matriz A (sparse):\n", A)
print("\nMatriz B (sparse):\n", B)
print("\nMatriz resultado (por filas):\n", result_by_rows)
print("\nMatriz resultado (por columnas):\n", result_by_columns)
