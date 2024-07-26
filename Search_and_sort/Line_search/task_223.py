N = int(input())
arr = (int(x) for x in input().split())
x = int(input())

count = 0

for i in arr:
    if x == i:
        count += 1

print(count)
