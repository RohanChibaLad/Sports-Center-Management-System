from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from account_info import account


class CreateAccountPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        # Have a variable for the main window object, so we can change page widget
        self.mainWindow = mainWindow

        # Page layout
        self.layout = QVBoxLayout()
        # Align everything to center
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Set this page (which is in fact a widget) layout
        self.setLayout(self.layout)

        # Page label
        label = QLabel("Create an Account", self)
        label.setStyleSheet("font: bold 18px;")
        label.setContentsMargins(0, 0, 0, 20)
        # Specifically align the label to center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Add the label to the widget
        self.layout.addWidget(label)

        # text box created for user to enter their firstname
        self.firstname_textbox = QLineEdit(account.firstname, self)
        self.firstname_textbox.setObjectName("firstname_textbox")
        self.firstname_textbox.setFixedSize(250, 30)
        self.firstname_textbox.setPlaceholderText("Enter Firstname")
        self.firstname_textbox.setStyleSheet("border-radius: 10px;"
                                             "color: black;")
        self.layout.addWidget(self.firstname_textbox)

        # error message to say that the user has not entered a firstname
        self.firstname_null_error_label = QLabel("Please enter Firstname", self)
        self.firstname_null_error_label.setObjectName("firstname_null_label")
        self.firstname_null_error_label.setStyleSheet("color: red;")
        self.firstname_null_error_label.hide()
        self.layout.addWidget(self.firstname_null_error_label)

        # text box created for user to enter their lastname
        self.lastname_textbox = QLineEdit(account.lastname, self)
        self.lastname_textbox.setObjectName("lastname_textbox")
        self.lastname_textbox.setFixedSize(250, 30)
        self.lastname_textbox.setPlaceholderText("Enter Lastname")
        self.lastname_textbox.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.layout.addWidget(self.lastname_textbox)

        # error message to say that the user has not entered a lastname
        self.lastname_null_error_label = QLabel("Please enter Lastname", self)
        self.lastname_null_error_label.setObjectName("lastname_null_label")
        self.lastname_null_error_label.setStyleSheet("color: red;")
        self.lastname_null_error_label.hide()
        self.layout.addWidget(self.lastname_null_error_label)

        # text box created for user to enter their desired username
        self.email_textbox = QLineEdit(account.email, self)
        self.email_textbox.setObjectName("email_textbox")
        self.email_textbox.setFixedSize(250, 30)
        self.email_textbox.setPlaceholderText("Enter Email")
        self.email_textbox.setStyleSheet("border-radius: 10px;"
                                         "color: black;")
        self.layout.addWidget(self.email_textbox)

        # error message to say that the user has not entered an email
        self.email_null_error_label = QLabel("Please enter Email", self)
        self.email_null_error_label.setObjectName("email_null_label")
        self.email_null_error_label.setStyleSheet("color: red;")
        self.email_null_error_label.hide()
        self.layout.addWidget(self.email_null_error_label)

        # error message to say user has not entered a valid email
        self.email_invalid_error_label = QLabel("Please enter a valid Email. E.g. test@leeds.ac.uk", self)
        self.email_invalid_error_label.setObjectName("email_invalid_label")
        self.email_invalid_error_label.setStyleSheet("color: red;")
        self.email_invalid_error_label.hide()
        self.layout.addWidget(self.email_invalid_error_label)

        # error message to say that the user has entered an email that already exists
        self.email_already_exists_error_label = QLabel("That email is already registered!", self)
        self.email_already_exists_error_label.setObjectName("email_exists_label")
        self.email_already_exists_error_label.setStyleSheet("color: red;")
        self.email_already_exists_error_label.hide()
        self.layout.addWidget(self.email_already_exists_error_label)

        # layout for enter password with button
        password_layout = QHBoxLayout()

        # textbox created for user to enter their desired password
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setObjectName("password_textbox")
        self.password_textbox.setFixedSize(200, 30)
        self.password_textbox.setPlaceholderText("Create Password")
        self.password_textbox.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_textbox.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        password_layout.addWidget(self.password_textbox)

        # image used to show password
        password_image_button = QPushButton()
        password_image_button.setFixedSize(40, 30)
        password_image_button.setStyleSheet("image: url(UI/eye.jpg); "
                                            "border-radius: 10px;"
                                            "background-color: #75B8C8;")
        password_image_button.setCheckable(True)
        password_image_button.clicked.connect(self.show_password_button_click)
        password_layout.addWidget(password_image_button)
        self.layout.addLayout(password_layout)

        # error message to say that the user has not entered a password
        self.password_null_error_label = QLabel("Please enter Password", self)
        self.password_null_error_label.setObjectName("password_null_label")
        self.password_null_error_label.setStyleSheet("color: red;")
        self.password_null_error_label.hide()
        self.layout.addWidget(self.password_null_error_label)

        # error message to say that the user has not entered a password
        self.password_type_error_label = QLabel("Enter a valid password which must include:\n"
                                                "- uppercase letter,\n"
                                                "- lowercase letter,\n"
                                                "- number,\n"
                                                "- 8 characters long", self)
        self.password_type_error_label.setObjectName("password_type_error_label")
        self.password_type_error_label.setStyleSheet("color: red;")
        self.password_type_error_label.hide()
        self.layout.addWidget(self.password_type_error_label)

        # layout for enter password check with button
        password_check_layout = QHBoxLayout()

        # text box created for user to re-enter their password for checking
        self.password_check_textbox = QLineEdit(self)
        self.password_check_textbox.setObjectName("password_check_textbox")
        self.password_check_textbox.setFixedSize(200, 30)
        self.password_check_textbox.setPlaceholderText("Re-enter Password")
        self.password_check_textbox.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_check_textbox.setStyleSheet("border-radius: 10px;"
                                                  "color: black;")
        password_check_layout.addWidget(self.password_check_textbox)

        # image used to show password when pressed
        password_check_image_button = QPushButton()
        password_check_image_button.setFixedSize(40, 30)
        password_check_image_button.setStyleSheet("image: url(UI/eye.jpg); "
                                                  "border-radius: 10px;"
                                                  "background-color: #75B8C8;")
        password_check_image_button.setCheckable(True)
        password_check_image_button.clicked.connect(self.show_password_check_button_click)
        password_check_layout.addWidget(password_check_image_button)
        self.layout.addLayout(password_check_layout)

        # error message to say that the passwords do not match
        self.password_similar_error_label = QLabel("Passwords DO NOT Match", self)
        self.password_similar_error_label.setObjectName("password_mismatch_label")
        self.password_similar_error_label.setStyleSheet("color: red;")
        self.password_similar_error_label.hide()
        self.layout.addWidget(self.password_similar_error_label)

        # ask the user to add a membership
        membership_label = QLabel("Would you like to add a membership?", self)
        self.layout.addWidget(membership_label)

        # dropbox for membership type
        self.membership_type_dropbox = QComboBox()
        self.membership_type_dropbox.setObjectName("membership_dropdown")
        self.membership_type_dropbox.addItem('No Membership')
        self.membership_type_dropbox.addItem('Monthly - £35 per month')
        self.membership_type_dropbox.addItem('Annual - £300 per year (£120 cheaper)')
        self.membership_type_dropbox.setCurrentIndex(account.membership_type)
        self.layout.addWidget(self.membership_type_dropbox)

        # a button that creates the account
        # also send user to the main page
        create_account_button = QPushButton("Create Account")
        create_account_button.setObjectName("create_account_button")
        create_account_button.setFixedSize(250, 50)
        create_account_button.setCheckable(True)
        create_account_button.setStyleSheet("background-color: #220C10;"
                                            "border-radius: 10px;"
                                            "color: white;"
                                            "font-size: 16px;"
                                            "margin: 10px 0px 0px 0px;")
        create_account_button.clicked.connect(self.account_created_button_click)
        self.layout.addWidget(create_account_button)

        # a button that returns user to login page
        back_button = QPushButton("Back")
        back_button.setObjectName("back_button")
        back_button.setFixedSize(250, 50)
        back_button.setCheckable(True)
        back_button.setStyleSheet("background-color: #220C10;"
                                  "border-radius: 10px;"
                                  "color: white;"
                                  "font-size: 16px;"
                                  "margin: 10px 0px 0px 0px;")
        back_button.clicked.connect(self.back_button_click)
        self.layout.addWidget(back_button)

    # function that checks whether the two passwords entered are the same
    # if the passwords do match then return true
    # if the passwords do not match then print an error to the user and return false
    def password_similar_check(self):
        if account.password == account.password_check:
            self.password_similar_error_label.hide()
            return True
        else:
            self.password_similar_error_label.show()
            return False

    def null_error_check(self):
        error = False
        if account.firstname == "":
            self.firstname_null_error_label.show()
            error = True
        else:
            self.firstname_null_error_label.hide()
        if account.lastname == "":
            self.lastname_null_error_label.show()
            error = True
        else:
            self.lastname_null_error_label.hide()
        if account.email == "":
            self.email_null_error_label.show()
            error = True
        else:
            self.email_null_error_label.hide()
        if account.password == "":
            self.password_null_error_label.show()
            error = True
        else:
            self.password_null_error_label.hide()
        return error

    def test_email_already_exists(self):
        data = self.mainWindow.database.getData("SELECT * FROM users WHERE email = ?", account.email)
        if len(data) > 0:
            self.email_already_exists_error_label.show()
            return True
        return False

    # function to set window to login page when the return to login page button is pressed
    def back_button_click(self):
        self.mainWindow.changePage("Login", "Create Account")

    # function to set window to main page when create account button is pressed
    # function also stores all variables entered that can be stored into the database
    # function also does all error checking methods
    def account_created_button_click(self):
        account.firstname = self.firstname_textbox.text()
        account.lastname = self.lastname_textbox.text()
        account.email = self.email_textbox.text()
        account.password = self.password_textbox.text()
        account.password_check = self.password_check_textbox.text()
        account.membership_type = self.membership_type_dropbox.currentIndex()

        if not self.tests():
            if account.membership_type != 0:
                self.mainWindow.changePage("Payment", "Create Account")
            else:
                self.mainWindow.changePage("Check Account", "Create Account")

    # function for the show password button that lets the user see the password they entered
    def show_password_button_click(self):
        if self.password_textbox.echoMode() == QLineEdit.EchoMode.Password:
            self.password_textbox.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_textbox.setEchoMode(QLineEdit.EchoMode.Password)

    # function for the show check password button that lets the user see the password they entered
    def show_password_check_button_click(self):
        if self.password_check_textbox.echoMode() == QLineEdit.EchoMode.Password:
            self.password_check_textbox.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_check_textbox.setEchoMode(QLineEdit.EchoMode.Password)

    def test_email(self):
        at_symbol = False
        after_at_symbol = False
        dot_symbol = False
        end = False
        for letter in account.email:
            if at_symbol:
                if after_at_symbol:
                    if dot_symbol:
                        if letter == "@" or letter == ".":
                            end = False
                        else:
                            end = True
                    else:
                        if letter == ".":
                            dot_symbol = True
                else:
                    after_at_symbol = True
            else:
                if letter == "@":
                    at_symbol = True
        if not end:
            self.email_invalid_error_label.show()
        else:
            self.email_invalid_error_label.hide()

        return end

    def test_password(self):
        lowercase = False
        uppercase = False
        number = False
        for letter in account.password:
            if letter.isupper():
                uppercase = True
            if letter.islower():
                lowercase = True
            if letter.isnumeric():
                number = True
        if lowercase and uppercase and number and (len(account.password) >= 8):
            self.password_type_error_label.hide()
            return True
        self.password_type_error_label.show()
        return False

    def tests(self):
        error = False
        if self.null_error_check():
            error = True
        if not self.password_similar_check():
            error = True
        if not self.test_email():
            error = True
        if not self.test_password():
            error = True
        if self.test_email_already_exists():
            error = True
        return error
