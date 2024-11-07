import time

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

from account_info import account
from navbar import Navbar


class BasketPage(QWidget):
    """
        Class that represents the basket page used to pay for sessions when
        the logged-in user does not have a membership

        Attributes
        ----------
        mainWindow : QMainWindow
            the main window object that is passed to be able to control
            what the central widget is, change pages and communicate with
            the database object

        sessionsGrid : QGridLayout
            grid layout that is dynamically filled when sessions are booked
            to display the sessions that are in the basket

        price : int
            stores the price of the session and is later than manipulated
            if a discount is applied

        apply_discount : Boolean
            whether to apply the discount based on how many booked sessions

        discount : int
            the discount amount as determined what is saved in the database,
            can be changed in the management page

        Methods
        --------
        generate_listings(session, iterator, sessionsGrid)
            creates a row in the sessionsGrid layout for each booked session

        cancel_button_click(session)
            removes a booked session from the basket

        pay_button_click()
            pays for the booked sessions, will direct to the payment page
    """

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(50, 30, 50, 0)

        navbar = Navbar("Basket", self.mainWindow).getNavbar()

        # Initialises the grid layout for the booked sessions
        sessionsGrid = QGridLayout()
        sessionsGrid.setContentsMargins(5, 20, 5, 0)
        sessionsGrid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sessionsGrid.setVerticalSpacing(20)

        self.setStyleSheet("QLabel { font-size: 18px;}")

        # Set a strech in each column of the grid to correctly lay out the element
        for i in range(7):
            sessionsGrid.setColumnStretch(i, 1)

        # Add the grid column headings
        sessionsGrid.addWidget(QLabel("Facility"), 0, 0)
        sessionsGrid.addWidget(QLabel("Activity"), 0, 1)
        sessionsGrid.addWidget(QLabel("Date"), 0, 2)
        sessionsGrid.addWidget(QLabel("Time"), 0, 3)
        sessionsGrid.addWidget(QLabel("Team Session"), 0, 4)
        sessionsGrid.addWidget(QLabel("Price"), 0, 5)
        sessionsGrid.addWidget(QLabel("Cancel Booking"), 0, 6)

        self.price = 0

        # Determine if we need to apply discount
        apply_discount = True if len(account.sql_statements) >= 3 else False
        discount = 0

        # Get number of booked sessions
        no_of_booked_sessions = len(account.sql_statements)

        # Generate a row listing for each booked session
        for i in range(no_of_booked_sessions):
            self.generate_listing(account.sql_statements[i], i+1, sessionsGrid)

        # If we apply a discount, find the discount amount and display the amount
        # to the user
        if apply_discount:
            discount = self.mainWindow.database.getData("SELECT discount FROM discount")[0][0]
            discount_label = QLabel("Discount Applied! " + str(discount) + "%")
            discount_label.setStyleSheet("color: green;")
            sessionsGrid.addWidget(discount_label, no_of_booked_sessions + 2, 4)

        # Determine the cost depending on if we apply a discount
        cost = self.price * (1 - discount / 100) if apply_discount else self.price

        sessionsGrid.addWidget(QLabel("Total: £" + str(cost)), no_of_booked_sessions + 2, 5)

        # Add pay button
        pay_button = QPushButton("Pay")
        pay_button.setFixedSize(80, 40)
        pay_button.setStyleSheet("background-color: #220C10;"
                                 "border-radius: 5px;"
                                 "color: white;"
                                 "font-size: 18px;"
                                 "alignment: center;")
        pay_button.clicked.connect(self.pay_button_click)

        pay_button_layout = QHBoxLayout()
        pay_button_layout.addStretch(1)
        pay_button_layout.addWidget(pay_button)
        pay_button_layout.addStretch(1)

        mainLayout.addWidget(navbar)
        mainLayout.addLayout(sessionsGrid)
        mainLayout.addLayout(pay_button_layout)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

    def generate_listing(self, session, i, sessionsGrid):
        # Parse all the data we got from the booked session to be in a nice and readable format
        facility = str(session[1]).replace("_", " ").capitalize()
        activity = str(session[2]).replace("_", " ").capitalize()
        date = time.strftime("%A %d %B %Y", time.gmtime(float(session[0])))
        hour = time.strftime("%H:%M", time.gmtime(float(session[0])))
        team_session = "True" if session[4] == '1' else "False"

        # Add a label for each part of the data
        sessionsGrid.addWidget(QLabel(facility), i, 0)
        sessionsGrid.addWidget(QLabel(activity), i, 1)
        sessionsGrid.addWidget(QLabel(date), i, 2)
        sessionsGrid.addWidget(QLabel(hour), i, 3)
        sessionsGrid.addWidget(QLabel(team_session), i, 4)

        # Get the price as to what is stored in the database
        price = self.mainWindow.database.getData("SELECT price FROM activities WHERE facility = (?) AND activity = (?)",
                                                 str(session[1]), str(session[2]))
        self.price += price[0][0]

        sessionsGrid.addWidget(QLabel("£" + str(price[0][0])), i, 5)

        cancel_button = QPushButton("X")
        cancel_button.setFixedSize(25, 25)
        cancel_button.setStyleSheet("background-color: red; "
                                    "color: white;"
                                    "border-radius: 5px;")
        cancel_button.clicked.connect(lambda: self.cancel_button_click(session))

        sessionsGrid.addWidget(cancel_button, i, 6)

    def cancel_button_click(self, session):
        """
            Called when the 'X' button is clicked on a booked session and
            removes that booked session

        :param session:
            The session the cancel button is for
        """
        account.sql_statements.remove(session)
        self.mainWindow.changePage("Basket", "Basket")

    def pay_button_click(self):
        """
            Called when the pay button is clicked and redirects user
            to payment page
        """
        self.mainWindow.changePage("Payment", "Basket")
