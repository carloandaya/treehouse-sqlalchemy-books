from books.models import Base, Book, session, engine
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


def clean_id(book_id, id_list):
    try:
        book_id = int(book_id)
    except ValueError:
        print("*** ID ERROR ***")
        return
    else:
        if book_id in id_list:
            return book_id
        else:
            return


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
                books = session.query(Book)
                for book in books:
                    print(f"{book.id} | {book.title} | {book.author}")
            case 3:
                print("Search for book.")
                # Get a list of available book ids
                book_id_list = [book.id for book in session.query(Book).all()]
                id_error = True
                while id_error:
                    print(f"ID Options: {book_id_list}")
                    id_choice = input("Please make a selection: ")
                    id_choice = clean_id(id_choice, book_id_list)
                    if type(id_choice) == int:
                        id_error = False
                selected_book = session.query(Book).filter(Book.id == id_choice).first()
                print(
                    f"""
                \n{selected_book.title} by {selected_book.author}
                \rPublished Date: {selected_book.publish_date}
                \rPrice: ${selected_book.price / 100}"""
                )
            case 5:
                print("GOODBYE")
                app_running = False
            case _:
                print("default action.")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    add_csv()
    app()
