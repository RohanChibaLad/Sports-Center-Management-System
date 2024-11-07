import sys

from PyQt6.QtWidgets import *

from basket_page import BasketPage
from database import Database
from calendar_page import CalendarPage
from create_account_page import CreateAccountPage
from home_page import HomePage
from login_page import LoginPage
from payment_page import PaymentPage
from check_account_page import CheckAccountPage
from management_page import ManagementPage, EditInfo, Add_Act_Fac, Graphs
from edit_account_page import EditAccountPage
from sessions import SessionsPage


class MainWindow(QMainWindow):
    """
        This class represents the main window which is always shown, to show
        different pages as we simply change the central widget of this object
        to different widgets (pages)

        Attributes
        ----------
        database : Database
            the database object which is referenced by other pages to execute
            statements to the database

        Methods
        ---------
        change_page(page, camefrom)
            changes to the given page and also takes in which page the
            user will be coming from as some pages need to know which
            page the user came from
    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setObjectName("main")
        self.setStyleSheet("QMainWindow#main { background-color: #CDD3D5; }")

        self.database = Database()
        # Comment the line out below if you don't want the database to be reset every time on launch
        # self.database.resetDatabase()

        # Set window title and minimum size (window is resizable)
        self.setWindowTitle("Sport Centre Management System")
        self.setMinimumSize(1280, 700)

        # Set the central widget to the login page as default
        # We also pass in the main window object to the LoginPage,
        # so we can set the main windows' central widget in other pages
        self.setCentralWidget(LoginPage(self))

    def changePage(self, page, camefrom):
        match page:
            case "Login":
                self.setCentralWidget(LoginPage(self))
            case "Home":
                self.setCentralWidget(HomePage(self))
            case "Sessions":
                self.setCentralWidget(SessionsPage(self))
            case "Calendar":
                self.setCentralWidget(CalendarPage(self))
            case "Create Account":
                self.setCentralWidget(CreateAccountPage(self))
            case "Payment":
                self.setCentralWidget(PaymentPage(self, camefrom))
            case "Check Account":
                self.setCentralWidget(CheckAccountPage(self))
            case "Management Page":
                self.setCentralWidget(ManagementPage(self))
            case "Edit Info":
                self.setCentralWidget(EditInfo(self))
            case "Graph Page":
                self.setCentralWidget(Graphs(self))
            case "Add Info":
                self.setCentralWidget(Add_Act_Fac(self))
            case "Edit Account":
                self.setCentralWidget(EditAccountPage(self, camefrom))
            case "Basket":
                self.setCentralWidget(BasketPage(self))


# Put the run statements in a __main__ if statement since the test suite
# needs these statements to NOT run in order for the test instance to work
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())