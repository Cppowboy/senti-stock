import json
import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    counter = Counter()
    num_list = []
    stock_number = 0
    news_number = 0
    for filename in os.listdir('.'):
        sym, ext = os.path.splitext(filename)
        if ext == '.json':
            data = json.load(open(filename, 'r', encoding='utf-8'))
            num_list.append(len(data))
            stock_number += 1
            news_number += len(data)
    # print(num_list)
    count = 0
    total = 0
    for k in num_list:
        if k > 500:
            count += 1
            total += k
    print(count, total)
    print(stock_number, news_number)
