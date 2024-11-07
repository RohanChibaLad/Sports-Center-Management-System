import sqlite3 as sql


class Database:
    """
        Class that represents the database and uses helper methods
        to execute statements and get data from the database.

        Methods
        -------
        exeStatement(statements, *args)
            executes the given statement with the given arguments.
            Uses a replacement technique with ? as placeholders
            (similar to actual SQLite statements) since f strings
            don't seem to work with passing the entire statement as
            a single string

        getData(statement, *args)
            gets data from the database from the given statement and
            returns the retrieved data

        createTable()
            Initialises the table to create all the tables and their
            respective columns

        initialiseStandardInfo()
            initialises the data that should exist in the database by default

        resetDatabase()
            Clears the database. Used for testing purposes
    """

    def __init__(self):
        """1. Creates the database file if file doesn't exist.
            2. Makes a connection"""
        self.connection = sql.connect("database.db")
        self.cursor = self.connection.cursor()
        self.createTable()

    def exeStatement(self, statement, *args):
        # Need to use a replacement trick since f strings don't work with SQL statements
        for i in range(statement.count("?")):
            statement = statement.replace("?", "'" + args[i] + "'", 1)
        self.cursor.execute(statement)
        self.connection.commit()

    def getData(self, statement, *args):
        for i in range(statement.count("?")):
            statement = statement.replace("?", "'" + args[i] + "'", 1)
        self.cursor.execute(statement)
        return self.cursor.fetchall()

    def createTable(self):
        self.cursor.executescript("""
        
        CREATE TABLE IF NOT EXISTS discount (
        discount REAL);
        
        CREATE TABLE IF NOT EXISTS memberships (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_id INT,
        membership_type TEXT,
        membership_expiry INT,
        FOREIGN KEY (user_id) REFERENCES users (id));
        
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        password TEXT,
        priority INT DEFAULT 0);
    
        CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        facility TEXT,
        activity TEXT,
        booked_time INT,
        booker INT,
        team_session INT,
        FOREIGN KEY (facility) REFERENCES facilities (facility),
        FOREIGN KEY (activity) REFERENCES activities (activity),
        FOREIGN KEY (booker) REFERENCES users (id));  

        CREATE TABLE IF NOT EXISTS facilities (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        facility TEXT,
        capacity INT);

        CREATE TABLE IF NOT EXISTS activities (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        activity TEXT,
        facility TEXT,
        price INT,
        FOREIGN KEY (activity) REFERENCES facilities (facility),
        FOREIGN KEY (facility) REFERENCES facilities (facility));
        
        CREATE TABLE IF NOT EXISTS card_information (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        user_id INT,
        card_number INT,
        name_on_card TEXT,
        expiry_date INT,
        cvv INT,
        FOREIGN KEY (user_id) REFERENCES users (id));
        
        """)

        self.connection.commit()

    # Function to insert the standard facilities and activities
    # Copy the below line into the execute script to be able to see the prefill card information feature for the
    # user with user id 2
    # INSERT INTO card_information (user_id, card_number, name_on_card, expiry_date, cvv) VALUES ('2', '1234567812345678', 'test name', '07/25', '666');
    def initialiseStandardInfo(self):
        self.cursor.executescript("""
            INSERT INTO users (first_name, last_name, email, password, priority) VALUES ('admin', 'account', 'admin', 'admin', 2);
            
            INSERT INTO discount (discount) VALUES ('15');
        
            INSERT INTO facilities (facility, capacity) VALUES ('swimming_pool', 30);
            INSERT INTO facilities (facility, capacity) VALUES ('fitness_room', 35);
            INSERT INTO facilities (facility, capacity) VALUES ('squash_court', 2);
            INSERT INTO facilities (facility, capacity) VALUES ('sports_hall', 45);
            INSERT INTO facilities (facility, capacity) VALUES ('climbing_wall', 22);
            INSERT INTO facilities (facility, capacity) VALUES ('studio', 25);
            
            INSERT INTO activities (activity, facility, price) VALUES ('general_use', 'swimming_pool', 5);
            INSERT INTO activities (activity, facility, price) VALUES ('lane_swimming', 'swimming_pool', 10);
            INSERT INTO activities (activity, facility, price) VALUES ('lessons', 'swimming_pool', 15);
            INSERT INTO activities (activity, facility, price) VALUES ('team_events', 'swimming_pool', 25);
            
            INSERT INTO activities (activity, facility, price) VALUES ('general_use', 'fitness_room', 5);
            
            INSERT INTO activities (activity, facility, price) VALUES ('1_hour_session', 'squash_court', 8);
            
            INSERT INTO activities (activity, facility, price) VALUES ('1_hour_session', 'sports_hall', 10);
            INSERT INTO activities (activity, facility, price) VALUES ('team_events', 'sports_hall', 25);
            
            INSERT INTO activities (activity, facility, price) VALUES ('general_use', 'climbing_wall', 7);
            

            INSERT INTO activities (activity, facility, price) VALUES ('pilates', 'studio', 8);
            INSERT INTO activities (activity, facility, price) VALUES ('aerobics', 'studio', 9);
            INSERT INTO activities (activity, facility, price) VALUES ('yoga', 'studio', 18);         
   
            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('lessons', 'swimming_pool', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('general_use', 'swimming_pool', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('lessons', 'swimming_pool', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('lessons', 'swimming_pool', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('lane_swimming', 'swimming_pool', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('team_events', 'swimming_pool', 18, 1, 1);            

            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('general_use', 'fitness_room', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('general_use', 'fitness_room', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('general_use', 'fitness_room', 18, 1, 1);

            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('1_hour_session', 'squash_court', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('1_hour_session', 'squash_court', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('1_hour_session', 'squash_court', 18, 1, 1);            

            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('1_hour_session', 'sports_hall', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('1_hour_session', 'sports_hall', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('1_hour_session', 'sports_hall', 18, 1, 1); 
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('team_events', 'sports_hall', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('team_events', 'sports_hall', 18, 1, 1);
            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('pilates', 'studio', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('pilates', 'studio', 18, 1, 1);            

            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('aerobics', 'studio', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('aerobics', 'studio', 18, 1, 1);            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('aerobics', 'studio', 18, 1, 1);
            
            INSERT INTO sessions (activity, facility, booked_time, booker, team_session) VALUES ('yoga', 'studio', 18, 1, 1);
        """)

        self.connection.commit()

    # Function to reset database to a clean state
    def resetDatabase(self):#
        tables = ["users", "sessions", "memberships", "card_information", "activities", "discount", "facilities"]

        for table in tables:
            self.cursor.execute(f"DROP TABLE IF EXISTS {table}")
        self.connection.commit()

        self.createTable()

        self.initialiseStandardInfo()


# Run this file specifically or click the green arrow on the line below to reset the database
if __name__ == '__main__':
    test = Database()
    test.resetDatabase()
