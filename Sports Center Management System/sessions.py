import math
import time

from PyQt6.QtWidgets import *

from account_info import account
from navbar import Navbar


class SessionsPage(QWidget):
    """
        Class that represents the booked sessions of the logged-in user

        Attributes
        ----------
        mainWindow : QMainWindow
            the main window object that is passed to be able to control
            what the central widget is, change pages and communicate with
            the database object

        gridLayout : QGridLayout
            similar to other pages with a grid layout, this is simply used
            to lay out the booked sessions of the user in a grid layout

        sessions : List
            stores the booked sessions in the database for the current user

        sessionsToDisplay : int
            the number of sessions that is to be displayed, used in a for loop

        Methods
        ---------
        getSessions()
            returns the sessions in the database for the current logged-in user

        generate_card(data)
            generates a card for each session which shows the facility, activity,
            date, time and a cancel button

        session_clicked(session_id)
            cancels the session of the given session_id
    """

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(50, 30, 50, 0)

        navbar = Navbar("Sessions", self.mainWindow).getNavbar()

        #
        # SESSIONS GRID
        #
        gridLayout = QGridLayout()
        gridLayout.setContentsMargins(5, 0, 5, 0)

        sessions = self.getSessions()
        sessionsToDisplay = len(sessions)

        # A for loop with 2 variables using zip() to be able to lay out
        # the sessions in the grid in a certain way
        for i, j in zip(range(sessionsToDisplay * 2), range(sessionsToDisplay)):
            widget = self.generate_card(sessions[i])
            gridLayout.addWidget(widget, math.floor(i / 3), j % 3)

        if sessionsToDisplay == 1:
            gridLayout.addWidget(QWidget(), 0, 1)

        mainLayout.addWidget(navbar)
        if sessionsToDisplay == 0:
            mainLayout.addStretch(1)
        mainLayout.addLayout(gridLayout)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def generate_card(self, data):
        card = QPushButton()
        # card.setEnabled(False)
        card.setObjectName("card")
        card.setFixedSize(350, 250)
        # Styling for the card
        card.setStyleSheet("QPushButton#card { "
                           "background-color: #1E1E24;"
                           "image: url(UI/" + data[1] + "_smaller.png); "
                           "padding: -65px 0px 10px 0px;"
                           "border-radius: 10px; }"
                           "QLabel { color: white; }")

        card_layout = QVBoxLayout()
        card_layout.addStretch(1)

        information_layout = QGridLayout()
        card_layout.addLayout(information_layout)

        # Parse the data into a readable and nice format for the card
        session_facility = QLabel("Facility: " + str(data[1]).replace("_", " ").capitalize())
        session_activity = QLabel("Activity: " + str(data[2]).replace("_", " ").capitalize())

        # First convert booked_time from seconds since epoch to a python time object
        date = time.strftime("%A %d %B %Y", time.gmtime(data[3]))
        hour = time.strftime("%H:%M", time.gmtime(data[3]))
        session_date_and_time = QLabel("Date: " + date + " Time: " + hour)

        # Add the cancel button
        cancel_button = QPushButton("Cancel")
        cancel_button.setObjectName("cancel_button")
        cancel_button.setFixedSize(80, 50)
        cancel_button.setStyleSheet("QPushButton#cancel_button {"
                                    "border-radius: 5px;"
                                    "background-color: red;"
                                    "color: white; }")
        cancel_button.clicked.connect(lambda: self.session_clicked(data[0]))

        information_layout.addWidget(session_facility, 0, 0)
        information_layout.addWidget(session_activity, 1, 0)
        information_layout.addWidget(session_date_and_time, 2, 0)
        information_layout.addWidget(cancel_button, 0, 1, 3, 1)

        card.setLayout(card_layout)

        return card

    def session_clicked(self, session_id):
        self.mainWindow.database.exeStatement("DELETE FROM sessions WHERE id = ?", str(session_id))
        self.mainWindow.changePage("Sessions", "Sessions")

    def getSessions(self):
        return self.mainWindow.database.getData("SELECT * FROM sessions WHERE booker = ?", str(account.user_id))
