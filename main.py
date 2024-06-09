from todo_list import TodoList
from activity_generator_dictionary import generate_activity
from quote_api import QuoteService
from utils import display_menu

def main():
    todo_list = TodoList()
    quote_service = QuoteService()

    while True:
        choice = display_menu([
            "Manage To-Do List",
            "What to do?",
            "Get Quote of the Day",
            "Exit"
        ])

        if choice == 1:
            todo_list.manage()
        elif choice == 2:
            generate_activity()
        elif choice == 3:
            quote_service.display_quote()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()