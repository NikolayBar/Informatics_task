input_ = [int(x) for x in input().split()]

n = input_[0]
_min = min(input_[1:])
_max = max(input_[1:])

for i in range(1, n + 1):
    if input_[i] == _max:
        print(_min, end=' ')
    else:
        print(input_[i], end=' ')
