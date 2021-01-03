# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PIL import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QPushButton, QFileDialog, QLabel
from yolo import YOLO, detect_video
from yolo import YOLO

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def echo(self, value):
        '''显示对话框返回值'''
        print(value)
        QMessageBox.information(self, "返回值", "得到：{}\n\ntype: {}".format(value, type(value)),
                                QMessageBox.Yes | QMessageBox.No)
        # pass

    def changePic(self,str):#改变图片
        print(str)
        self.picture_label.setPixmap(QPixmap(str))

    def helpme(self, event):  # 帮助我们按钮
        reply = QMessageBox.about(self,
                                        "使用帮助",
                                        "♥点击左侧菜单栏的实时检测和图片检测来完成口罩检测。\n"
                                        "♥或直接联系开发团队进行人工帮助，详见联系我们♥♥")

    def aboutus(self, event): # 关于我们按钮
        reply = QMessageBox.about(self,
                                        "番茄蛋花汤@",
                                        "是番茄蛋花汤呀❤\n"
                                        "我们是充满爱的小家庭❤\n"
                                        "这是我们的工作人员名单❤\n"
                                        "可以联系我们来解决您的问题❤\n"
                                        "⭐余闽喆\n"
                                        "⭐邓皓文\n"
                                        "⭐傅芷琴\n"
                                        "⭐常虹\n"
                                        "⭐杨思恒\n"
                                        "⭐多家赫\n"
                                        "⭐感谢您的使用\n"
                                        "\n")

    def find_picture(self, event):  # 文件：单文件
        file_, filetype = QFileDialog.getOpenFileName(self,
                                                      "选取文件",
                                                      "C:/",
                                                      "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(file_)
        img = file_
        image = Image.open(img)
        yolo = YOLO()
        image = yolo.detect_image(image)
        image.save('test/save.jpg', quality=95, subsampling=0)
        img2 = 'test/save.jpg'
        image2 = Image.open(img2)
        print(image2.format)
        self.changePic(img2)

    def find_video(self):
        yolo = YOLO()
        detect_video(yolo, 0)



    def init_ui(self):
        self.setFixedSize(960, 600)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle("番茄蛋花汤口罩检测系统")

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 11, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.left_close = QtWidgets.QPushButton(" ")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton(" ")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton(" ")  # 最小化按钮
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_label_1 = QtWidgets.QPushButton("视频检测")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("图片检测")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "实时检测")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.find_video)
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "图片检测")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(self.find_picture)
        self.left_button_7 = QPushButton(qtawesome.icon('fa.comment', color='white'), "使用帮助")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.helpme)
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "联系我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(self.aboutus)
        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(./images/back.jpg);}")

        self.left_widget.setStyleSheet('''
              QPushButton{border:none;color:white;}
              QPushButton#left_label{
                  border:none;
                  border-bottom:1px solid white;
                  font-size:18px;
                  font-weight:700;
                  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
              }
              QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
          ''')


        self.right_recommend_label = QtWidgets.QLabel("图片检测系统")
        self.right_recommend_label.setObjectName('right_lable')
        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)


        self.picture_label=QtWidgets.QLabel();
        self.picture_label.setScaledContents(1)
        self.picture_label.setPixmap(QPixmap("./images/win.jpg"))

        '''
        s = './images/mask1.jpg'
        self.changePic(s)
        '''
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("添加图片")  # 设置按钮文本
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.clicked.connect(self.find_picture)

        self.right_recommend_layout.addWidget(self.recommend_button_1, 1, 0)
        self.right_recommend_layout.addWidget(self.picture_label,0,0)
        self.right_layout.addWidget(self.right_recommend_label, 0, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        self.right_widget.setStyleSheet('''
                        QWidget#right_widget{
                            color:#232C51;
                            background:white;
                            border-top:1px solid darkGray;
                            border-bottom:1px solid darkGray;
                            border-right:1px solid darkGray;
                            border-top-right-radius:10px;
                            border-top-left-radius:10px;
                            border-bottom-right-radius:10px;
                            border-bottom-left-radius:10px;
                        }
                        QLabel#right_lable{
                            border:none;
                            font-size:16px;
                            font-weight:700;
                            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                        }
                    ''')


        '''
        self.setWindowOpacity(1)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        '''
        self.setWindowOpacity(1)  # 设置窗口透明度








def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()