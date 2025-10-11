import sys

# Import all functionality scripts
from add_member import addmember
from update_member import updatememberemail
from delete_member import deletemember
from add_book import addbook
from update_book_stock import updatebookstock
from delete_book import deletebook
from list_books import listbooks
from barrow_book import borrowbook
from return_book import returnbook
from list_product import listproducts
from update_product import updatestock

def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Member")
        print("2. Update Member Email")
        print("3. Delete Member")
        print("4. Add Book")
        print("5. Update Book Stock")
        print("6. Delete Book")
        print("7. List Books")
        print("8. Borrow Book")
        print("9. Return Book")
        print("10. List Products")
        print("11. Update Product Stock")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter member name: ").strip()
            email = input("Enter member email: ").strip()
            result = addmember(name, email)
            print("Result:", result)
        elif choice == "2":
            member_id = int(input("Enter member ID: ").strip())
            new_email = input("Enter new email: ").strip()
            result = updatememberemail(member_id, new_email)
            print("Result:", result)
        elif choice == "3":
            member_id = int(input("Enter member ID: ").strip())
            result = deletemember(member_id)
            print("Result:", result)
        elif choice == "4":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            category = input("Enter category (optional): ").strip() or None
            stock = int(input("Enter stock: ").strip())
            result = addbook(title, author, category, stock)
            print("Result:", result)
        elif choice == "5":
            book_id = int(input("Enter book ID: ").strip())
            new_stock = int(input("Enter new stock: ").strip())
            result = updatebookstock(book_id, new_stock)
            print("Result:", result)
        elif choice == "6":
            book_id = int(input("Enter book ID: ").strip())
            result = deletebook(book_id)
            print("Result:", result)
        elif choice == "7":
            books = listbooks()
            if books:
                for book in books:
                    print(book)
            else:
                print("No books found.")
        elif choice == "8":
            member_id = int(input("Enter member ID: ").strip())
            book_id = int(input("Enter book ID: ").strip())
            result = borrowbook(member_id, book_id)
            print("Result:", result)
        elif choice == "9":
            member_id = int(input("Enter member ID: ").strip())
            book_id = int(input("Enter book ID: ").strip())
            result = returnbook(member_id, book_id)
            print("Result:", result)
        elif choice == "10":
            products = listproducts()
            if products:
                for product in products:
                    print(product)
            else:
                print("No products found.")
        elif choice == "11":
            product_id = int(input("Enter product ID: ").strip())
            new_stock = int(input("Enter new stock value: ").strip())
            result = updatestock(product_id, new_stock)
            print("Result:", result)
        elif choice == "0":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
