f = open("data_input.txt", "r")
r = f.read()

words = r.split()       # 쪼개진 단어들을 배열로 words에 저장

# sort

analyze = {}
for i in words:
    analyze[i] = analyze.get(i, 0) + 1
    # get함수는 key값(i)가 dictionary안에 있을 경우 value값 출력, 없으면 뒤의 값(여기서는 0)출력

lst = sorted(analyze.items(), key=lambda kv:kv[1], reverse=True)
# items 함수는 dictionary의 key와 value를 모두 출력한다.
# 여기서 reverse = True이면 내림차순, False면 오름차순
# lambda는 뭘까?

print("number of words is ", len(lst))
# print(lst)

cnt = 0

for k, v in lst:
    print(k, v)
    if cnt > 400:
        break
    cnt += 1
