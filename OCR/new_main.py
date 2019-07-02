# -*- coding: utf-8 -*-
import re
import os
import base64
import sys
import random

from aip import AipOcr
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QIcon,  QPainter
from PyQt5.QtCore import Qt

from  main_ui_new import Ui_Dialog
from extract_str  import all_path
from pdf_image import all_path_img
from img_str import  get_file_str
from pics import mgs
from hotKeys import *
__author__ = 'zq'
__date__ = '2019/6/24 21:56'




def get_pic(pic_code, pic_name):
    """
    全局图片资源加载。
    :param pic_code: 导入的base64图片编码
    :param pic_name: 生成的图片文件名字。
    :return:
    """
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()
    return image

get_pic(mgs, 'mg.ico')

APP_ID = '' # 百度申请
API_KEY = '' #百度申请
SECRET_KEY = '' #百度申请

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)




class MyCalc(QWidget):
    oksignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.__bindEvent()
        self.params = {}
        self.Seticon()
        self.start = (0, 0)  # 开始坐标点
        self.end = (0, 0)  # 结束坐标点
        self.Process({'hotkey':'run'})
        self.counts = 1
        self.gens = {}
        self.setGens()



    def Seticon(self):
        """
        设置图标。
        :return:
        """
        self.winIconPix = QPixmap(16, 16)
        self.ui.setWindowIcon(QIcon('mg.ico'))

    def __bindEvent(self):
        self.ui.extract_id_btn.clicked.connect(self.__openFileAll)
        self.ui.extract_img_btn.clicked.connect(self.__openFilesPdf)

        self.ui.starts.clicked.connect(self.starProcess)
        self.ui.img_id_long_text.setText('8,9')
        self.ui.file_id_long_text.setText('8,9')
        self.ui.extract_txt_btn.clicked.connect(self.click_btn)
        self.ui.radio_btn.toggled.connect(lambda :self.changeGens(self.ui.radio_btn))
        self.ui.radio_btn_gen.toggled.connect(lambda :self.changeGens(self.ui.radio_btn_gen))
        self.ui.starts.clicked.connect(self.pprint)

        self.oksignal.connect(lambda: self.screenshots(self.start, self.end))

    def setGens(self):
        if self.ui.radio_btn_gen.isCheckable():
            self.gens.update({'gens':"high"})


    def pprint(self):
        print(self.gens)

    def changeGens(self, object):
        """选择模式"""
        # sender = object.sender()
        # print(sender.text())
        if object.text() == "高精度":
            if object.isChecked():
                self.gens.update({'gens': "high"})
        if object.text() == "普通精度":
            if object.isChecked():
                self.gens.update({'gens': "low"})


    def click_btn(self):
        # self.showMinimized()
        # self.screenshot = ScreenShotsWin()
        self.showFullScreen()
        self.setWindowOpacity(0.4)



    def __openFileAll(self):
        """文件编码提取"""
        open_file_name = QFileDialog.getExistingDirectory(self, "选取文件", "./")
        self.ui.text_up.setHtml(open_file_name)
        self.params['ID'] = open_file_name
        self.params['TYPES'] = "FILES"

    def __openFilesImg(self):
        """PDF图片提取"""
        open_file_name = QFileDialog.getOpenFileNames(self,"选取文件", "./", "img(*.png *.jpg);;")
        self.ui.text_up.setHtml("<br/>".join(open_file_name[0]))
        self.params['IMG'] = open_file_name[0]
        self.params['TYPES'] = "IMG"

    def __openFilesPdf(self):
        open_file_name = QFileDialog.getOpenFileNames(self,"选取文件", "./", "PDF(*.pdf);;")
        self.ui.text_up.setHtml("<br/>".join(open_file_name[0]))
        self.params['PDF'] = open_file_name[0]
        self.params['TYPES'] = "PDF"

    def Process(self, *args):
        """核心线程模块"""
        self.myThread = Runthread(*args)
        self.myThread.updata_date.connect(self.Callback)
        self.myThread.start()


    def starProcess(self):
        self.params['ID_ID'] = self.ui.file_id_long_text.text()
        self.params['IMG_ID'] = self.ui.img_id_long_text.text()
        if self.params.get('TYPES', None):
            self.Process(self.params)


    def Randomcolor(self):
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0, 14)]
        return "#" + color

    def Callback(self,data):
        """线程结束回调函数"""
        print(data,self.counts)
        if data[0] == 'hotKet':
            if self.counts >= 2:
                print("回调")
                self.click_btn()
            if self.counts == 1:
                self.counts += 1


        if data[0] == 'content':
            datas = data[1]
            lens = len(self.params['IMG'])
            colors = set()
            for i in range(1, lens + 1):
                color = "<font color='%s'>" % self.Randomcolor()
                colors.add(color)
                repl_data = re.sub('=' * 20, color, datas, count=1)
                repl_data1 = re.sub(r'\+' * 20, '</font>', repl_data, count=1)
                datas = repl_data1
            print(datas)
            self.ui.text_down.setHtml(datas)
        if data[0] == 'ok':
            self.params.clear()
            self.ui.text_up.clear()
            QMessageBox.information(self, 'info', '操作成功', QMessageBox.Yes, QMessageBox.Yes)


    def screenshots(self, start, end):
        '''
        截图功能
        :param start:截图开始点
        :param end:截图结束点
        :return:
        '''
        x = min(start[0], end[0])
        y = min(start[1], end[1])
        width = abs(end[0] - start[0])
        height = abs(end[1] - start[1])

        des = QApplication.desktop()
        screen = QApplication.primaryScreen()
        if screen:
            self.setWindowOpacity(0.1)
            pix = screen.grabWindow(des.winId(), x, y, width, height)
            pix.save('./1.png')
            with open('./1.png', 'rb') as fp:
                image = fp.read()
            options = {}
            content = []
            options["detect_direction"] = "true"
            if self.gens.get('gens') == 'high':
                restu1 = client.basicAccurate(image, options)
            else :
                restu1 = client.basicGeneral(image, options)
            try:
                if restu1.get('error_code') == 17:
                    reply4 = QMessageBox.about(self, "about", "当前次数已经用完,请选择普通精度！")
                print(restu1)
                lists = restu1['words_result']  # 列表
                if lists:
                    for listss in lists:
                        content.append(listss['words'])
                    content = "\n".join(content)
                    if content:
                         self.ui.tip_input.getMultiLineText(self, "按ESC可关闭", "提取完成！",content)
                         self.ui.tip_input.close()

                else:
                    reply4 = QMessageBox.about(self, "about", "请重新截图！截图异常。！")

            except:
                if restu1.get('error_code') != 216202:
                    reply4 = QMessageBox.about(self, "about", "请重新截图！截图过大！")

                if restu1.get('error_code') != 17:
                    reply4 = QMessageBox.about(self, "about", "请重新截图！")


    def paintEvent(self, event):
        '''
        给出截图的辅助线
        :param event:
        :return:
        '''

        x = self.start[0]
        y = self.start[1]
        w = self.end[0] - x
        h = self.end[1] - y

        pp = QPainter(self)
        pp.setBrush(Qt.SolidPattern)
        pp.setPen(Qt.blue)
        pp.drawRect(x, y, w, h)
        pp.end()


    def mousePressEvent(self, event):

        # 点击左键开始选取截图区域
        if event.button() == Qt.LeftButton:
            self.start = (event.pos().x(), event.pos().y())


    def mouseReleaseEvent(self, event):

        # 鼠标左键释放开始截图操作
        if event.button() == Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            self.oksignal.emit()
            self.update()
            self.start = (0, 0)  # 开始坐标点
            self.end = (0, 0)  # 结束坐标点

            self.close()


    def mouseMoveEvent(self, event):
    # 鼠标左键按下的同时移动鼠标绘制截图辅助线
        if event.buttons() and Qt.LeftButton:
            self.end = (event.pos().x(), event.pos().y())
            self.update()






class Runthread(QtCore.QThread):
    updata_date = QtCore.pyqtSignal(list)

    def __init__(self, *args):
        super(Runthread, self).__init__()
        self.args = args[0]

        self.args.update({'bar_value':self.updata_date})

    def run(self):

        print(self.args)
        if self.args['hotkey'] == "run":
            print('进入hot')
            global EXIT  # 定义全局变量，这个可以在不同线程间共用。
            global RUN
            hotkey = Hotkey(self.args)
            hotkey.runs()
            print('over')

        if self.args['TYPES'] == 'FILES':
            all_path(self.args)

        if self.args['TYPES'] == 'PDF':
            all_path_img(self.args)

        if self.args['TYPES'] == 'IMG':
            content = get_file_str(self.args)
            self.updata_date.emit(['content',content])
        self.updata_date.emit(['ok', 1])



if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyleSheet(
        "QInputDialog QFrame{background: #393D49;color:#FFB800;}"
        "QInputDialog {background: #393D49;}"
        "QInputDialog QPushButton {padding: 2px;border-radius: 5px;background: #5FB878;}"
        "QInputDialog QPushButton:hover {background: darkCyan;}"
        "QMessageBox QFrame{background: #393D49;color:#FFB800;}"
        "QMessageBox {background: #393D49;}"
        "QMessageBox QPushButton {padding: 2px;border-radius: 5px;background: #5FB878;}"
    )
    MainWindow = QMainWindow()
    win = MyCalc()
    os.remove('mg.ico')
    sys.exit(app.exec_())