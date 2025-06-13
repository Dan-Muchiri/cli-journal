from models.entry import Entry
from models.todo import Todo
from init import Base, engine
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

fake = Faker()

# Ensure entries directory exists
os.makedirs("entries", exist_ok=True)

try:
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except SQLAlchemyError as e:
    print("Error creating database tables:", e)

def generate_seed_data():
    Base.metadata.bind = engine
    
    # Create session
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    try:
        entries = []
        for _ in range(5):
            title = fake.sentence(nb_words=3).rstrip(".")
            content = fake.paragraph(nb_sentences=5)
            mood = fake.random_int(min=1, max=5)

            entry = Entry.add_entry(title=title, content=content, mood=mood)
            entries.append(entry)

            # Add 2–3 todos per entry
            for _ in range(fake.random_int(min=2, max=3)):
                task = fake.sentence(nb_words=4).rstrip(".")
                status = fake.random_element(elements=('pending', 'done'))
                Todo.add_todo(task=task, entry_id=entry.id, status=status)

        return entries

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()

if __name__ == "__main__":

    generate_seed_data()


