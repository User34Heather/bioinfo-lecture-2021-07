handle = open("sequence.protein.2.fasta", "r")
cnt = 0
line_num = int(input("Which line? :"))

for line in handle:
    cnt += 1
    line = line.strip()

    if cnt == line_num:
        break

print(line)

handle.close()
