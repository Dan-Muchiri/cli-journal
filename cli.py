from helpers import (
    exit_program,
    list_entries,
    find_entry_by_title,
    find_entry_by_id,
    find_entries_by_mood,
    create_entry,
    update_entry,
    delete_entry,
    view_entry_details,
    list_todos,
    get_entry_todos,
    create_todo,
    update_todo,
    delete_todo,
    find_todo_by_task,
    find_todo_by_id
)

from colorama import init, Fore, Style

init(autoreset=True)


def show_menu():
    print(Fore.GREEN + "\n📓 Welcome to Your Personal CLI Journal")
    print(Fore.YELLOW + "======================================")
    print(Fore.CYAN + " Journal Entries")
    print(Fore.YELLOW + "--------------------------------------")
    print(" 1.  📋  List all journal entries")
    print(" 2.  🔍  Find a journal entry by title")
    print(" 3.  🔍  Find a jornal entry by ID")
    print(" 4.  😊  Find journal entries by mood")
    print(" 5.  📖  View journal entry content")
    print(" 6.  ✍️   Create a new journal entry")
    print(" 7.  📝  Update a journal entry")
    print(" 8.  ❌  Delete a journal entry")
    print()
    print(Fore.CYAN + " To-Dos (Linked to Entries)")
    print(Fore.YELLOW + "--------------------------------------")
    print(" 9.  📑  View a specific journal entry to-dos")
    print("10.  📋  List all to-dos")
    print("11.  ➕  Add a to-do to a journal entry")
    print("12.  🛠️   Update a to-do")
    print("13.  🗑️   Delete a to-do")
    print("14.  🔎  Find a to-do by task")
    print("15.  🔎  Find a to-do by ID")
    print()
    print(" 0.  🚪  Exit")
    print(Fore.YELLOW + "======================================\n")


def main():
    while True:
        show_menu()
        choice = input(Fore.BLUE + "What would you like to do? " + Style.RESET_ALL).strip()

        if choice == "1":
            list_entries()
        elif choice == "2":
            find_entry_by_title()
        elif choice == "3":
            find_entry_by_id()
        elif choice == "4":
            find_entries_by_mood()
        elif choice == "5":
            view_entry_details()
        elif choice == "6":
            create_entry()
        elif choice == "7":
            update_entry()
        elif choice == "8":
            delete_entry()
        elif choice == "9":
            get_entry_todos()
        elif choice == "10":
            list_todos()
        elif choice == "11":
            create_todo()
        elif choice == "12":
            update_todo()
        elif choice == "13":
            delete_todo()
        elif choice == "14":
            find_todo_by_task()
        elif choice == "15":
            find_todo_by_id()
        elif choice == "0":
            exit_program()
        else:
            print(Fore.RED + "❗ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
