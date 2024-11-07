from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *

from account_info import account


class Navbar:
    """
        Class that represents the navbar shown on most pages to allow
        the user easier navigation through the application

        Attributes
        ----------
        currentPage : String
            stores the current page so the navbar knows to disable the corresponding
            button if we are on that page

        navbar_background : QWidget
            Base widget which holds the layout for the buttons of the navbar

        navbar : QHBoxLayout
            Layout for the various buttons

        Methods
        ----------
        getNavbar()
            returns the navbar_background widget

        navbar_click(page)
            redirects user to the respective page for the clicked button on
            the navbar
    """
    def __init__(self, currentPage, mainWindow):
        self.mainWindow = mainWindow
        self.currentPage = currentPage

        #
        #   NAVBAR
        #
        self.navbar_background = QWidget()
        self.navbar_background.setObjectName("navbar_background")
        self.navbar_background.setStyleSheet("QWidget#navbar_background { background-color: #1E1E24; border-radius: 10px; }")
        self.navbar_background.setContentsMargins(40, 0, 40, 0)
        self.navbar_background.setMaximumHeight(100)

        # Horizontal box layout for the buttons
        navbar = QHBoxLayout()

        self.navbar_background.setLayout(navbar)

        # Icon for the navbar
        icon = QLabel()
        icon.setPixmap(QPixmap("UI/logo.png"))

        home_button = QPushButton("Home")
        home_button.setFixedSize(100, 50)
        home_button.setStyleSheet("background-color: #21A179;"
                                  "border-radius: 5px;"
                                  "color: white;"
                                  "font-size: 18px;")
        # Checks if the current page isn't home to allow the button to
        # redirect on click since we don't want the home button to do
        # anything if the user is already on the home page.
        # This is the same with most other buttons
        if currentPage != "Home":
            home_button.clicked.connect(lambda: self.navbar_click("Home"))

        my_sessions_button = QPushButton("My Sessions")
        my_sessions_button.setFixedSize(120, 50)
        my_sessions_button.setStyleSheet("background-color: #21A179;"
                                         "border-radius: 5px;"
                                         "color: white;"
                                         "font-size: 18px;")
        if self.currentPage != "Sessions":
            my_sessions_button.clicked.connect(lambda: self.navbar_click("Sessions"))

        logout_button = QPushButton("Logout")
        logout_button.setFixedSize(140, 50)
        logout_button.setStyleSheet("background-color: #21A179;"
                                    "border-radius: 5px;"
                                  "color: white;"
                                  "font-size: 18px;")
        # if self.currentPage != "Memberships":
        logout_button.clicked.connect(lambda: self.navbar_click("Login"))
            # pass

        basket_widget = QWidget()
        basket_widget_layout = QHBoxLayout(basket_widget)

        basket_button = QPushButton(basket_widget)
        basket_button.setFixedSize(65, 65)
        basket_button.setStyleSheet("image: url(UI/basket_logo.png);"
                                    "border-radius: 10px;"
                                    "background-color: #75B8C8;")
        if self.currentPage != "Basket":
            basket_button.clicked.connect(lambda: self.navbar_click("Basket"))

        items_in_basket = QLabel(str(len(account.sql_statements)), basket_widget)
        items_in_basket.move(55, 55)
        items_in_basket.setFixedSize(24, 24)
        items_in_basket.setStyleSheet("border-radius: 12px;"
                                      "background-color: #DA1D28;"
                                      "color: white;"
                                      "font-size: 16px;"
                                      "padding: -3px 0px 0px 4px;")

        basket_widget_layout.addWidget(basket_button)
        basket_widget.setLayout(basket_widget_layout)

        account_button = QPushButton()
        account_button.setFixedSize(65, 65)
        account_button.setStyleSheet("image: url(UI/account_logo.png);"
                                     "border-radius: 10px;")

        if self.currentPage != "Edit Account":
            account_button.clicked.connect(lambda: self.navbar_click("Edit Account"))

        # Add the various widgets and buttons to the navbar layout with
        # a stretch between each widget to space out the widgets neatly
        navbar.addWidget(icon)
        navbar.addStretch(1)
        navbar.addWidget(home_button)
        navbar.addStretch(1)
        navbar.addWidget(my_sessions_button)
        navbar.addStretch(1)
        navbar.addWidget(logout_button)
        navbar.addStretch(1)
        navbar.addWidget(basket_widget)
        navbar.addWidget(account_button)

    def getNavbar(self):
        return self.navbar_background

    def navbar_click(self, page):
        match page:
            case "Home":
                self.mainWindow.changePage("Home", self.currentPage)
            case "Sessions":
                self.mainWindow.changePage("Sessions", self.currentPage)
            case "Login":
                account.clear_account()
                self.mainWindow.changePage("Login", self.currentPage)
            case "Basket":
                self.mainWindow.changePage("Basket", self.currentPage)
            case "Edit Account":
                self.mainWindow.changePage("Edit Account", self.currentPage)
