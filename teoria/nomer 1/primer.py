from itertools import permutations

matrix = '' #распишем матрицу
graph = '' #распишем графы поочередно

for i in permutations(''): #запишем все буквы
        if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
            print(*i)