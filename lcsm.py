from Bio import SeqIO

sequences = []
for s in SeqIO.parse("C:/Users/ettod/Downloads/rosalind_lcsm(1).txt", "fasta"):
    seq = ''
    for nuc in s.seq:
        seq += nuc
    sequences.append(seq)

sequences.sort()
tem = sequences[0]
comp = sequences[1:]

shared = ""
for x in range(len(tem)):
    for y in range(x, len(tem)):
        m = tem[x:y+1]
        for el in comp:
            if m in el:
                if len(m) > len(shared):
                    shared = m
            else:
                break
print(shared)

