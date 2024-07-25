N = int(input())
arr = (int(x) for x in input().split())
x = int(input())

for i in arr:
    if x == i:
        print ('YES')
        break
else:
    print('NO')

