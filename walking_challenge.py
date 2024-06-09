def walking_challenge(goal_km, current_progress_km):
    print("\n*** Walking Challenge ***")
    print(f"Goal: {goal_km} km")
    print(f"Current progress: {current_progress_km} km")

    today_km = float(input("\nEnter the kilometers you walked today: "))

    # calculations
    # updating current progress
    current_progress_km += today_km
    # calculating remaining kilometers for reaching the goal
    remaining_km = goal_km - current_progress_km

    # some inspiration defined by how much has been walked
    if today_km >= 10:
        print("Congratulations! You're doing a great job!")
    else:
        print("Keep it up! You can walk more tomorrow.")

    print(f"\nYou need to walk {remaining_km} km more to reach your goal.\n")
