import os 
import json 


file_number = 0 
total_count = 0
for filename in os.listdir('.'):
    _, ext = os.path.splitext(filename)
    if ext == '.json':
        file_number += 1 
        data = json.load(open(filename))
        total_count += len(data)
print(file_number, total_count, total_count/file_number)