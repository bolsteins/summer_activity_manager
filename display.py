def display_menu(options):
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    choice = int(input("Choose an option: "))
    return choice