# for ~ in문
languages = ['Python', 'C', 'Java', 'Javascript']

for lang in languages:
    if lang in ['Python', 'Javascript']:
        print(f'{lang} need interpreter') #인터프리터
    else:
        print(f'{lang} need compiler') #컴파일러

# 구구단 출력
dan = 4

result = ""

for i in range(1, 10):
    current_val =f'{dan} x {i} = {dan * i}\n'
    result = result + current_val; #여기서 +는 연결자
print(result)

#이러면 나중에 리턴 가능

"""
for i in range(1, 10):
    print(f'{dan} x {i} = {dan * i}')

"""


