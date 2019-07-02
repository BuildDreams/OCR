# -*- coding: UTF-8 -*-
from aip import AipOcr
import os
import time
# 定义常量
APP_ID = '16200162'
API_KEY = 'A73jrKZsLGEM7K3Q7zbFQ5FM'
SECRET_KEY = 'voQqRFKhCHWqMg2VIn7CTayR9XqxObqU'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 的方法"""


def get_file_content(filePaths):
    with open(filePaths, 'rb') as fp:
        return fp.read()


def get_file_str(params):
# 定义图片的绝对路径
    file_paths  = params['IMG']
    bar_value = params['bar_value']
    print(file_paths)
    content = []
    all_content = []
    for i, file_path in enumerate(file_paths):#循环获取图片文件
        time.sleep(2)
        bar_value.emit(['bar',90 / len(file_paths) * (i+1)])
        print(90 / len(file_paths) * i)
        path,title = os.path.split(file_path)
        image = get_file_content(file_path)
        """ 调用通用文字识别（高精度版） """
        options = {}
        options["detect_direction"] = "true"
        # restu1 = client.basicAccurate(image, options)
        restu1 = client.basicGeneral(image, options)

        print(restu1)
        lists = restu1.get('words_result', None)  # 列表
        if lists:
            for listss in lists:
                content.append(listss['words'])
            content ="<br /><br /><h4>--------------%s--------------</h4>"%title + '<br />'+ "<br />".join(content)+'+'*20
            all_content.append(content)
            content = []
    split_str = '='*20
    all_content = '%s'%split_str.join(all_content)
    return all_content


if __name__ == '__main__':
    file_path = r'E:\pdfs\图片\C170C0219\C170C0219_1.jpg'
    get_file_str(file_path)
