class Student:
    pass


print("-- create objects --")

kim = Student()
lee = Student()

print(kim)
print(lee)
print("same object?", kim is lee)
print()


print("-- add attributes at runtime --")

# Python에서는 객체를 만든 뒤에도 속성을 붙일 수 있습니다.
kim.name = "Kim"
kim.score = 91

lee.name = "Lee"
lee.score = 84

print(kim.name, kim.score)
print(lee.name, lee.score)