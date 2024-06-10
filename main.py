from activity_generator_dictionary import generate_activity
from quote_api import quote
from walking_challenge import walking_challenge
from task_game import task_game
from display import display_menu

def main():
    quote_s = quote()
    # walking challenge goal is set to 500 km
    goal_km = 500 
    # walking challenge progress that can be changed here every day
    # last updated: 09.06.2024
    current_progress_km = 70.4 

    while True:
        choice = display_menu([
            "What to do?",
            "Walking challenge",
            "Daily task game",
            "Quote of the Day",
            "Exit"
        ])

        if choice == 1:
            generate_activity()
        elif choice == 2:
            walking_challenge(goal_km, current_progress_km)
        elif choice == 3:
            task_game()
        elif choice == 4:
            quote_s.display_quote()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Try again!")

if __name__ == "__main__":
    main()