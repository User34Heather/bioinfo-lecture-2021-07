# 리드의 갯수 출력
# 전체 base count(두번째줄)

read_cnt=0
base_cnt = dict()

with open('061.fastq', 'r') as handle:
    for line in handle:
        if read_cnt % 4 == 0: #header
            pass
        elif read_cnt % 4 == 1: #base
            for base in line.strip():
                if base not in base_cnt:
                    base_cnt[base] = 0
                base_cnt[base] += 1
        elif read_cnt % 4 == 2: #delimiter
            pass
        elif read_cnt % 4 == 3: #qual
            pass
        read_cnt += 1

print(read_cnt / 4)  #100.0
print(base_cnt) # {'G': 2446, 'C': 2391, 'A': 2766, 'T': 2497}
