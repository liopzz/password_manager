from PyQt5 import QtWidgets,QtGui,QtCore
class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #топбар
        h_topbar = QtWidgets.QHBoxLayout()
        topbar = QtWidgets.QFrame()
        self.btn_add_password = QtWidgets.QPushButton('Добавить пароль')
        h_topbar.addStretch(6)
        h_topbar.addWidget(self.btn_add_password,stretch = 2)
        topbar.setLayout(h_topbar)

        self.list_pwd = QtWidgets.QListWidget()
        v_main = QtWidgets.QVBoxLayout()
        v_main.addWidget(topbar)
        v_main.addWidget(self.list_pwd)

class AddPsswordWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        v_main =QtWidgets.QVBoxLayout()
        lbl_service = QtWidgets.QLabel('СЕРВИС')
        lbl_login = QtWidgets.QLabel('ЛОГИН')
        lbl_password = QtWidgets.QLabel('ПАРОЛЬ')

        self.service_edit = QtWidgets.QLineEdit()
        self.password_edit = QtWidgets.QLineEdit()
        self.login_edit = QtWidgets.QLineEdit()
        self.password_edit.setEchoMode(...)

 
if __name__== "__main__":
    app = QtWidgets.QApplication([])
    mw = MainWindow()
    mw.show()
    app.exec()   
    