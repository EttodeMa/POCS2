def deadrabbit(n, m):
    months = [0] * (n)
    months[0] = 1
    for x in range(0, n):
        temp = months[x]
        months[x] = months[x-1] + months[x-2]
        months[x] = temp + months[x]
        if x == m:
            months[x] = months[x] - 1
        if x >= m:
            months[x] = months[x] - months[(x - m) - 1]
    return months[n-1]


with open("C:/Users/ettod/Downloads/rosalind_fibd.txt") as D:
    f = D.read().split()
n = int(f[0])
m = int(f[1])
t = deadrabbit(n, m)
print(t)
