from todo_list import TodoList
from activity_generator_dictionary import generate_activity
from quote_api import QuoteService
from walking_challenge import walking_challenge
from utils import display_menu

def main():
    todo_list = TodoList()
    quote_service = QuoteService()

    # walking challenge goal is set to 500 km
    goal_km = 500 
    # walking challenge progress that can be changed here every day
    current_progress_km = 70.4 

    while True:
        choice = display_menu([
            "Manage To-Do List",
            "What to do?",
            "Walking challenge",
            "Get Quote of the Day",
            "Exit"
        ])

        if choice == 1:
            todo_list.manage()
        elif choice == 2:
            generate_activity()
        elif choice == 3:
            walking_challenge(goal_km, current_progress_km)
        elif choice == 4:
            quote_service.display_quote()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()