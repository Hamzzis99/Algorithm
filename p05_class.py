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

print()


print("-- constructor --")


class CourseStudent:
    def __init__(self, name, score):
        # __init__은 객체가 만들어질 때 자동으로 호출됩니다.
        # self.name과 self.score는 이 객체가 계속 가지고 있을 속성입니다.
        self.name = name
        self.score = score


park = CourseStudent("Park", 77)
choi = CourseStudent("Choi", 95)

print(park.name, park.score)
print(choi.name, choi.score)