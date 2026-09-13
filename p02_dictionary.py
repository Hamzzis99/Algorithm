scores = {
    "Kim": 91,
    "Lee": 84,
    "Park": 77,
}

print("-- dictionary --")
print(scores)
print()


# 리스트는 숫자 인덱스로 값을 찾지만, dictionary는 key로 값을 찾습니다.
print("-- lookup by key --")
print("Kim:", scores["Kim"])
print("Lee:", scores["Lee"])
print()


# 이미 존재하는 key에 다시 값을 대입하면 value가 바뀝니다.
scores["Park"] = 88
print("-- update value --")
print(scores)

print()


print("-- missing key raises KeyError --")

# 아래 줄처럼 없는 key를 바로 조회하면 KeyError가 발생합니다.
# print(scores["Choi"])
#
# 수업 예제가 중간에 멈추지 않도록 여기서는 try/except로 에러를 관찰합니다.
try:
    print(scores["Choi"])
except KeyError as error:
    print("KeyError:", error)
print()


print("-- check key before lookup --")

name = "Choi"
if name in scores:
    print(name, scores[name])
else:
    print(name, "is not in scores")

print()


print("-- get with default value --")

print("Kim:", scores.get("Kim", 0))
print("Choi:", scores.get("Choi", 0))
print("after get:", scores)

name = "Kim"
if name in scores:
    print(name, scores[name])
else:
    print(name, "is not in scores")

