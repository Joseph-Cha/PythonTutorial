def profile(name, age, main_lang):
    print(name, age, main_lang)

# 키워드를 사용하면 모든 파라미터를 키워드로 보내야한다.
# 키워드를 사용함으로 인해 어떤 것 값으로 파라미러를 넘길지 미정이기 때문
profile(name= "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")
