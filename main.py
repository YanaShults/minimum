#минимум
import random

mass = [[random.randint(1, 9) for i in range(5)] for j in range(5)]
num = 0
print(mass)
# print(sum(mass[0]))
def minimum(mass):
    summa_row = [sum(i) for i in mass]
    summa = 0
    summa_column = []

    for i in range(len(mass)):
        for j in range(len(mass[i])):
            summa += mass[j][i]

        summa_column.append(summa)
        summa = 0

    # print(summa_row)
    # print(summa_column)
    index_row = summa_row.index(min(summa_row)) + 1
    index_column = summa_column.index(min(summa_column)) + 1
    return [index_row, index_column]

print(minimum(mass))