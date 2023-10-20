with open("C:/Users/ettod/Downloads/rosalind_hamm.txt") as X:
    i = X.readlines()
DNA1 = i[0].strip()
DNA2 = i[1].strip()
c = 0
v = 0
for w in DNA1:
    if w != DNA2[v]:
        c = c + 1
    v = v + 1
print(c)
