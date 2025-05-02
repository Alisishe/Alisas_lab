# lab 1

# VAR1

def reccurent_rel(n, k):
    F = [0] * (n + 1)

    F[1] = 1
    F[2] = 1
    if n > 1:
        for i in range(3, n + 1):
         F[i] = (F[i - 1] + (k * F[i - 2]))

    return F[n]

n = 9
k = 3

result = reccurent_rel(n, k)
print(f"число кроличьих пар на {n} месяц: {result}")





