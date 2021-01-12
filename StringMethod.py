python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 대문자인지 여부
print(len(python)) # 문자 길이
print(python.replace("Python", "java")) # 문자 대체

index = python.index("n") # n이 있는 위치
print(index)
index = python.index("n", index + 1) # 첫번째(1) n이 나온 다음에 n이 몇번째이 있는지
print(index) 

print(python.find("n")) # n이 있는 위치
print(python.find("Java")) # 원하는 값이 없을 때 -1 return
# print(python.index("Java")) # 없으면 오류가 발생 / find와 차이점
print(python.count("n")) # 동일문자 카운트
