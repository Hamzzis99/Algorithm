# Python 01. List
#
# 리스트(list)는 여러 값을 하나의 이름으로 묶어서 다루는 자료구조입니다.
# 알고리즘 수업에서는 입력 데이터, 중간 결과, 정렬 대상, DP 테이블의 한 줄 등을
# 리스트로 표현하는 일이 많습니다.


# 대괄호 안에 값을 나열하면 리스트가 됩니다.
# 리스트의 각 값은 원소(element)라고 부릅니다.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(10)은 0부터 9까지의 정수 흐름을 나타냅니다.
# 출력해 보면 리스트처럼 모든 값이 펼쳐져 보이지는 않습니다.
indices = range(10)

print("-- list vs range --")
print(numbers)
print(indices)
print()


# 리스트와 range는 for loop에서 비슷하게 사용할 수 있습니다.
# for value in numbers는 numbers 안의 값을 앞에서부터 하나씩 꺼냅니다.
print("-- for loop over list --")
for value in numbers:
    print(value, end=" - ")
print("//")

# range도 반복문에서 값을 하나씩 만들어 줍니다.
# 큰 범위가 필요할 때는 실제 리스트를 미리 만들지 않는 range가 더 가볍습니다.
print("-- for loop over range --")
for value in indices:
    print(value, end=" - ")
print("//")
print()


# print()는 기본적으로 출력 뒤에 줄바꿈을 붙입니다.
# end 값을 지정하면 줄 끝에 무엇을 붙일지 바꿀 수 있습니다.
print("A", end=" ")
print("B", end=" ")
print("C")
print()


# len()은 원소의 개수를 알려줍니다.
# 인덱스가 0부터 시작하기 때문에 마지막 인덱스는 len(numbers) - 1입니다.
print("-- len of list / range --")
print(len(numbers))
print(len(indices))
print("first:", numbers[0])
print("last:", numbers[len(numbers) - 1])
print()


# range를 실제 리스트로 바꾸어 눈으로 확인하고 싶을 때는 list()를 사용합니다.
print("-- range to list --")
print(list(indices))

print()


print("-- value loop vs index loop --")

# 값만 필요하다면 리스트에서 값을 바로 꺼내는 방식이 가장 읽기 쉽습니다.
for score in [82, 91, 77]:
    print("score:", score)

# 값의 위치도 필요하다면 인덱스를 사용합니다.
# 예를 들어 "몇 번째 값인지" 함께 출력하거나, 같은 위치의 다른 리스트와 비교할 때 필요합니다.
scores = [82, 91, 77]
for i in range(len(scores)):
    print("index:", i, "score:", scores[i])

    print()

    print("-- list update / append / pop --")

    # 리스트는 mutable 객체입니다.
    # 즉, 같은 리스트를 유지한 채 안의 값을 바꿀 수 있습니다.
    scores = [82, 91, 77]
    print("before:", scores)

    scores[2] = 88
    print("after update:", scores)

    # append()는 리스트 맨 뒤에 새 값을 추가합니다.
    scores.append(95)
    print("after append:", scores)

    # pop()은 맨 뒤 값을 꺼내면서 리스트에서 제거합니다.
    last_score = scores.pop()
    print("popped:", last_score)
    print("after pop:", scores)

    # Python 01-2. List Slicing
    #
    # slicing은 리스트의 일부 구간을 잘라 새 리스트처럼 사용하는 문법입니다.
    # 분할 정복, 문자열 처리, 부분 배열을 다루는 코드에서 자주 만납니다.

    letters = ["a", "b", "c", "d", "e", "f"]

    print("-- original list --")
    print(letters)
    print()

    print("-- basic slicing --")

    # letters[start:end]는 start 위치부터 end 바로 앞까지 가져옵니다.
    # end 위치의 원소는 포함하지 않습니다.
    print("letters[1:4] =", letters[1:4])

    # start를 생략하면 처음부터 가져옵니다.
    print("letters[:3] =", letters[:3])

    # end를 생략하면 끝까지 가져옵니다.
    print("letters[3:] =", letters[3:])
    print()

    print("-- negative index --")

    # 음수 인덱스는 뒤에서부터 셉니다.
    # -1은 마지막 원소, -2는 마지막에서 두 번째 원소입니다.
    print("letters[-1] =", letters[-1])
    print("letters[-3:] =", letters[-3:])

    print()

    print("-- reference vs slicing copy --")

    original = [10, 20, 30]

    # copied_name은 original과 같은 리스트를 가리키는 이름입니다.
    copied_name = original
    copied_name[0] = 99
    print("after copied_name[0] = 99")
    print("original:", original)
    print("copied_name:", copied_name)

    # sliced_copy는 slicing으로 만든 새 리스트입니다.
    sliced_copy = original[:]
    sliced_copy[1] = 77
    print("after sliced_copy[1] = 77")
    print("original:", original)
    print("sliced_copy:", sliced_copy)