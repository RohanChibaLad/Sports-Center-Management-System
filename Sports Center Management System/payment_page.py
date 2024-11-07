from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from account_info import account


class PaymentPage(QWidget):
    def __init__(self, mainWindow, camefrom):
        super().__init__()
        # Have a variable for the main window object, so we can change page widget
        self.mainWindow = mainWindow
        # Set the page we previously came from
        self.came_from = camefrom

        # Page layout
        layout = QVBoxLayout()
        # Align everything to center
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Set this page (which is in fact a widget) layout
        self.setLayout(layout)

        # Page label
        label = QLabel("Enter Payment Details", self)
        label.setStyleSheet("font: bold 18px;")
        label.setContentsMargins(0, 0, 0, 20)
        # Specifically align the label to center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Add the label to the widget
        layout.addWidget(label)

        # textbox for card number
        card_number_layout = QHBoxLayout()
        card_number_label = QLabel("Enter Card Number: ", self)
        card_number_label.setFixedSize(150, 30)
        self.card_number_textbox = QLineEdit(str(account.card_number))
        self.card_number_textbox.setObjectName("card_number_textbox")
        self.card_number_textbox.setFixedSize(150, 30)
        self.card_number_textbox.setPlaceholderText("Enter Card Number")
        self.card_number_textbox.setStyleSheet("border-radius: 10px;"
                                               "color: black;")
        card_number_layout.addWidget(card_number_label)
        card_number_layout.addWidget(self.card_number_textbox)

        self.card_number_invalid_error_label = QLabel("Please enter a valid Card Number. E.g. 0123456789123456", self)
        self.card_number_invalid_error_label.setObjectName("invalid_card_number")
        self.card_number_invalid_error_label.setStyleSheet("color: red;")
        self.card_number_invalid_error_label.hide()

        # textbox for name on card
        name_on_card_layout = QHBoxLayout()
        name_on_card_label = QLabel("Enter Name on Card: ", self)
        name_on_card_label.setFixedSize(150, 30)
        self.name_on_card_textbox = QLineEdit(account.name_on_card)
        self.name_on_card_textbox.setObjectName("name_on_card_textbox")
        self.name_on_card_textbox.setFixedSize(150, 30)
        self.name_on_card_textbox.setPlaceholderText("Enter Name on Card")
        self.name_on_card_textbox.setStyleSheet("border-radius: 10px;"
                                                "color: black;")
        name_on_card_layout.addWidget(name_on_card_label)
        name_on_card_layout.addWidget(self.name_on_card_textbox)

        self.name_on_card_invalid_error_label = QLabel("Please enter a valid name on card. E.g. John Smith", self)
        self.name_on_card_invalid_error_label.setObjectName("invalid_name_on_card")
        self.name_on_card_invalid_error_label.setStyleSheet("color: red;")
        self.name_on_card_invalid_error_label.hide()

        # textbox for expiry date
        expiry_date_layout = QHBoxLayout()
        expiry_date_label = QLabel("Enter Expiry Date: ", self)
        expiry_date_label.setFixedSize(150, 30)
        self.expiry_date_textbox = QLineEdit(account.expiry_date)
        self.expiry_date_textbox.setObjectName("expiry_date_textbox")
        self.expiry_date_textbox.setFixedSize(150, 30)
        self.expiry_date_textbox.setPlaceholderText("Enter Expiry Date")
        self.expiry_date_textbox.setStyleSheet("border-radius: 10px;"
                                               "color: black;")
        expiry_date_layout.addWidget(expiry_date_label)
        expiry_date_layout.addWidget(self.expiry_date_textbox)

        # error message for an inavlid expiry date
        self.expiry_date_invalid_error_label = QLabel("Please enter a valid Expiry Date. E.g. 07/25", self)
        self.expiry_date_invalid_error_label.setObjectName("invalid_expiry_date")
        self.expiry_date_invalid_error_label.setStyleSheet("color: red;")
        self.expiry_date_invalid_error_label.hide()

        # textbox for cvv
        cvv_layout = QHBoxLayout()
        cvv_label = QLabel("Enter CVV: ", self)
        cvv_label.setFixedSize(150, 30)
        self.cvv_textbox = QLineEdit(str(account.cvv))
        self.cvv_textbox.setObjectName("cvv_textbox")
        self.cvv_textbox.setFixedSize(150, 30)
        self.cvv_textbox.setPlaceholderText("Enter CVV")
        self.cvv_textbox.setStyleSheet("border-radius: 10px;"
                                       "color: black;")
        cvv_layout.addWidget(cvv_label)
        cvv_layout.addWidget(self.cvv_textbox)

        self.cvv_invalid_error_label = QLabel("Please enter a valid CVV. E.g. 123", self)
        self.cvv_invalid_error_label.setObjectName("invalid_cvv")
        self.cvv_invalid_error_label.setStyleSheet("color: red;")
        self.cvv_invalid_error_label.hide()

        button_layout = QHBoxLayout()

        # button that adds the membership
        add_membership_button = QPushButton("Add Payment Details")
        add_membership_button.setObjectName("payment_button")
        add_membership_button.setFixedSize(170, 50)
        add_membership_button.setCheckable(True)
        add_membership_button.setStyleSheet("background-color: #220C10;"
                                            "border-radius: 10px;"
                                            "color: white;"
                                            "font-size: 16px;"
                                            "margin: 20px 0px 0px 0px;")
        add_membership_button.clicked.connect(self.add_membership_button_click)

        # button that goes back
        back_button = QPushButton("Back")
        back_button.setFixedSize(170, 50)
        back_button.setCheckable(True)
        back_button.setStyleSheet("background-color: #220C10;"
                                  "border-radius: 10px;"
                                  "color: white;"
                                  "font-size: 16px;"
                                  "margin: 20px 0px 0px 0px;")
        back_button.clicked.connect(self.back_button_click)

        button_layout.addWidget(add_membership_button)
        button_layout.addWidget(back_button)

        layout.addLayout(card_number_layout)
        layout.addWidget(self.card_number_invalid_error_label)
        layout.addLayout(name_on_card_layout)
        layout.addWidget(self.name_on_card_invalid_error_label)
        layout.addLayout(expiry_date_layout)
        layout.addWidget(self.expiry_date_invalid_error_label)
        layout.addLayout(cvv_layout)
        layout.addWidget(self.cvv_invalid_error_label)
        layout.addLayout(button_layout)

    # function that sets the main window to the home page
    def add_membership_button_click(self):
        account.card_number = self.card_number_textbox.text()
        account.name_on_card = self.name_on_card_textbox.text()
        account.expiry_date = self.expiry_date_textbox.text()
        account.cvv = self.cvv_textbox.text()
        if self.all_payment_test():
            card_details = self.mainWindow.database.getData("SELECT * FROM card_information WHERE user_id = (?)",
                                                            str(account.user_id))
            if len(card_details) == 0:
                self.mainWindow.database.exeStatement("INSERT INTO card_information (user_id, card_number,"
                                                      "name_on_card, expiry_date, cvv)"
                                                      "VALUES (?, ?, ?, ?, ?)", str(account.user_id),
                                                      str(account.card_number), account.name_on_card,
                                                      account.expiry_date, str(account.cvv))

            if len(account.sql_statements) != 0:
                for statement in account.sql_statements:
                    self.mainWindow.database.exeStatement("INSERT INTO sessions (facility, activity, booked_time, "
                                                          "booker, team_session) VALUES (?, ?, ?, ?, ?)", statement[1],
                                                          statement[2], str(statement[0]), str(account.user_id),
                                                          statement[4])
                # Clear the sql statements list after the current sessions have been inserted
                account.sql_statements = []
                self.mainWindow.changePage("Home", "Payment")
            else:
                self.mainWindow.changePage("Check Account", "Payment")

    def back_button_click(self):
        self.mainWindow.changePage(self.came_from, "Payment")

    def all_payment_test(self):
        success = True
        if not self.test_card_number():
            self.card_number_invalid_error_label.show()
            success = False
        else:
            self.card_number_invalid_error_label.hide()

        if not self.test_name_on_card():
            self.name_on_card_invalid_error_label.show()
            success = False
        else:
            self.name_on_card_invalid_error_label.hide()

        if not self.test_expiry_date():
            self.expiry_date_invalid_error_label.show()
            success = False
        else:
            self.expiry_date_invalid_error_label.hide()

        if not self.test_cvv():
            self.cvv_invalid_error_label.show()
            success = False
        else:
            self.cvv_invalid_error_label.hide()

        return success

    def test_card_number(self):
        if len(account.card_number) == 16:
            if account.card_number.isnumeric():
                return True
        return False

    # function to make sure there are two words on the name on card
    def test_name_on_card(self):
        # set variables to false
        letter_before_space = False
        space = False
        letter_after_space = False
        for letter in account.name_on_card:
            # if there is not a letter before the space so far check there is
            # if there is then set this to true
            if not letter_before_space:
                if letter != " ":
                    letter_before_space = True
            # if there is a letter before the space check if there is a space
            # if there has been a space then check there is a letter after the space
            else:
                if space:
                    if letter != " ":
                        letter_after_space = True
                if letter == " ":
                    space = True

        self.name_on_card_invalid_error_label.show()
        return letter_after_space

    def test_expiry_date(self):
        num1 = ""
        num2 = ""
        count = 0
        valid = True
        if len(account.expiry_date) == 5:
            # for each value entered
            for num in account.expiry_date:
                # check if the first digit is a 0 or a 1
                if count == 0:
                    num1 = num
                    if num != "0" and num != "1":
                        valid = False
                # check the second digit is one of the months
                if count == 1:
                    if num1 == "1":
                        if num != "0" and num != "1" and num != "2":
                            valid = False
                    else:
                        if not num.isnumeric():
                            valid = False
                # check the third value is a backslash
                if count == 2:
                    if num != "/":
                        valid = False
                # check the fourth value is a 2 or 3 for the start of the year
                if count == 3:
                    num2 = num
                    if num != "2" and num != "3":
                        valid = False
                # check the last value entered is a valid year
                if count == 4:
                    if num2 == "2":
                        if num == "0" or num == "1" or num == "2":
                            valid = False
                    if not num.isnumeric():
                        valid = False
                count += 1
            return valid

    def test_cvv(self):
        if len(account.cvv) == 3:
            if account.cvv.isnumeric():
                return True
        return False
