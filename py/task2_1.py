# f0 = 0, f1 = 1, f2 = 2, fk = fk–1 + fk–3
# f1, f2, f3 ... fn

n = int(input())
k_array = [int(i) for i in input().split()]


def func(n):
    if n <= 2: return n
    return func(n - 1) + func(n - 3)


result = list()
result.append(func(k_array[0]))
result.append(func(k_array[1]))
result.append(func(k_array[2]))
for k in k_array[3:]:
    result.append(result[-3] + result[-1])

print(result)
