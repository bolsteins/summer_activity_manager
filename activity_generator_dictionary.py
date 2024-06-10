activities = {
    "weekday_one": ["Read a book", "Go for a run", "Visit a museum", "Go to the cinema", "Go for a walk", "Go to IKEA"],
    "weekday_multiple": ["Have a game night", "Go to a cafe", "Go to a workshop"],
    "weekend_one": ["Go hiking", "Mow the lawn", "Do yoga",  "Watch a movie", "Bake a cake"],
    "weekend_multiple": ["Host a BBQ", "Go to Jūrmala", "Go to a concert", "Plan a day trip", "Go camping"]
}

def find_activity(day_type, participants):
    key = f"{day_type}_{participants}"
    return activities.get(key, ["No activities available"])[0]

def generate_activity():
    day_type = input("Is it a weekday or weekend? ").strip().lower()
    participants = input("Is it for one person or multiple people? ").strip().lower()
    
    if day_type not in ["weekday", "weekend"]:
        print("Invalid day type. Please enter 'weekday' or 'weekend'.")
        return
    
    if participants not in ["one", "multiple"]:
        print("Invalid number of participants. Please enter 'one' or 'multiple'.")
        return

    activity = find_activity(day_type, participants)
    print("Suggested Activity:", activity)
