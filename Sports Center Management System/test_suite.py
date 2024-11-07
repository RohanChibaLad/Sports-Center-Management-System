import sys
from unittest import TestCase

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtTest import QTest
from PyQt6.QtWidgets import *

from check_account_page import CheckAccountPage
from create_account_page import CreateAccountPage
from home_page import HomePage
from login_page import LoginPage
from main import MainWindow
from payment_page import PaymentPage


class TestSuite(TestCase):
    # Set up the application in the test
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()

    def tearDown(self):
        self.app.quit()


# Tests to run for the MainWindow class
class TestMainWindow(TestSuite):
    # Checking window title was set correctly
    def test_window_title(self):
        self.assertEqual(self.window.windowTitle(), "Sport Centre Management System")

    # Checking minimum size was set correctly
    def test_minimum_size(self):
        self.assertEqual(self.window.minimumSize(), QSize(1280, 700))

    # Checking the central widget is set to the LoginPage
    def test_central_widget(self):
        self.assertTrue(isinstance(self.window.centralWidget(), LoginPage))


# Tests to run for the Login class
class TestLogin(TestSuite):
    def test_null_email(self):
        # Click login button with empty email text box
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "login_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "null_email_label").isHidden(),
                         "Incorrect error message for empty Email field in login page")

    def test_null_password(self):
        # Click login button with empty password text box
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "login_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "null_password_label").isHidden(),
                         "Incorrect error message for empty Password field in login page")

    def test_non_existent_email(self):
        # Type a non-existent email and random password in each text box
        QTest.keyPress(self.window.centralWidget().findChild(QLineEdit, "email_textbox",
                                                             Qt.FindChildOption.FindChildrenRecursively), Qt.Key.Key_A)
        QTest.keyPress(self.window.centralWidget().findChild(QLineEdit, "password_textbox",
                                                             Qt.FindChildOption.FindChildrenRecursively), Qt.Key.Key_A)
        # Click login button
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "login_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check non-existent error message showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "non_existent_email_label").isHidden(),
                         "Incorrect error message for non existent email")

    def test_incorrect_password(self):
        # Type a valid email but with the incorrect password
        emailTextbox = self.window.centralWidget().findChild(QLineEdit, "email_textbox",
                                                             Qt.FindChildOption.FindChildrenRecursively)
        QTest.keyPress(emailTextbox, Qt.Key.Key_A)
        QTest.keyPress(emailTextbox, Qt.Key.Key_D)
        QTest.keyPress(emailTextbox, Qt.Key.Key_M)
        QTest.keyPress(emailTextbox, Qt.Key.Key_I)
        QTest.keyPress(emailTextbox, Qt.Key.Key_N)
        QTest.keyPress(self.window.centralWidget().findChild(QLineEdit, "password_textbox",
                                                             Qt.FindChildOption.FindChildrenRecursively), Qt.Key.Key_A)
        # Click login button
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "login_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check non-existent error message showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "incorrect_password_label").isHidden(),
                         "Incorrect error message for incorrect password")

    def test_valid_login_details(self):
        # Add in temporary user to database
        self.window.database.exeStatement("INSERT INTO users (first_name, last_name, email, password) VALUES (?, ?, "
                                          "?, ?)", "Test", "Name", "test@email.com", "Password1")
        emailTextbox = self.window.centralWidget().findChild(QLineEdit, "email_textbox",
                                                             Qt.FindChildOption.FindChildrenRecursively)
        passwordTextbox = self.window.centralWidget().findChild(QLineEdit, "password_textbox",
                                                                Qt.FindChildOption.FindChildrenRecursively)
        if isinstance(emailTextbox, QLineEdit) and isinstance(passwordTextbox, QLineEdit):
            # Set email and password text boxes for temporary user
            emailTextbox.setText("test@email.com")
            passwordTextbox.setText("Password1")
            QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "login_button",
                                                                   Qt.FindChildOption.FindChildrenRecursively),
                             Qt.MouseButton.LeftButton)
            # Check we were directed to the Home Page
            self.assertTrue(isinstance(self.window.centralWidget(), HomePage))
            # Delete the temporary user from database
            self.window.database.exeStatement("DELETE FROM users WHERE email = (?)", "test@email.com")


# Test to run for the CreateAccountPage class
class TestCreateAccount(TestSuite):
    def goto_create_account_page(self):
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_page_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        self.firstname_textbox = self.window.centralWidget().findChild(QLineEdit, "firstname_textbox",
                                                                       Qt.FindChildOption.FindChildrenRecursively)
        self.lastname_textbox = self.window.centralWidget().findChild(QLineEdit, "lastname_textbox",
                                                                      Qt.FindChildOption.FindChildrenRecursively)
        self.email_textbox = self.window.centralWidget().findChild(QLineEdit, "email_textbox",
                                                                   Qt.FindChildOption.FindChildrenRecursively)
        self.password_textbox = self.window.centralWidget().findChild(QLineEdit, "password_textbox",
                                                                      Qt.FindChildOption.FindChildrenRecursively)
        self.check_password_textbox = self.window.centralWidget().findChild(QLineEdit, "password_check_textbox",
                                                                            Qt.FindChildOption.FindChildrenRecursively)
        self.membership_dropdown = self.window.centralWidget().findChild(QComboBox, "membership_dropdown",
                                                                         Qt.FindChildOption.FindChildrenRecursively)
        if isinstance(self.firstname_textbox, QLineEdit) and \
                isinstance(self.lastname_textbox, QLineEdit) and \
                isinstance(self.email_textbox, QLineEdit) and \
                isinstance(self.password_textbox, QLineEdit) and \
                isinstance(self.check_password_textbox, QLineEdit):
            self.firstname_textbox.setText("")
            self.lastname_textbox.setText("")
            self.email_textbox.setText("")
            self.password_textbox.setText("")
            self.check_password_textbox.setText("")

    def test_back_button(self):
        # Click create account button
        self.goto_create_account_page()
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "back_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        self.assertTrue(isinstance(self.window.centralWidget(), LoginPage))

    def test_redirect_to_create_account(self):
        # Click create account button
        self.goto_create_account_page()
        # Test we are actually on the create account page
        self.assertTrue(isinstance(self.window.centralWidget(), CreateAccountPage))

    def test_null_firstname(self):
        # Click create account button
        self.goto_create_account_page()
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "firstname_null_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for empty Firstname field in create account page")

    def test_null_lastname(self):
        # Click create account button
        self.goto_create_account_page()
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "lastname_null_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for empty Lastname field in create account page")

    def test_null_email(self):
        # Click create account button
        self.goto_create_account_page()
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "email_null_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for empty Email field in create account page")

    def test_invalid_email(self):
        # Click create account button
        self.goto_create_account_page()
        self.firstname_textbox.setText("a")
        self.lastname_textbox.setText("a")
        self.email_textbox.setText("a")
        self.password_textbox.setText("a")
        self.check_password_textbox.setText("a")
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "email_invalid_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for invalid email in create account page")

    def test_email_exists(self):
        # Click create account button
        self.goto_create_account_page()

        # Insert temporary details
        self.window.database.exeStatement("INSERT INTO users (first_name, last_name, email, password, priority) VALUES "
                                          "(?, ?, ?, ?, ?)", 'first', 'last', 'name@domain.com', 'password', '0')

        # Fill in textboxes
        self.firstname_textbox.setText("a")
        self.lastname_textbox.setText("a")
        self.email_textbox.setText("name@domain.com")
        self.password_textbox.setText("123456Aa")
        self.check_password_textbox.setText("123456Aa")

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "email_exists_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for email already exists in create account page")

        # Delete temporary details
        self.window.database.exeStatement("DELETE FROM users WHERE email = (?)", "name@domain.com")

    def test_null_password(self):
        # Click create account button
        self.goto_create_account_page()

        # Fill in text boxes
        self.firstname_textbox.setText("a")
        self.lastname_textbox.setText("a")
        self.email_textbox.setText("name@domain.com")

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "password_null_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for empty password in create account page")

    def test_type_error_password(self):
        # Click create account button
        self.goto_create_account_page()

        # Fill in textboxes
        self.firstname_textbox.setText("a")
        self.lastname_textbox.setText("a")
        self.email_textbox.setText("name@domain.com")
        self.password_textbox.setText("a")
        self.check_password_textbox.setText("a")

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "password_type_error_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for invalid password in create account page")

    def test_mismatch_password(self):
        # Click create account button
        self.goto_create_account_page()

        # Fill in text boxes
        self.firstname_textbox.setText("a")
        self.lastname_textbox.setText("a")
        self.email_textbox.setText("name@domain.com")
        self.password_textbox.setText("a")
        self.check_password_textbox.setText("b")

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if the corresponding error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "password_mismatch_label",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for mismatched passwords in create account page")

    def test_correct_details_no_membership_redirect(self):
        # Click create account button
        self.goto_create_account_page()

        # Fill in text boxes
        self.firstname_textbox.setText("Firstname")
        self.lastname_textbox.setText("Lastname")
        self.email_textbox.setText("name@domain.com")
        self.password_textbox.setText("123456Aa")
        self.check_password_textbox.setText("123456Aa")

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        # Check if we changed to the correct page
        self.assertTrue(isinstance(self.window.centralWidget(), CheckAccountPage))

    def test_correct_details_no_membership(self):
        # Click create account button
        self.goto_create_account_page()

        # Fill in text boxes
        self.firstname_textbox.setText("Firstname")
        self.lastname_textbox.setText("Lastname")
        self.email_textbox.setText("name@domain.com")
        self.password_textbox.setText("123456Aa")
        self.check_password_textbox.setText("123456Aa")
        self.membership_dropdown.setCurrentIndex(0)

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        # Check we did change page
        self.assertTrue(isinstance(self.window.centralWidget(), CheckAccountPage))

        # Find membership type label
        membership_label = self.window.centralWidget().findChild(QLabel, "membership_type_label",
                                                                 Qt.FindChildOption.FindChildrenRecursively)

        # Check membership label shows correct type
        if isinstance(membership_label, QLabel):
            self.assertEqual(membership_label.text(), "No Membership")

    def test_correct_details_membership_redirect(self):
        # Click create account button
        self.goto_create_account_page()

        # Fill in text boxes
        self.firstname_textbox.setText("Firstname")
        self.lastname_textbox.setText("Lastname")
        self.email_textbox.setText("name@domain.com")
        self.password_textbox.setText("123456Aa")
        self.check_password_textbox.setText("123456Aa")
        self.membership_dropdown.setCurrentIndex(1)

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        # Check we did change page
        self.assertTrue(isinstance(self.window.centralWidget(), PaymentPage))


class TestPaymentPage(TestSuite):
    def goto_payment_page_through_create_account(self):
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_page_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)
        self.window.centralWidget().findChild(QLineEdit, "firstname_textbox",
                                              Qt.FindChildOption.FindChildrenRecursively).setText("Firstname")
        self.window.centralWidget().findChild(QLineEdit, "lastname_textbox",
                                              Qt.FindChildOption.FindChildrenRecursively).setText("Lastname")
        self.window.centralWidget().findChild(QLineEdit, "email_textbox",
                                              Qt.FindChildOption.FindChildrenRecursively).setText("test@email.com")
        self.window.centralWidget().findChild(QLineEdit, "password_textbox",
                                              Qt.FindChildOption.FindChildrenRecursively).setText("123456Aa")
        self.window.centralWidget().findChild(QLineEdit, "password_check_textbox",
                                              Qt.FindChildOption.FindChildrenRecursively).setText("123456Aa")
        self.window.centralWidget().findChild(QComboBox, "membership_dropdown",
                                              Qt.FindChildOption.FindChildrenRecursively).setCurrentIndex(1)

        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "create_account_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        self.card_number_textbox = self.window.centralWidget().findChild(QLineEdit, "card_number_textbox",
                                                                         Qt.FindChildOption.FindChildrenRecursively)
        self.name_on_card_textbox = self.window.centralWidget().findChild(QLineEdit, "name_on_card_textbox",
                                                                          Qt.FindChildOption.FindChildrenRecursively)
        self.expiry_date_textbox = self.window.centralWidget().findChild(QLineEdit, "expiry_date_textbox",
                                                                         Qt.FindChildOption.FindChildrenRecursively)
        self.cvv_textbox = self.window.centralWidget().findChild(QLineEdit, "cvv_textbox",
                                                                 Qt.FindChildOption.FindChildrenRecursively)

    def test_correct_redirect(self):
        # Goto payment page
        self.goto_payment_page_through_create_account()

        self.assertTrue(isinstance(self.window.centralWidget(), PaymentPage))

    def test_invalid_card_number(self):
        # Goto payment page
        self.goto_payment_page_through_create_account()

        self.card_number_textbox.setText("1234")

        # Click payment button
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "payment_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        # Test error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "invalid_card_number",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for invalid card number in payment page")

    def test_invalid_name_on_card(self):
        # Goto payment page
        self.goto_payment_page_through_create_account()

        self.name_on_card_textbox.setText("1234")

        # Click payment button
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "payment_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        # Test error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "invalid_name_on_card",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for invalid name on card in payment page")

    def test_invalid_expiry_date(self):
        # Goto payment page
        self.goto_payment_page_through_create_account()

        self.expiry_date_textbox.setText("hello")

        # Click payment button
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "payment_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        # Test error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "invalid_expiry_date",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for invalid expiry date in payment page")

    def test_invalid_cvv(self):
        # Goto payment page
        self.goto_payment_page_through_create_account()

        self.cvv_textbox.setText("hello")

        # Click payment button
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "payment_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        # Test error label showed
        self.assertFalse(self.window.centralWidget().findChild(QLabel, "invalid_cvv",
                                                               Qt.FindChildOption.FindChildrenRecursively).isHidden(),
                         "Incorrect error message for invalid cvv in payment page")

    def test_correct_details(self):
        # Goto payment page
        self.goto_payment_page_through_create_account()

        self.card_number_textbox.setText("1234567812345678")
        self.name_on_card_textbox.setText("First Last")
        self.expiry_date_textbox.setText("07/25")
        self.cvv_textbox.setText("123")

        # Click payment button
        QTest.mouseClick(self.window.centralWidget().findChild(QPushButton, "payment_button",
                                                               Qt.FindChildOption.FindChildrenRecursively),
                         Qt.MouseButton.LeftButton)

        self.assertTrue(isinstance(self.window.centralWidget(), CheckAccountPage))
