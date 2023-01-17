import re

import jieba
import pandas as pd

POP = ["郑分", " "]

result = pd.read_excel(open(r"Z:\\公司\\jenkins-python-demo\\test\\bank.xlsx", mode='rb'), index_col=None, sheet_name="base_bank_branch_code", header=None)
data = pd.read_excel(r"Z:\\公司\\jenkins-python-demo\\test\\dd.xls", index_col=None, sheet_name="aa", header=None, names=["A", "B", "C", "D"])


res = result[0].to_dict()


out = []
for row in data.itertuples():
    dd = list(row)
    name = row.A
    cut_name = jieba.cut(name, cut_all=False)
    cut_name = list(cut_name)
    new_cut_name = []
    for i in cut_name:
        if i in POP or i == "市" and len(i) == 1 and i == "分行":
            continue
        if i == "工行":
            i = "工商银行"
        if i == "浦发":
            i = "上海浦东发展"
        if i == "建行":
            i = "中国建设银行"
        if re.search('市', i) or re.search('省', i):
            i = i[:-1]
        new_cut_name.append(i)    
        
            
    print("开始处理【%s】- %s" % (name, new_cut_name))
    cut_name = new_cut_name
    my_dict = {}
    for key, value in res.items():
        if len(cut_name) == 1:
            if cut_name[0] in value:
                my_dict[key] = value
        elif len(cut_name) == 2:
            if cut_name[0] in value and cut_name[1] in value:
                my_dict[key] = value
        elif len(cut_name) == 3:
            if cut_name[0] in value and cut_name[1] in value and cut_name[2] in value:
                my_dict[key] = value
        elif len(cut_name) == 4:
            if cut_name[0] in value and cut_name[1] in value and cut_name[2] in value and cut_name[3] in value:
                my_dict[key] = value
        elif len(cut_name) == 5:
            if cut_name[0] in value and cut_name[1] in value and cut_name[2] in value and cut_name[3] in value and cut_name[4] in value:
                my_dict = {}
                my_dict[key] = value
            if not my_dict:
                if cut_name[0] in value  and cut_name[2] in value and cut_name[3] in value and cut_name[4] in value:
                    my_dict[key] = value
            if not my_dict:
                if cut_name[0] in value  and cut_name[2] in value and cut_name[4] in value:
                    my_dict[key] = value
        elif len(cut_name) == 6:
            if cut_name[0] in value and cut_name[1] in value and cut_name[2] in value and cut_name[3] in value and cut_name[4] in value and cut_name[5] in value:
                my_dict = {}
                my_dict[key] = value
            if cut_name[0] in value  and cut_name[2] in value and cut_name[3] in value and cut_name[4] in value:
                my_dict[key] = value
        else:
            if cut_name[0] in value  and cut_name[1] in value and cut_name[2] in value and cut_name[3] in value and cut_name[4] in value:
                my_dict[key] = value

 
    if my_dict and len(my_dict) == 1:
        for k, v in my_dict.items():
            u = result[result[0] == v]
            dd.append(u.iloc[0][0])
            dd.append(u.iloc[0][1])
    else:
        
        print("pass")
    out.append(dd)



df1 = pd.DataFrame(out)
df1.to_excel("bb.xlsx", index=False)