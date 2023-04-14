import os,fitz,requests,time,shutil,filetype,sys
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QApplication
from IndexUI import Windows

class method(Windows):
    def __init__(self):
        super(method, self).__init__()
        self.LineName.setText(time.strftime("%Y-%m-%d %H-%M", time.localtime()))
        self.ButtonChoose.clicked.connect(self.ChoosePath)
        self.ButtonStart.clicked.connect(self.MakePDF)
        self.ButtonClear.clicked.connect(self.ClearContent)
        self.ButtonDownload.clicked.connect(self.DownloadImage)
        self.ButtonAll.clicked.connect(self.OneClickMade)

    '''def execute(self,text):
        self.work = thread()
        self.work.start()
        self.work.trigger.connect(self.display)

    def display(self,str):
        self.LabelTip.append(str)'''

    def ChoosePath(self):
        path = QFileDialog.getExistingDirectory()
        self.LabelPath.setText(path)

    def DownloadImage(self):
        def download(ImageUrl,FilePath,path):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                              " Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44",
            }
            r = requests.get(ImageUrl, headers=headers)
            with open(FilePath, "wb") as f:
                f.write(r.content)
            shutil.move(FilePath, path)
        #初始化检查
        FileName,FilePath=self.InitialPage()
        if FilePath=="Filealreadyexists":
            return 0
        path = FilePath + "\\" + FileName
        if not os.path.exists(path):
            os.mkdir(path)
        #检查图片地址
        ImageUrl=self.LineUrl.text()
        if ImageUrl=="":
            QMessageBox.information(self, "提示", "您未输入图片地址")
            return 0
        #检查图片是否存在
        try:
            RequestCode=requests.get(ImageUrl).status_code
            if RequestCode!=200:
                QMessageBox.information(self, "提示", "爬虫状态码为{}".format(RequestCode))
                return 0
        except:
            QMessageBox.information(self, "提示", "爬虫出问题了，请联系作者")
            return 0
        #预处理图片地址
        PreImageUrl=""
        list=ImageUrl.split("/")[:-1]
        for i in range(len(list)):
            PreImageUrl+=(list[i]+"/")
        #下载图片
        NowNum=1
        while requests.get(PreImageUrl + str(NowNum) + '.png').status_code == 200:
            download(PreImageUrl + str(NowNum) + '.png', str(NowNum) + '.png', path)
            self.LabelTip.append("  正在下载第{}张图片，请耐心等待".format(NowNum))
            NowNum += 1
            QApplication.processEvents()
            time.sleep(0.5)
        self.LabelTip.append("  图片下载完成")

    def InitialPage(self):
        #检查文件名
        FileName=self.LineName.text()
        if FileName=="":
            FileName=time.strftime("%Y-%m-%d %H-%M", time.localtime())
        #检查文件地址
        FilePath=self.LabelPath.text()
        if FilePath=="":
            FilePath=os.getcwd()
        if os.path.exists(os.path.join(FilePath,FileName)) or os.path.exists(os.path.join(FilePath,"{}.pdf".format(FileName))):
            QMessageBox.warning(self,"警告","已经有同名文件或者文件夹")
            return "Filealreadyexists","Filealreadyexists"
        return FileName,FilePath

    def MakePDF(self):
        #初始化
        FileName, FilePath = self.InitialPage()
        if FilePath=="Filealreadyexists":
            return 0
        FileList=os.listdir(FilePath)
        if not os.path.exists(os.path.join(FilePath,"1.png")):
            QMessageBox.information(self, "提示", "请重新选择地址")
            return 0
        os.chdir(FilePath)
        #写文件
        doc = fitz.open()
        for i in range(len(FileList)):
            if filetype.guess(os.path.join(FilePath, str(i+1)+".png")) != None:
                imgdoc = fitz.open(str(i+1)+".png")
                pdfbytes = imgdoc.convertToPDF()
                imgpdf = fitz.open(str(i+1)+".png".replace(".png",".pdf"), pdfbytes)
                doc.insertPDF(imgpdf)
                self.LabelTip.append("  目前进度{}/{}，请耐心等待".format(i+1,len(FileList)))
                QApplication.processEvents()
                time.sleep(0.1)
            else:
                self.LabelTip.append("  第{}张图片有误，无法插入PDF中".format(i+1))
                QApplication.processEvents()
                time.sleep(0.1)
        doc.save(FileName + '.pdf')
        doc.close()
        self.LabelTip.append("  PDF制作完成")
        #删除多余的图片
        choice = QMessageBox.question(self, "Question", "是否删除过程中下载的图片", QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            for i in range(1, len(FileList)+1):
                try:
                    os.remove(os.path.join(FilePath,str(i)+'.png'))
                except:
                    QMessageBox.information(self, "提示", "删除照片“ {}.png ”有误".format(i))
            self.LabelTip.append("  删除照片成功")
        choice = QMessageBox.question(self, "Question", "是否移动文件到指定文件夹", QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            shutil.move(os.path.join(FilePath,"{}.pdf".format(FileName)),os.path.join(FilePath,".."))
            self.LabelTip.append("  PDF文件位于{}".format(os.path.abspath(os.path.join(FilePath,".."))))
        else:
            self.LabelTip.append("  PDF文件位于{}".format(FilePath))

    def ClearContent(self):
        self.LabelPath.setText(os.getcwd())
        self.LineName.setText("")
        self.LineUrl.setText("")

    def OneClickMade(self):
        a=self.DownloadImage()
        if a==0:
            return 0
        picpath=os.path.join(self.LabelPath.text(),self.LineName.text())
        self.LabelPath.setText(picpath)
        QApplication.processEvents()
        self.MakePDF()
        self.LabelPath.setText(os.path.abspath(os.path.join(picpath,"..")))
        QApplication.processEvents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui=method()
    ui.show()
    sys.exit(app.exec_())