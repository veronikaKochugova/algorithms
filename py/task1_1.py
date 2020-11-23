# 1 ≤ n ≤ 300 000
# 0 ≤ ai ≤ 1 000 000 000

n = int(input())
array = [int(i) for i in input().split()]

counts = dict()
for a in array:
    try:
        counts[a] += 1
    except:
        counts[a] = 1

max_v = max_k = 0
for k, v in counts.items():
    if v > max_v:
        max_v = v
        max_k = k

print(max_k)

