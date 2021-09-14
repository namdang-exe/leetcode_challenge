from collections import Counter

text = "nlaebolko"

# counter
cnt = Counter(text)
res = min(cnt['b'], cnt['a'], cnt['l']//2, cnt['o']//2, cnt['n'])
print(res)
