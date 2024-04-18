import sys
import os

def arg_checker(args):
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
