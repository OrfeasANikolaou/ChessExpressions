import sys

import chess_helper_functions as chf
import my_re_functions as mrf


def main():
    if chf.arg_checker(sys.argv) != 0:
        return 1
    games = chf.mk_games(sys.argv[1])
    n_of_games = len(games)
    for i in range(n_of_games):
        print(f"\nΔΕΔΟΜΕΝΑ ΤΟΥ ΑΓΩΝΑ n.{i+1}:")
        print(f"\tΔΙΑΦΟΡΑ ΔΥΝΑΜΙΚΟΤΗΤΑΣ: {mrf.diff_elo(games[i])}")
        print(f"\tΝΙΚΗΤΗΣ: {mrf.winner(games[i])}")
        print(f"\tΗΜΕΡΟΜΗΝΙΑ ΑΓΩΝΑ: {mrf.date_of_game(games[i])}")
        print(f"\tΠΛΗΘΟΣ ΚΙΝΗΣΕΩΝ: {mrf.moves(games[i])}")


if __name__ == "__main__":
    main()
