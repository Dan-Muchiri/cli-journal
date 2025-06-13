import datetime
from models.entry import Entry
from models.todo import Todo


def exit_program():
    print("Thank you for using the Personal CLI Journal App!")
    exit()

# ======== ENTRY HELPERS ========

def list_entries():
    entries = Entry.get_all_entries()
    print("All Entries:")
    for entry in entries:
        print(entry)


def find_entry_by_title():
    title = input("Enter the entry title: ")
    entries = Entry.find_by_title(title)
    if entries:
        print("Entries found:")
        for entry in entries:
            print(entry)
    else:
        print(f'Entry with title "{title}" not found.')


def find_entry_by_id():
    id_ = input("Enter the entry ID: ")
    entry = Entry.find_by_id(id_)
    if entry:
        print("Entry found:")
        print(entry)
    else:
        print(f'Entry with ID "{id_}" not found.')

def find_entries_by_mood():
    mood_value = input("Enter your mood (1-5): 1-😞 Very Sad, 2-😕 Sad, 3-😐 Neutral, 4-🙂 Happy, 5-😄 Very Happy: ") or None

    if mood_value:
        entries = Entry.find_by_mood(mood_value)
        if entries:
            for entry in entries:
                print(entry)
        else:
            print(f"No entries found with mood '{mood_value}'.")
    else:
        print("Invalid mood input. Please use a number 1–5.")



def create_entry():
    title = input("Enter the entry title: ")
    mood = input("Enter your mood (1-5): 1-😞 Very Sad, 2-😕 Sad, 3-😐 Neutral, 4-🙂 Happy, 5-😄 Very Happy: ") or None
    content = input("Enter your journal content:\n")

    try:
        mood_val = int(mood) if mood else None
        entry = Entry.add_entry(title=title, content=content, mood=mood_val)
        print(f'Entry "{title}" created successfully.')
    except ValueError:
        print("Invalid mood. Please enter a number between 1 and 5.")


def update_entry():
    id_ = input("Enter the entry ID to update: ")
    entry = Entry.find_by_id(id_)
    if not entry:
        print(f'Entry with ID "{id_}" not found.')
        return

    title = input(f"New title (press Enter to keep '{entry.title}'): ") or entry.title
    mood = input(f"New mood (1-5): 1-😞 Very Sad, 2-😕 Sad, 3-😐 Neutral, 4-🙂 Happy, 5-😄 Very Happy, press Enter to keep '{entry.mood}'): ") or entry.mood
    content = input("New content (press Enter to keep current content): ")

    try:
        mood_val = int(mood) if mood else entry.mood
        new_content = content if content else None
        Entry.update_entry(id_, title=title, mood=mood_val, content=new_content)
        print(f'Entry "{title}" updated successfully.')
    except ValueError:
        print("Invalid mood. Please enter a number between 1 and 5.")



def delete_entry():
    id_ = input("Enter the entry ID to delete: ")
    entry = Entry.find_by_id(id_)
    if entry:
        Entry.delete_entry(id_)
        print(f'Entry "{entry.title}" deleted.')
    else:
        print(f'Entry with ID "{id_}" not found.')



def view_entry_details():
    id_ = input("Enter the entry ID: ")
    entry = Entry.find_by_id(id_)
    if entry:
        print("\n=== Entry Details ===")
        Entry.read_entry_content(entry.id)
    else:
        print("Entry not found.")


# ======== TODO HELPERS ======== 

def list_todos():
    todos = Todo.get_all_todos()
    print("All To-Do Items:")
    for todo in todos:
        print(todo)


def get_entry_todos():
    id_ = input("Enter the entry ID: ")
    entry = Entry.find_by_id(id_)
    if entry:
        todos = entry.get_todos()
        if todos:
            print(f"\n📝 To-Do List for Entry '{entry.title}':")
            for todo in todos:
                print(todo)
        else:
            print(f"No to-dos found for Entry '{entry.title}'.")
    else:
        print("Entry not found.")



def create_todo():
    task = input("Enter the to-do task: ")
    entry_id = input("Enter the associated entry ID: ")

    if not Entry.find_by_id(entry_id):
        print(f"No entry found with ID {entry_id}.")
        return

    status = input("Enter the task status (pending/done) [default: pending]: ") or "pending"
    Todo.add_todo(task=task, entry_id=entry_id, status=status)
    print(f'Task "{task}" added to entry {entry_id} successfully.')

def update_todo():
    id_ = input("Enter the to-do ID to update: ")
    todo = Todo.find_by_id(id_)
    if not todo:
        print(f"Todo with ID {id_} not found.")
        return

    task = input(f"New task name (press Enter to keep '{todo.task}'): ") or todo.task
    status = input(f"New status (press Enter to keep '{todo.status}'): ") or todo.status
    entry_id = todo.entry_id

    if not Entry.find_by_id(entry_id):
        print(f"No entry found with ID {entry_id}.")
        return

    Todo.update_todo(todo_id=id_, task=task, status=status, entry_id=entry_id)
    print(f"Todo updated successfully.")

def delete_todo():
    id_ = input("Enter the to-do ID to delete: ")
    todo = Todo.find_by_id(id_)
    if todo:
        Todo.delete_todo(id_)
        print(f'Todo "{todo.task}" deleted.')
    else:
        print(f"Todo with ID {id_} not found.")


def find_todo_by_task():
    task = input("Enter a task name to search: ")
    todos = Todo.find_by_task(task)
    if todos:
        print("To-Dos found:")
        for todo in todos:
            print(todo)
    else:
        print("No matching to-dos found.")


def find_todo_by_id():
    id_ = input("Enter the to-do ID: ")
    todo = Todo.find_by_id(id_)
    if todo:
        print("To-Do found:")
        print(todo)
    else:
        print(f"Todo with ID {id_} not found.")


