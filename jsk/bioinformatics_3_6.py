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
print(f"title: {title}")
print(f"seq: {seq}")
