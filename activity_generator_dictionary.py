activities = {
    "weekday_one": ["Read a book", "Go for a run", "Visit a museum"],
    "weekday_multiple": ["Have a game night", "Go to a restaurant", "Attend a workshop"],
    "weekend_one": ["Go hiking", "Watch a movie", "Do a DIY project"],
    "weekend_multiple": ["Host a BBQ", "Go to a concert", "Plan a day trip"]
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
