import mysql.connector
from mysql.connector import Error

def run_hms_queries(connection, cursor):
    """
    Executes the SQL queries from the dbms project PDF.
    Assumes connection and cursor are already established and pointing to 'hms' database.
    """
    print("\n--- Executing Queries ---")

    try:
        # 1. Get All Rooms Information
        print("\nQuery 1: Get All Rooms Information")
        cursor.execute("SELECT * FROM room")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 2. Get Available Rooms
        print("\nQuery 2: Get Available Rooms")
        cursor.execute("SELECT * FROM room WHERE availability = 'Available'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 3. Get Occupied Rooms
        print("\nQuery 3: Get Occupied Rooms")
        cursor.execute("SELECT * FROM room WHERE availability = 'Occupied'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 4. Get Room Details by Room Number
        print("\nQuery 4: Get Room Details for room_number '101'")
        cursor.execute("SELECT * FROM room WHERE room_number = '101'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 5. Get All Customers
        print("\nQuery 5: Get All Customers")
        cursor.execute("SELECT * FROM customer")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 6. Get Customers with Status 'Checked-in'
        print("\nQuery 6: Get Customers with Status 'Checked-in'")
        cursor.execute("SELECT * FROM customer WHERE status = 'Checked-in'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 7. Get Customers with Deposit Greater Than 1000
        print("\nQuery 7: Get Customers with Deposit Greater Than 1000")
        cursor.execute("SELECT * FROM customer WHERE deposit > 1000")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 8. Get Customer Information and Room Details (JOIN)
        print("\nQuery 8: Get Customer Information and Room Details")
        cursor.execute("""
            SELECT c.name, c.room_number, r.bed_type, r.price
            FROM customer c
            JOIN room r ON c.room_number = r.room_number
        """)
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 9. Get Customer Details by Customer ID
        print("\nQuery 9: Get Customer Details by Customer ID 'C001'")
        cursor.execute("SELECT * FROM customer WHERE id = 'C001'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 10. Get Employees Working in Housekeeping Department (job = 'Housekeeper')
        print("\nQuery 10: Get Employees Working in Housekeeping Department")
        cursor.execute("SELECT * FROM employee WHERE job = 'Housekeeper'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 11. Get Employees with Salary Above 30000
        print("\nQuery 11: Get Employees with Salary Above 30000")
        cursor.execute("SELECT * FROM employee WHERE salary > 30000")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 12. Get Driver Information for Available Drivers
        print("\nQuery 12: Get Driver Information for Available Drivers")
        cursor.execute("SELECT * FROM driver WHERE available = 'Yes'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 13. Get All Departments with Their Budget
        print("\nQuery 13: Get All Departments with Their Budget")
        cursor.execute("SELECT * FROM department")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 14. Get Employees from the 'Front Desk' Department (job = 'Receptionist')
        print("\nQuery 14: Get Employees from the 'Front Desk' Department")
        cursor.execute("SELECT * FROM employee WHERE job = 'Receptionist'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 15. Get Rooms by Price Range (BETWEEN 2000 AND 3000)
        print("\nQuery 15: Get Rooms by Price Range (2000-3000)")
        cursor.execute("SELECT * FROM room WHERE price BETWEEN 2000 AND 3000")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 16. Update Customer Status to 'Checked-out' for C001
        print("\nQuery 16: Update Customer Status to 'Checked-out' for C001")
        cursor.execute("UPDATE customer SET status = 'Checked-out' WHERE id = 'C001'")
        connection.commit()
        print(f"Rows updated: {cursor.rowcount}")
        # Verify update
        cursor.execute("SELECT id, status FROM customer WHERE id = 'C001'")
        print("Updated C001 status:", cursor.fetchone())


        # 17. Update Room Availability to 'Occupied' for room 101
        print("\nQuery 17: Update Room Availability to 'Occupied' for room 101")
        cursor.execute("UPDATE room SET availability = 'Occupied' WHERE room_number = '101'")
        connection.commit()
        print(f"Rows updated: {cursor.rowcount}")
        # Verify update
        cursor.execute("SELECT room_number, availability FROM room WHERE room_number = '101'")
        print("Updated room 101 availability:", cursor.fetchone())

        # 18. Insert New Employee
        print("\nQuery 18: Insert New Employee")
        new_employee_data = ('Mark Johnson', '30', 'Male', 'Manager', '50000', '9876543220', '1234567899', 'mark.johnson@example.com')
        # Check if employee already exists to prevent duplicates
        cursor.execute("SELECT COUNT(*) FROM employee WHERE name = 'Mark Johnson'")
        if cursor.fetchone()[0] == 0:
            cursor.execute("""
                INSERT INTO employee (name, age, gender, job, salary, phone, aadhar, email)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, new_employee_data)
            connection.commit()
            print(f"Rows inserted: {cursor.rowcount}")
            print("New employee 'Mark Johnson' inserted.")
        else:
            print("Employee 'Mark Johnson' already exists, skipping insertion.")


        # 19. Delete Room by Room Number
        print("\nQuery 19: Delete Room by Room Number '101'")
        # Note: This might fail if there are foreign key constraints from 'customer' table
        # You might need to delete related customer records first or set ON DELETE CASCADE
        try:
            cursor.execute("DELETE FROM room WHERE room_number = '101'")
            connection.commit()
            print(f"Rows deleted: {cursor.rowcount}")
            print("Room '101' deleted (if no foreign key conflicts).")
        except Error as e:
            print(f"Could not delete room '101' due to foreign key constraint: {e}")
            print("To delete, first remove customers associated with room 101 or modify table schema.")


        # 20. Delete Customer by Customer ID
        print("\nQuery 20: Delete Customer by Customer ID 'C002'")
        cursor.execute("DELETE FROM customer WHERE id = 'C002'")
        connection.commit()
        print(f"Rows deleted: {cursor.rowcount}")
        print("Customer 'C002' deleted.")

        # 21. Get Total Revenue from All Occupied Rooms
        print("\nQuery 21: Get Total Revenue from All Occupied Rooms")
        cursor.execute("SELECT SUM(CAST(price AS UNSIGNED)) AS total_revenue FROM room WHERE availability = 'Occupied'")
        results = cursor.fetchone()
        print(f"Total Revenue from Occupied Rooms: {results[0]}")

        # 22. Get the Number of Rooms in Each Availability Status
        print("\nQuery 22: Get the Number of Rooms in Each Availability Status")
        cursor.execute("SELECT availability, COUNT(*) AS num_rooms FROM room GROUP BY availability")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 23. Get All Employees and Their Job Titles
        print("\nQuery 23: Get All Employees and Their Job Titles")
        cursor.execute("SELECT name, job FROM employee")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 24. Get All Customers Who Stayed in a Specific Room
        print("\nQuery 24: Get All Customers Who Stayed in Room '101'")
        cursor.execute("SELECT c.name, c.room_number, c.status FROM customer c WHERE c.room_number = '101'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 25. Find All Rooms with 'Dirty' Cleaning Status
        print("\nQuery 25: Find All Rooms with 'Dirty' Cleaning Status")
        cursor.execute("SELECT * FROM room WHERE clean_status = 'Dirty'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 26. Find Employees Who Have Worked for More Than 5 Years (based on age > 30)
        print("\nQuery 26: Find Employees Who Have Worked for More Than 5 Years (age > 30)")
        cursor.execute("SELECT * FROM employee WHERE CAST(age AS UNSIGNED) > 30")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 27. Get Customers by Country 'USA'
        print("\nQuery 27: Get Customers by Country 'USA'")
        cursor.execute("SELECT * FROM customer WHERE country = 'USA'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 28. Get the Room with the Highest Price
        print("\nQuery 28: Get the Room with the Highest Price")
        cursor.execute("SELECT * FROM room WHERE CAST(price AS UNSIGNED) = (SELECT MAX(CAST(price AS UNSIGNED)) FROM room)")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 29. Get the Total Number of Employees
        print("\nQuery 29: Get the Total Number of Employees")
        cursor.execute("SELECT COUNT(*) AS total_employees FROM employee")
        results = cursor.fetchone()
        print(f"Total Employees: {results[0]}")

        # 30. Get a List of All Available Rooms Sorted by Price
        print("\nQuery 30: Get All Available Rooms Sorted by Price ASC")
        cursor.execute("SELECT * FROM room WHERE availability = 'Available' ORDER BY CAST(price AS UNSIGNED) ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 31. Get List of Drivers Working for a Specific Company 'ABC Transport'
        print("\nQuery 31: Get List of Drivers Working for 'ABC Transport'")
        cursor.execute("SELECT * FROM driver WHERE company = 'ABC Transport'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 32. Get the Average Salary of Employees
        print("\nQuery 32: Get the Average Salary of Employees")
        cursor.execute("SELECT AVG(CAST(salary AS UNSIGNED)) AS average_salary FROM employee")
        results = cursor.fetchone()
        print(f"Average Salary: {results[0]}")

        # 33. Get List of Customers Who Have Deposited More Than 1000
        print("\nQuery 33: Get List of Customers Who Have Deposited More Than 1000")
        cursor.execute("SELECT * FROM customer WHERE CAST(deposit AS UNSIGNED) > 1000")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 34. Get List of Customers Who Have Checked-out
        print("\nQuery 34: Get List of Customers Who Have Checked-out")
        cursor.execute("SELECT * FROM customer WHERE status = 'Checked-out'")
        results = cursor.fetchall()
        for row in results:
            print(row)

        # 35. Update Employee Salary for 'Sara Parker' to '60000'
        print("\nQuery 35: Update Employee Salary for 'Sara Parker' to '60000'")
        cursor.execute("UPDATE employee SET salary = '60000' WHERE name = 'Sara Parker'")
        connection.commit()
        print(f"Rows updated: {cursor.rowcount}")
        # Verify update
        cursor.execute("SELECT name, salary FROM employee WHERE name = 'Sara Parker'")
        print("Updated Sara Parker salary:", cursor.fetchone())

    except Error as e:
        print(f"Error during query execution: {e}")


def create_database_and_tables():
    """
    Connects to MySQL, creates the 'hms' database, and sets up all tables
    and initial data as defined in the dbms project PDF.
    """
    connection = None
    cursor = None
    try:
        # --- Database Connection Details ---
        # IMPORTANT: Replace with your MySQL server details
        host = "localhost"  # e.g., "localhost", "127.0.0.1"
        user = "your_mysql_username"  # e.g., "root"
        password = "your_mysql_password"  # e.g., "password"
        database = "hms"  # The database name we will create and use

        # Connect to MySQL server (without specifying a database initially)
        print("Attempting to connect to MySQL server...")
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connection.is_connected():
            print(f"Successfully connected to MySQL Server version {connection.get_server_info()}")
            cursor = connection.cursor()

            # --- 1. Create Database ---
            try:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
                print(f"Database '{database}' created or already exists.")
            except Error as e:
                print(f"Error creating database: {e}")
                return # Exit if database creation fails

            # Reconnect to use the newly created database
            connection.disconnect() # Disconnect from the server
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if connection.is_connected():
                print(f"Successfully connected to database '{database}'.")
                cursor = connection.cursor()
            else:
                print("Failed to reconnect to the database.")
                return

            # --- 2. Creating Tables and Inserting Data ---

            # a. Login Table
            print("\nCreating 'login' table and inserting data...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS login (
                    username VARCHAR(40),
                    password VARCHAR(40)
                )
            """)
            login_data = [('admin', '12345')]
            # Check if data already exists to prevent duplicates on re-run
            cursor.execute("SELECT COUNT(*) FROM login WHERE username = 'admin'")
            if cursor.fetchone()[0] == 0:
                cursor.executemany("INSERT INTO login VALUES (%s, %s)", login_data)
                print("Login data inserted.")
            else:
                print("Login data already exists, skipping insertion.")
            connection.commit()

            # b. Room Table
            print("\nCreating 'room' table and inserting data...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS room (
                    room_number VARCHAR(20) NOT NULL,
                    availability VARCHAR(20) NOT NULL,
                    clean_status VARCHAR(20) NOT NULL,
                    price VARCHAR(20) NOT NULL,
                    bed_type VARCHAR(30) NOT NULL,
                    PRIMARY KEY (room_number)
                )
            """)
            room_data = [
                ('101', 'Available', 'Clean', '2000', 'Single'),
                ('102', 'Available', 'Clean', '2500', 'Double'),
                ('103', 'Occupied', 'Clean', '3000', 'Single'),
                ('104', 'Available', 'Clean', '3500', 'Double'),
                ('105', 'Occupied', 'Dirty', '2200', 'Single'),
                ('106', 'Available', 'Clean', '2700', 'Single'),
                ('107', 'Occupied', 'Clean', '2300', 'Double'),
                ('108', 'Available', 'Dirty', '2000', 'Single'),
                ('109', 'Occupied', 'Clean', '4000', 'Double'),
                ('110', 'Available', 'Clean', '3000', 'Single'),
                ('111', 'Occupied', 'Clean', '2500', 'Single'),
                ('112', 'Available', 'Dirty', '3200', 'Double'),
                ('113', 'Available', 'Clean', '2100', 'Single'),
                ('114', 'Occupied', 'Dirty', '3500', 'Double'),
                ('115', 'Available', 'Clean', '2700', 'Single'),
                ('116', 'Occupied', 'Clean', '3000', 'Double'),
                ('117', 'Available', 'Dirty', '2600', 'Single'),
                ('118', 'Occupied', 'Clean', '2200', 'Double'),
                ('119', 'Available', 'Clean', '2800', 'Single'),
                ('120', 'Occupied', 'Dirty', '3300', 'Double')
            ]
            # Check if data already exists (e.g., room 101)
            cursor.execute("SELECT COUNT(*) FROM room WHERE room_number = '101'")
            if cursor.fetchone()[0] == 0:
                cursor.executemany("INSERT INTO room VALUES (%s, %s, %s, %s, %s)", room_data)
                print("Room data inserted.")
            else:
                print("Room data already exists, skipping insertion.")
            connection.commit()

            # c. Customer Table
            print("\nCreating 'customer' table and inserting data...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customer (
                    id VARCHAR(30) NOT NULL,
                    number VARCHAR(30) NOT NULL,
                    name VARCHAR(30) NOT NULL,
                    gender VARCHAR(30) NOT NULL,
                    country VARCHAR(30) NOT NULL,
                    room_number VARCHAR(30) NOT NULL,
                    status VARCHAR(30) NOT NULL,
                    deposit VARCHAR(30) NOT NULL,
                    PRIMARY KEY (id),
                    FOREIGN KEY(room_number) REFERENCES room(room_number)
                )
            """)
            customer_data = [
                ('C001', '9876543210', 'John Doe', 'Male', 'USA', '101', 'Checked-in', '1000'),
                ('C002', '9876543211', 'Jane Doe', 'Female', 'Canada', '102', 'Checked-in', '1500'),
                ('C003', '9876543212', 'Robert Smith', 'Male', 'UK', '103', 'Checked-out', '500'),
                ('C004', '9876543213', 'Emily Davis', 'Female', 'Australia', '104', 'Checked-in', '2000'),
                ('C005', '9876543214', 'William Brown', 'Male', 'India', '105', 'Checked-out', '1000'),
                ('C006', '9876543215', 'Jessica Wilson', 'Female', 'USA', '106', 'Checked-in', '1200'),
                ('C007', '9876543216', 'Michael Taylor', 'Male', 'USA', '107', 'Checked-out', '800'),
                ('C008', '9876543217', 'Sarah Johnson', 'Female', 'Canada', '108', 'Checked-in', '1400'),
                ('C009', '9876543218', 'James Lee', 'Male', 'China', '109', 'Checked-in', '1600'),
                ('C010', '9876543219', 'Patricia Harris', 'Female', 'Mexico', '110', 'Checked-out', '600'),
                ('C011', '9876543220', 'Charles Clark', 'Male', 'India', '111', 'Checked-in', '1800'),
                ('C012', '9876543221', 'Linda Allen', 'Female', 'Australia', '112', 'Checked-out', '1500'),
                ('C013', '9876543222', 'David Hall', 'Male', 'USA', '113', 'Checked-in', '900'),
                ('C014', '9876543223', 'Maria Scott', 'Female', 'Canada', '114', 'Checked-out', '700'),
                ('C015', '9876543224', 'Thomas Young', 'Male', 'UK', '115', 'Checked-in', '1100'),
                ('C016', '9876543225', 'Susan King', 'Female', 'USA', '116', 'Checked-in', '1300'),
                ('C017', '9876543226', 'Daniel Wright', 'Male', 'India', '117', 'Checked-out', '400'),
                ('C018', '9876543227', 'Karen Adams', 'Female', 'Mexico', '118', 'Checked-in', '1700'),
                ('C019', '9876543228', 'Steven Martinez', 'Male', 'USA', '119', 'Checked-in', '2000'),
                ('C020', '9876543229', 'Laura Perez', 'Female', 'Canada', '120', 'Checked-out', '1200')
            ]
            cursor.execute("SELECT COUNT(*) FROM customer WHERE id = 'C001'")
            if cursor.fetchone()[0] == 0:
                cursor.executemany("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", customer_data)
                print("Customer data inserted.")
            else:
                print("Customer data already exists, skipping insertion.")
            connection.commit()

            # d. Employee Table
            print("\nCreating 'employee' table and inserting data...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employee (
                    name VARCHAR(30) NOT NULL,
                    age VARCHAR(10) NOT NULL,
                    gender VARCHAR(30) NOT NULL,
                    job VARCHAR(30) NOT NULL,
                    salary VARCHAR(30) NOT NULL,
                    phone VARCHAR(30) NOT NULL,
                    aadhar VARCHAR(30) NOT NULL,
                    email VARCHAR(40) NOT NULL
                )
            """)
            employee_data = [
                ('John Miller', '30', 'Male', 'Manager', '50000', '9876543210', '1234567890', 'john.miller@example.com'),
                ('Sara Parker', '28', 'Female', 'Receptionist', '30000', '9876543211', '1234567891', 'sara.parker@example.com'),
                ('Tom Scott', '35', 'Male', 'Chef', '40000', '9876543212', '1234567892', 'tom.scott@example.com'),
                ('Emily Taylor', '29', 'Female', 'Housekeeper', '25000', '9876543213', '1234567893', 'emily.taylor@example.com'),
                ('Robert Brown', '45', 'Male', 'Security', '35000', '9876543214', '1234567894', 'robert.brown@example.com'),
                ('Anna Wilson', '32', 'Female', 'Manager', '55000', '9876543215', '1234567895', 'anna.wilson@example.com'),
                ('Michael Clark', '40', 'Male', 'Driver', '30000', '9876543216', '1234567896', 'michael.clark@example.com'),
                ('Sarah Lewis', '38', 'Female', 'Housekeeper', '22000', '9876543217', '1234567897', 'sarah.lewis@example.com'),
                ('David Walker', '50', 'Male', 'Security', '36000', '9876543218', '1234567898', 'david.walker@example.com'),
                ('Jessica Harris', '27', 'Female', 'Receptionist', '28000', '9876543219', '1234567899', 'jessica.harris@example.com')
            ]
            cursor.execute("SELECT COUNT(*) FROM employee WHERE name = 'John Miller'")
            if cursor.fetchone()[0] == 0:
                cursor.executemany("INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", employee_data)
                print("Employee data inserted.")
            else:
                print("Employee data already exists, skipping insertion.")
            connection.commit()

            # e. Driver Table
            print("\nCreating 'driver' table and inserting data...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS driver (
                    name VARCHAR(30) NOT NULL,
                    age VARCHAR(10) NOT NULL,
                    gender VARCHAR(20) NOT NULL,
                    company VARCHAR(30) NOT NULL,
                    brand VARCHAR(30) NOT NULL,
                    available VARCHAR(10) NOT NULL,
                    location VARCHAR(50) NOT NULL
                )
            """)
            driver_data = [
                ('John Smith', '40', 'Male', 'ABC Transport', 'Toyota', 'Yes', 'New York'),
                ('Amy Johnson', '28', 'Female', 'XYZ Cabs', 'Honda', 'No', 'Chicago'),
                ('David Green', '33', 'Male', 'Speed Cabs', 'Ford', 'Yes', 'San Francisco'),
                ('Laura Adams', '36', 'Female', 'Sunshine Rides', 'Chevrolet', 'Yes', 'Los Angeles'),
                ('Paul Brown', '45', 'Male', 'Quick Transport', 'Mercedes', 'No', 'Houston'),
                ('Alice Clark', '38', 'Female', 'ABC Transport', 'BMW', 'Yes', 'Miami'),
                ('George White', '50', 'Male', 'XYZ Cabs', 'Audi', 'Yes', 'Dallas'),
                ('Emma Davis', '29', 'Female', 'Sunshine Rides', 'Nissan', 'No', 'Austin'),
                ('Robert Martinez', '42', 'Male', 'Speed Cabs', 'Toyota', 'Yes', 'Seattle'),
                ('Sophia Wilson', '31', 'Female', 'Quick Transport', 'Hyundai', 'No', 'Denver')
            ]
            cursor.execute("SELECT COUNT(*) FROM driver WHERE name = 'John Smith'")
            if cursor.fetchone()[0] == 0:
                cursor.executemany("INSERT INTO driver VALUES (%s, %s, %s, %s, %s, %s, %s)", driver_data)
                print("Driver data inserted.")
            else:
                print("Driver data already exists, skipping insertion.")
            connection.commit()

            # f. Department Table
            print("\nCreating 'department' table and inserting data...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS department (
                    department VARCHAR(30) NOT NULL,
                    budget VARCHAR(30) NOT NULL
                )
            """)
            department_data = [
                ('Housekeeping', '100000'),
                ('Front Desk', '150000'),
                ('Security', '120000'),
                ('Maintenance', '80000'),
                ('Restaurant', '200000'),
                ('Laundry', '50000'),
                ('Transportation', '70000'),
                ('Administration', '250000'),
                ('Marketing', '150000'),
                ('Events', '30000')
            ]
            cursor.execute("SELECT COUNT(*) FROM department WHERE department = 'Housekeeping'")
            if cursor.fetchone()[0] == 0:
                cursor.executemany("INSERT INTO department VALUES (%s, %s)", department_data)
                print("Department data inserted.")
            else:
                print("Department data already exists, skipping insertion.")
            connection.commit()

            print("\nDatabase setup complete!")

            # --- Run all the defined queries ---
            run_hms_queries(connection, cursor)

    except Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
            print("Cursor closed.")
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database_and_tables()
