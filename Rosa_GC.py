from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

file = "C:/Users/ettod/Downloads/rosalind_gc(1).txt"
bio_seq = list(SeqIO.parse(file, "fasta"))

max_gc = 0.0
seq_max_gc = None

for ID in bio_seq:
    seq = str(ID.seq)
    gc = gc_fraction(seq)

    if gc > max_gc:
        max_gc = gc
        seq_max_gc = ID.id

print(seq_max_gc)
print(max_gc * 100)
