# 🎓 CLI Student Management System

A robust, terminal-based CRUD application built entirely in Python. This project demonstrates modular architecture, data persistence using JSON, and comprehensive error handling.

## ✨ Features
* **Create, Read, Update, Delete (CRUD):** Full management of student records.
* **Data Persistence:** Automatically saves and loads data from `students_data.json`.
* **Corrupted File Protection:** Automatically detects broken JSON files and creates safe backups.
* **Input Sanitization:** Forces Title Case for names and UPPERCASE for courses.
* **Modular Design:** Clean separation of UI, logic, and utility functions.

## 📂 Project Structure
```text
student_management_system/
├── main.py             # The entry point and main menu UI
├── operations.py       # Core CRUD logic
├── utils.py            # Helper functions, colors, and JSON handling
├── students_data.json  # The database
└── .gitignore