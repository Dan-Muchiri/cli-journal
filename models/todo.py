# todo.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init import Base, session
import os


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    task = Column(String, nullable=False)
    status = Column(String, default='pending')  # e.g., 'pending', 'done'
    entry_id = Column(Integer, ForeignKey('entries.id'))

    # Relationship with Entry (many-to-one)
    entry = relationship("Entry", back_populates="todos")

    def __repr__(self):
        return f"Todo(id={self.id}, task='{self.task}', status='{self.status}', Entry ID={self.entry_id})"
    
    @classmethod
    def add_todo(cls, task, entry_id, status='pending'):
        """
        Add a new to-do item to the database and update the associated entry file.
        """
        new_todo = cls(task=task, entry_id=entry_id, status=status)
        session.add(new_todo)
        session.commit()

        # After commit, update the entry file
        entry = session.query(new_todo.__class__.entry.property.mapper.class_).get(entry_id)
        if entry and os.path.exists(entry.content_path):
            try:
                with open(entry.content_path, "a", encoding="utf-8") as f:
                    f.write("\n" + "="*40 + "\n")
                    f.write("          ✅ To-Do\n")
                    f.write("="*40 + "\n")
                    f.write(f"📝 Task   : {task}\n")
                    f.write(f"📌 Status : {status.capitalize()}\n")
            except Exception as e:
                print("Failed to update entry file with new to-do:", e)



    @classmethod
    def get_all_todos(cls):
        """
        Retrieve all to-do items.

        :return: A list of Todo objects.
        """
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, todo_id):
        """
        Find a to-do item by its ID.

        :param todo_id: The ID of the to-do item.
        :return: The Todo object if found, else None.
        """
        return session.query(cls).filter_by(id=todo_id).first()

    @classmethod
    def find_by_task(cls, task):
        """
        Search to-do items by task name (case-insensitive and supports partial matches).

        :param task: The task string to search.
        :return: A list of matching Todo objects.
        """
        return session.query(cls).filter(cls.task.ilike(f"%{task}%")).all()
    
    @staticmethod
    def delete_todo(todo_id):
        """
        Delete a to-do item and annotate its deletion in the associated entry file.
        """
        todo = session.query(Todo).get(todo_id)
        if not todo:
            print("To-do not found.")
            return

        # Preserve info before deletion
        task = todo.task
        status = todo.status
        entry = todo.entry

        session.delete(todo)
        session.commit()

        # Log deletion in the file
        if entry and os.path.exists(entry.content_path):
            try:
                with open(entry.content_path, "a", encoding="utf-8") as f:
                    f.write("\n" + "="*40 + "\n")
                    f.write("       ❌ To-Do Deleted\n")
                    f.write("="*40 + "\n")
                    f.write(f"📝 Task   : {task}\n")
                    f.write(f"📌 Status : {status.capitalize() if status else 'N/A'}\n")
            except Exception as e:
                print("Failed to log deleted to-do in entry file:", e)


    @staticmethod
    def update_todo(todo_id, task=None, status=None, entry_id=None):
        """
        Update an existing to-do item and annotate the old version as updated,
        then append the new version in the associated entry file.
        """
        todo = session.query(Todo).get(todo_id)
        if not todo:
            print("To-do not found.")
            return

        original_entry = todo.entry

        # Save old values
        old_task = todo.task
        old_status = todo.status

        # Apply updates
        if task:
            todo.task = task
        if status:
            todo.status = status
        if entry_id:
            todo.entry_id = entry_id

        session.commit()

        entry_to_update = session.query(Todo).get(todo_id).entry or original_entry
        file_path = entry_to_update.content_path

        if entry_to_update and os.path.exists(file_path):
            try:
                with open(file_path, "a", encoding="utf-8") as f:
                    f.write("\n" + "="*40 + "\n")
                    f.write("   ❗️ Previous To-Do Updated\n")
                    f.write("="*40 + "\n")
                    f.write(f"📝 Old Task   : {old_task}\n")
                    f.write(f"📌 Old Status : {old_status.capitalize() if old_status else 'N/A'}\n")

                    f.write("\n" + "="*40 + "\n")
                    f.write("       🔄 New To-Do\n")
                    f.write("="*40 + "\n")
                    f.write(f"📝 Task   : {todo.task}\n")
                    f.write(f"📌 Status : {todo.status.capitalize() if todo.status else 'N/A'}\n")

            except Exception as e:
                print("Failed to append to-do update in entry file:", e)



    