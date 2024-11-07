import datetime
import time
from datetime import timedelta

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from account_info import account


class CheckAccountPage(QWidget):
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
        label = QLabel("Check Account Page", self)
        # Specifically align the label to center
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Add the label to the widget
        self.layout.addWidget(label)

        # show user their firstname
        self.show_firstname_label = QLabel(self)
        self.show_firstname_label.setText(account.firstname)

        # show user their lastname
        self.show_lastname_label = QLabel(self)
        self.show_lastname_label.setText(account.lastname)

        # show user their email
        self.show_email_label = QLabel(self)
        self.show_email_label.setText(account.email)

        # show user their password
        self.show_password_label = QLabel(self)
        self.show_password_label.setText(account.password)

        # show user their membership type
        self.show_membership_type_label = QLabel(self)
        self.show_membership_type_label.setObjectName("membership_type_label")
        if account.membership_type == 0:
            self.show_membership_type_label.setText("No Membership")
        elif account.membership_type == 1:
            self.show_membership_type_label.setText("Monthly Membership")
        elif account.membership_type == 2:
            self.show_membership_type_label.setText("Annual Membership")

        # form to show user all their account details
        account_formLayout = QFormLayout()
        account_formLayout.addRow("Firstname:", self.show_firstname_label)
        account_formLayout.addRow("Lastname:", self.show_lastname_label)
        account_formLayout.addRow("Email:", self.show_email_label)
        account_formLayout.addRow("Password:", self.show_password_label)
        account_formLayout.addRow("Membership Type:", self.show_membership_type_label)
        self.layout.addLayout(account_formLayout)

        # show user their card number
        self.show_card_number_label = QLabel(self)
        self.show_card_number_label.setText(str(account.card_number))

        # show user their lastname
        self.show_name_on_card_label = QLabel(self)
        self.show_name_on_card_label.setText(account.name_on_card)

        # show user their email
        self.show_expiry_date_label = QLabel(self)
        self.show_expiry_date_label.setText(account.expiry_date)

        # show user their password
        self.show_cvv_label = QLabel(self)
        self.show_cvv_label.setText(str(account.cvv))

        # form to show user all their payment details
        payment_formLayout = QFormLayout()
        payment_formLayout.addRow("Card Number:", self.show_card_number_label)
        payment_formLayout.addRow("Name on Card:", self.show_name_on_card_label)
        payment_formLayout.addRow("Expiry Date:", self.show_expiry_date_label)
        payment_formLayout.addRow("CVV:", self.show_cvv_label)
        if account.card_number is not None:
            self.layout.addLayout(payment_formLayout)

        # label to ask user if they want to make changes to account or not
        edit_account_label = QLabel("\n\nWould you like to make changes to your account?", self)
        self.layout.addWidget(edit_account_label)

        # a button that returns user to login page
        edit_account_button = QPushButton("Edit Account Information")
        edit_account_button.setFixedSize(250, 50)
        edit_account_button.setCheckable(True)
        edit_account_button.setStyleSheet("background-color: #220C10;"
                                          "border-radius: 10px;"
                                          "color: white;"
                                          "font-size: 16px;"
                                          "margin: 20px 0px 0px 0px;")
        edit_account_button.clicked.connect(self.edit_account_button_click)
        self.layout.addWidget(edit_account_button)

        # a button that returns the user to payment page
        edit_payment_button = QPushButton("Edit Payment Information")
        edit_payment_button.setFixedSize(250, 50)
        edit_payment_button.setCheckable(True)
        edit_payment_button.setStyleSheet("background-color: #220C10;"
                                          "border-radius: 10px;"
                                          "color: white;"
                                          "font-size: 16px;"
                                          "margin: 20px 0px 0px 0px;")
        edit_payment_button.clicked.connect(self.edit_payment_button_click)
        self.layout.addWidget(edit_payment_button)

        # a button that send user on to home page
        save_account_button = QPushButton("Save Account")
        save_account_button.setFixedSize(250, 50)
        save_account_button.setCheckable(True)
        save_account_button.setStyleSheet("background-color: #220C10;"
                                          "border-radius: 10px;"
                                          "color: white;"
                                          "font-size: 16px;"
                                          "margin: 20px 0px 0px 0px;")
        save_account_button.clicked.connect(self.save_account_button_click)
        self.layout.addWidget(save_account_button)

    def edit_account_button_click(self):
        self.mainWindow.changePage("Edit Account", "Check Account")


    def edit_payment_button_click(self):
        self.mainWindow.changePage("Payment", "Check Account")

    def get_future_time(self, weeks):
        return (datetime.datetime.now() + timedelta(weeks=weeks)).timestamp()

    def save_account_button_click(self):
        if account.edit_details:
            self.mainWindow.database.exeStatement("UPDATE users SET first_name = (?), last_name = (?),"
                                                  "email = (?), password = (?) WHERE id = (?) ",
                                                  account.firstname, account.lastname, account.email,
                                                  account.password, str(account.user_id))
            account.edit_details = False
        else:
            # Insert user information into users table
            self.mainWindow.database.exeStatement("INSERT INTO users (first_name, last_name, email, password) VALUES "
                                                  "(?, ?, ?, ?)", account.firstname, account.lastname, account.email,
                                                  account.password)

            # Get the id of the user just created
            user_id = self.mainWindow.database.getData("SELECT id FROM users WHERE email = (?) AND password = (?)",
                                                       account.email, account.password)
            # Set the user id of the newly created user
            account.user_id = str(user_id[0][0])

            # Check for any card details that have been inputted and if so enter them into the table
            if account.card_number is not None \
                    and account.name_on_card is not None \
                    and account.expiry_date is not None \
                    and account.cvv is not None:
                # Parse the expiry date to a time since epoch
                expiry_date = datetime.datetime.strptime(account.expiry_date, "%m/%y").timestamp()
                self.mainWindow.database.exeStatement("INSERT INTO card_information (user_id, card_number, name_on_card, "
                                                      "expiry_date, cvv) VALUES (?, ?, ?, ?, ?)", account.user_id,
                                                      account.card_number, account.name_on_card, str(expiry_date),
                                                      account.cvv)

            # Check for a membership
            if account.membership_type != 0:
                match account.membership_type:
                    case 1:
                        in_a_months_time = str(self.get_future_time(4))
                        self.mainWindow.database.exeStatement("INSERT INTO memberships (user_id, membership_type, "
                                                              "membership_expiry) VALUES (?, ?, ?)", account.user_id,
                                                              "monthly", in_a_months_time)
                        account.membership_type = 1
                    case 2:
                        in_a_years_time = str(self.get_future_time(52))
                        self.mainWindow.database.exeStatement("INSERT INTO memberships (user_id, membership_type, "
                                                              "membership_expiry) VALUES (?, ?, ?)", account.user_id,
                                                              "annual", in_a_years_time)
                        account.membership_type = 2

        self.mainWindow.changePage("Home", "Check Account")
