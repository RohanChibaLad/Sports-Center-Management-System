import time

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

from account_info import account


class LoginPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.email = None
        self.password = None
        # Have a variable for the main window object, so we can change page widget
        self.mainWindow = mainWindow

        # Page layout
        layout = QVBoxLayout()
        # Align everything to center
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Set this page (which is in fact a widget) layout


        # Page label
        label = QLabel("Login Page", self)
        label.setStyleSheet("font: bold 18px;")
        label.setContentsMargins(0, 0, 0, 20)
        # Specifically align the label to center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Add the label to the widget
        layout.addWidget(label)

        # create a label used to store the image for the user profile photo
        login_image_label = QLabel(self)
        login_profile_pixmap = QPixmap('UI/login_image.png')
        login_image_pixmap_resize = login_profile_pixmap.scaled(250, 250)
        login_image_label.setPixmap(login_image_pixmap_resize)
        layout.addWidget(login_image_label)

        # text box for user to enter their email
        self.email_textbox = QLineEdit()
        self.email_textbox.setObjectName("email_textbox")
        self.email_textbox.setFixedSize(250, 30)
        self.email_textbox.setPlaceholderText("Enter Email")
        self.email_textbox.setStyleSheet("border-radius: 10px;"
                                         "color: black;")
        layout.addWidget(self.email_textbox)

        # error message to say that the user has not entered an email
        self.email_null_error_label = QLabel("Please enter an Email", self)
        # Set object names, so they can be found in unit tests
        self.email_null_error_label.setObjectName("null_email_label")
        self.email_null_error_label.setStyleSheet("color: red;")
        self.email_null_error_label.hide()
        layout.addWidget(self.email_null_error_label)

        # error message to say that the user has entered a non-existent email
        self.email_non_exist_error_label = QLabel("Account not found, email may be mistyped", self)
        self.email_non_exist_error_label.setObjectName("non_existent_email_label")
        self.email_non_exist_error_label.setStyleSheet("color: red;")
        self.email_non_exist_error_label.hide()
        layout.addWidget(self.email_non_exist_error_label)

        # add a layout for show password line
        password_layout = QHBoxLayout()

        # text box for user to enter their password
        self.password_textbox = QLineEdit()
        self.password_textbox.setObjectName("password_textbox")
        self.password_textbox.setFixedSize(200, 30)
        self.password_textbox.setPlaceholderText("Enter Password")
        self.password_textbox.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.password_textbox.setEchoMode(QLineEdit.EchoMode.Password)
        password_layout.addWidget(self.password_textbox)

        # add an eye image to show the password entered
        password_image_button = QPushButton()
        password_image_button.setFixedSize(40, 30)
        password_image_button.setStyleSheet("image: url(UI/eye.jpg); "
                                         "border-radius: 10px;"
                                         "background-color: #75B8C8;")
        password_image_button.setCheckable(True)
        password_image_button.clicked.connect(self.show_password_button_click)
        password_layout.addWidget(password_image_button)
        layout.addLayout(password_layout)

        # error message to say that the user has not entered a password
        self.password_null_error_label = QLabel("Please enter a Password", self)
        self.password_null_error_label.setObjectName("null_password_label")
        self.password_null_error_label.setStyleSheet("color: red;")
        self.password_null_error_label.hide()
        layout.addWidget(self.password_null_error_label)

        # error message to say that the user has entered an incorrect password
        self.password_incorrect_error_label = QLabel("Incorrect Password!", self)
        self.password_incorrect_error_label.setObjectName("incorrect_password_label")
        self.password_incorrect_error_label.setStyleSheet("color: red;")
        self.password_incorrect_error_label.hide()
        layout.addWidget(self.password_incorrect_error_label)

        # Button to 'login'
        login_button = QPushButton("Login")
        login_button.setObjectName("login_button")
        # Resizes the button
        login_button.setFixedSize(250, 50)
        # Make the button clickable
        login_button.setCheckable(True)
        # style sheet to change appearance of button
        login_button.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        # Make a connect signal for the button to run a function
        login_button.clicked.connect(self.login_button_click)
        # Add the button to the layout
        layout.addWidget(login_button)

        # button for user to create an account if they don't have one already
        create_account_button = QPushButton("Create an Account")
        create_account_button.setObjectName("create_account_page_button")
        create_account_button.setFixedSize(250, 50)
        create_account_button.setCheckable(True)
        create_account_button.setStyleSheet("background-color: #220C10;"
                                            "border-radius: 10px;"
                                            "color: white;"
                                            "font-size: 16px;"
                                            "margin: 10px 0px 0px 0px;")
        create_account_button.clicked.connect(self.create_account_button_click)
        layout.addWidget(create_account_button)

        self.setLayout(layout)

    # Function that runs on button click which changes the page to the HomePage
    def login_button_click(self):
        self.email = self.email_textbox.text()
        self.password = self.password_textbox.text()

        # Run tests for valid login
        if not self.null_error_check() and self.test_email_existence() and self.test_correct_password():
            self.fill_account_details()

            # Check the priority of the retrieved user and if manager priority then change to respective page
            if account.account_type == 2:
                self.mainWindow.changePage("Management Page", "Login")
            else:
                self.mainWindow.changePage("Home", "Login")

    def fill_account_details(self):
        # Get user id of logged in user
        user_data = self.mainWindow.database.getData("SELECT * FROM users WHERE email = (?) AND "
                                                     "password = (?)", self.email, self.password)
        # Set the user id in the account class of the user
        account.user_id = user_data[0][0]
        # Set the user first and last name in the account class
        account.firstname = user_data[0][1]
        account.lastname = user_data[0][2]
        # Set the user email in the account class
        account.email = user_data[0][3]
        # set the user password in the account class
        account.password = user_data[0][4]
        # Set user account type
        account.account_type = user_data[0][5]

        # Get membership details (if any) of logged-in user
        membership = self.mainWindow.database.getData("SELECT * FROM memberships WHERE user_id = (?)",
                                                      str(account.user_id))
        if len(membership) != 0:
            # Set the users membership details
            match membership[0][2]:
                case "monthly":
                    account.membership_type = 1
                case "annual":
                    account.membership_type = 2
        else:
            account.membership_type = 0

        # Get card details (if any) of logged-in user
        card_details = self.mainWindow.database.getData("SELECT * FROM card_information WHERE user_id = (?)",
                                                        str(account.user_id))

        # Set the card details in the account class if any card information was found
        if len(card_details) != 0:
            account.card_number = card_details[0][2]
            account.name_on_card = card_details[0][3]
            account.expiry_date = card_details[0][4]
            account.cvv = card_details[0][5]

    def null_error_check(self):
        error = False
        if self.email == "":
            self.email_null_error_label.show()
            error = True
        else:
            self.email_null_error_label.hide()
        if self.password == "":
            self.password_null_error_label.show()
            error = True
        else:
            self.password_null_error_label.hide()
        return error

    def test_email_existence(self):
        data = self.mainWindow.database.getData("SELECT * FROM users WHERE email = ?", self.email)
        if len(data) > 0:
            return True
        self.email_non_exist_error_label.show()
        return False

    def test_correct_password(self):
        data = self.mainWindow.database.getData("SELECT * FROM users WHERE email = ?", self.email)
        if len(data) > 0:
            if self.password == data[0][4]:
                return True
        self.password_incorrect_error_label.show()
        return False

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    # function that sets the window to create an account page when create an account button is pressed
    def create_account_button_click(self):
        self.mainWindow.changePage("Create Account", "Login")

    # function for the show password button that lets the user see the password they entered
    def show_password_button_click(self):
        if self.password_textbox.echoMode() == QLineEdit.EchoMode.Password:
            self.password_textbox.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_textbox.setEchoMode(QLineEdit.EchoMode.Password)
