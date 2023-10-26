def align(s, t):
    loc = []
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            loc.append(i+1)
    return loc


with open("C:/Users/ettod/Downloads/rosalind_subs.txt") as c:
    m = c.readlines()
s = m[0].strip()
t = m[1].strip()

ins = align(s, t)
S_ins = " ".join(map(str, ins))
print(S_ins)
