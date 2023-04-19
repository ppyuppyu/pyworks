# 딕셔너리
d = {'Tomas': 13, 'Jane': 9}

# 요소 추가 - Mike가 10살 추가
d['Mike'] = 10
print(d)

# 모든 키 가져오기
print(d.keys())

# 모든 값(value) 가져오기
print(d.values())

# 모든 키와 값 가져오기 - keys(), values(), items()
""" 내가 찾은 방법
print(d.keys(), d.values())
석색스 """

for key, val in d.items():
    print(key, ':', val)

""" 이거 안되 그냥 객체  ㄴㄴ item 함수 써
for key, val in d:
    print(key, ':', val)
"""

print(d.values())
print(list(d.values())) # 리스트 자료로 변
