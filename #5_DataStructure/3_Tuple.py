# 튜플 : ()
# List와 차이점
# 변경은 불가능 하지만 List보다 빠르다
# 변경되지 않는 데이터 관리에 용이

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
