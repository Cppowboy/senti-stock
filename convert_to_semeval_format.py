import json
import xml.etree.cElementTree as ET
import random


def convert(data_list, xml_file):
    # data_list = json.load(open(json_file, 'r', encoding='utf-8'))
    root = ET.Element('sentences')
    dic = {-1: 'negative', 0: 'neutral', 1: 'positive'}
    for item in data_list:
        sentence = ET.SubElement(root, 'sentence')
        text = ET.SubElement(sentence, 'text')
        text.text = item['title']
        # aspectTerms = ET.SubElement(sentence, 'aspectTerms')
        # aspectTerm = ET.SubElement(aspectTerms, 'aspectTerm')
        # aspectTerm.set('term', item['symbol'])
        # aspectTerm.set('polarity', dic[item['polarity']])
        aspectCategories = ET.SubElement(sentence, 'aspectCategories')
        aspectCategory = ET.SubElement(aspectCategories, 'aspectCategory')
        aspectCategory.set('category', item['symbol'])
        aspectCategory.set('polarity', dic[item['polarity']])
        print(item['title'], item['symbol'], dic[item['polarity']])
    tree = ET.ElementTree(root)
    tree.write(xml_file)


def split(filename):
    data_list = json.load(open(filename, 'r', encoding='utf-8'))
    random.shuffle(data_list)
    number = len(data_list)
    train_num = int(number*0.8)
    train_list = data_list[:train_num]
    test_list = data_list[train_num:]
    return train_list, test_list


if __name__ == '__main__':
    trainset, testset = split('long.json')
    json.dump(trainset, open('long-train.json', 'w', encoding='utf-8'))
    json.dump(testset, open('long-test.json', 'w', encoding='utf-8'))
    trainset = json.load(open('long-train.json'))
    testset = json.load(open('long-test.json'))
    convert(trainset, 'long-train.xml')
    convert(testset, 'long-test.xml')

    # trainset, testset = split('middle.json')
    # json.dump(trainset, open('middle-train.json', 'w', encoding='utf-8'))
    # json.dump(testset, open('middle-test.json', 'w', encoding='utf-8'))
    # trainset = json.load(open('middle-train.json'))
    # testset = json.load(open('middle-test.json'))
    # convert(trainset, 'middle-train.xml')
    # convert(testset, 'middle-test.xml')

    # trainset, testset = split('short.json')
    # json.dump(trainset, open('short-train.json', 'w', encoding='utf-8'))
    # json.dump(testset, open('short-test.json', 'w', encoding='utf-8'))
    # trainset = json.load(open('short-train.json'))
    # testset = json.load(open('short-test.json'))
    # convert(trainset, 'short-train.xml')
    # convert(testset, 'short-test.xml')


# import xml.etree.cElementTree as ET

# root = ET.Element("root")
# doc = ET.SubElement(root, "doc")

# ET.SubElement(doc, "field1", name="blah").text = "some value1"
# ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

# tree = ET.ElementTree(root)
# tree.write("filename.xml")
