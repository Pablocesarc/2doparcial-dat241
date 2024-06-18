import numpy as np
from scipy.sparse import csr_matrix
from multiprocessing import Pool

# Tamaño de las matrices
rows = 1000
cols = 1000

# Número de elementos no cero en las matrices
num_nonzeros = 50000  # Ajusta este valor según sea necesario

# Generar datos aleatorios para las matrices dispersas
matrix1_data = np.random.rand(num_nonzeros)
matrix1_row_indices = np.random.randint(low=0, high=rows, size=num_nonzeros)
matrix1_col_indices = np.random.randint(low=0, high=cols, size=num_nonzeros)

matrix2_data = np.random.rand(num_nonzeros)
matrix2_row_indices = np.random.randint(low=0, high=rows, size=num_nonzeros)
matrix2_col_indices = np.random.randint(low=0, high=cols, size=num_nonzeros)

# Crear las matrices dispersas en formato CSR (Compressed Sparse Row)
matrix1 = csr_matrix((matrix1_data, (matrix1_row_indices, matrix1_col_indices)), shape=(rows, cols))
matrix2 = csr_matrix((matrix2_data, (matrix2_row_indices, matrix2_col_indices)), shape=(rows, cols))

def multiply_chunk(start_row, end_row, matrix1, matrix2):
    return matrix1[start_row:end_row].dot(matrix2)

# Definir el número de procesos paralelos
num_processes = 4

# Calcular el tamaño de cada chunk (bloque)
chunk_size = rows // num_processes

# Crear los argumentos para cada proceso
chunks = [(i*chunk_size, (i+1)*chunk_size if i != num_processes - 1 else rows, matrix1, matrix2) for i in range(num_processes)]

# Multiplicar las matrices dispersas en paralelo
with Pool(processes=num_processes) as pool:
    result_chunks = pool.starmap(multiply_chunk, chunks)

# Concatenar los resultados de los chunks
result = csr_matrix((rows, cols))
for chunk in result_chunks:
    result += chunk

print(f"Resultado de la multiplicación de dos matrices dispersas de tamaño {rows}x{cols}:")
print(result)
