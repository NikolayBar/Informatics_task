N = int(input())
arr = tuple(int(x) for x in input().split())

res = [2*1e9, 2*1e9]

for el in arr:
    if el < res[0]:
        res[1], res[0] = res[0], el
    elif res[0] < el < res[1]:
        res[1] = el

print(*res)
