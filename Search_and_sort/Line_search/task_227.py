N = int(input())
arr = list(int(x) for x in input().split())

arr.sort(reverse=True)
print(arr[0])
