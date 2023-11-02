#
#


from database import create_database_and_tables


def retrieve_numeric_input(called):
    input_ok = False
    n = None

    while not input_ok:
        n = input(f"\nEnter {called}")

        try:
            n = float(n)
            input_ok = True
        except ValueError:
            print("Please provide a numeric input")

    return n


def add_box_menu():
    box_name = input("\nPlease enter a name for the box: ")

    box_height = retrieve_numeric_input(called="the box's height in meters")
    box_width = retrieve_numeric_input(called="the box's width in meters")
    box_length = retrieve_numeric_input(called="the box's length in meters")

    # add_box_to_database
    

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
