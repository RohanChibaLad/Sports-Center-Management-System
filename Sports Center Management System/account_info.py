class Account:
    def __init__(self):
        # variable to store user id
        self.user_id = None
        # variable to store first name
        self.firstname = None
        # variable to store last name
        self.lastname = None
        # variable to store email
        self.email = None
        # variable to store password
        self.password = None
        # variable to store password check
        self.password_check = None
        # variable to store account type
        self.account_type = 0
        # variable to store membership type
        self.membership_type = 0
        # variable to see if the user is going to update details or add new ones
        self.edit_details = False
        # variable to store card number
        self.card_number = None
        # variable to store name on card
        self.name_on_card = None
        # variable to store expiry date
        self.expiry_date = None
        # variable to store cvv
        self.cvv = None

        # variable to track what facility was clicked on the home page
        self.clicked_facility = None

        # variable to store sql statements to insert sessions into the database
        # this variable is only used when a user does not have a membership and
        # gets redirected to the payment page, in which this variable saves the
        # statements to get executed once the user has filled out the payment information
        self.sql_statements = []

    def clear_account(self):
        self.user_id = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.password = None
        self.password_check = None
        self.account_type = 0
        self.membership_type = 0
        self.edit_details = False

        self.card_number = None
        self.name_on_card = None
        self.expiry_date = None
        self.cvv = None

        self.clicked_facility = None

        self.sql_statements = []


account = Account()
