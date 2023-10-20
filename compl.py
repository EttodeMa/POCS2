#with open("C:/Users/ettod/Downloads/rosalind_revc.txt") as X :
  #  i = X.readline()
i = "AAAACCCGGT"
DNA = ""
for y in i :
    if y == "T":
        DNA += "A"
    elif y == "A":
        DNA += "T"
    elif y == "C":
        DNA += "G"
    elif y == "G":
        DNA += "C"
print(DNA)
DNA_R = DNA[::-1]
print(DNA_R)