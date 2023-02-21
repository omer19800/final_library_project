import customer
import library
import library as lib
import logger
import book
import time
import re

#need function to print all books on file
# logger.print_all_books()
#need function to print all customers on file
# logger.get_all_customers_details()
#need function to print all logs
# logger.print_all_logs()
#print all late logs
# logger.print_all_late_logs()



#make a simple nice ui for the library
#like a [1] loan a book [2]return a book [3]customer menu [4]book menu [5]log menu [6]exit


#log menu: [1] get all logs [2] get all customers [3] get all books [4] get all logs of late books
#[6] exit generates a goodbye message and exits the program

loaned = bool

if __name__ == '__main__':
    print(f"Hello and welcome to the library!\n"
          f"we have an (allegedly) wide selection of books available for you to take home and read!")
    print("Please use the menu below to interact with the library")
    print("all you need to do is enter the number of the option you want to perform and then press Enter")
    print("please be advised - if it is your first visit to the library please enter 6 at the next menu")
    print("\n")
    # time.sleep(3.5) ###################

    while True:
        print("\n")
        print(f"Please enter the number of the option\n"
            f"[1] Loan A Book\n"
            f"[2] Return A Book\n"
            f"[3] Customer Management Menu\n"
            f"[4] Book Management Menu\n"
            f"[5] Log Management Menu\n"
            f"[6] First Time Customer\n"
            f"[7] Exit\n")


        menu_selection = input("Please Enter Your Selected Option Number: ")

        if re.match(r"[1]", menu_selection):
            print("\n")
            if menu_selection == "1":
                print("Alright so let's loan a book!")
                input_val = input("Do you have the id number of the book you want to loan? if not i can get it for you y/n: ")

                if re.match(r"[yY]", input_val):
                    selected_book_id = int(input("Please enter the id number of the book you want to loan: "))

                elif re.match(r"[nN]", input_val):
                    input_val = input("please enter the book name: ")
                    library.small_loading_animation() #prettify
                    selected_book_id = logger.get_book_id_from_name(input_val) #getting the book id
                    if selected_book_id is not None:
                        print("Now we got the book id from the system lets make the loan")
                    else:
                        print("There was an error retrieving the book id from the system, please try again")
                        pass

                input_val = input("Do you have your customer id number? if not i can get it for you y/n: ")

                if re.match(r"[yY]", input_val):
                    customer_id = int(input("Please enter the customer id number: "))

                elif re.match(r"[nN]", input_val):
                    print("Alright please enter your name so i can fetch it for you")
                    customer_name = input("Please enter your name: ")
                    library.small_loading_animation()  # prettify
                    customer_id = logger.get_customer_id_from_name(customer_name.capitalize())
                    print(f" Got it! your customer id is {customer_id}")

                print("\n")
                print("Now lets make the loan")
                library.Library.loan_a_book(selected_book_id, customer_id)
                loaned = True
                library.small_processing_animation()  # prettify
                logger.update_a_customer_loans(selected_book_id, customer_id)

                print("Completed loan successfully")
            else:
                pass

        # ------------------------------------------------------------------ # visual separation

        elif re.match(r"[2]", menu_selection):
            print("\n")
            if menu_selection == "2":
                print("Alright so let's return a book!, hopefully you've enjoyed it!")

                input_val = input("Do you have the id number of the book you want to return? or shall i get it for you? y/n: ")

                if re.match(r"[yY]", input_val):
                    book_id = int(input("Please enter the id number of the book you want to return: "))

                elif re.match(r"[nN]", input_val):
                    input_val = input("please enter the book name: ")
                    library.small_loading_animation() #prettify
                    selected_book_id = logger.get_book_id_from_name(input_val) #getting the book id
                    if selected_book_id is not None:
                        print("Now we got the book id from the system lets make the loan")
                    else:
                        print("There was an error retrieving the book id from the system, please try again")
                        pass

                input_val = input("Do you have your customer id number? or shall i get it for you? y/n: ")

                if re.match(r"[yY]", input_val):
                    customer_id = int(input("Please enter the customer id number: "))

                elif re.match(r"[nN]", input_val):
                    print("Alright please enter your name so i can fetch it for you")
                    customer_name = input("Please enter your name: ")
                    library.small_loading_animation()  # prettify
                    customer_id = logger.get_customer_id_from_name(customer_name.capitalize())
                    print(f" Got it! your customer id is {customer_id}")

                print("\n")
                print("Now lets make the return")
                print("\n")

                library.Library.return_a_book(selected_book_id, customer_id)
                loaned = False
                library.small_processing_animation()  # prettify
                logger.remove_book_from_customer(selected_book_id, customer_id)
                print("\n completed return successfully\n")

            else:
                pass
        # ------------------------------------------------------------------ # visual separation

        elif re.match(r"[3]", menu_selection):
            while True:
                print("\n")
                print("--Customer Management Menu--\n")
                print("[1] Add a Customer\n"
                      "[2] Remove a Customer\n"
                      "[3] Change a Customer Details\n"
                      "[4] List All Customers\n"
                      "[5] Back to main menu\n")

                menu_selection = input("Please Enter Your Selected Option Number: ")

                if menu_selection == "1":
                    print("\n")
                    print("Alright! welcome to the library!\n"
                        "lets create your account\n")
                    print("We will need some details first\n")
                    personal_id_number = input("Please enter your personal id number: ")
                    customer_name: str.capitalize = input("Please enter your name: ")
                    customer_email = customer.check_customer_email()
                    customer_birth_date = customer.check_birthday()
                    customer_city = input("Please enter your city: ")
                    customer_street = input("Please enter your street: ")
                    customer_house_num = input("Please enter your house number: ")

                    library.Library.create_a_customer(personal_id_number, customer_name, customer_email, customer_birth_date,
                                                        customer_city, customer_street, customer_house_num)

                elif menu_selection == "2":
                    #either get customer id from customer of from name
                    library.Library.remove_a_customer()
                    library.small_loading_animation()  # prettify
                    print("Suuccessfully removed a customer")

                elif menu_selection == "4":
                    print("\n")
                    print("Fetching all customers and their information")
                    library.small_loading_animation()
                    logger.get_all_customers_details()

                elif menu_selection == "3":
                    print("\n")
                    print("--Customer Details--\n")
                    print("First ill need the customer id number\n")
                    customer_id = int(input("Please enter the customer id number: "))
                    print("so what do you want to change?\n")

                    selected_customer = logger.get_customer_instance_by_id(customer_id)

                    print("To change customer name  - enter 1\n"
                          "To change customer address - enter 2\n"
                          "To change customer email - enter 3\n")
                    menu_selection = input("Please Enter Your Selected Option Number: ")

                    if menu_selection == "1":
                        new_name = input("Please enter the new name: ")
                        selected_customer.set_customer_name(new_name)

                    elif menu_selection == "2":
                        new_city = input("Please enter the new city: ")
                        new_street = input("Please enter the new street: ")
                        new_house_num = input("Please enter the new house number: ")
                        selected_customer.address.set_city(new_city)
                        selected_customer.address.set_street(new_street)
                        selected_customer.address.set_house_num(new_house_num)
                        logger.update_a_customer_instance(selected_customer)

                    elif menu_selection == "3":
                        print("\n")
                        selected_customer.set_customer_email(customer.check_customer_email())
                        logger.update_a_customer_instance(selected_customer)

                elif menu_selection == "5":
                        break
                else:
                    pass

        # ------------------------------------------------------------------ # visual separation

        elif re.match(r"[4]", menu_selection):
            while True:
                print("\n")
                print("--Book Management Menu--\n")
                print("[1] Add a Book\n"
                      "[2] Change a Book Details\n"
                      "[3] List All Books\n"
                      "[4] Back to main menu\n")

                menu_selection = input("Please Enter Your Selected Option Number: ")

                if menu_selection == "1":
                    print("\n")
                    print("Alright! Let's add a book to the library\n")
                    book_title = input("Please enter the book title: ")
                    book_author = input("Please enter the book author: ")
                    book_year = input("Please enter the book year of release: ")
                    book_type = input("If you want to specify a loan time limit through type (1/2/3), please enter the number now, else keep empty: ")
                    if book_type is not None:
                        library.Library.add_a_book(book_title, book_author, book_year, book_type)
                    else:
                        library.Library.add_a_book(book.Book.generate_book_id, book_title, book_author, book_year)

                elif menu_selection == "2":
                    print("\n")
                    print("--Book Details--\n")
                    print("First I'll need the book's ID number\n")
                    book_id = int(input("Please enter the book ID number: "))
                    selected_book = logger.get_book_instance_by_id(book_id)

                    print("So what do you want to change?\n")

                    print("To change book title - enter 1\n"
                          "To change book author - enter 2\n"
                          "To change book year - enter 3\n"
                          "To change book type (loan time limit) - enter 4\n")

                    menu_selection = input("Please Enter Your Selected Option Number: ")

                    if menu_selection == "1":
                        new_title = input("Please enter the new title: ")
                        selected_book.set_book_title(new_title)

                    elif menu_selection == "2":
                        new_author = input("Please enter the new author: ")
                        selected_book.set_book_author(new_author)

                    elif menu_selection == "3":
                        new_genre = input("Please enter the new year: ")
                        selected_book.set_book_year(new_genre)

                    elif menu_selection == "4":
                        print("There are 3 options for limiting the length of the loan:\n"
                              "1) Type 1 - Allows the book to be loaned up to 10 days\n"
                              "2) Type 2 - Allows the book to be loaned up to 5 days\n"
                              "3) Type 3 - Allows the book to be loaned up to 2 days\n")

                        new_type = int(input("Please enter the new type for the loan time limit: "))
                        selected_book.set_book_type(new_type)
                        logger.update_a_book(selected_book)

                elif menu_selection == "3":
                    print("\n")
                    print("Fetching all books and their information\n")
                    library.small_loading_animation()
                    logger.print_all_books()

                elif menu_selection == "4":
                    break
            else:
                pass

        # ------------------------------------------------------------------ # visual separation

        elif re.match(r"[5]", menu_selection):
            while True:
                print("\n")
                print("--Logs Management Menu--\n")
                print("[1] Get All Logs\n"
                      "[2] Get All Customers\n"
                      "[3] Get All Books\n"
                      "[4] Get All Logs of Late Books\n"
                      "[5] Back to main menu\n")

                menu_selection = input("Please Enter Your Selected Option Number: ")

                if menu_selection == "1":
                    print("\n")
                    print("Fetching all logs")
                    library.small_loading_animation()
                    logger.print_all_logs()

                elif menu_selection == "2":
                    print("\n")
                    print("Fetching all customers and their information")
                    library.small_loading_animation()
                    logger.print_all_customers()

                elif menu_selection == "3":
                    print("\n")
                    print("Fetching all books")
                    library.small_loading_animation()
                    logger.print_all_books()

                elif menu_selection == "4":
                    print("\n")
                    print("Fetching all logs of late books")
                    library.small_loading_animation()
                    logger.print_all_late_logs()

                elif menu_selection == "5":
                    break
            else:
                pass

        # ------------------------------------------------------------------ # visual separation

        elif re.match(r"[6]", menu_selection):
            print("Alright! welcome to the library!\n"
                  "lets create your account\n")
            print("We will need some details first\n")
            personal_id_number = input("Please enter your personal id number: ")
            customer_name: str.capitalize = input("Please enter your name: ")
            customer_email = customer.check_customer_email()
            customer_birth_date = customer.check_birthday()
            customer_city = input("Please enter your city: ")
            customer_street = input("Please enter your street: ")
            customer_house_num = input("Please enter your house number: ")

            library.Library.create_a_customer(personal_id_number, customer_name, customer_email, customer_birth_date,
                                              customer_city,
                                              customer_street, customer_house_num)

        # ------------------------------------------------------------------ # visual separation

        elif re.match(r"[7]", menu_selection):
            print("Thank you for using the library!\n")
            print(f"Goodbye, have a nice day!")
            if loaned:
                print("Enjoy your books!")
            exit()

        # ------------------------------------------------------------------ # visual separation
