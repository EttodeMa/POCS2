from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

with open("C:/Users/ettod/Downloads/rosalind_prot(1).txt") as seq:
    rna = seq.read()
rna_obj = Seq(rna)
prot = rna_obj.translate()
prot_rec = SeqRecord(prot, id = "protein_sequence", description = "translated from RNA")
print(prot_rec.seq.rstrip("*"))
