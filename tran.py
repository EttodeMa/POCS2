from Bio import SeqIO


lns = []
for line in SeqIO.parse("C:/Users/ettod/Downloads/rosalind_tran.txt", 'fasta'):
    sq = str(line.seq)
    lns.append(sq)
s = lns[0]
t = lns[1]
transi = 0
transv = 0
for x in range(len(s)):
    if s[x] != t[x]:
        if s[x] == "A":
            if t[x] == "G":
                transi += 1
            else:
                transv += 1
        if s[x] == "G":
            if t[x] == "A":
                transi += 1
            else:
                transv += 1
        if s[x] == "T":
            if t[x] == "C":
                transi += 1
            else:
                transv += 1
        if s[x] == "C":
            if t[x] == "T":
                transi += 1
            else:
                transv += 1

ratio = transi/transv
print(round(ratio, 10))