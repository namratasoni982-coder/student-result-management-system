# Student Result Management System

## Project Overview

The **Student Result Management System** is a simple Python-based application used to manage student details and marks.

The project allows the user to add students, update their marks, and display all student records.

This project demonstrates the use of **Object-Oriented Programming (OOP)** concepts in Python.

---

## Features

- Add a new student
- Store student name, roll number, and marks
- Search for a student using roll number
- Update student marks
- Display all student records
- Display a message when a student is not found
- Exit the program through a menu-driven system

---

## Technologies / Tools Used

- **Programming Language:** Python
- **Concepts Used:** Object-Oriented Programming (OOP)
- **Python Concepts:**
  - Classes and Objects
  - Constructor (`__init__`)
  - Class Variables
  - Class Methods
  - Lists
  - `if-else` statements
  - `for` loop
  - `while` loop
  - Functions/Methods
  - User Input
  - F-strings

- **Tool/IDE:** VS Code

---

## Installation and Running the Project

### Step 1: Install Python

Download and install Python from the official Python website:

https://www.python.org/downloads/

### Step 2: Download or Copy the Project

Save the Python program in a file named:

```text
results.py
```

### Step 3: Open the Terminal

Navigate to the folder containing `results.py`.

### Step 4: Run the Program

Use the following command:

```bash
python results.py
```

The main menu will appear:

```text
1. Add Student
2. Update Marks
3. Show All
4. Exit

Enter choice:
```

---

## How to Use the Project

### 1. Add Student

Select:

```text
1
```

Enter:

```text
Student name
Roll number
Marks
```

The program will display:

```text
Student <name> added successfully.
```

### 2. Update Marks

Select:

```text
2
```

Enter the student's roll number and then enter the new marks.

The program will display:

```text
Marks updated successfully.
```

If the roll number does not exist:

```text
Student not found.
```

### 3. Show All Students

Select:

```text
3
```

The program displays all stored student records.

Example:

```text
Name: namrata, Roll: 101, Marks: 95
Name: kavya, Roll: 102, Marks: 91
```

### 4. Exit

Select:

```text
4
```

The program will terminate.

---

## Testing Instructions

The following test cases can be used to check the project.

### Test Case 1: Add Student

**Input:**

```text
Choice: 1
Name: namrata
Roll Number: 101
Marks: 95
```

**Expected Output:**

```text
Student namrata added successfully.
```

---

### Test Case 2: Show Students

**Input:**

```text
Choice: 3
```

**Expected Output:**

```text
Name: namrata, Roll: 101, Marks: 95
```

---

### Test Case 3: Update Marks

**Input:**

```text
Choice: 2
Roll Number: 101
New Marks: 99
```

**Expected Output:**

```text
Marks updated successfully.
```

---

### Test Case 4: Search for a Non-existing Student

Enter a roll number that has not been added.

**Expected Output:**

```text
Student not found.
```

---

### Test Case 5: Empty Student List

Select `3` before adding any student.

**Expected Output:**

```text
No students found.
```

---

## Screenshots

Screenshots can be added here to show the working of the project.

### Main Menu

![Main Menu](screenshots/main_menu.png)

### Adding a Student

![Add Student](screenshots/add_student.png)

### Updating Marks

![Update Marks](screenshots/update_marks.png)

### Showing All Students

![All Students](screenshots/all_students.png)

---

## Project Structure

```text
Student-Result-Management/
│
├── results.py
├── README.md
└── screenshots/
    ├── main_menu.png
    ├── add_student.png
    ├── update_marks.png
    └── all_students.png
```

---

## Author

**Namrata Soni**

---

## Conclusion

The Student Result Management System is a basic Python project that demonstrates how **OOP concepts** can be used to create a simple student record management application. It provides basic operations for adding students, updating marks, and displaying student results.
