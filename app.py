from models import Base, Book, session, engine
import datetime
import csv


def clean_date(publish_date: str) -> datetime.date:
    try:
        clean_date = datetime.datetime.strptime(publish_date, "%B %d, %Y").date()
    except ValueError:
        input("*** DATE ERROR ***")
        return
    else:
        return clean_date


def clean_price(price_str):
    try:
        price_float = float(price_str)
    except ValueError:
        input("*** PRICE ERROR ***")
        return
    else:
        return int(price_float * 100)


def add_csv():
    with open("suggested_books.csv") as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title == row[0]).one_or_none()
            if book_in_db == None:
                book = Book(
                    title=row[0],
                    author=row[1],
                    publish_date=clean_date(row[2]),
                    price=clean_price(row[3]),
                )
                session.add(book)

        session.commit()


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
                title = input("Title: ")
                author = input("Author: ")
                date_error = True
                while date_error:
                    publish_date = input("Published Date: ")
                    publish_date = clean_date(publish_date)
                    if type(publish_date) == datetime.date:
                        date_error = False
                price_error = True
                while price_error:
                    price = input("Price: ")
                    price = clean_price(price)
                    if type(price) == int:
                        price_error = False

                new_book = Book(
                    title=title, author=author, publish_date=publish_date, price=price
                )
                session.add(new_book)
                session.commit()
                print("Book added!")
            case 2:
                print("view all books")
            case 5:
                print("GOODBYE")
                app_running = False
            case _:
                print("default action.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    app()
