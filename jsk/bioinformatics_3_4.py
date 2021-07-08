fasta2 = open("sequence.protein.2.fasta", "w")

with open("sequence.protein.fasta", "r") as handle:
    lines = handle.readlines()
    for line in lines:
        fasta2.write(line)

fasta2.close()
