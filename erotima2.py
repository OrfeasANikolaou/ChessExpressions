import sys
from datetime import datetime

import matplotlib.pyplot as plt

import chess_helper_functions as chf
import my_re_functions as mrf


def main():
    if chf.arg_checker(sys.argv) != 0:
        return 1

    games = chf.mk_games(sys.argv[1])
    day_of_week_game_count = chf.days_counter(games)

    days = list(day_of_week_game_count.keys())
    values = list(day_of_week_game_count.values())

    plt.bar(days, values, color="deeppink")
    plt.xlabel("Days of the week")
    plt.ylabel("Number of matches")
    plt.show()


if __name__ == "__main__":
    main()
