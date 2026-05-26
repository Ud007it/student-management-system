import sys
from utils import C
from operations import (
    add_student, view_students, search_student, 
    update_student, delete_student
)

def main_menu():
    while True:
        print(f"""
{C.BOLD}{C.CYAN}╔══════════════════════════════════════╗
║    STUDENT MANAGEMENT SYSTEM         ║
╠══════════════════════════════════════╣{C.RESET}
{C.CYAN}║  {C.GREEN}1.{C.RESET} Add Student                      {C.CYAN}║
{C.CYAN}║  {C.BLUE}2.{C.RESET} View Students                    {C.CYAN}║
{C.CYAN}║  {C.YELLOW}3.{C.RESET} Search Student                   {C.CYAN}║
{C.CYAN}║  {C.MAGENTA}4.{C.RESET} Update Student                   {C.CYAN}║
{C.CYAN}║  {C.RED}5.{C.RESET} Delete Student                   {C.CYAN}║
{C.CYAN}║  {C.WHITE}6.{C.RESET} Exit                             {C.CYAN}║
{C.BOLD}{C.CYAN}╚══════════════════════════════════════╝{C.RESET}""")

        choice = input(f"\n  {C.CYAN}➤{C.RESET}  {C.BOLD}Enter your choice:{C.RESET} ").strip()

        match choice:
            case "1": add_student()
            case "2": view_students()
            case "3": search_student()
            case "4": update_student()
            case "5": delete_student()
            case "6":
                print(f"\n  {C.BOLD}{C.CYAN}Thank you for using the system! Goodbye. 👋{C.RESET}\n")
                sys.exit()
            case _:
                print(f"\n  {C.RED}[!] Invalid menu option. Please choose 1-6.{C.RESET}")

if __name__ == "__main__":
    main_menu()