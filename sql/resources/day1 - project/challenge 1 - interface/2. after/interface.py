#
#
# Scope of work:
# - create an interface that offers the user a menu of 5 choices:
# -- 1. Add a box type
# -- 2. Show box types
# -- 3. Load box to container
# -- 4. Show containers
# -- 5. Summary Report
# -- X. Close

# - for now, each choice should print a simple statement indicating
# the choice, eg "Choice 2 selected"

# - the menu should be offered continuously until the user chooses X,
# in which case, the interface greets the user and the
# program terminates

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
    main_menu()

