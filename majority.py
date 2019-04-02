import json
from collections import Counter


def key_of_max_value(dic):
    max_value = -1000
    key = None
    for k, v in dic.items():
        if v > max_value:
            key = k
            max_value = v
    return key


# mtrain = json.load(open('middle-train.json'))
# mtest = json.load(open('middle-test.json'))
mtrain = json.load(open('short-train.json'))
mtest = json.load(open('short-test.json'))
train_counter = Counter()
test_counter = Counter()
for item in mtrain:
    p = item['polarity']
    train_counter[p] += 1
for item in mtest:
    p = item['polarity']
    test_counter[p] += 1
print(train_counter, test_counter)

# train_counter = {}
# test_counter = {}
# for item in mtrain:
#     symbol = item['symbol']
#     p = item['polarity']
#     if symbol not in train_counter:
#         train_counter[symbol] = Counter()
#     train_counter[symbol][p] += 1
# for item in mtest:
#     symbol = item['symbol']
#     p = item['polarity']
#     if symbol not in test_counter:
#         test_counter[symbol] = Counter()
#     test_counter[symbol][p] += 1
# key_list = list(train_counter.keys())
# correct = 0
# total = 0
# for k in key_list:
#     print(train_counter[k], test_counter[k])
#     kk = key_of_max_value(train_counter[k])
#     total += sum(test_counter[k].values())
#     correct += test_counter[k][kk]
# print(correct, total, correct/total)
