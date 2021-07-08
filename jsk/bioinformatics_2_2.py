# len 함수의 정의
def my_len(string):
    cnt = 0
    for s in string:  # string : 시퀀스 자료형
        cnt += 1
    return cnt


message = input("Enter a string: ")
length = my_len(message)

print(f"The string length is {length}")
