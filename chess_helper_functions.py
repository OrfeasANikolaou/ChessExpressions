import os
import sys
from datetime import datetime

import my_re_functions as mrf


def arg_checker(args):
    """
    Checks if given arguments are valid for program
    paramter is sys.argv
    """
    if len(args) != 2:
        print(f"argument count must be 2, given is {len(sys.argv)}")
        return 1
    # https://stackoverflow.com/a/82852
    if not os.path.isfile(args[1]):
        print(f"{sys.argv[1]} not found")
        return 2
    if args[1][-4:] != ".pgn":
        print(f"file extension must be .pgn")
        return 3
    return 0


def mk_games(file_name):
    """
    Reads .pgn format file and makes a list of each game
    parameter must be a .pgn format file, since implementation depends on it
    """
    games = []
    # https://chat.openai.com/share/fd663b5a-31cf-44f6-803e-fe64adb07834
    with open(file_name, "r", encoding="latin-1") as f:
        first_time = True
        game = ""
        for line in f:
            if ("Event" in line) and first_time == False:
                games.append(game)
                game = ""
            elif ("Event" in line) and first_time == True:
                first_time = False
            game += line
    return games


def days_counter(games):
    """
    Returns dictioary of days, where value is how many times a match has been played in that day of the week
    paramter must be list of games
    """
    days_count = {"Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0, "Sun": 0}
    for game in games:
        if mrf.date_of_game(game) != None:
            # https://chat.openai.com/share/532292e6-1c57-4632-9d57-727aedb61420
            try:
                date_obj = datetime.strptime(mrf.date_of_game(game), "%d-%m-%Y")
                day_of_week = date_obj.strftime("%a")
                # https://chat.openai.com/share/b48e4985-d8c1-468c-860e-0c8d5dee6311
                days_count[day_of_week] += 1
            except ValueError:
                # spoof interpreter to execture except and goes to next game
                pass
    # https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
    return days_count
