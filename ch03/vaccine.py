# 문자열 응용 if문

# 백신 접종자 분류
# 접종 대상 : 20세 ~ 65세, 미 대상 - "하반기 일정 확인"


""" 오노!
vaccine = int(input("출생년도 입력 : "))
if 1965 =< vaccine =< 2005:
    print("백신 접종 대상")
    if
    
else:
    print("하반기 일정 확인")
"""





birth_year = input("출생년도 입력 : ")
age = 2023 - int(birth_year) + 1 #birth year가 문자니까 따옴표 해야돼
print(age)
if age >= 20 or age <= 65:
    print("백신 접종 대상")
    print(birth_year)
    # 접종대상 - 출생년도 끝자리 비교
    # if ~ elif ~ else
    if birth_year[-1] == '1' or birth_year[-1] == '6': 
        print("월요일 접종")
    elif birth_year[-1] == '2' or birth_year[-1] == '7':
        print("화요일 접종")
    elif birth_year[-1] == '3' or birth_year[-1] == '8':
        print("수요일 접종")
    elif birth_year[-1] == '4' or birth_year[-1] == '9':
        print("목요일 접종")
    else:
        print("금요일 접종")
else:
    print("하반기 일정 확인")
