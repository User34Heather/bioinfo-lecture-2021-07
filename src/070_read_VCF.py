# Meta-info 라인과 헤더라인을 제외한 Data의 행 개수세기

cnt_all = 0     # 전체 행 개수
cnt_pass = 0    # FILTER가 PASS인 행 개수세기

with open('070.vcf', 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        cnt_all += 1
        #if data[6] == "PASS":
        if data[filter_idx] == "PASS":
            cnt_pass += 1

print(cnt_pass, cnt_all, cnt_pass / cnt_all)
