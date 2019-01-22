import json
import os
import pandas as pd
#from sklearn.model_selection import train_test_split


def data_process():
    path = "/home/isliusihong/NLP_team/WikiJoin/data" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    list_class = []
    str=''
    out= open("all_data_cut.tsv",'a+')
    for file in files: #遍历文件夹
        
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            print(path+"/"+file)

            with open(path+"/"+file, 'r') as f:
                load_dict = json.load(f)
                for para_num in range(len(load_dict)):
                    #list_class=["simple","full"]
                    text_a_list = load_dict[para_num]["simple"]["sectionContents"]
                    
                    for list_num_a in range(len(text_a_list)):
                        if text_a_list[list_num_a]["isContentSection"] == True and text_a_list[list_num_a]["title"] != "References":
                            text_a = text_a_list[list_num_a]["text"]
                            if text_a:  # ["text"]: not empty
                                text_a = text_a.split('\n') # split text_a with '\n' into para
                                for text_a_num in range(len(text_a)):
                                    if 60 <= len(text_a[text_a_num]) <= 128:
                                        result_a=text_a[text_a_num].replace('\t'," ")
                                        out.write("simple"+'\t'+result_a+'\n')

                    text_b_list = load_dict[para_num]["full"]["sectionContents"]
                    
                    for list_num_b in range(len(text_b_list)):
                        if text_b_list[list_num_b]["isContentSection"] == True and text_b_list[list_num_b]["title"] != "References":

                            text_b = text_b_list[list_num_b]["text"]
                            if text_b:
                                text_b = text_b.split('\n') # split text_a with '\n' into para
                                for text_b_num in range(len(text_b)):
                                    if 60 <= len(text_b[text_b_num]) <= 128:
                                        result_b=text_b[text_b_num].replace('\t'," ")
                                        out.write("full"+'\t'+result_b+'\n')

#data_process()
