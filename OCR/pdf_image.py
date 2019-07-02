import fitz
import time
import re
import os


def pdf2pic(path, num, bar_value):
    t0 = time.clock()  # 生成图片初始时间
    checkXO = r"/Type(?= */XObject)"  # 使用正则表达式来查找图片
    checkIM = r"/Subtype(?= */Image)"
    doc = fitz.open(path)  # 打开pdf文件
    imgcount = 0  # 图片计数
    lenXREF = doc._getXrefLength()  # 获取对象数量长度
    parrent = re.compile(r'[a-zA-Z0-9]{%s}' % num)
    (filepath, tempfilename) = os.path.split(path)
    filename, tmp = os.path.splitext(tempfilename)
    result = re.findall(parrent, filename)
    result = "".join(result)
    print('==========',result,'==========')
    if result:
        res = result
        pic_name = res
    else:
        res = filename
        pic_name = "_"
    # 打印PDF的信息
    print("文件名:{}, 页数: {}, 对象: {}".format(path, len(doc), lenXREF - 1))

    # 遍历每一个对象
    for i in range(1, lenXREF):
        text = doc._getXrefString(i)  # 定义对象字符串
        isXObject = re.search(checkXO, text)  # 使用正则表达式查看是否是对象
        isImage = re.search(checkIM, text)  # 使用正则表达式查看是否是图片
        if not isXObject or not isImage:  # 如果不是对象也不是图片，则continue
            continue
        imgcount += 1
        pix = fitz.Pixmap(doc, i)  # 生成图像对象
        new_name = "{}_{}.jpg".format(pic_name,imgcount)  # 生成图片的名称
        new_path  = os.getcwd() +r"\图片"
        bar_value.emit(['bar', 90 / lenXREF * (i + 1)])
        if os.path.exists(new_path):
            print("文件夹已存在，不必重新创建！")
            pass
        else:
            os.makedirs(new_path)

        new_filepath = new_path+ r"\%s"%res
        print(new_filepath)
        if os.path.exists(new_filepath):
            print("文件夹已存在，不必重新创建！")
        else:
            os.makedirs(new_filepath)

        if pix.n < 5:  # 如果pix.n<5,可以直接存为PNG
            pix.writePNG(os.path.join(new_filepath, new_name))
        else:  # 否则先转换CMYK
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(new_filepath, new_name))
            pix0 = None
        pix = None  # 释放资源
        t1 = time.clock()  # 图片完成时间
        print("运行时间:{}s".format(t1 - t0))
        print("提取了{}张图片".format(imgcount))

def all_path_img(params):
    """
    获取文件夹pdf
    :param dirname:
    :param num:
    :return:
    """
    dirname = params['PDF'][0]
    num = params['IMG_ID']
    f = os.path.isfile(dirname)

      # 所有的文件
    if os.path.isfile(dirname):
        print(dirname, num, '-===================')
        pdf2pic(dirname, num, params['bar_value'])
    elif os.path.isdir(dirname):
        for maindir, subdir, file_name_list in os.walk(dirname):
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)  # 合并成一个完整路径
                if '.pdf' in apath:
                    pdf2pic(apath, num)
    else:
        raise ValueError





if __name__ == '__main__':
    path = r"E:\共享\MSA201款).pdf"
    files = all_path_img(path,9)
    # for i in files:
    #     pdf2pic(i, 9)

    #创建保存图片的文件夹
