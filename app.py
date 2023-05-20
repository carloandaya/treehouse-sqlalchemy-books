from models import Base, Book, session, engine

if __name__ == '__main__': 
    Base.metadata.create_all(engine)

    