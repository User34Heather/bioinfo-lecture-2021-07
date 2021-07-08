#!/usr/bin/env python

# 013. 사용자로부터 값 받기 - 하드코딩 피하기
"""
name = input("이름입력 : ")
print(f"Hello {name}")
"""

# 014. 숫자인지 문자인지? .isalpha()
"""
s = input("입력:")

print(s.isalpha())

if s.isalpha():
    print("%s는 문자." %s)
else:
    print("%s는 숫자." %s)
"""

# 015. 커맨드라인에서 인수 입력받기
"""
import sys

if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [sample]")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f"{err}, your input: {sys.argv[1]}")
    sys.exit(3)
try:
    res = 10/ num
except ZeroDivisionError as err:
    print(err)
    sys.exit(2)


print(res)
"""

# 016. 파일읽기
"""
file_name = "read_sample.txt"
"""
# 방법1
"""
with open(file_name, "r") as handle:    # 파일오픈 객체를 as로 
    for line in handle:                 
        print(line.strip())             #print(line, end="")
"""

# 방법2
"""
handle = open(file_name, "r")           # for문에 indent 안해도되고, 대신 close 해줘야
for line in handle:
    print(line.strip())
handle.close()
"""

# 방법3
"""
handle = open(file_name, "r")
lines = handle.readlines()              # 리스트 같은게 나온다
for line in lines:
    print(line.strip())
handle.close()
"""

# 방법1+3
"""
with open(file_name, "r") as handle:
    lines = handle.readlines()      
    for line in lines:
        print(line.strip())
""" 

# 017. 파일쓰기
"""
# <영상> join으로 리스트 원하는 형식으로 바꾸기
# tab을 탭으로 ?? tsv
# tab기준으로 바꾸려면...


handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("Bioinformatics\n")


with open(file_name, "w") as handle:
    handle.write("Heather\n")
    handle.write("1,2,3\")
"""

# 019. 예외처리하기
"""
import sys

try:
    with open("hahaha.txt", 'r') as handle:
        data = handle.readlines()
except FileNotFoundError as err:
    print("파일이 없습니다.")
    sys.exit()
    
print(data)
"""

# 교재 예제
"""
import sys

try:
    val = int(input("Enter: "))
except ValueError as err:
    print(err)
    sys.exit()

try:
    print(10/val)
except ZeroDivisionError as err:
    print(err)
    sys.exit()
"""

# 두가지 경우 합쳐서
"""
import sys

try:
    val = int(input("Enter: "))
    print(10 / val)

except ZeroDivisionError as err1:
    print(err1)
    sys.exit()
except ValueError as err2:  
    print(err2)
    sys.exit()
"""

# class 관련

class A:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __mul__(self, other):
        return "__mul__"

a1 = A("a")
a2 = A("b")
print(a1.val + a2.val)
print(a1+a2)
print(a1 * a2)

