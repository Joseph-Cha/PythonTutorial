# 사전 : {}

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) # 키 값이 없으면 곧바로 프로그램이 종료.
print(cabinet.get(5)) # 키 값이 없으면 None을 출력하고 다음 프로그램 실행
print(cabinet.get(5, "사용가능")) # 키 값이 없으면 "사용가능을 가져옴"

# in을 사용해서 사전 자료형의 키값이 있는지 여부 확인 
print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet)

# 새 손님
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)