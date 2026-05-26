import json
import os

FILE_NAME = "students_data.json"

class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        if os.path.exists(FILE_NAME):
            os.rename(FILE_NAME, "students_data_backup.json")
        print(f"\n  {C.BOLD}{C.RED}[!] ERROR: Database corrupted. A backup was created.{C.RESET}")
        print(f"  {C.YELLOW}[!] Starting with a fresh database.{C.RESET}\n")
        return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def get_str_input(prompt):
    while True:
        value = input(f"  {C.CYAN}➤{C.RESET}  {C.BOLD}{prompt}{C.RESET} ").strip()
        if value:
            return value
        print(f"  {C.RED}[!] Error: Input cannot be empty. Please try again.{C.RESET}")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(f"  {C.CYAN}➤{C.RESET}  {C.BOLD}{prompt}{C.RESET} ").strip())
            if value > 0:
                return value
            print(f"  {C.RED}[!] Error: Number must be greater than 0.{C.RESET}")
        except ValueError:
            print(f"  {C.RED}[!] Error: Please enter a valid number.{C.RESET}")

def generate_roll_number(students):
    if not students:
        return 1
    highest_roll = max(student["rollno"] for student in students)
    return highest_roll + 1

def search_student_by_rollno(rollno, students):
    for index, student in enumerate(students):
        if student["rollno"] == rollno:
            return student, index
    return None, None