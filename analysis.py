import json

# mtrain = json.load(open('middle-train.json'))
# mtrain = json.load(open('middle-test.json'))
# mtrain = json.load(open('short-train.json'))
# mtrain = json.load(open('short-test.json'))
# mtrain = json.load(open('long-train.json'))
mtrain = json.load(open('long-test.json'))
counter = {}
for item in mtrain:
    title = item['title']
    symbol = item['symbol']
    polarity = item['polarity']
    if title not in counter:
        counter[title] = []
    counter[title].append([symbol, polarity])
total = 0 
multi = 0
good = 0
for k, l in counter.items():
    v = len(l)
    total += v 
    if v > 1:
        multi += v 
    dic = dict(l)
    if 1 in dic.values() and -1 in dic.values():
        print(k, dic)
        good += 1
print(good, multi, total)