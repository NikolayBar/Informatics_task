N = int(input())
arr = tuple(int(x) for x in input().split())
x = int(input())

res = [i + 1 for i in range(len(arr)) if arr[i] == x]
res.sort()
if res:
    print(*res)
