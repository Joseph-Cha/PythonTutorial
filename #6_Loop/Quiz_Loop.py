# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2명

# my answer
from random import *

costomer = range(0, 50)
count = 0
for i in costomer:
    time = randint(5, 50)
    if 5 <= time <= 15 :
        print(f"[0] {i}번째 손님 (소요시간 : {time}분)" )
        count += 1
    else:
        print(f"[ ] {i}번째 손님 (소요시간 : {time}분)" )
print(f"\n총 탑승 승객 : {count}명")

# teacher answer
cnt = 0 
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print(f"[0] {i}번째 손님 (소요시간 : {time}분)" )
        cnt += 1
    else:
        print(f"[ ] {i}번째 손님 (소요시간 : {time}분)" )
print(f"\n총 탑승 승객 : {count}명")


