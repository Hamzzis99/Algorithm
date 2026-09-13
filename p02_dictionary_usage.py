words = [
    "apple",
    "algorithm",
    "banana",
    "binary",
    "cat",
    "code",
    "data",
]

counts = {}

for word in words:
    first_char = word[0]

    # first_char가 처음 나온 글자라면 먼저 0으로 초기화합니다.
    if first_char not in counts:
        counts[first_char] = 0

    # 이미 있던 글자든 방금 만든 글자든, 단어 하나를 발견했으므로 1 증가시킵니다.
    counts[first_char] += 1

print("-- count words by first character --")
print(counts)