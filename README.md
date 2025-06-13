# CLI Journal Application

## Project Overview

The CLI Journal Application is a terminal-based Python program that allows users to manage daily journal entries and associated to-do tasks. Designed with simplicity and functionality in mind, the application uses a text-based interface for input and output, storing user entries persistently through both **file read/write operations** and **a database backend**.

Each journal entry includes a title, mood, and content. Users can also attach multiple to-do items to a specific entry, enabling thoughtful reflection and actionable planning in one place. The colorful CLI interface, powered by `colorama`, enhances usability and makes journaling an engaging experience.

## Benefits

- Combines journaling and task management in one CLI tool.
- Simplifies daily reflections and planning.
- Persists data both in files and in a database, ensuring durability.
- Clean and colorful text-based interface using `colorama`.
- Search functionality to retrieve entries by mood, ID, or title.

## Timeline

1. Core logic design using functions and classes.
2. Menu system implementation for journal and to-do workflows.
3. File I/O and database persistence setup.
4. Development of all CRUD operations.
5. UI enhancements and error handling.
6. Documentation and submission.

## How to Use

1. Clone the repository to your machine.
2. Install dependencies using `pipenv install`.
3. Enter the virtual environment with `pipenv shell`.
4. Add sample data using `python seed.py`.
5. Run the CLI application with `python cli.py`.
6. Follow the interactive menu to manage your journal and tasks.

## Usage

Explore your thoughts and tasks using this intuitive command-line application. The main menu separates journal and to-do functionalities clearly for smooth operation.

### Journal Entries Menu

- 📋 List all journal entries  
- 🔍 Find a journal entry by title  
- 🔍 Find a journal entry by ID  
- 😊 Find entries by mood  
- 📖 View full journal entry content  
- ✍️ Create a new journal entry  
- 📝 Update a journal entry  
- ❌ Delete a journal entry  

### To-Dos Menu

- 📑 View to-dos for a specific journal entry  
- 📋 List all to-dos  
- ➕ Add a to-do task to a journal entry  
- 🛠️ Update a to-do  
- 🗑️ Delete a to-do  
- 🔎 Find a to-do by task  
- 🔎 Find a to-do by ID  

Each menu option prompts the user to input relevant data and performs the necessary operation, either retrieving, modifying, or storing data from files and the database.

## Key Features

- ✅ **Dual Persistence**: Stores journal entries and to-dos in both files and a database.
- ✅ **Modular Design**: All functionalities organized into helper functions.
- ✅ **OOP Usage**: Uses object-oriented principles including encapsulation and class instantiation.
- ✅ **Interactive CLI Menu**: Numbered menu system for intuitive use.
- ✅ **External Libraries**: Uses `colorama` for colored terminal output.
- ✅ **User-Friendly Experience**: Emoji-enhanced prompts and clean menu formatting.

## Technologies Used

- **Python 3**
- **colorama**
- **faker**
- **Built-in File I/O**
- **SQLite / SQLAlchemy**
- **Modular Python Scripting**

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more details.
# cli-journal
