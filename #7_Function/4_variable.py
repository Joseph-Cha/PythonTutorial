# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}\t나이 : {age}\t", end = " ") # end를 붙이면 다음 문장이 이어서 출력됨
#     print(lang1, lang2, lang3, lang4, lang5)

# 가변 인자(*name)를 사용하면 원하는 갯수만큼 파라미터를 받을 수 있다.
def profile(name, age, *language):
    print(f"이름 : {name}\t나이 : {age}\t", end = " ") # end를 붙이면 다음 문장이 이어서 출력됨
    for lang in language:
        print(lang, end="")
    print() #\n



profile("유재석", 20, "python", "java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
