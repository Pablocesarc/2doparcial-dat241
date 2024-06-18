import numpy as np
from scipy.sparse import csr_matrix


rows = 1000
cols = 1000


nroele = 50000


mat1 = np.random.rand(nroele)
matri1fil = np.random.randint(low=0, high=rows, size=nroele)
matri1col = np.random.randint(low=0, high=cols, size=nroele)

mat2 = np.random.rand(nroele)
matri2fil = np.random.randint(low=0, high=rows, size=nroele)
matri2col = np.random.randint(low=0, high=cols, size=nroele)

ma1 = csr_matrix((mat1, (matri1fil, matri1col)), shape=(rows, cols))
ma2 = csr_matrix((mat2, (matri2fil, matri2col)), shape=(rows, cols))
print()


result = ma1.dot(ma2)

print(result)
