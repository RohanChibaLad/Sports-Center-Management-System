from PyQt6.QtWidgets import *

from account_info import account
from navbar import Navbar


class HomePage(QWidget):
    """
        Class that represents the home page. Shows the navbar with
        the 6 facilities the user can book for.

        Attributes
        ---------
        mainWindow : QMainWindow
            the main window object that is passed to be able to control
            what the central widget is, change pages and communicate with
            the database object

        gridLayout : QGridLayout
            Used to lay out the 6 facilities into two rows of 3 columns,
            stores the facilities as buttons so users can click on each facility

        Methods
        ---------
        button_click(facility)
            redirects the user to the calendar page whilst noting the facility that
            was clicked
    """

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(50, 30, 50, 0)

        navbar = Navbar("Home", self.mainWindow).getNavbar()

        #
        #   FACILITY GRID
        #
        gridLayout = QGridLayout()
        gridLayout.setContentsMargins(5, 20, 5, 0)

        swimming_pool_button = QPushButton("Swimming Pool")
        swimming_pool_button.setFixedSize(350, 250)
        swimming_pool_button.setStyleSheet("background-color: #1E1E24; "
                                           "border-radius: 10px;"
                                           "image: url(UI/swimming_pool.png); "
                                           "padding: -53px 0px 10px 0px;"
                                           "color: white;"
                                           "font-size: 32px;"
                                           "text-align: bottom;")
        swimming_pool_button.clicked.connect(lambda: self.button_click("swimming_pool"))

        fitness_room_button = QPushButton("Fitness Room")
        fitness_room_button.setFixedSize(350, 250)
        fitness_room_button.setStyleSheet("background-color: #1E1E24; "
                                          "border-radius: 10px;"
                                          "image: url(UI/fitness_room.png); "
                                          "padding: -53px 0px 10px 0px;"
                                          "color: white;"
                                          "font-size: 32px;"
                                          "text-align: bottom;")
        fitness_room_button.clicked.connect(lambda: self.button_click("fitness_room"))

        squash_court_button = QPushButton("Squash Court")
        squash_court_button.setFixedSize(350, 250)
        squash_court_button.setStyleSheet("background-color: #1E1E24; "
                                          "border-radius: 10px;"
                                          "image: url(UI/squash_court.png); "
                                          "padding: -53px 0px 10px 0px;"
                                          "color: white;"
                                          "font-size: 32px;"
                                          "text-align: bottom;")
        squash_court_button.clicked.connect(lambda: self.button_click("squash_court"))

        sports_hall_button = QPushButton("Sports Hall")
        sports_hall_button.setFixedSize(350, 250)
        sports_hall_button.setStyleSheet("background-color: #1E1E24; "
                                         "border-radius: 10px;"
                                         "image: url(UI/sports_hall.png); "
                                         "padding: -53px 0px 10px 0px;"
                                         "color: white;"
                                         "font-size: 32px;"
                                         "text-align: bottom;")
        sports_hall_button.clicked.connect(lambda: self.button_click("sports_hall"))

        climbing_wall_button = QPushButton("Climbing Wall")
        climbing_wall_button.setFixedSize(350, 250)
        climbing_wall_button.setStyleSheet("background-color: #1E1E24; "
                                           "border-radius: 10px;"
                                           "image: url(UI/climbing_wall.png); "
                                           "padding: -53px 0px 10px 0px;"
                                           "color: white;"
                                           "font-size: 32px;"
                                           "text-align: bottom;")
        climbing_wall_button.clicked.connect(lambda: self.button_click("climbing_wall"))

        studio_button = QPushButton("Studio")
        studio_button.setFixedSize(350, 250)
        studio_button.setStyleSheet("background-color: #1E1E24; "
                                    "border-radius: 10px;"
                                    "image: url(UI/studio.png); "
                                    "padding: -53px 0px 10px 0px;"
                                    "color: white;"
                                    "font-size: 32px;"
                                    "text-align: bottom;")
        studio_button.clicked.connect(lambda: self.button_click("studio"))

        gridLayout.addWidget(swimming_pool_button, 0, 0)
        gridLayout.addWidget(fitness_room_button, 0, 1)
        gridLayout.addWidget(squash_court_button, 0, 2)
        gridLayout.addWidget(sports_hall_button, 1, 0)
        gridLayout.addWidget(climbing_wall_button, 1, 1)
        gridLayout.addWidget(studio_button, 1, 2)

        mainLayout.addWidget(navbar)
        mainLayout.addLayout(gridLayout)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def button_click(self, facility):
        account.clicked_facility = facility
        self.mainWindow.changePage("Calendar", "Home")
