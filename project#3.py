import urllib.request

url = "http://news.joins.com/article/21947878"

f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')         # utf-8 또는 euc-kr로 decode

begin = data.find("꽃게철이다.")
end = data.find("시사점을 준다.")

end += len("시사점을 준다.")
print("total =", len(data))
print("begin =", begin)
print("end =", end)
print(data[begin:begin+100])
print(data[end-100:end])
print("length =", end-begin)

speech = data[begin:end]
speech = speech.replace("<br/>", "")
speech = speech.replace("&nbsp", "")
speech = speech.split()

# sort

analyze = {}
for i in speech:
    analyze[i] = analyze.get(i, 0) + 1
    # get함수는 key값(i)가 dictionary안에 있을 경우 value값 출력, 없으면 뒤의 값(여기서는 0)출력

lst = sorted(analyze.items(), key=lambda kv:kv[1], reverse=True)
# items 함수는 dictionary의 key와 value를 모두 출력한다.
# 여기서 reverse = True이면 내림차순, False면 오름차순

print("number of words is ", len(lst))
# print(lst)

cnt = 0

for k, v in lst:
    print(k, v)
    if cnt > 400:
        break
    cnt += 1

