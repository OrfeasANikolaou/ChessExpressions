import my_re_functions as mrf
import sys
import os




def main():
    games = []
    if len(sys.argv) != 2:
        print(f"argument count must be 2, given is {len(sys.argv)}")
        exit(1)
    if sys.argv[1][-4:] != ".pgn":
        print(f"argument extension must be .pgn")
        exit(1)
    # https://stackoverflow.com/a/82852
    if not os.path.isfile(sys.argv[1]):
        print(f"{sys.argv[1]} not found or could not be opened")
        exit(1)
    with open(sys.argv[1], "r") as file:
        first_time = True
        game = ""
        for line in file:
            if ("Event" in line) and first_time == False:
                games.append(game)
                game = ""
            if ("Event" in line) and first_time == True:
                first_time = False
            game += line

    n_of_games = len(games)
    for i in range(n_of_games):
        print(f"\nΔΕΔΟΜΕΝΑ ΤΟΥ ΑΓΩΝΑ n.{i+1}:") 
        print(f"\tΔΙΑΦΟΡΑ ΔΥΝΑΜΙΚΟΤΗΤΑΣ: {mrf.diff_elo(games[i])}")
        print(f"\tΝΙΚΗΤΗΣ: {mrf.winner(games[i])}")
        print(f"\tΗΜΕΡΟΜΗΝΙΑ ΑΓΩΝΑ: {mrf.date_of_game(games[i])}")
        print(f"\tΠΛΗΘΟΣ ΚΙΝΗΣΕΩΝ: {mrf.moves(games[i])}")
        

if __name__ == "__main__":
    main()
