#
#


from database import create_database_and_tables


def main_menu():
    print("Welcome to Freight Manager!\n")

    n = "no_op"

    while n.upper() != 'X':
        print("1. Add a box type\n2. Show box types\n3. Load box to container"
              "\n4. Show container\n5. Summary Report\nX. Close\n")

        n = input("Your choice: ")

        if n == "1":
            print("\nChoice 1 selected\n")
        elif n == "2":
            print("\nChoice 2 selected\n")
        elif n == "3":
            print("\nChoice 3 selected\n")
        elif n == "4":
            print("\nChoice 4 selected\n")
        elif n == "5":
            print("\nChoice 5 selected\n")

    print("\nGoodbye!")


if __name__ == "__main__":
    create_database_and_tables(filename="freight_prod.db")
    main_menu()
