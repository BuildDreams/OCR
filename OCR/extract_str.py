import re
import os
import pandas as pd


def all_path(params ):
    result = []  # 所有的文件
    froms = []
    print(params)
    dirname = params['ID']
    num = params['ID_ID']
    parrent = re.compile(r'[a-zA-Z0-9]{%s}'%num)
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            (filepath, tempfilename) = os.path.split(apath)
            filename ,tmp= os.path.splitext(tempfilename)
            res = re.findall(parrent, filename)
            res = "".join(res)
            result.append(res)
            froms.append(filename)
    if result  == []:
        result.append(dirname)
    print(result)
    df = pd.DataFrame({'编码':result,"from":froms})
    df.to_excel('编码.xlsx')
    return result




if __name__ == '__main__':
    all_path(r'E:\pdfs',9)