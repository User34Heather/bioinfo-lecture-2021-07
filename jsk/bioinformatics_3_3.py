with open("sequence.protein.fasta", "r") as handle:
    lines = handle.readlines()
    for line in lines:
        print(line.rstrip())
