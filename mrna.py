codon = {'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
         'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
         'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
         'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
         'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
         'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
         'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
         'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
         'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
         'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
         'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
         'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
         'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
         'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
         'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
         'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W',
         }

tot = {}
for amac in codon.values():
    if amac in tot:
        tot[amac] += 1
    else:
        tot[amac] = 1

tot_stop = tot["_"]

with open("C:/Users/ettod/Downloads/rosalind_mrna.txt") as D:
    f = D.readline().strip()

for ammino in f:
    tot_stop *= tot[ammino]

print(tot_stop % 1000000)
