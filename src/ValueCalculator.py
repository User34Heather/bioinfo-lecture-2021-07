class ValueCalculator:
    def __init__(self, val: str):
        self.val = val
    def __add__(self,other):
        return self.val + other.val

#자체를 실행할때만 나오고, import 할 때는 나오지 않게 하기
#인터프리터로 실행할때만 실행
#파이썬으로 실행하면 name이 main이 되기 때문에 실행된다.
#python ValueCalculatorRunner.py 하면 name이 ValueCalculator로 나옴

 
print(__name__)

if __name__=="__main__":
    print('hi')

