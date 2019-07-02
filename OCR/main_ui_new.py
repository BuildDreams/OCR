# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui_new.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import base64

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QAction, QMenu, QSystemTrayIcon, QInputDialog
from pics import mgs
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



class Ui_Dialog(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(971, 785)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setStatusTip("")
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.horizontalLayout_radio = QtWidgets.QHBoxLayout()

        self.radio_btn = QtWidgets.QRadioButton(self.tab)
        self.radio_btn.setObjectName("progressBar")
        self.radio_btn_gen = QtWidgets.QRadioButton(self.tab)
        self.radio_btn_gen.setObjectName("progressBar")
        self.horizontalLayout_radio.addWidget(self.radio_btn)
        self.horizontalLayout_radio.addWidget(self.radio_btn_gen)

        self.tips = QtWidgets.QLabel(self.tab)
        self.tips.setObjectName("tips")
        self.tips.setText("高精度每天只有500次")
        self.verticalLayout_5.addWidget(self.tips)

        self.radio_btn_gen.setChecked(True)
        self.verticalLayout_5.addLayout(self.horizontalLayout_radio)

        self.verticalLayout_5.addWidget(self.progressBar)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.extract_id_btn = QtWidgets.QPushButton(self.tab)
        self.extract_id_btn.setObjectName("btn")
        self.verticalLayout_3.addWidget(self.extract_id_btn)
        self.extract_img_btn = QtWidgets.QPushButton(self.tab)
        self.extract_img_btn.setObjectName("btn")
        self.verticalLayout_3.addWidget(self.extract_img_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 80)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setSizeIncrement(QtCore.QSize(0, 50))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(79)
        self.label.setOpenExternalLinks(False)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.file_id_long_text = QtWidgets.QLineEdit(self.tab)
        self.file_id_long_text.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.file_id_long_text.sizePolicy().hasHeightForWidth())
        self.file_id_long_text.setSizePolicy(sizePolicy)
        self.file_id_long_text.setMinimumSize(QtCore.QSize(100, 40))
        self.file_id_long_text.setReadOnly(False)
        self.file_id_long_text.setPlaceholderText("")
        self.file_id_long_text.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.file_id_long_text.setClearButtonEnabled(False)
        self.file_id_long_text.setObjectName("text")
        self.verticalLayout_4.addWidget(self.file_id_long_text)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setLineWidth(10)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(3)
        self.label_2.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label_2)
        self.img_id_long_text = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_id_long_text.sizePolicy().hasHeightForWidth())
        self.img_id_long_text.setSizePolicy(sizePolicy)
        self.img_id_long_text.setMinimumSize(QtCore.QSize(0, 40))
        self.img_id_long_text.setMaximumSize(QtCore.QSize(16777215, 8))
        self.img_id_long_text.setFrame(True)
        self.img_id_long_text.setObjectName("text")
        self.verticalLayout_4.addWidget(self.img_id_long_text)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.text_up = QtWidgets.QTextBrowser(self.tab)
        self.text_up.setObjectName("text")
        self.horizontalLayout_4.addWidget(self.text_up)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.starts = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(150)
        sizePolicy.setHeightForWidth(self.starts.sizePolicy().hasHeightForWidth())
        self.starts.setSizePolicy(sizePolicy)
        self.starts.setMaximumSize(QtCore.QSize(150, 50))
        self.starts.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.starts.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.starts.setAutoRepeat(False)
        self.starts.setAutoExclusive(False)
        self.starts.setObjectName("btn")
        self.horizontalLayout_3.addWidget(self.starts)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.extract_txt_btn = QtWidgets.QPushButton(self.tab)
        self.extract_txt_btn.setObjectName("btn")
        self.verticalLayout.addWidget(self.extract_txt_btn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_down = QtWidgets.QTextBrowser(self.tab)
        self.text_down.setObjectName("text_down")
        self.verticalLayout_2.addWidget(self.text_down)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab, "主页")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textBrowserlog = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowserlog.setObjectName("logs")
        self.verticalLayout_7.addWidget(self.textBrowserlog)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_6.addWidget(self.tabWidget)

        self.tip_input = QInputDialog()
        self.tip_input.setObjectName("tips_input")
        self.show()
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "截图"))
        self.extract_id_btn.setText(_translate("Dialog", "文件编码提取"))
        self.extract_img_btn.setText(_translate("Dialog", "PDF图片提取"))
        self.label.setText(_translate("Dialog", "提取文件编码长度"))
        self.label_2.setText(_translate("Dialog", "提取文件编码长度"))
        self.starts.setText(_translate("Dialog", "STAR"))
        self.extract_txt_btn.setText(_translate("Dialog", "图文转换"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "更新日志"))

        self.extract_txt_btn.setText(_translate("Dialog", "截图(F2)"))
        self.radio_btn.setText(_translate("Dialog", "普通精度"))
        self.radio_btn_gen.setText(_translate("Dialog", "高精度"))

        self.text_down.hide()

        self.progressBar.hide()
        self.addSystemTray()
        Dialog.setStyleSheet(
            "#btn{background-color:#009688;border-radius:10px;color:white;min-height: 30px;min-width: 100px;border:none;}"
            "#btn:hover{background-color:#5FB878;}"
            "#label{color:#FFB800;}"
            "#btn:pressed{background-color:red;}"
            "#Dialog{background-color:#393D49;}"
            "#text{background-color:#6E6E6E;border:none;border-radius:10px;font-size:15pt;color:#7CFC00;}"
            "#text:hover{border:2px solid #5FB878;}"
            "#text_down{background-color:#6E6E6E;border:1px solid #EAEAEA;border-radius:10px;font-size:15pt;}"
            "#progressBar{border-radius:10px;color:red;text-align:center;}"
            "#progressBar::chunk{background-color:#00BFFF;border-radius:10px;}"
            "#tips{color:#FFB800;font-size:15pt;}"
            "#tab,#tab_2{background-color:#393D49;}"
            "#logs{background-color:#393D49;border:none;}"
            "QTabBar {background-color: #009688;;outline: solid 2px;min-width: 20px;}"
            "QTabBar::tab {min-width: 20px;min-height: 100px;text-align:center;background-color: #009688;;}"
            "QTabBar::tab:selected {background-color: #5FB878;color: green;}"
            "QTabBar::tab:hover:!selected {color: red;background-color: #009688;}"
            "#tips_input{background-color:#393D49;}")

        self.setWindowOpacity(0.9)
        self.tips.setAlignment(Qt.AlignCenter)
        self.textBrowserlog.setHtml('<font color="#FF5722">'
                                    '<h2>更新日志v0.2.3</h2>'
                                    '<ul>'
                                    '<li>取消原始显示方式改为弹框提示。</li>'
                                    '<li>弹框内容可不用复制，直接粘贴即可。</li>'
                                    '<li>按ECS可关闭弹框</li>'
                                    '<li>增加程序启动后最小化至托盘运行。</li>'
                                    '</ul>'
                                    '<h3>程序最小化到托盘步骤</h3><ul>'
                                    '<font color="green"><li>程序启动后点击最小化按钮即可</li></font>'
                                    '</ul>'
                                    '<font color="yellow"><h3>about</h3>'
                                    '<ul>关于程序启动后，同目录下会有1.png的图片说明'
                                    '<li>图片可自行删除,此图片为每次截图生成的文件,每次截图会重复覆盖写入，不用担心删除程序异常。</li></ul></font>'
                                    '<h2>更新日志v0.2.2</h2>'
                                    '<ul>'
                                    '<li>增加F2一键截图。</li>'
                                    "<li>增加截图时鼠标左键双击取消截图。"
                                    "<li>修复一些Bug。</li>"
                                    "</ul>"
                                    "</font>")


    def addSystemTray(self):
        minimizeAction = QAction("&最小化", self, triggered=self.hide)
        maximizeAction = QAction("&最大化", self, triggered=self.showMaximized)
        restoreAction = QAction("&还原", self, triggered=self.showNormal)
        quitAction = QAction("&退出", self,triggered=QApplication.instance().quit)
        # quitAction = QAction(u'退出 ', self, triggered=self.close)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(minimizeAction)
        self.trayIconMenu.addAction(maximizeAction)
        self.trayIconMenu.addAction(restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("mg.ico"))
        self.setWindowIcon(QIcon("mg.ico"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()

    # def hideEvent(self, QHideEvent):
    #     print("shows")
    #     """
    #     重写closeEvent方法，实现dialog窗体关闭时执行一些代码
    #     :param event: close()触发的事件
    #     :return: None
    #     """
    #     self.hide()  # 忽略关闭事件

    # def closeEvent(self, event):
    #     print("重写关闭")
    #     event.ignore()  # 忽略关闭事件
    #     self.hide()  # 隐藏窗体



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    win = Ui_Dialog()

    sys.exit(app.exec_())