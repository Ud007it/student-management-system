from utils import (
    C, load_students, save_students, get_str_input, 
    get_positive_int, generate_roll_number, search_student_by_rollno
)

def add_student():
    print(f"\n{C.BOLD}{C.CYAN}--- Add New Student ---{C.RESET}")
    students = load_students()

    name   = get_str_input("Enter student name:  ").title()
    course = get_str_input("Enter course name:   ").upper()
    age    = get_positive_int("Enter age:           ")

    new_student = {
        "rollno": generate_roll_number(students),
        "name":   name,
        "age":    age,
        "course": course
    }

    students.append(new_student)
    save_students(students)
    print(f"\n  {C.BOLD}{C.GREEN}[✓] Student '{name}' added successfully! (Roll No: {new_student['rollno']}){C.RESET}\n")

def view_students():
    students = load_students()

    if not students:
        print(f"\n  {C.YELLOW}[!] No students available in the database.{C.RESET}\n")
        return

    print(f"\n{C.BOLD}{C.CYAN}{'=' * 60}{C.RESET}")
    print(f"{C.BOLD}{C.WHITE}{'Roll No':<8} | {'Name':<20} | {'Age':<5} | {'Course':<15}{C.RESET}")
    print(f"{C.DIM}{'-' * 60}{C.RESET}")

    for i, student in enumerate(students):
        row = C.WHITE if i % 2 == 0 else C.DIM + C.WHITE
        print(
            f"{row}"
            f"{student['rollno']:<8} | "
            f"{student['name']:<20} | "
            f"{student['age']:<5} | "
            f"{student['course']:<15}"
            f"{C.RESET}"
        )

    print(f"{C.BOLD}{C.CYAN}{'=' * 60}{C.RESET}")
    print(f"  {C.DIM}Total: {len(students)} student(s){C.RESET}\n")

def search_student():
    print(f"\n{C.BOLD}{C.CYAN}--- Search Student ---{C.RESET}")
    students = load_students()

    rollno = get_positive_int("Enter roll number to search: ")
    student, _ = search_student_by_rollno(rollno, students)

    if not student:
        print(f"\n  {C.YELLOW}[!] Student not found.{C.RESET}\n")
        return

    print(f"\n  {C.BOLD}{C.GREEN}[✓] STUDENT FOUND{C.RESET}")
    print(f"  {C.DIM}{'-' * 30}{C.RESET}")
    print(f"  {C.BOLD}Roll Number :{C.RESET} {C.CYAN}{student['rollno']}{C.RESET}")
    print(f"  {C.BOLD}Name        :{C.RESET} {C.WHITE}{student['name']}{C.RESET}")
    print(f"  {C.BOLD}Age         :{C.RESET} {student['age']}")
    print(f"  {C.BOLD}Course      :{C.RESET} {C.MAGENTA}{student['course']}{C.RESET}")
    print(f"  {C.DIM}{'-' * 30}{C.RESET}\n")

def delete_student():
    print(f"\n{C.BOLD}{C.RED}--- Delete Student ---{C.RESET}")
    students = load_students()

    rollno = get_positive_int("Enter roll number to delete: ")
    student, index = search_student_by_rollno(rollno, students)

    if not student:
        print(f"\n  {C.YELLOW}[!] Student not found.{C.RESET}\n")
        return

    print(f"\n  {C.BOLD}Found Student:{C.RESET} {C.WHITE}{student['name']}{C.RESET} {C.DIM}(Course: {student['course']}){C.RESET}")
    confirm = get_str_input("Are you sure you want to delete? (yes/no): ").lower()

    if confirm in ["yes", "y"]:
        students.pop(index)
        save_students(students)
        print(f"\n  {C.BOLD}{C.GREEN}[✓] Student '{student['name']}' deleted successfully!{C.RESET}\n")
    else:
        print(f"\n  {C.YELLOW}[-] Deletion cancelled.{C.RESET}\n")

def update_student():
    print(f"\n{C.BOLD}{C.MAGENTA}--- Update Student ---{C.RESET}")
    students = load_students()

    rollno = get_positive_int("Enter roll number to update: ")
    student, _ = search_student_by_rollno(rollno, students)

    if not student:
        print(f"\n  {C.YELLOW}[!] Student not found.{C.RESET}\n")
        return

    while True:
        print(f"\n  {C.BOLD}Updating:{C.RESET} {C.CYAN}{student['name']}{C.RESET} {C.DIM}| {student['course']} | Age: {student['age']}{C.RESET}")
        print(f"""
{C.BOLD}{C.MAGENTA}  ╔══════════════════════════╗
  ║      UPDATE MENU         ║
  ╠══════════════════════════╣{C.RESET}
{C.CYAN}  ║  1.{C.RESET} Update Name          {C.MAGENTA}║
{C.CYAN}  ║  2.{C.RESET} Update Course        {C.MAGENTA}║
{C.CYAN}  ║  3.{C.RESET} Update Age            {C.MAGENTA}║
{C.CYAN}  ║  4.{C.RESET} Update All            {C.MAGENTA}║
{C.CYAN}  ║  5.{C.RESET} Save & Exit           {C.MAGENTA}║
{C.BOLD}{C.MAGENTA}  ╚══════════════════════════╝{C.RESET}
""")

        choice = input(f"  {C.CYAN}➤{C.RESET}  {C.BOLD}Enter choice:{C.RESET} ").strip()

        match choice:
            case "1":
                student["name"] = get_str_input("Enter new name:   ").title()
                save_students(students)
                print(f"  {C.GREEN}[✓] Name updated successfully!{C.RESET}")

            case "2":
                student["course"] = get_str_input("Enter new course: ").upper()
                save_students(students)
                print(f"  {C.GREEN}[✓] Course updated successfully!{C.RESET}")

            case "3":
                student["age"] = get_positive_int("Enter new age:    ")
                save_students(students)
                print(f"  {C.GREEN}[✓] Age updated successfully!{C.RESET}")

            case "4":
                student["name"]   = get_str_input("Enter new name:   ").title()
                student["course"] = get_str_input("Enter new course: ").upper()
                student["age"]    = get_positive_int("Enter new age:    ")
                save_students(students)
                print(f"  {C.GREEN}[✓] All details updated successfully!{C.RESET}")

            case "5":
                print(f"\n  {C.YELLOW}[-] Exiting update menu...{C.RESET}\n")
                break

            case _:
                print(f"  {C.RED}[!] Invalid option. Please choose 1-5.{C.RESET}")