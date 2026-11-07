
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

teams = []
matches = []

MIN_ID = 1


def show_manu():
    print("""
        ====== TORNAMENT MANAGER ======
        1. Add team
        2. Show all teams
        3. Add match result
        4. Show standings
        5. Show leading team
        6. Show best attacking team
        7. Show team success rate
        8. Show teams without wins
        9. Show tournament summary
        10. Check championship potential
        0. Exit
        Choose an option:
        """)


def get_input():
   while True:
    try:
        result = int(input("Choose Option from 0 - 10: "))

        if result > 10 or result < 0:
            print("enter number between 0 - 10")
            continue

        return result
    except ValueError:
        print("Enter a Number!!")


def add_team():
    while True:
        try:
            team_id = int(input("enter ID number:"))

            if team_id < MIN_ID:
                print("enter a valid id")
                continue

            break

        except ValueError:
            print("invalid id")

    for team in teams:
        if team["id"] == team_id:
            print("team id already exists")
            return

    team_name = input("enter the team name:").strip()

    if team_name.strip() == "":
        print("enter a name")
        return team_name

    for team in teams:
        if team["name"].lower() == team_name.lower():
            print("team already exists")
            return team_name

    new_team = {
        "id": team_id,
        "name": team_name,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }

    teams.append(new_team)
    print("Team added successfully!")


def show_team():
    if not teams:
        print("there is no team")
        return

    for team in teams:
        print(
            team["id"],
            team["name"],
            team["played"],
            team["points"]
        )

def find_team(team_id):
    for team in teams:
        if team["id"] == team_id:
            return team
       

    return None

def add_match():
    try:
        home_team_id = int(input("entar home team id:"))
        
        if home_team_id < MIN_ID:
            print("invalid team id")
            return
        home_team = find_team(home_team_id)
        if home_team is None:
            print("team not found")
            return

    except ValueError:
        print("invalid team id")
        return
        


def main():
    
    while True:
        show_manu()
        user_choice = get_input()

        if user_choice == 1:
            add_team()

        elif user_choice == 2:
            show_team()


        elif user_choice == 3:
            add_match()


        elif user_choice == 0:
            print("Goodbye!")
            break


main()
