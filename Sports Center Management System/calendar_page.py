import time
from datetime import datetime, timedelta, date

from PyQt6.QtCore import Qt, QSize

from navbar import *


class CalendarPage(QWidget):
    """
        A class used to represent the page to book time slots

        ...

        Attributes
        -----------
        selected_date : Date
            Stores the selected date on the calendar

        week_ranges : list
            stores the start and end of each of the weeks

        mainWindow : QMainWindow
            stores the main window the page will appear in

        default_bookable_times : List
            stores all the times which are available to book by default

        activity_menu : QComboBox
            The drop-down menu for selecting your activity

        time_menu : QComboBox
            The drop-down menu to select what time you are booking

        Methods
        --------
        find_week_ranges()
            updates week_ranges

        facility_change()
            updates activity dropdown

        export_calendar()
            updates database

        clicked_date(q_date)
            Updates selected date
    """

    def __init__(self, main_window):
        """
            Initialises calendar window

            :param main_window: QMainWindow
        """
        super().__init__()

        self.selected_date = None

        navbar = Navbar("calendar", main_window).getNavbar()

        # List to store the start and ends of each of the weeks
        self.week_ranges = []
        self.find_week_ranges()

        # the times available to book on
        self.default_bookable_times = ["8:00",
                                       "9:00",
                                       "10:00",
                                       "11:00",
                                       "12:00",
                                       "13:00",
                                       "14:00",
                                       "15:00",
                                       "16:00",
                                       "17:00",
                                       "18:00",
                                       "19:00",
                                       "20:00",
                                       "21:00",
                                       "22:00"]

        self.mainWindow = main_window

        # initialise title label
        title = QLabel("Calendar Page", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Get all facilities from database and add to dropdown menu
        self.mainWindow.database.exeStatement("SELECT * FROM facilities")
        facilities = self.mainWindow.database.cursor.fetchall()

        self.activity_menu = QComboBox(self)

        self.time_menu = QComboBox(self)
        self.time_menu.addItems(self.default_bookable_times)

        # Call facility_change once to fill the initial activities
        self.facility_change()

        # Button to get all the selected sessions and to re-direct to a payment page if user has no membership
        book_sessions_layout = QVBoxLayout()
        book_sessions = QPushButton("Book Selected Sessions")
        book_sessions.setFixedSize(250, 50)
        book_sessions.clicked.connect(self.export_calendar)
        book_sessions_layout.addWidget(book_sessions)

        # initialise main layout
        page_layout = QVBoxLayout()
        page_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # initialise left layout in calendar layout
        left_cal_layout = QVBoxLayout()
        calendar = QCalendarWidget()
        calendar.clicked.connect(self.clicked_date)
        self.clicked_date(calendar.selectedDate())
        calendar.setMinimumDate(date.today())
        calendar.setMaximumDate(date.today() + timedelta(weeks=3) - timedelta(days=date.today().weekday()+1))
        left_cal_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_cal_layout.addStretch(1)
        calendar.setMinimumSize(QSize(300, 300))
        left_cal_layout.addWidget(calendar)
        left_cal_layout.addStretch(1)

        # initialise right layout in calendar layout
        right_cal_layout = QVBoxLayout()
        right_cal_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        right_cal_layout.addWidget(self.activity_menu)
        right_cal_layout.addWidget(self.time_menu)

        # initialise calendar layout
        cal_layout = QHBoxLayout()
        cal_layout.addLayout(left_cal_layout)
        cal_layout.addLayout(right_cal_layout)

        # add title and time selection to main
        page_layout.addWidget(navbar)
        page_layout.addWidget(title)
        page_layout.addLayout(cal_layout)
        page_layout.addLayout(book_sessions_layout)
        book_sessions_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setLayout(page_layout)

    def find_week_ranges(self):
        """
        Method to find the start and end of the current and 2 upcoming weeks and add them to self.week_ranges
        """

        for i in range(3):
            # Store a date that is in the current week iteration
            today = date.today() + timedelta(days=i * 7)

            # Find the start of that week
            start = today - timedelta(days=today.weekday())

            # Parse the start and end dates and then format it to a nice readable format
            start_of_week = time.strftime("%A %d %B %Y", time.strptime(str(start), "%Y-%m-%d"))
            end_of_week = time.strftime("%A %d %B %Y", time.strptime(str(start + timedelta(days=6)), "%Y-%m-%d"))

            # Add each start and end dates to the week ranges list
            self.week_ranges.append([start_of_week, end_of_week])

    def facility_change(self):
        """
        Updates the activity dropdown with the respective activities when a facility is chosen
        """

        # First clear the activity dropdown
        self.activity_menu.clear()

        # Get the current facility selected and format it to what the database expects
        current_facility = account.clicked_facility.replace(" ", "_").lower()

        # Query the database for the selected facility activities
        activities = self.mainWindow.database.getData("SELECT * FROM activities WHERE facility = (?)", current_facility)

        # Loop through the activities for that facility and add them to the activity dropdown
        for activity in activities:
            self.activity_menu.addItems([str(activity[1]).replace("_", " ").capitalize() + " - £" + str(activity[3])])

    def export_calendar(self):
        """
        Changes the database to reflect the changes made to the calendar

        Called when the book sessions button is clicked
        """

        # List to store the data for all the selected sessions to book
        sql_statement_data = []

        # add to database
        sql_time = self.selected_date
        sql_facility = account.clicked_facility
        sql_activity = self.activity_menu.currentText().split("-")[0].strip().replace(" ", "_").lower()
        sql_user_id = str(account.user_id)
        sql_team_session = "1" if sql_activity == "team_events" else "0"

        account.sql_statements.append(
            [sql_time, sql_facility, sql_activity, str(account.user_id), sql_team_session])

        # Re-direct to a payment page here if user does not have membership, and pass sql_statement_data so after
        # the user has paid, all their selected sessions can be inserted into the database. This also allows us
        # to count how many sessions were selected, so we can determine whether to apply the discount or not
        if account.membership_type == 0:
            # Empty the sql statements variable beforehand to prevent any statements from previous
            # bookings getting passed along
            account.sql_statements += sql_statement_data
            self.mainWindow.changePage("Home", "Calendar")
        else:
            # If the user has a membership we want to immediately add their selected sessions to the database
            for statement in sql_statement_data:
                self.mainWindow.database.exeStatement("INSERT INTO sessions (facility, activity, booked_time, booker, "
                                                      "team_session) VALUES (?, ?, ?, ?, ?)", statement[1], statement[2],
                                                      statement[0], str(account.user_id), statement[4])
            self.mainWindow.changePage("Home", "Calendar")

    def clicked_date(self, q_date):
        """
        Is called when a date is clicked on the calendar
        Takes the QDate selected in the calendar provided and updates self.selected_date to that new date

        :param q_date: QDate
            The date that is currently selected
        """

        # convert to Date format from QDate
        date_clicked = q_date.toPyDate()

        # store as a dateTime by adding the value of the time menu to the date
        self.selected_date = (datetime(date_clicked.year, date_clicked.month, date_clicked.day) +
                              timedelta(hours=int(self.time_menu.currentText().split(":")[0]))).timestamp()
