import my_re_functions as mrf
import chess_helper_functions as chf
import sys
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    if chf.arg_checker(sys.argv) != 0:
        return 1
    games = chf.mk_games(sys.argv[1])
    
    count = {"Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0, "Sun": 0}
    for game in games:
        if mrf.date_of_game(game) != None:
            # https://chat.openai.com/share/728d7c1d-f517-4145-b4d6-1f0ea7b8dc8e 
            try:
                date_obj = datetime.strptime(mrf.date_of_game(game), "%d-%m-%Y")
                day_of_week = date_obj.strftime("%a")
                count[day_of_week] += 1
            except ValueError:
                # spoof interpreter to execute except and goes to next
                pass
    # https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
    days = list(count.keys())
    values = list(count.values())
    plt.bar(days, values, color="deeppink")
    plt.xlabel("Days of the week")
    plt.ylabel("Number of matches")
    plt.show()

if __name__ == "__main__":
    main()
