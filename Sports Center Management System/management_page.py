import math

#Imports below are needed for the program to work
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import matplotlib.pyplot as p

class ManagementPage(QWidget): #Main class for management page
    def __init__(self, mainWindow): #Initialisation  of main variables
        super().__init__() #Uses the init function of the of the main window
        self.mainWindow = mainWindow #Initialises the main window var

        #Sorts out the main window
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)

        #Title label
        label = QLabel("Management Page", self) #Label
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) #Aligns it in center
        label.setMaximumHeight(50) #Makes it 50 pixels tall
        label.setStyleSheet("background-color: #00ffff") #Sets the background colour to cyan
        label.setStyleSheet("font: bold 18px;") #Changes the font to be bold and size of 18

        #Code below creates buttons that can be clicked ad changes the size of them

        test_graph_button = QPushButton("GRAPHS")
        test_graph_button.setFixedSize(250, 50)
        test_graph_button.setCheckable(True)
        test_graph_button.clicked.connect(self.graph)
        test_graph_button.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        # Amend Prices button
        amend_prices_button = QPushButton("Amend Facilities or Activities") #Button
        amend_prices_button.setFixedSize(250, 50) #Sets the size of the button to 250x50
        amend_prices_button.setCheckable(True) #Allows the button to be clicked
        amend_prices_button.clicked.connect(self.sessions) #Connects the button to the sessions function when clicked
        amend_prices_button.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;") #Styles the button

        add = QPushButton("Add Facilities or Activities")
        add.setFixedSize(250, 50)
        add.setCheckable(True)
        add.clicked.connect(self.add)
        add.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        # Add Staff Members button
        add_staff_members_button = QPushButton("Add Staff Members")
        add_staff_members_button.setFixedSize(250, 50)
        add_staff_members_button.setCheckable(True)
        add_staff_members_button.clicked.connect(self.submit_staff)
        add_staff_members_button.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        # Staff info
        staff = QLabel("Staff Information")
        staff.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black;")
        staff.setFixedSize(250, 30)
        staff.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Code below creates text multiple text fields for admins to enter for a new staff

        self.fn = QLineEdit(self) #Creates a text field
        self.fn.setFixedSize(250, 30) #Changes the size to 250x30
        self.fn.setPlaceholderText("Enter First Name") #Text that tells you what its for
        self.fn.setStyleSheet("border-radius: 10px;"
                                            "color: black;") #Sets the outline of the box to black
        self.ln = QLineEdit(self)
        self.ln.setFixedSize(250, 30)
        self.ln.setPlaceholderText("Enter Last Name")
        self.ln.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.email = QLineEdit(self)
        self.email.setFixedSize(250, 30)
        self.email.setPlaceholderText("Enter Email")
        self.email.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.password = QLineEdit(self)
        self.password.setFixedSize(250, 30)
        self.password.setPlaceholderText("Enter Password")
        self.password.setStyleSheet("border-radius: 10px;"
                                            "color: black;")

        self.priority = QComboBox() #Creates a combobox
        self.priority.addItems(["1 - Employee", "2 - Manager"]) #Items in the combo box
        self.priority.setFixedSize(250, 35) #Sizes the combo box
        self.priority.setStyleSheet("border-radius: 10px;"
                                            "color: black;") #Outlines the combo box with a 10px black border
        # Change Discount button
        change_discount_button = QPushButton("Change Discount")
        change_discount_button.setFixedSize(250, 50)
        change_discount_button.setCheckable(True)
        change_discount_button.clicked.connect(self.discount_click)
        change_discount_button.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        old_discount_val = self.mainWindow.database.getData("SELECT discount FROM discount")[0][0] #Gets the old discount value from the database

        discount_label = QLabel("Change Discount")
        old_discount_label = QLabel("Old Discount Value: " + str(old_discount_val) + "%")

        discount_label.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black;")
        discount_label.setFixedSize(250, 30)
        discount_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        old_discount_label.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black;")
        old_discount_label.setFixedSize(250, 30)
        old_discount_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.discount = QComboBox()
        self.discount.addItems(["0", "15", "20", "30", "40"])
        self.discount.setFixedSize(250, 35)
        self.discount.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        back = QPushButton("Back")
        back.setFixedSize(250, 50)
        back.setCheckable(True)
        back.clicked.connect(self.back)
        back.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        """ 
        The code below adds all of the buttons and widgets to the layout
        It has 1 horizontal layout and 3 vertical layout
        The vertical layouts allow a neat column display for 3 different options and functions
        The left column is the button to take you to different pages
        The middle column allows you to add a staff member
        The right column allows you to amend the current discount
        """
        # Adding the buttons to a layout
        buttonLayout = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()
        v3 = QVBoxLayout()

        v1.addWidget(amend_prices_button, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(add, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(test_graph_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Staff
        v2.addWidget(staff, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.fn, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.ln, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.email, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.password, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.priority, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(add_staff_members_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Discount Box
        v3.addWidget(discount_label, alignment=Qt.AlignmentFlag.AlignCenter)
        v3.addWidget(old_discount_label, alignment=Qt.AlignmentFlag.AlignCenter)
        v3.addWidget(self.discount, alignment=Qt.AlignmentFlag.AlignCenter)
        v3.addWidget(change_discount_button, alignment=Qt.AlignmentFlag.AlignCenter)

        buttonLayout.addLayout(v1)
        buttonLayout.addLayout(v2)
        buttonLayout.addLayout(v3)

        mainLayout.addWidget(label)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(back, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(mainLayout)

    def discount_click(self):
        # Gets the current value in the combo box
        discount_val = str(self.discount.currentText())
        self.mainWindow.database.exeStatement("UPDATE discount SET discount = (?)", discount_val) #Updates the discount value

        self.mainWindow.changePage("Management Page", "Management Page") #Refreshes the page

    def submit_staff(self):
        #Gets the values inputted from each of the text fields
        fn = self.fn.text()
        ln = self.ln.text()
        email = self.email.text()
        pw = self.password.text()
        priority = str(self.priority.currentIndex() + 1)

        self.mainWindow.database.exeStatement("INSERT INTO users (first_name, last_name, email, password, priority) "
                                              "VALUES (?, ?, ?, ?, ?)", fn, ln, email, pw, priority) #Updates it into the database

        self.mainWindow.changePage("Management Page", "Management Page") #Refreshes the page

    def sessions(self):
        self.mainWindow.changePage("Edit Info", "Management Page") #Takes you to the edit info page
    def add(self):
        self.mainWindow.changePage("Add Info", "Management Page") #Takes you to the add info page

    def back(self):
        self.mainWindow.changePage("Login", "Management Page") #Takes you back to the login page

    def graph(self):
        self.mainWindow.changePage("Graph Page", "Management Page")


class EditInfo(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)

        label1 = QLabel("Update Facility", self)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label1.setMaximumHeight(50)
        label1.setStyleSheet("background-color: #ff00ff")
        label1.setStyleSheet("font: bold 18px;")

        # Submit Info Button
        update_info_button = QPushButton("Update Information")
        update_info_button.setFixedSize(250, 50)
        update_info_button.setCheckable(True)
        update_info_button.clicked.connect(self.submit_facility_info)
        update_info_button.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        #Facility Info

        label2 = QLabel("Select Facility", self)
        label2.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black;")
        label2.setFixedSize(250, 30)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.name = QLineEdit(self)
        self.name.setFixedSize(250, 30)
        self.name.setPlaceholderText("Enter The New Name")
        self.name.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.cap = QLineEdit(self)
        self.cap.setFixedSize(250, 30)
        self.cap.setPlaceholderText("Enter The New Capacity")
        self.cap.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        #Activity Info
        update_info_button2 = QPushButton("Update Information")
        update_info_button2.setFixedSize(250, 50)
        update_info_button2.setCheckable(True)
        update_info_button2.clicked.connect(self.submit_activity_info)
        update_info_button2.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        label3 = QLabel("Select Activity", self)
        label3.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black;")
        label3.setFixedSize(250, 30)
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label4 = QLabel("Select Facility", self)
        label4.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black;")
        label4.setFixedSize(250, 30)
        label4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.actName = QLineEdit(self)
        self.actName.setFixedSize(250, 30)
        self.actName.setPlaceholderText("Enter The New Activity Name")
        self.actName.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        label5 = QLabel("Select New Facility", self)
        label5.setStyleSheet("border: 1px solid black; border-radius: 10px; color: black;")
        label5.setFixedSize(250, 30)
        label5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.price = QLineEdit(self)
        self.price.setFixedSize(250, 30)
        self.price.setPlaceholderText("Enter The New Price")
        self.price.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        back = QPushButton("Back")
        back.setFixedSize(250, 50)
        back.setCheckable(True)
        back.clicked.connect(self.back)
        back.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        """
        Code below gets the available activities and facilities 
        It gets them from the database and the adds them to a list 
        This way allows me to add the list to a combo box
        """

        activities = self.mainWindow.database.getData("SELECT DISTINCT(activity) FROM activities") #Gets the activities from the database
        act_list = [] #Creates a list to store the activities
        for act in activities: #Loops for each activity
            act_list.append(act[0]) #Appends it to the list so they can be used

        facilities = self.mainWindow.database.getData("SELECT * FROM facilities")
        fac_list = []
        for fac in facilities:
            fac_list.append(str(fac[1]))

        self.acts = QComboBox()
        self.acts.addItems(act_list)
        self.acts.setFixedSize(250, 35)
        self.acts.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.fac2 = QComboBox()
        self.fac2.addItems(fac_list)
        self.fac2.setFixedSize(250, 35)
        self.fac2.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.fac3 = QComboBox()
        self.fac3.addItems(fac_list)
        self.fac3.setFixedSize(250, 35)
        self.fac3.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.fac = QComboBox()
        self.fac.addItems(fac_list)
        self.fac.setFixedSize(250, 35)
        self.fac.setStyleSheet("border-radius: 10px;"
                                            "color: black;")

        # Adding the buttons to a layout
        buttonLayout = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()

        v1.addWidget(label3, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(self.acts, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(self.actName, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(label4, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(self.fac, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(label5, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(self.fac3, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(self.price, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(update_info_button2, alignment=Qt.AlignmentFlag.AlignCenter)

        v2.addWidget(label2, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.fac2, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.cap, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(update_info_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Info

        buttonLayout.addLayout(v1)
        buttonLayout.addLayout(v2)

        mainLayout.addWidget(label1)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(back, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(mainLayout)
    def submit_activity_info(self):
        #Gets the current text from the fields
        act = str(self.acts.currentText())
        fac = str(self.fac.currentText())
        new_fac = str(self.fac3.currentText())
        new_name = self.actName.text()
        price = str(self.price.text())

        self.mainWindow.database.getData("UPDATE activities SET price = (?), activity = (?), facility = (?) WHERE facility = (?) AND activity = (?)", price, new_name, new_fac, fac, act) #Updates the database

        self.mainWindow.changePage("Edit Info", "Edit Info") #Refreshes the page

    def submit_facility_info(self):
        #Gets the current text from the fields
        fac = str(self.fac2.currentText())
        new_name = self.name.text()
        new_cap = self.cap.text()

        #Updates the database
        self.mainWindow.database.getData("UPDATE facilities SET facility = (?) WHERE facility = (?)", new_name, fac)
        self.mainWindow.database.getData("UPDATE facilities SET capacity = (?) WHERE facility = (?)", new_cap, fac)

        self.mainWindow.changePage("Edit Info", "Edit Info") #Refreshes the page

    def back(self):
        self.mainWindow.changePage("Management Page", "Edit Info") #Changes the page back to the management page

class Add_Act_Fac(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)

        label1 = QLabel("Add Facility", self)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label1.setMaximumHeight(50)
        label1.setStyleSheet("background-color: #ff00ff")
        label1.setStyleSheet("font: bold 18px;")

        # Submit Info Button
        update_info_button = QPushButton("Add Activity")
        update_info_button.setFixedSize(250, 50)
        update_info_button.setCheckable(True)
        update_info_button.clicked.connect(self.submit_facility_info)
        update_info_button.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        #Facility Info
        self.name = QLineEdit(self)
        self.name.setFixedSize(250, 30)
        self.name.setPlaceholderText("Enter The Facility Name")
        self.name.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.cap = QLineEdit(self)
        self.cap.setFixedSize(250, 30)
        self.cap.setPlaceholderText("Enter The Capacity")
        self.cap.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        #Activity Info
        update_info_button2 = QPushButton("Update Information")
        update_info_button2.setFixedSize(250, 50)
        update_info_button2.setCheckable(True)
        update_info_button2.clicked.connect(self.submit_activity_info)
        update_info_button2.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        self.actName = QLineEdit(self)
        self.actName.setFixedSize(250, 30)
        self.actName.setPlaceholderText("Enter The Activity Name")
        self.actName.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        facilities = self.mainWindow.database.getData("SELECT * FROM facilities")
        fac_list = []
        for fac in facilities:
            fac_list.append(str(fac[1]))

        self.fac = QComboBox()
        self.fac.addItems(fac_list)
        self.fac.setFixedSize(250, 35)
        self.fac.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        self.price = QLineEdit(self)
        self.price.setFixedSize(250, 30)
        self.price.setPlaceholderText("Enter The Price")
        self.price.setStyleSheet("border-radius: 10px;"
                                            "color: black;")
        back = QPushButton("Back")
        back.setFixedSize(250, 50)
        back.setCheckable(True)
        back.clicked.connect(self.back)
        back.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        # Adding the buttons to a layout
        buttonLayout = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()

        v1.addWidget(self.actName, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(self.fac, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(self.price, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(update_info_button2, alignment=Qt.AlignmentFlag.AlignCenter)

        v2.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(self.cap, alignment=Qt.AlignmentFlag.AlignCenter)
        v2.addWidget(update_info_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Info

        buttonLayout.addLayout(v1)
        buttonLayout.addLayout(v2)

        mainLayout.addWidget(label1)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(back, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(mainLayout)
    def submit_activity_info(self):
        #Gets the inputs from the text fields
        new_act = self.actName.text()
        new_fac = self.fac.currentText()
        price = str(self.price.text())

        self.mainWindow.database.exeStatement("INSERT INTO activities (activity, facility, price) VALUES (?, ?, ?)", new_act, new_fac, price) #Updates the database

        self.mainWindow.changePage("Add Info", "Add Info") #Refreshes the page

    def submit_facility_info(self):
        #Gets the inputs from the text fields
        new_name = self.name.text()
        new_cap = self.cap.text()

        self.mainWindow.database.exeStatement("INSERT INTO facilities (facility, capacity) VALUES (?, ?)", new_name, new_cap) #Updates the database

        self.mainWindow.changePage("Add Info", "Add Info") #Refreshes the pool

    def back(self):
        self.mainWindow.changePage("Management Page", "Edit Info") #Refreshes the page

class Graphs(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)

        label1 = QLabel("Graphs", self)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label1.setMaximumHeight(50)
        label1.setStyleSheet("background-color: #ff00ff")
        label1.setStyleSheet("font: bold 18px;")

        use_fac = QPushButton("Usage / Facilities")
        use_fac.setFixedSize(250, 50)
        use_fac.setCheckable(True)
        use_fac.clicked.connect(self.graph1)
        use_fac.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        use_fac1 = QPushButton("Activity Usage / Swimming Pool")
        use_fac1.setFixedSize(250, 50)
        use_fac1.setCheckable(True)
        use_fac1.clicked.connect(self.graph2)
        use_fac1.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        use_fac2 = QPushButton("Activity Usage / Fitness Room")
        use_fac2.setFixedSize(250, 50)
        use_fac2.setCheckable(True)
        use_fac2.clicked.connect(self.graph3)
        use_fac2.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        use_fac3 = QPushButton("Activity Usage / Squash Court")
        use_fac3.setFixedSize(250, 50)
        use_fac3.setCheckable(True)
        use_fac3.clicked.connect(self.graph4)
        use_fac3.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        use_fac4 = QPushButton("Activity Usage / Sports Hall")
        use_fac4.setFixedSize(250, 50)
        use_fac4.setCheckable(True)
        use_fac4.clicked.connect(self.graph5)
        use_fac4.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        use_fac5 = QPushButton("Activity Usage / Climbing Wall")
        use_fac5.setFixedSize(250, 50)
        use_fac5.setCheckable(True)
        use_fac5.clicked.connect(self.graph6)
        use_fac5.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        use_fac6 = QPushButton("Activity Usage / Studio")
        use_fac6.setFixedSize(250, 50)
        use_fac6.setCheckable(True)
        use_fac6.clicked.connect(self.graph7)
        use_fac6.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")

        back = QPushButton("Back")
        back.setFixedSize(250, 50)
        back.setCheckable(True)
        back.clicked.connect(self.back)
        back.setStyleSheet("background-color: #220C10;"
                                   "border-radius: 10px;"
                                   "color: white;"
                                   "font-size: 16px;"
                                   "margin: 10px 0px 0px 0px;")
        # Adding the buttons to a layout
        buttonLayout = QHBoxLayout()
        v1 = QVBoxLayout()
        v2 = QVBoxLayout()

        v1.addWidget(use_fac, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(use_fac1, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(use_fac2, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(use_fac3, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(use_fac4, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(use_fac5, alignment=Qt.AlignmentFlag.AlignCenter)
        v1.addWidget(use_fac6, alignment=Qt.AlignmentFlag.AlignCenter)


        buttonLayout.addLayout(v1)
        buttonLayout.addLayout(v2)

        mainLayout.addWidget(label1)
        mainLayout.addLayout(buttonLayout)
        mainLayout.addWidget(back, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(mainLayout)

    def graph1(self):
        facilities = self.mainWindow.database.getData("SELECT * FROM facilities")
        fac_list = []
        for fac in facilities:
            fac_list.append(str(fac[1]))

        usage_list = []
        for fac in fac_list:
            usage = self.mainWindow.database.getData("SELECT count(activity) FROM activities WHERE facility = (?)", fac)
            for use in usage:
                usage_list.append(int(str(use[0])))

        fig = p.figure()
        ax = fig.add_subplot(111)
        p.xticks(rotation=90)
        p.xlabel("Facility")
        p.ylabel("Usage")
        p.title("Usage of each Facility")
        ax.bar(fac_list, usage_list)
        fig.tight_layout()
        p.savefig("Management Graphs/Use_Fac.png", bbox_inches = "tight")
        p.show()

    def graph2(self):
        act_list = []
        usage_list = []

        activities = self.mainWindow.database.getData("SELECT distinct(activity) FROM activities")
        for act in activities:
            act_list.append(str(act[0]))
            usage = self.mainWindow.database.getData("SELECT count(activity) FROM sessions WHERE facility = 'swimming_pool' AND activity = (?)", str(act[0]))
            for use in usage:
                usage_list.append(int(str(use[0])))

        fig = p.figure()
        ax = fig.add_subplot(111)
        p.xticks(rotation=90)
        p.xlabel("Activity")
        p.ylabel("Usage")
        p.title("Usage of each Activity in the Swimming Pool")
        ax.bar(act_list, usage_list)
        fig.tight_layout()
        p.savefig("Management Graphs/Swim_Act_Use.png", bbox_inches = "tight")
        p.show()

    def graph3(self):
        act_list = []
        usage_list = []

        activities = self.mainWindow.database.getData("SELECT distinct(activity) FROM activities")
        for act in activities:
            act_list.append(str(act[0]))
            usage = self.mainWindow.database.getData("SELECT count(activity) FROM sessions WHERE facility = 'fitness_room' AND activity = (?)", str(act[0]))
            for use in usage:
                usage_list.append(int(str(use[0])))

        fig = p.figure()
        ax = fig.add_subplot(111)
        p.xticks(rotation=90)
        p.xlabel("Activity")
        p.ylabel("Usage")
        p.title("Usage of each Activity in the Fitness Room")
        ax.bar(act_list, usage_list)
        fig.tight_layout()
        p.savefig("Management Graphs/Fitn_Act_Use.png", bbox_inches = "tight")
        p.show()

    def graph4(self):
        act_list = []
        usage_list = []

        activities = self.mainWindow.database.getData("SELECT distinct(activity) FROM activities")
        for act in activities:
            act_list.append(str(act[0]))
            usage = self.mainWindow.database.getData(
                "SELECT count(activity) FROM sessions WHERE facility = 'squash_court' AND activity = (?)", str(act[0]))
            for use in usage:
                usage_list.append(int(str(use[0])))

        fig = p.figure()
        ax = fig.add_subplot(111)
        p.xticks(rotation=90)
        p.xlabel("Activity")
        p.ylabel("Usage")
        p.title("Usage of each Activity in the Squash Court")
        ax.bar(act_list, usage_list)
        fig.tight_layout()
        p.savefig("Management Graphs/Squa_Act_Use.png", bbox_inches="tight")
        p.show()

    def graph5(self):
        act_list = []
        usage_list = []

        activities = self.mainWindow.database.getData("SELECT distinct(activity) FROM activities")
        for act in activities:
            act_list.append(str(act[0]))
            usage = self.mainWindow.database.getData(
                "SELECT count(activity) FROM sessions WHERE facility = 'sports_hall' AND activity = (?)", str(act[0]))
            for use in usage:
                usage_list.append(int(str(use[0])))

        fig = p.figure()
        ax = fig.add_subplot(111)
        p.xticks(rotation=90)
        p.xlabel("Activity")
        p.ylabel("Usage")
        p.title("Usage of each Activity in the Sports Hall")
        ax.bar(act_list, usage_list)
        fig.tight_layout()
        p.savefig("Management Graphs/SportH_Act_Use.png", bbox_inches="tight")
        p.show()

    def graph6(self):
        act_list = []
        usage_list = []

        activities = self.mainWindow.database.getData("SELECT distinct(activity) FROM activities")
        for act in activities:
            act_list.append(str(act[0]))
            usage = self.mainWindow.database.getData(
                "SELECT count(activity) FROM sessions WHERE facility = 'climbing_wall' AND activity = (?)", str(act[0]))
            for use in usage:
                usage_list.append(int(str(use[0])))

        fig = p.figure()
        ax = fig.add_subplot(111)
        p.xticks(rotation=90)
        p.xlabel("Activity")
        p.ylabel("Usage")
        p.title("Usage of each Activity in the Climbing Wall")
        ax.bar(act_list, usage_list)
        fig.tight_layout()
        p.savefig("Management Graphs/Climb_Act_Use.png", bbox_inches="tight")
        p.show()
    def graph7(self):
        act_list = []
        usage_list = []

        activities = self.mainWindow.database.getData("SELECT distinct(activity) FROM activities")
        for act in activities:
            act_list.append(str(act[0]))
            usage = self.mainWindow.database.getData(
                "SELECT count(activity) FROM sessions WHERE facility = 'studio' AND activity = (?)", str(act[0]))
            for use in usage:
                usage_list.append(int(str(use[0])))

        fig = p.figure()
        ax = fig.add_subplot(111)
        p.xticks(rotation=90)
        p.xlabel("Activity")
        p.ylabel("Usage")
        p.title("Usage of each Activity in the Studio")
        ax.bar(act_list, usage_list)
        fig.tight_layout()
        p.savefig("Management Graphs/Studio_Act_Use.png", bbox_inches="tight")
        p.show()
    def back(self):
        self.mainWindow.changePage("Management Page", "Graph Info")
