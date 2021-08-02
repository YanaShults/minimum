#минимум
import random
import numpy as np

mass = [[random.randint(1, 9) for i in range(5)] for j in range(5)]
num = 0
print(mass)
# print(sum(mass[0]))
def minimum(mass):
    # summa_row = [sum(i) for i in mass]
    summa_row = list(np.sum(mass, axis=1))
    summa_column = list(np.sum(mass, axis=0))
    print(summa_row)
    print(summa_column)
    index_row = summa_row.index(min(summa_row)) + 1
    index_column = summa_column.index(min(summa_column)) + 1
    return [index_row, index_column]

print(minimum(mass))