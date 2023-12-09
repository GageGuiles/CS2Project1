from PyQt6.QtWidgets import *
from gui import *


class BankingApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tabWidget.tabBar().hide()
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        self.tabWidget.setTabEnabled(4, False)

        self.user_data = {"user1": {"password": "password1", "balance": 0}}

        self.button_login.clicked.connect(lambda: self.log_in_feature())
        self.button_register.clicked.connect(lambda: self.register_screen())
        self.button_register2.clicked.connect(lambda: self.register())
        self.button_login2.clicked.connect(lambda: self.home_screen())
        self.button_checking.clicked.connect(lambda:self.checking_screen())
        self.button_savings.clicked.connect(lambda: self.savings_screen())
        self.button_home.clicked.connect(lambda: self.welcome_screen())
        self.button_home2.clicked.connect(lambda: self.welcome_screen())
        self.button_logout.clicked.connect(lambda: self.home_screen())
        self.button_logout2.clicked.connect(lambda: self.home_screen())
        self.button_logout3.clicked.connect(lambda: self.home_screen())

        self.button_ch_dep.clicked.connect(lambda: self.deposit_checking())
        self.button_ch_wit.clicked.connect(lambda: self.withdraw_checking())
        self.button_ch_balance.clicked.connect(lambda: self.balance_checking())
    def home_screen(self):
        self.tabWidget.setCurrentIndex(0)

    def register_screen(self):
        self.tabWidget.setTabEnabled(1, True)
        self.tabWidget.setCurrentIndex(1)
    def welcome_screen(self):
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget.setTabEnabled(2, True)

    def checking_screen(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget.setTabEnabled(3, True)

    def savings_screen(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget.setTabEnabled(4, True)

    def log_in_feature(self):
        self.username = self.text_username.toPlainText().strip()
        self.password = self.text_password.toPlainText().strip()

        if self.username in self.user_data and self.user_data[self.username]["password"] == self.password:
            self.label_status.setText("Log in Successful")
            self.text_username.clear()
            self.text_password.clear()
            self.tabWidget.setTabEnabled(2, True)
            self.tabWidget.setCurrentIndex(2)
        else:
            self.label_status.setText("Log in attempt failed")
            self.text_username.clear()
            self.text_password.clear()

    def register(self):
        self.tabWidget.setTabEnabled(1, True)
        self.tabWidget.setCurrentIndex(1)
        self.new_username = self.text_username2.toPlainText().strip()
        self.new_password = self.text_password2.toPlainText().strip()

        if self.new_username == '' or self.new_password == '':
            self.label_2.setText("Cannot be blank")
        elif self.new_username in self.user_data:
            self.label_2.setText("Username already exists")
        else:
            self.user_data[self.new_username] = {"password": self.new_password, "balance": 0}
            self.label_2.setText("Registration Successful")


    def deposit_checking(self):
        try:
            self.deposit_amount_ch = float(self.text_ch_amount.text().strip())
            self.user_data = self.user_data.get(self.username)

            if self.user_data and self.deposit_amount_ch > 0:
                self.user_data["balance"] += self.deposit_amount_ch
                self.label_ch_info.setText("Deposit Successful")
            else:
                self.label_ch_info.setText("Deposit Failed")

        except:
                self.label_ch_info.setText("Amount must be numeric")

    def withdraw_checking(self):
        try:
            self.withdraw_amount_ch = float(self.text_ch_amount.text().strip())
            self.user_data = self.user_data.get(self.username)

            if self.withdraw_amount_ch > self.user_data.get("balance", 0):
                self.label_ch_info.setText("Insufficient funds")
            elif self.withdraw_amount_ch <= 0:
                self.label_ch_info.setText("Withdraw Failed")
            else:
                self.user_data["balance"] -= self.withdraw_amount_ch
                self.label_ch_info.setText("Withdraw Successful")

        except:
                self.label_ch_info.setText("Amount must be numeric")

    def balance_checking(self):
        self.user_data = self.user_data.get(self.username)
        self.balance_ch = self.user_data.get("balance", 0)
        self.label_ch_balance.setText(f"${self.balance_ch:.2f}")




