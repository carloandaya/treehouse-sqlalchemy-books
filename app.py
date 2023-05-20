from models import Base, Book, session, engine

def menu(): 
    while True: 
        print('''
            \nPROGRAMMING BOOKS
            \r1) Add book
            \r2) View all books
            \r3) Search for book
            \r4) Book analysis
            \r5) Exit
        ''')
        choice = int(input('What would you like to do? '))

        if choice in range(1, 5):
            return choice
        else: 
            print('Please make a selection from the list above.')
            input('Press Enter.')

def app():
    app_running = True
    while app_running: 
        choice = menu()

        match choice:
            case 1: 
                print('add book')
            case 2: 
                print('view all books')
            case _:
                print('default action.')


if __name__ == '__main__': 
    Base.metadata.create_all(engine)

    app()
    