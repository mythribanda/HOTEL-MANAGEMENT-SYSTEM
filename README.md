# 🏨 Hotel Management System (HMS)

This repository contains the complete MySQL schema, seed data, and a Python connector script for a **Hotel Management System**. The project is designed to demonstrate basic database design, data operations, and Python-MySQL integration.

---

## 📚 Table of Contents

- [📌 Project Overview](#project-overview)
- [✨ Features](#features)
- [🗃️ Database Schema](#database-schema)
- [🧩 ER Diagram](#er-diagram)
- [⚙️ Setup Instructions](#setup-instructions)
  - [🔧 Prerequisites](#prerequisites)
  - [🛠️ Database Setup](#database-setup)
  - [🐍 Python Script Execution](#python-script-execution)
- [🚀 How to Use](#how-to-use)
- [🧠 Future Enhancements](#future-enhancements)
- [📎 License](#license)
- [🙋‍♀️ Contributing](#contributing)
- [📬 Contact](#contact)

---

## 📌 Project Overview

The **Hotel Management System** (HMS) is a foundational project to manage hotel operations such as rooms, customers, staff, and administrative processes. It provides a structured, relational approach to storing and retrieving hotel data.

---

## ✨ Features

### 🛏️ Room Management
- View all room details
- Identify available vs occupied rooms
- Filter by room number, price, or clean status

### 👤 Customer Management
- List all guests
- Filter by check-in/check-out status
- Query based on deposit amount
- Update or delete customer records

### 👥 Employee & Department Management
- View employee details and job types
- Filter by job role (e.g., Receptionist, Housekeeper)
- Track salaries and department budgets
- Add/update employee records

### 🚗 Driver Management
- View all drivers and availability
- Filter by company (Uber, Ola, etc.)

### 🔗 Data Relationships
- JOIN operations between customers, rooms, employees, etc.
- Aggregation and advanced filtering

---

## 🗃️ Database Schema

The HMS system includes the following tables:

- `login`: Authentication credentials
- `room`: Hotel room details and status
- `customer`: Guest and booking details
- `employee`: Hotel staff data
- `driver`: Driver info linked with transport services
- `department`: Hotel departments and their budgets

---

## 🧩 ER Diagram

[login]

[room] <── [customer]

[employee]
│
[department]

[driver]

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- **MySQL Server**: e.g., XAMPP, WAMP, or standalone MySQL
- **Python 3.x**
- **MySQL Connector for Python**:
```bash
pip install mysql-connector-python
```
🛠️ Database Setup
Clone this repository:

```bash
git clone https://github.com/yourusername/hotel-management-system.git
cd hotel-management-system

```
```bash
mysql -u your_username -p < hms_full_script.sql
```
This will:

✅ Create the database hms

✅ Create all necessary tables

✅ Insert more than 35 rows into each table

🐍 Python Script Execution
Open hms_connector.py in a code editor and update your MySQL credentials:

```python

host = "localhost"
user = "your_mysql_username"
password = "your_mysql_password"
database = "hms"
```
Run the script using the terminal:

```bash

python hms_connector.py
```
---

### ✅ What This Script Does

When you run `hms_connector.py`, it will:

- 🔌 Connect to the **hms** MySQL database
- 🛠️ Execute predefined SQL queries
- 🖨️ Print query results directly to your terminal

---

## 🚀 How to Use

- 🔍 **Run the Python script** to view outputs in your terminal
- 💻 Use **MySQL Workbench**, **phpMyAdmin**, or **MySQL CLI** to explore the `hms` database manually
- 🧪 Test or practice with the **20 SQL queries** provided in the `hms_queries.txt` file
- ➕ Extend the Python script with your own SQL queries, filters, or even user inputs

---

## 🧠 Future Enhancements

- 🎨 Develop a **GUI** using **Tkinter**, **PyQt**, or a web framework like **Flask**/**Django**
- 📊 Create advanced **analytical dashboards** and visual reports
- 🔐 Implement **secure user login** using password hashing and role-based access
- ⚙️ Add **robust error handling** and **form validations**
- 🧪 Write **unit tests** and refactor into **modular Python code** for better maintainability

---

## 📎 License

This project is open-source and available under the **MIT License**.

---

## 🙋‍♀️ Contributing

Pull requests are welcome! If you'd like to contribute:

```bash
1. Fork this repository
2. Create a new feature branch
3. Commit your changes
4. Push to your fork
5. Open a pull request 🚀

```
