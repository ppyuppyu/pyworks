# bmi.py
# 체질량 지수 = 몸무게 / 키의 제곱
# 키 = 키 / 100 -> cm로 환산
# 거듭제곱 3 ** 2 = 3 x 3

name = input("이름을 입력하세요 : ")
weight = float(input("몸무게(kg)를 입력하세요: "))
height = float(input("키(cm)를 입력하세요: "))
height = height / 100 # cm를 환산

# 체질량 지수
bmi = weight / (height ** 2)

print(f'{name}님의 bmi는 {bmi:.2f}입니다.')   # f 스트링(string) 방식
print("%s님의 bmi는 %.2f입니다." % (name, bmi)) # % 포맷 방식

if bmi < 18.5:
    print('저체중입니다.')
elif bmi < 25:
    print('정상입니다.')
elif bmi < 30:
    print('과체중입니다.')
else:
    print('비만')
