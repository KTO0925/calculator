#ch 4.4.1 main.py
import sys   #시스템 제어 관련 모듈

#위젯이란: GUI 프로그램에서 구성요소를 뜻하는 용어
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton, QVBoxLayout,
                             QMessageBox,QPlainTextEdit,QHBoxLayout)

from PyQt5.QtGui import QIcon

class Calculator(QWidget) : #계산기 유형을 직접 정의한다. QWidget에 기반을 둔다.

    def __init__(self):
        super().__init__()   #뭔가에 기반을 둘 경우 써줘야 하는 코드
        self.initUI()

    def initUI(self): #생성할떄 초기화

        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message',self)
        #이벤트 핸들링: 클릭했을 때 , 뭐를 할거다! 라고 정의하는 것
        self.btn1.clicked.connect(self.activateMessage)

        self.btn2 = QPushButton('Clear',self)
        self.btn2.clicked.connect(self.clearMessage)

        hbox = QHBoxLayout() #수평 박스 레이아웃을 추가하기
        hbox.addStretch(1)
        hbox.addWidget(self.btn1) #버튼 1 배치
        hbox.addWidget(self.btn2) #버튼 2 배치

        vbox = QVBoxLayout() #수직 박스 레이아웃 추가하기
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox) #설정 적용

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def activateMessage(self):
        #QMessageBox.information(self,"Information","Button clicked!")
        self.te1.appendPlainText("Hello,PyQt App!")

    def clearMessage(self):
        self.te1.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv) #Qt 프로그램 실행코드
    view = Calculator() #내가 만든 계산기 GUI 생성 코드
    sys.exit(app.exec_()) # 계산기 종료 시 시스템 종료 명령