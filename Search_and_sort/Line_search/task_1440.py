n = int(input())
marks = (int(x) for x in input().split())
gold = 0
silver = 0

for rate in marks:
    if rate > gold:
        silver = gold
        gold = rate
    elif gold > rate > silver:
        silver = rate

print(silver)

