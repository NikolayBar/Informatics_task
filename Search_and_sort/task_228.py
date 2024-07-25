N = int(input())
arr = list(int(x) for x in input().split())

index = 0

for i in range(len(arr)):
    if arr[i] > arr[index]:
        index = i

print(index + 1)

