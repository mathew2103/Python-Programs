books = []
def push():
    bookNo = int(input("Enter book number: "))
    name = input("Enter book name: ")

    books.append([bookNo, name])
    print("Added book!")


def pop():
    book = books.pop()
    print(f"Removed {book[1]} (ID: {book[0]})")


def display():
    print("Books Stack:")
    for i in books[::-1]:
        print(i)


while True:
    print("BOOKS MENU\n1. Add book\n2. Remove book\n3. Display Books")
    x = int(input("Enter desired option: ") or 0)
    if x == 1:
        push()
    elif x == 2:
        pop()
    elif x == 3:
        display()
    else:
        break
