from PySide6 import QtWidgets, QtCore, QtWebEngineWidgets


class Window(QtWidgets.QWidget):

    myURL="http://127.0.0.1:8000"

    def __init__(self) -> None:
        super().__init__()

        self.main_layout = QtWidgets.QGridLayout(self)

        self.spin = QtWidgets.QSpinBox()
        self.spin.setValue(30)
        self.spin.setRange(7, 1200)

        self.btn_refresh = QtWidgets.QPushButton("Refresh")
        self.btn_refresh.clicked.connect(self.refresh)

        #self.spin.setStyleSheet("color:white;")
        self.btn_refresh.setStyleSheet("coloe:white;")
        self.btn_refresh.setFlat(True)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.load(QtCore.QUrl(self.myURL))

        self.setWindowTitle("Dashboard Currencies")

        self.main_layout.addWidget(self.spin, 0, 0, 1, 1)
        self.main_layout.addWidget(self.btn_refresh, 0, 1, 1, 1)

        self.main_layout.addWidget(self.view, 1, 0, 1, 2)


    def refresh(self):
        days=self.spin.value()
        self.view.load(QtCore.QUrl(f"{self.myURL}/days_range={days}&currencies=USD"))


app = QtWidgets.QApplication([])
win = Window()
win.show()
app.exec_()
