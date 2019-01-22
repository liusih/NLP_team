import json
import os
import collections
import random


# from sklearn.model_selection import train_test_split

def extract_list(section_contents):
    for list_num_a in range(len(section_contents)):
        if section_contents[list_num_a]["isContentSection"] == True and section_contents[list_num_a][
            "title"] != "References":
            text_a = section_contents[list_num_a]["text"]
            if text_a:  # ["text"]: not empty
                text_a = text_a.split('\n')  # split text_a with '\n' into para
                for text_a_num in range(len(text_a)):
                    if 80 <= len(text_a[text_a_num].split()) <= 128:
                        result_a = text_a[text_a_num].replace('\t', " ")
                        yield result_a


def extract_entry(entry):
    simple_list = list(extract_list(entry["simple"]["sectionContents"]))
    full_list = list(extract_list(entry["full"]["sectionContents"]))
    return simple_list, full_list


def data_process():
    random.seed(0)
    path = "/home/isliusihong/NLP_team/WikiJoin/data"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    list_class = []
    str = ''
    out = open("all_data_cut.tsv", 'a+')
    number_map = collections.defaultdict(list)
    all_simple = []
    total_full = 0
    for file in files:  # 遍历文件夹

        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            print(path + "/" + file)

            with open(path + "/" + file, 'r') as f:
                load_dict = json.load(f)
                for para_num in range(len(load_dict)):
                    simple_list, full_list = extract_entry(load_dict[para_num])
                    all_simple.extend(simple_list)
                    random.shuffle(full_list)
                    number_map[len(full_list)].append(full_list)
                    total_full += len(full_list)
    max_length = max(number_map.keys())
    while total_full > len(all_simple):
        while max_length not in number_map:
            max_length -= 1
            if max_length == 0:
                raise ValueError
        number_list = number_map[max_length]
        full_list = number_list.pop()
        if not number_list:
            del number_map[max_length]
        full_list.pop()
        if full_list:
            number_map[max_length - 1].append(full_list)
        total_full -= 1
    all_full = []
    for number_list in number_map.values():
        for full_list in number_list:
            all_full.extend(full_list)
    for text in all_simple:
        out.write("simple\t" + text + "\n")

    for text in all_full:
        out.write("full\t" + text + "\n")


data_process()
