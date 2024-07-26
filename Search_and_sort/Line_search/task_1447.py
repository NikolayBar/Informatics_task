input_ = (int(x) for x in input().split())

lst_ = list(input_)[1:]

max_ = max(lst_)
min_ = min(lst_)

for i in range(len(lst_)):
    if lst_[i] == max_:
        lst_[i] = min_

print(*lst_)
