#! /usr/bin/env python

# 002.Variable
"""
import math
import sys

if len(sys.argv) != 2:   #길이가 2가 아닐 경우 오류 메시지 print
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

#r=3
r = int(sys.argv[1])   #외부에서 반지름 받아오기, 받아온 str을 int로 변환

#PI=3.14
pi=math.pi


#surface_area = r * r * PI
surface_area = r**2*pi
result = round(surface_area, 2)  #소수점 2자리 까지


print(surface_area) ## 28.26
print(result)
"""

# 003. Operator
"""
import sys

if len(sys.argv) != 3:
    print(f"#usage: python {sys.argv[0]} [n1] [n2]")
    sys.exit()

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} + {n2} = {n1+n2}")
"""

# 004. if - else
"""
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])

"""
"""
if num % 2 == 0:
    print("even")
else:   
    print("odd")
"""
"""
#else를 안쓰고 하는 방법은?

result = "odd"  # 디폴트로 결과값을 odd로 해준다.

if num % 2 == 0 :
    result = "even"

print(result)
"""

# 005. if-elif-else
"""
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [n1]")
    sys.exit()

n1 = int(sys.argv[1])

result = "neither 3,7"

if n1 % 3 == 0 and n1 % 7 == 0:
    result = "3,7"
elif n1 % 3 == 0:
    result = "3"
elif n1 % 7 == 0:
    result = "7"

print(result)
"""

# 006.for
"""
val = 0

for i in range(1, 11):
    val += i

print(val)
"""

# 006.for - 곱으로 해보기
"""
val = 1

for i in range(1, 11):
    #val = val*i
    val *= i

print (val)
"""

# 008. while
"""
import sys
n = int(sys.argv[1])
val = 1

while n>0:
    val *= n
    n -= 1   # 5라면 한번 돌면 4, 두번 돌면 3, 세번돌면 2, 네번돌면 1, 다섯번 돌면 0, 0이니까 여섯번은 안돌고 탈출


print(val)
"""

# 009. 함수

def greet():                        # 함수를 정의
    print("Hello, Bioinformatics")

def greet1(name: str) -> None:
    print(f"Hello, {name}")

def greet2(num: int) -> int:
    return num *2



greet()                             # 함수를 호출
ret1 = greet1("Heather")
print(ret1)                         # NONE 실행한것과  반환은 다르다

ret2 = greet2(3)
print(ret2)







