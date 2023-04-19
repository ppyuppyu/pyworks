# 중첩 for문
# 5행 5열

"""
for i in range(5): # range(0, 5, 1)
    print(i)
"""

for i  in range(5):
    for j in range(5):
        print('$', end='')
    print()


# 스타(*) 출력
# 삼각형


""" 행은 바뀌는 게 없는데 열이 추가 되고 있다
*
**
***
****
*****
"""


for i  in range(0,5):
    for j in range(0,i+1):
        print('*', end='')
    print()
    
""" 이거슨 디버깅
i=0,           
i=1, j=0                      *
i=2, j=0, j=1                 **
i=3, j=0, j=1, j=2            ***
i=4, j=0, j=1, j=2, j=3       ****
i=5, j=0, j=1, j=2, j=3, j=4  *****

1  2  3  4  5  -> 5*0+1, 5*0+2, 5*0+3, 5*0+4, 5*0+5
6  7  8  9  10 -> 5*1+1, 5*1+2, 5*1+3, 5*1+4, 5*1+5
11 12 13 14 15 -> 5*2+1, 5*2+2, 5*2+3, 5*2+4, 5*2+5
16 17 18 19 20 -> 5*3+1, 5*3+2, 5*3+3, 5*3+4, 5*3+5
21 22 23 24 25 -> 5*4+1, 5*4+2, 5*4+3, 5*4+4, 5*4+5
"""

for i  in range(0,5):
    for j in range(1,6):
        print(5*i+j, end=' ') # 5는 j의 종료값
    print()

print('='*20)

row = 5
col = 5

for i  in range(0,row):
    for j in range(1,col+1):
        print(col*i+j, end=' ') # 5는 j의 종료값
    print()


