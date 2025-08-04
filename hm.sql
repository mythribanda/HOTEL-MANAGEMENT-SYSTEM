-- MySQL Script for Hotel Management System (HMS)

-- Database Creation
CREATE DATABASE IF NOT EXISTS hms;
USE hms;

-- Creating Tables

-- Login Table
CREATE TABLE IF NOT EXISTS login (
    username VARCHAR(40),
    password VARCHAR(40)
);
INSERT INTO login VALUES ('admin', '12345');

-- Room Table
CREATE TABLE IF NOT EXISTS room (
    room_number VARCHAR(20) NOT NULL PRIMARY KEY,
    availability VARCHAR(20) NOT NULL,
    clean_status VARCHAR(20) NOT NULL,
    price VARCHAR(20) NOT NULL,
    bed_type VARCHAR(30) NOT NULL
);
INSERT INTO room VALUES
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
('120', 'Occupied', 'Dirty', '3300', 'Double');

-- Customer Table
CREATE TABLE IF NOT EXISTS customer (
    id VARCHAR(30) NOT NULL PRIMARY KEY,
    number VARCHAR(30) NOT NULL,
    name VARCHAR(30) NOT NULL,
    gender VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    room_number VARCHAR(30) NOT NULL,
    status VARCHAR(30) NOT NULL,
    deposit VARCHAR(30) NOT NULL,
    FOREIGN KEY(room_number) REFERENCES room(room_number)
);
INSERT INTO customer VALUES
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
('C020', '9876543229', 'Laura Perez', 'Female', 'Canada', '120', 'Checked-out', '1200');

-- Employee Table
CREATE TABLE IF NOT EXISTS employee (
    name VARCHAR(30) NOT NULL,
    age VARCHAR(10) NOT NULL,
    gender VARCHAR(30) NOT NULL,
    job VARCHAR(30) NOT NULL,
    salary VARCHAR(30) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    aadhar VARCHAR(30) NOT NULL,
    email VARCHAR(40) NOT NULL
);
INSERT INTO employee VALUES
('John Miller', '30', 'Male', 'Manager', '50000', '9876543210', '1234567890', 'john.miller@example.com'),
('Sara Parker', '28', 'Female', 'Receptionist', '30000', '9876543211', '1234567891', 'sara.parker@example.com'),
('Tom Scott', '35', 'Male', 'Chef', '40000', '9876543212', '1234567892', 'tom.scott@example.com'),
('Emily Taylor', '29', 'Female', 'Housekeeper', '25000', '9876543213', '1234567893', 'emily.taylor@example.com'),
('Robert Brown', '45', 'Male', 'Security', '35000', '9876543214', '1234567894', 'robert.brown@example.com'),
('Anna Wilson', '32', 'Female', 'Manager', '55000', '9876543215', '1234567895', 'anna.wilson@example.com'),
('Michael Clark', '40', 'Male', 'Driver', '30000', '9876543216', '1234567896', 'michael.clark@example.com'),
('Sarah Lewis', '38', 'Female', 'Housekeeper', '22000', '9876543217', '1234567897', 'sarah.lewis@example.com'),
('David Walker', '50', 'Male', 'Security', '36000', '9876543218', '1234567898', 'david.walker@example.com'),
('Jessica Harris', '27', 'Female', 'Receptionist', '28000', '9876543219', '1234567899', 'jessica.harris@example.com');

-- Driver Table
CREATE TABLE IF NOT EXISTS driver (
    name VARCHAR(30) NOT NULL,
    age VARCHAR(10) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    company VARCHAR(30) NOT NULL,
    brand VARCHAR(30) NOT NULL,
    available VARCHAR(10) NOT NULL,
    location VARCHAR(50) NOT NULL
);
INSERT INTO driver VALUES
('John Smith', '40', 'Male', 'ABC Transport', 'Toyota', 'Yes', 'New York'),
('Amy Johnson', '28', 'Female', 'XYZ Cabs', 'Honda', 'No', 'Chicago'),
('David Green', '33', 'Male', 'Speed Cabs', 'Ford', 'Yes', 'San Francisco'),
('Laura Adams', '36', 'Female', 'Sunshine Rides', 'Chevrolet', 'Yes', 'Los Angeles'),
('Paul Brown', '45', 'Male', 'Quick Transport', 'Mercedes', 'No', 'Houston'),
('Alice Clark', '38', 'Female', 'ABC Transport', 'BMW', 'Yes', 'Miami'),
('George White', '50', 'Male', 'XYZ Cabs', 'Audi', 'Yes', 'Dallas'),
('Emma Davis', '29', 'Female', 'Sunshine Rides', 'Nissan', 'No', 'Austin'),
('Robert Martinez', '42', 'Male', 'Speed Cabs', 'Toyota', 'Yes', 'Seattle'),
('Sophia Wilson', '31', 'Female', 'Quick Transport', 'Hyundai', 'No', 'Denver');

-- Department Table
CREATE TABLE IF NOT EXISTS department (
    department VARCHAR(30) NOT NULL,
    budget VARCHAR(30) NOT NULL
);
INSERT INTO department VALUES
('Housekeeping', '100000'),
('Front Desk', '150000'),
('Security', '120000'),
('Maintenance', '80000'),
('Restaurant', '200000'),
('Laundry', '50000'),
('Transportation', '70000'),
('Administration', '250000'),
('Marketing', '150000'),
('Events', '30000');

-- Queries

-- 1. Get All Rooms Information
SELECT * FROM room;

-- 2. Get Available Rooms
SELECT * FROM room WHERE availability = 'Available';

-- 3. Get Occupied Rooms
SELECT * FROM room WHERE availability = 'Occupied';

-- 4. Get Room Details by Room Number
SELECT * FROM room WHERE room_number = '101';

-- 5. Get All Customers
SELECT * FROM customer;

-- 6. Get Customers with Status 'Checked-in'
SELECT * FROM customer WHERE status = 'Checked-in';

-- 7. Get Customers with Deposit Greater Than 1000
SELECT * FROM customer WHERE CAST(deposit AS UNSIGNED) > 1000;

-- 8. Get Customer Information and Room Details
SELECT c.name, c.room_number, r.bed_type, r.price
FROM customer c
JOIN room r ON c.room_number = r.room_number;

-- 9. Get Customer Details by Customer ID
SELECT * FROM customer WHERE id = 'C001';

-- 10. Get Employees Working in Housekeeping Department
SELECT * FROM employee WHERE job = 'Housekeeper';

-- 11. Get Employees with Salary Above 30000
SELECT * FROM employee WHERE CAST(salary AS UNSIGNED) > 30000;

-- 12. Get Driver Information for Available Drivers
SELECT * FROM driver WHERE available = 'Yes';

-- 13. Get All Departments with Their Budget
SELECT * FROM department;

-- 14. Get Employees from the 'Front Desk' Department
SELECT * FROM employee WHERE job = 'Receptionist';

-- 15. Get Rooms by Price Range
SELECT * FROM room WHERE CAST(price AS UNSIGNED) BETWEEN 2000 AND 3000;

-- 16. Update Customer Status to 'Checked-out'
UPDATE customer SET status = 'Checked-out' WHERE id = 'C001';

-- 17. Update Room Availability to 'Occupied'
UPDATE room SET availability = 'Occupied' WHERE room_number = '101';

-- 18. Insert New Employee
INSERT INTO employee (name, age, gender, job, salary, phone, aadhar, email)
VALUES ('Mark Johnson', '30', 'Male', 'Manager', '50000', '9876543220', '1234567899', 'mark.johnson@example.com');

-- 19. Delete Room by Room Number
-- NOTE: This might fail if foreign key constraints exist.
DELETE FROM room WHERE room_number = '101';

-- 20. Delete Customer by Customer ID
DELETE FROM customer WHERE id = 'C002';

-- 21. Get Total Revenue from All Occupied Rooms
SELECT SUM(CAST(price AS UNSIGNED)) AS total_revenue
FROM room
WHERE availability = 'Occupied';

-- 22. Get the Number of Rooms in Each Availability Status
SELECT availability, COUNT(*) AS num_rooms
FROM room
GROUP BY availability;

-- 23. Get All Employees and Their Job Titles
SELECT name, job FROM employee;

-- 24. Get All Customers Who Stayed in a Specific Room
SELECT c.name, c.room_number, c.status
FROM customer c
WHERE c.room_number = '101';

-- 25. Find All Rooms with 'Dirty' Cleaning Status
SELECT * FROM room WHERE clean_status = 'Dirty';

-- 26. Find Employees Who Have Worked for More Than 5 Years (based on age)
SELECT * FROM employee WHERE CAST(age AS UNSIGNED) > 30;

-- 27. Get Customers by Country
SELECT * FROM customer WHERE country = 'USA';

-- 28. Get the Room with the Highest Price
SELECT * FROM room WHERE CAST(price AS UNSIGNED) = (SELECT MAX(CAST(price AS UNSIGNED)) FROM room);

-- 29. Get the Total Number of Employees
SELECT COUNT(*) AS total_employees FROM employee;

-- 30. Get a List of All Available Rooms Sorted by Price
SELECT * FROM room WHERE availability = 'Available' ORDER BY CAST(price AS UNSIGNED) ASC;

-- 31. Get List of Drivers Working for a Specific Company
SELECT * FROM driver WHERE company = 'ABC Transport';

-- 32. Get the Average Salary of Employees
SELECT AVG(CAST(salary AS UNSIGNED)) AS average_salary FROM employee;

-- 33. Get List of Customers Who Have Deposited More Than 1000
SELECT * FROM customer WHERE CAST(deposit AS UNSIGNED) > 1000;

-- 34. Get List of Customers Who Have Checked-out
SELECT * FROM customer WHERE status = 'Checked-out';

-- 35. Update Employee Salary
UPDATE employee SET salary = '60000' WHERE name = 'Sara Parker';
