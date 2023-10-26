from Bio import SeqIO

file = "C:/Users/ettod/Downloads/rosalind_cons.txt"

fasta = list(SeqIO.parse(file, "fasta"))

matrix = {"A": [0] * len(fasta[0].seq),
          "C": [0] * len(fasta[0].seq),
          "G": [0] * len(fasta[0].seq),
          "T": [0] * len(fasta[0].seq)}

for X in fasta:
    for i, base in enumerate(X.seq):
        matrix[base][i] += 1

cons = "".join(max(matrix, key=lambda x:matrix[x][i])for i in range(len(fasta[0].seq)))
print(cons)
for Y in matrix:
    print(Y + ": " + " ".join(map(str, matrix[Y])))

