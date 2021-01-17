gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(f"[함수내] 남은 총 :{gun}")

# 파라미터의 gun은 함수 내에서 지역변수 
def chechpoint_return(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수내] 남은 총 :{gun}")
    return gun


print(f"전체 총 : {gun}")
# checkpoint(2) # 2명이 경계 근무 나감

# 여거서 파라미터로 넘긴 gun은 가장 위에 있는 gun이다
gun = chechpoint_return(gun, 2)
print(f"남은 총 : {gun}")