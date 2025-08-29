 
# 🐍 Python Assignment 1 – Classes, Inheritance & Polymorphism

This repository contains solutions for **Assignment 1** of the PLP Python course.  
It demonstrates **Object-Oriented Programming (OOP)** concepts including **classes, attributes, methods, constructors, inheritance, and polymorphism**.

---

## 📘 Assignment Breakdown

### **Activity 1: Design Your Own Class 🏗️**
- Created a `Book` class with:
  - Attributes: `title`, `author`, `year`.
  - Methods: `display_info()` and `__str__()`.
- Added an **inheritance layer** with a child class `EBook`:
  - Extra attribute: `file_size`.
  - Overridden `display_info()` and `__str__()` to include file size.
- Demonstrates **encapsulation** by keeping attributes tied to objects.

---

### **Activity 2: Polymorphism Challenge 🎭**
- Implemented a **shared method** `move()` across different classes (`Car`, `Plane`).
- Each class defines its own version of `move()`:
  - `Car.move()` → prints `"Driving 🚗"`
  - `Plane.move()` → prints `"Flying ✈️"``
- Demonstrates **polymorphism**: the same method behaves differently depending on the object.

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Daniel-Dadzie/PLP_Python_Assignment.git
Navigate to the repo:

cd  PLP_Python_Assignment
Run the Python files:

python Opp.py       # Activity 1
python poly.py   # Activity 2
📂 File Structure
Assignment1/
│── book.py             # Activity 1: Book & EBook class with inheritance
│── polymorphism.py     # Activity 2: Car, , Plane demonstrating polymorphism
│── README.md           # Documentation
✍️ Author
Daniel Yaw Dadzie

📧 Email: 

🔗 GitHub: Daniel-Dadzie

💼 LinkedIn: Daniel Yaw Dadzie

✅ Notes
This assignment focuses on fundamentals of OOP in Python.

Code is kept simple and well-documented for easy understanding.

🚫 Please do not copy-paste directly for assignments—use this for reference and learning.

 