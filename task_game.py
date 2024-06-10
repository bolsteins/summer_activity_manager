def task_game():
    tasks = [
        "Task 1: Did you make your bed?",
        "Task 2: Did you exercise for at least 30 minutes?",
        "Task 3: Did you drink 8 glasses of water?",
        "Task 4: Did you read for 30 minutes?",
        "Task 5: Did you work on a personal project?",
        "Task 6: Did you connect with a friend or family member?"
    ]
    points = 0

    print("\n*** Daily Task Game ***")
    for task in tasks:
        response = input(f"{task} (yes/no): ").strip().lower()
        if response == "yes":
            points += 1

    print(f"\nYou have completed {points} out of 6 tasks today.")
    if points == 6:
        print("Excellent! You completed all your tasks today!")
    elif points >= 4:
        print("Great job! You completed most of your tasks.")
    elif points >= 2:
        print("Good effort! Try to complete more tasks tomorrow.")
    else:
        print("You can do better! Let's aim for more completed tasks tomorrow.")
    # 10 points for each task
    print(f"Total Points: {points * 10}\n")
