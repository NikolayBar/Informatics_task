n, m = (int(x) for x in input().split())
k = [[int(x) for x in input().split()] for _ in range(n)]
count = 0
r_min, c_max = [], []

for r in k:
    r_min.append(min(r))

for c in range(m):
    col = [k[r][c] for r in range(n)]
    c_max.append(max(col))

for i in r_min:
    for j in c_max:
        if i == j:
            count += 1

print(count)
