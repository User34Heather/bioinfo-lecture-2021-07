handle = open("sequence.protein.2.fasta", "r")
lines = handle.readlines()
title = ""
seq_list = list()
for line in lines:
    line = line.strip()
    if line == "":
        continue
    if line[0] != ">":
        seq_list.append(line)
    else:
        title = line
handle.close()

seq = "".join(seq_list)

index = -1


while True:
    amino = input("Searching for: ")
    if amino == "XXX":
        print("Okay, I will stop.")
        break
    else:
        l_position = []
        while True:
            index = seq.find(amino, index + 1)
            if index == -1:
                break
            position = index + 1
            l_position.append(position)
        s_position = ",".join(str(e) for e in l_position)
        print(f"Found at: {s_position}")
