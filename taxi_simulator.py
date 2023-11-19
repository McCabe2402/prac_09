from taxi import Taxi, SilverServiceTaxi


def display_taxis(taxis):
    """Display the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Choose a taxi from the available options."""
    display_taxis(taxis)
    choice = input("Choose taxi: ")
    try:
        choice = int(choice)
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input (not a number)")


def drive_taxi(taxi):
    """Drive the chosen taxi."""
    if taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0

    if taxi.fuel <= 0:
        print(f"{taxi.name} has no fuel. Choose another taxi.")
        return 0

    distance = input("Drive how far? ")
    try:
        distance = float(distance)
        fare = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid input (not a number)")
    return 0


def main():
    print("Let's drive!")
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    while True:
        print(f"Bill to date: ${bill_to_date:.2f}")
        print("q)uit, c)hoose taxi, d)rive")

        user_choice = input(">>> ").lower()

        if user_choice == 'q':
            print(f"Total trip cost: ${bill_to_date:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif user_choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif user_choice == 'd':
            bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
