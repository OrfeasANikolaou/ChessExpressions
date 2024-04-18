import re

a_pgn_game = """
[Event "WCh 2023"]
[Site "Astana KAZ"]
[Date "2023.04.09"]
[Round "1.1"]
[White "Nepomniachtchi,I"]
[Black "Ding Liren"]
[Result "1/2-1/2"]
[WhiteElo "2795"]
[BlackElo "2788"]
[ECO "C85"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Bxc6 dxc6 7.Re1 Nd7 8.d4 exd4
9.Qxd4 O-O 10.Bf4 Nc5 11.Qe3 Bg4 12.Nd4 Qd7 13.Nc3 Rad8 14.Nf5 Ne6 15.Nxe7+ Qxe7
16.Bg3 Bh5 17.f3 f6 18.h3 h6 19.Kh2 Bf7 20.Rad1 b6 21.a3 a5 22.Ne2 Rxd1 23.Rxd1 Rd8
24.Rd3 c5 25.Qd2 c6 26.Rxd8+ Nxd8 27.Qf4 b5 28.Qb8 Kh7 29.Bd6 Qd7 30.Ng3 Ne6
31.f4 h5 32.c3 c4 33.h4 Qd8 34.Qb7 Be8 35.Nf5 Qd7 36.Qb8 Qd8 37.Qxd8 Nxd8
38.Nd4 Nb7 39.e5 Kg8 40.Kg3 Bd7 41.Bc7 Nc5 42.Bxa5 Kf7 43.Bb4 Nd3 44.e6+ Bxe6
45.Nxc6 Bd7 46.Nd4 Nxb2 47.Kf3 Nd3 48.g3 Nc1 49.Ke3  1/2-1/2
"""


def winner(a_pgn_game):
    result = re.findall(r'\[Result "(\d/?\d?)-(\d/?\d?)"\]', a_pgn_game)
    if result[0][0] == '1/2':
        return "ΙΣΟΠΑΛΙΑ"
    # https://chat.openai.com/c/4ce5bc08-4a33-41cd-bc65-77828fdfe9c5
    # white wins when result "1-0"
    elif result[0][0] == '1':
        return "ΛΕΥΚΑ"
    else:
        return "ΜΑΥΡΑ"

def date_of_game(a_pgn_game):
    pass


def diff_elo(a_pgn_game):
    pass


def moves(a_pgn_game):
    pass


if __name__ == "__main__":
    print(f"ΔΙΑΦΟΡΑ ΔΥΝΑΜΙΚΟΤΗΤΑΣ: {diff_elo(a_pgn_game)}")
    print(f"ΝΙΚΗΤΗΣ: {winner(a_pgn_game)}")
    print(f"ΗΜΕΡΟΜΗΝΙΑ ΑΓΩΝΑ: {date_of_game(a_pgn_game)}")
    print(f"ΠΛΗΘΟΣ ΚΙΝΗΣΕΩΝ: {moves(a_pgn_game)}")
