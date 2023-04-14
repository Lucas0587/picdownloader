import os
from PyQt5.QtWidgets import (QLabel,QLineEdit,QPushButton,QWidget,QHBoxLayout,QVBoxLayout,QTextBrowser)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QIcon

path=os.getcwd()

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.LabelUrl=QLabel()
        self.LabelChoose=QLabel()
        self.LabelPath=QLabel()
        self.LabelName=QLabel()
        self.LabelTip=QTextBrowser()
        self.LineUrl=QLineEdit()
        self.LineName=QLineEdit()
        self.ButtonChoose=QPushButton("选择地址")
        self.ButtonStart=QPushButton("制作文件")
        self.ButtonClear=QPushButton("清空输入")
        self.ButtonDownload=QPushButton("下载图片")
        self.ButtonAll = QPushButton("一键制作")
        self.init()
        self.show()
    def init(self):
        def PagePadding():
            hbox1=QHBoxLayout()
            hbox1.addWidget(self.LabelChoose)
            hbox1.addWidget(self.ButtonChoose)
            hbox1.addWidget(self.LabelPath)
            hbox1.setSpacing(40)
            hbox2=QHBoxLayout()
            hbox2.addWidget(self.LabelName)
            hbox2.addWidget(self.LineName)
            hbox2.setSpacing(20)
            hbox3=QHBoxLayout()
            hbox3.addWidget(self.ButtonAll)
            hbox3.addWidget(self.ButtonDownload)
            hbox3.addWidget(self.ButtonStart)
            hbox3.addWidget(self.ButtonClear)
            hbox3.setSpacing(40)
            vbox=QVBoxLayout()
            vbox.addWidget(self.LabelUrl)
            vbox.setSpacing(20)
            vbox.addWidget(self.LineUrl)
            vbox.setSpacing(20)
            vbox.addLayout(hbox1)
            vbox.setSpacing(20)
            vbox.addLayout(hbox2)
            vbox.setSpacing(20)
            vbox.addLayout(hbox3)
            vbox.setSpacing(20)
            vbox.addWidget(self.LabelTip)
            vbox.setContentsMargins(40,40,30,40)
            self.setLayout(vbox)
        def StyleSet():
            self.LabelUrl.setAlignment(Qt.AlignLeft)
            self.LabelUrl.setText(
                "请输入pdf任意一页图片链接，例如：\n https://s3.ananas.chaoxing.com/sv-w8/doc/10/6a/cb/0bbc7da3c305b47148f3b87872069668/thumb/105.png")
            self.LabelUrl.setFont(QFont("宋体",12))
            self.LabelChoose.setText("请选择文件路径，默认为当前文件夹：")
            self.LabelChoose.setFont(QFont("宋体", 12))
            self.LabelPath.setText(path)
            self.LabelPath.setFont(QFont("宋体", 12))
            self.LabelName.setText("请输入文件名，默认名为当前时间")
            self.LabelName.setFont(QFont("宋体", 12))
            self.LabelTip.setStyleSheet("QLabel{background-color: #accbee;}")  # 设置label样式
            str = "\n - - - - - - - - - 注意事项 - - - - - - - - -\n" \
                  "\n" \
                  "  1、工作原理：利用requests库通过图片链接下载图片,利用fitz库制作pdf\n" \
                  "  2、由于利用爬虫下载图片，因此下载部分速度会较缓慢，请谅解\n" \
                  "  3、制作PDF文件需要重新设置文件路径\n" \
                  "  4、联系作者：1648633668（QQ）\n" \
                  "  5、此版本添加一键制作，使用时点击“一键制作”按钮即可，无需关注第三点内容\n" \
                  "\n" \
                  " - - - - - - - - - 工作区域 - - - - - - - - -\n"
            self.LabelTip.setText(str)
            self.LabelTip.setContentsMargins(20, 20, 20, 20)
            self.LabelTip.setFont(QFont("宋体", 13))

            self.LineUrl.setStyleSheet("QLineEdit{background-color: #fffefa;}")
            self.LineName.setStyleSheet("QLineEdit{background-color: #fffefa}")

            self.ButtonChoose.setStyleSheet("QPushButton{background-color:#9face6}")
            self.ButtonChoose.setFont(QFont("黑体", 14))
            self.ButtonChoose.setMinimumHeight(40)
            self.ButtonStart.setStyleSheet("QPushButton{background-color:#9face6}")
            self.ButtonStart.setFont(QFont("黑体", 14))
            self.ButtonStart.setMinimumHeight(40)
            self.ButtonClear.setStyleSheet("QPushButton{background-color:#9face6}")
            self.ButtonClear.setFont(QFont("黑体", 14))
            self.ButtonClear.setMinimumHeight(40)
            self.ButtonDownload.setStyleSheet("QPushButton{background-color:#9face6}")
            self.ButtonDownload.setFont(QFont("黑体", 14))
            self.ButtonDownload.setMinimumHeight(40)
            self.ButtonAll.setStyleSheet("QPushButton{background-color:#9face6}")
            self.ButtonAll.setFont(QFont("黑体", 14))
            self.ButtonAll.setMinimumHeight(40)
        self.setWindowTitle("学习通图片下载")
        self.resize(1280,720)
        self.setStyleSheet("QWidget{background-color: #e7f0fd;}")
        self.setWindowIcon(QIcon("pdfDownloader.ico"))
        StyleSet()
        PagePadding()