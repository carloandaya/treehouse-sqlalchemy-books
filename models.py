from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base): 
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publish_date = Column(Date)
    price = Column(Integer)

    def __repr__(self):
        return f'<title={self.title}, author={self.author}, publish_date={self.publish_date}, price={self.price}>'