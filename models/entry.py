from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from init import Base, session
from datetime import datetime
import os


class Entry(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    mood = Column(Integer, CheckConstraint('mood >= 1 AND mood <= 5'), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    content_path = Column(String, nullable=False)

    # Relationship with TodoItem (one-to-many)
    todos = relationship("Todo", back_populates="entry", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Entry(id={self.id}, title='{self.title}', mood={self.mood}, timestamp={self.timestamp})"

    @classmethod
    def add_entry(cls, title, content, mood=None):
        """
        Create a formatted journal entry file and save entry metadata in the database.
        """
        timestamp = datetime.utcnow()
        safe_title = title.replace(' ', '_')
        filename = f"entries/{safe_title}_{timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

        mood_map = {
            1: "😞 Very Sad",
            2: "😕 Sad",
            3: "😐 Neutral",
            4: "🙂 Happy",
            5: "😄 Very Happy"
        }

        mood_label = mood_map.get(mood, "N/A")

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            f.write("="*40 + "\n")
            f.write("       📝 Journal Entry\n")
            f.write("="*40 + "\n\n")
            f.write(f"Title     : {title}\n")
            f.write(f"Mood      : {mood_label}\n")
            f.write(f"Timestamp : {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("-"*40 + "\n")
            f.write("Content:\n")
            f.write("-"*40 + "\n")
            f.write(content + "\n")

        entry = cls(title=title, mood=mood, content_path=filename, timestamp=timestamp)
        session.add(entry)
        session.commit()
        return entry

    @classmethod
    def get_all_entries(cls):
        """
        Retrieve all journal entries.
        """
        return session.query(cls).order_by(cls.timestamp.desc()).all()
    
    @classmethod
    def find_by_id(cls, entry_id):
        """
        Retrieve a journal entry by ID.
        """
        return session.query(cls).filter_by(id=entry_id).first()
    
    @classmethod
    def find_by_title(cls, title):
        """
        Search entries by title (case-insensitive).
        """
        return session.query(cls).filter(cls.title.ilike(f"%{title}%")).all()
    
    @classmethod
    def find_by_mood(cls, mood):
        """
        Filter entries by mood (1 to 5).
        """
        return session.query(cls).filter_by(mood=mood).all()

  
    @staticmethod
    def read_entry_content(entry_id):
        entry = Entry.find_by_id(entry_id)
        if entry:
            try:
                with open(entry.content_path, "r", encoding="utf-8") as f:
                    print(f.read())
            except FileNotFoundError:
                print("Error: Content file not found.")
        else:
            print("Entry not found.")

    @staticmethod
    def delete_entry(entry_id):
        """
        Delete a journal entry by ID, including its associated file.
        """
        entry = session.query(Entry).get(entry_id)
        if entry:
            # Delete the file if it exists
            if entry.content_path and os.path.exists(entry.content_path):
                try:
                    os.remove(entry.content_path)
                except Exception as e:
                    print(f"Warning: Could not delete file. {e}")

            session.delete(entry)
            session.commit()
        else:
            print("Entry not found.")


    @staticmethod
    def update_entry(entry_id, title=None, content=None, mood=None):
        entry = session.query(Entry).get(entry_id)
        if entry:
            old_path = entry.content_path

            if title:
                new_filename = f"entries/{title.replace(' ', '_')}_{entry.timestamp.isoformat()}.txt"
                try:
                    os.rename(old_path, new_filename)
                    entry.content_path = new_filename
                except FileNotFoundError:
                    print("Warning: Original file not found during rename.")
                entry.title = title

            if mood is not None:
                if mood < 1 or mood > 5:
                    raise ValueError("Mood must be an integer between 1 and 5.")
                entry.mood = mood

            if content:
                try:
                    with open(entry.content_path, "w", encoding="utf-8") as f:
                        f.write(f"Title: {entry.title}\n")
                        f.write(f"Mood: {entry.mood if entry.mood else 'N/A'}\n")
                        f.write(f"Timestamp: {entry.timestamp}\n")
                        f.write("\n")
                        f.write(content)
                except FileNotFoundError:
                    print("Error: Content file not found.")

            session.commit()
        else:
            print("Entry not found.")

    
    def get_todos(self):
        """
        Retrieve all to-do items for this entry.
        """
        return self.todos


