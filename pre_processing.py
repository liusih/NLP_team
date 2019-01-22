import json

import os

def data_process():
    path = "/home/isliusihong/NLP_team/WikiJoin/data" #文件夹目录
    files= os.listdir(path) #得到文件夹下的所有文件名称
    s = []
    i=0
    str=''
    out= open("all_data.tsv",'a+')
    for file in files: #遍历文件夹
        
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            print(path+"/"+file)

            with open(path+"/"+file, 'r') as f:
                load_dict = json.load(f)
                for para_num in range(len(load_dict)):

                    text_a_list = load_dict[para_num]["simple"]["sectionContents"]
                    
                    for list_num_a in range(len(text_a_list)):
                        if text_a_list[list_num_a]["isContentSection"] == True or text_a_list[list_num_a]["title"] == "References":
                            text_a = text_a_list[list_num_a]["text"]
                            if text_a:
                                text_a=text_a.replace('\n',"")
                                out.write("simple"+'\t'+text_a+'\n')

                    text_b_list = load_dict[para_num]["full"]["sectionContents"]
                    
                    for list_num_b in range(len(text_b_list)):
                        if text_b_list[list_num_b]["isContentSection"] == True or text_b_list[list_num_b]["title"] == "References":

                            text_b = text_b_list[list_num_b]["text"]
                            if text_b:
                                text_b=text_b.replace('\n',"")
                                out.write("full"+'\t'+text_b+'\n')

        i=i+1
        if i>=5:
            break

data_process()
