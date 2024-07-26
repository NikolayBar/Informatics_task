"""
Для каждого столбца выведите YES, если в нем есть число Х,
и NO в противном случае. (Каждый ответ с новой строки)
"""
X, N = int(input()), int(input())

matrix = [[int(x) for x in input().split()] for _ in range(N)]

for i in range(N):
    res = [matrix[y][i] for y in range(N)]
    if X in res:
        print('YES')
    else:
        print('NO')

