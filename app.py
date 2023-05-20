from models import Base, Book, session, engine
from datetime import datetime
import csv


def clean_date(publish_date: str) -> datetime.date:
    clean = datetime.strptime(publish_date, "%B %d, %Y").date()
    return clean


def clean_price():
    pass


def add_csv():
    with open("suggested_books.csv") as csvfile:
        data = csv.reader(csvfile)
        for row in data: 
            book = Book(title=row[0], author=row[1], publish_date=clean_date(row[2]))
            print(book)


def menu():
    while True:
        print(
            """
            \nPROGRAMMING BOOKS
            \r1) Add book
            \r2) View all books
            \r3) Search for book
            \r4) Book analysis
            \r5) Exit
        """
        )
        choice = int(input("What would you like to do? "))

        if choice in range(1, 6):
            return choice
        else:
            print("Please make a selection from the list above.")
            input("Press Enter.")


def app():
    app_running = True
    while app_running:
        choice = menu()

        match choice:
            case 1:
                print("add book")
                add_csv()
            case 2:
                print("view all books")
            case 5:
                print("GOODBYE")
                app_running = False
            case _:
                print("default action.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    app()
