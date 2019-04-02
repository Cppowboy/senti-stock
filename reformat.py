import json
import os


def reformat(filename):
    fin = open(filename, 'r')
    data = json.load(fin)
    fin.close()
    fout = open(filename, 'w')
    json.dump(data, fout, indent=4, sort_keys=True)


for filename in os.listdir('.'):
    fn, ext = os.path.splitext(filename)
    if ext == '.json':
        print('processing', filename)
        reformat(filename)
