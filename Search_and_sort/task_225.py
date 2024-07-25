N = int(input())
arr = tuple(int(x) for x in input().split())
x = int(input())

c = [abs(i - x) for i in arr]
index = c.index(min(c))
print(arr[index])
