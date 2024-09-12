#ch 4.2.1 main.py
import sys   #시스템 제어 관련 모듈

#위젯이란: GUI 프로그램에서 구성요소를 뜻하는 용어
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton, QVBoxLayout,
                             QMessageBox)

from PyQt5.QtGui import QIcon

class Calculator(QWidget) : #계산기 유형을 직접 정의한다. QWidget에 기반을 둔다.

    def __init__(self):
        super().__init__()   #뭔가에 기반을 둘 경우 써줘야 하는 코드
        self.initUI()

    def initUI(self): #생성할떄 초기화
        self.btn1 = QPushButton('Message',self)

        #이벤트 핸들링: 클릭했을 때 , 뭐를 할거다! 라고 정의하는 것
        self.btn1.clicked.connect(self.activateMessage)

        #레이아웃 설정
        vbox=QVBoxLayout() #수직
        vbox.addStretch(1) #여백을 의미
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)

        self.setLayout(vbox) #설정 적용

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def activateMessage(self):
        QMessageBox.information(self,"Information","Button clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv) #Qt 프로그램 실행코드
    view = Calculator() #내가 만든 계산기 GUI 생성 코드
    sys.exit(app.exec_()) # 계산기 종료 시 시스템 종료 명령