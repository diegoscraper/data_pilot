#
#


from database import create_database_and_tables, add_box, get_all_boxes, get_box, get_container, add_box_to_container, seed_data
from tabulate import tabulate


def retrieve_numeric_input(called):
    input_ok = False
    n = None

    while not input_ok:
        n = input(f"\nEnter {called}: ")

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

    add_box(connection, (box_name, box_height, box_width, box_length))


def display_box_types():
    boxes = get_all_boxes(connection)

    print("\n" + tabulate(boxes,
                          headers=["box_id", "box_name", "height", "width", "length"],
                          tablefmt="psql") + "\n"
          )


def load_box_menu():
    # asking for the box name
    n = input("Enter the name of the box: ")

    # validate whether that exists
    box = get_box(connection, by_name=n)

    if not box:
        print("\nA box by that name could not be found. \n")
    else:
        box_dims = box.height * box.width * box.length
        container_id = input("Enter the id of the container to load the box to: ")

        container = get_container(connection, container_id)

        if container is None or (container.occupied_volume + box_dims <= 30):
            add_box_to_container(connection, box.id, container_id)
            print(f"\nBox '{box.name}' with id '{box.id}' was added to '{container_id}'.\n")
        else:
            print(f"Container {container_id} does not have enough space for box {box.id}.")


def main_menu():
    print("Welcome to Freight Manager!\n")

    n = "no_op"

    while n.upper() != 'X':
        print("1. Add a box type\n2. Show box types\n3. Load box to container"
              "\n4. Show containers\n5. Summary Report\nX. Close\n")

        n = input("Your choice: ")

        if n == "1":
            add_box_menu()
        elif n == "2":
            display_box_types()
        elif n == "3":
            load_box_menu()
        elif n == "4":
            print("\nChoice 4 selected\n")
        elif n == "5":
            print("\nChoice 5 selected\n")

    print("\nGoodbye!")


if __name__ == "__main__":
    connection = create_database_and_tables(filename="freight_prod.db")
    seed_data(connection)
    main_menu()
