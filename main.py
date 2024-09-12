#ch 4.2.1 main.py
import sys   #시스템 제어 관련 모듈

#위젯이란: GUI 프로그램에서 구성요소를 뜻하는 용어
from PyQt5.QtWidgets import QApplication,QWidget #애플리케이션 핸들러와 빈 GUI 위젯

class Calculator(QWidget) : #계산기 유형을 직접 정의한다. QWidget에 기반을 둔다.

    def __init__(self):
        super().__init__()   #뭔가에 기반을 둘 경우 써줘야 하는 코드
        self.initUI()

    def initUI(self): #생성할떄 초기화
        self.setWindowTitle('Calculator')
        self.resize(256,256)
        self.show() #열기

#클래스를 정의 했으니, 여기에서 실행하겠다.. 라는 실행부
# if __name__ == '__main__' : 이 모듈이 직접 실행되는 경우
if __name__ == '__main__':
    app = QApplication(sys.argv) #Qt 프로그램 실행코드
    view = Calculator() #내가 만든 계산기 GUI 생성 코드
    sys.exit(app.exec_()) # 계산기 종료 시 시스템 종료 명령