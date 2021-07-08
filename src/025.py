Seq1 = "ATGTTATAG"

# 025.

for i in range(0, len(Seq1), 3):
    print(Seq1[i])

# 026.

for i in range(0, len(Seq1), 3):
    print(Seq1[i:i+3])

# 027.
S_rev = Seq1[::-1]
print(Seq1)
print(S_rev)

for i in range(len(Seq1)):
    print(f"{Seq1[i]}{S_rev[i]}")

# 028.

dic_cDNA = {"A":"T", "T":"A", "C":"G", "G":"C"}

for i in range(len(Seq1)):
    print(dic_cDNA[Seq1[i]], end="")

print()

# 029. 

print("C" in Seq1)

# 030. 마크로젠 코딩테스트중 하나였음
# 정답 2, 3

Seq2 = "AGTTTATAG"

for i in range(len(Seq2)):
    s=Seq2[i:i+2]
    print(i, s, s=="TT")

for i in range(len(Seq2)):
    s=Seq2[i:i+2]
    if s == "TT":
        print(i)

# 031. 문자열 리스트로 바꾸기

str_Seq="AA,AC,AG,AT"

l_Seq=str_Seq.split(',')

print(l_Seq)

# 032. 리스트에 요소 추가하기

l_Seq.append("CA")

print(l_Seq)

# 033.

print(l_Seq[::-1])

# 034. min(list) max(list)

# 035.

l_int=[3, 1, 1, 2, 0, 0, 2, 3, 3]

cnt=dict()

for elem in l_int:
    if elem not in cnt:
        cnt[elem] = 0
    cnt[elem] += 1

print(cnt)        






