#주석
#자료형 - 숫자, 문자, 불리언, 리스트, 객체
#여러줄 주석: 쌍따옴표(홑따옴표) 3개를 쌍으로 적음.

print(12)
print(type(12))








n=1 #변수 선언 방법 - 자료형은 생략
print('n = ', n) #콤머(,)는 한 칸 띄움
print('n = ' + str(n) + '개') #str(숫자) - 문자로 변환함

msg= "좋은 하루!!"
print('메시지:', msg)
#print(type(msg)) # <class 'str'>


num = int('120') # int(문자형) - 숫자로 변환함
print(num)

num2 = int(120.7)
print(num2) # 12

# 불리언(참/거짓)
state = True
print(state)   # True - 첫글자 대문자
print(not state) # False

print( 10 > 11 ) #False
print( 10 < 11 ) #True
