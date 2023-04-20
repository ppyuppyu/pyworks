# 함수 - return 이 있는 함수

def one_up():   # 1을 더하는 함
    x = 0        # 지역 변수
    x = x + 1
    return x

"""
def sqaure(x):
    
    return x * x
"""

def square(x):       #제곱수를 계산
    val = x * x
    return val

#위 아래 밸류 다름 폴더라고 생각 지역에 잇자나

def add(x,y):       
    val = x + y
    return val

#print(one_up()) #1
#print(one_up()) #1

#square() 호출
print(square(2)) #4

result = square(3)
print(result) #9

# add() 함수 호출
print(add(3,4)) #7
