from utils import get_input

source = [val for val in get_input(day=4).split("\n")]

# Sample source
# source = [
#     "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
#     "",
#     "22 13 17 11  0",
#     " 8  2 23  4 24",
#     "21  9 14 16  7",
#     " 6 10  3 18  5",
#     " 1 12 20 15 19",
#     "",
#     " 3 15  0  2 22",
#     " 9 18 13 17  5",
#     "19  8  7 25 23",
#     "20 11 10 24  4",
#     "14 21 16 12  6",
#     "",
#     "14 21 17 24  4",
#     "10 16 15  9 19",
#     "18  8 23 26 20",
#     "22 11 13  6  5",
#     " 2  0 12  3  7",
# ]


class Board:
    def __init__(self, index, board_matrix):
        self.board = {}
        self.isDone = False
        self.name = f"Board {index}"
        self.init_board(board_matrix)

    def init_board(self, matrix):
        """
        '92  3 88 13 50',
        '90 70 24 28 52',
        '15 98 10 26  5',
        '84 34 37 73 87',
        '25 36 74 33 63',
        """
        for row_number, row in enumerate(matrix):
            numbers = [e for e in row.split(" ") if e != ""]
            for col_number, number in enumerate(numbers):
                # 92: (0, 0, False) = (row, col, visited)
                self.board[number] = (row_number, col_number, {"marked": False})

    def mark_number(self, value):
        """
        When a number is called out, if the value is in our board
        mark it.
        """
        if value in self.board:
            self.board[value][2]["marked"] = True

    def sum_of_unmarked(self):
        return sum(
            int(number)
            for number, entry in self.board.items()
            if entry[2]["marked"] == False
        )

    def check_rows(self):
        """
        Based on the defition of the board model, each individual entry
        in the board has a (row, col, {marked: bool}). To check the rows
        check the values in position 0.
        """
        return self.check_index(0)

    def check_cols(self):
        """
        Based on the defition of the board model, each individual entry
        in the board has a (row, col, {marked: bool}). To check the rows
        check the values in position 1.
        """
        return self.check_index(1)

    def check_index(self, index):
        """
        If all the entries in a given row or column are set as marked,
        return the index of that given position. The caller would know if
        the index represents a row or a column based on the index passed in.
        index: 0 => row
        index: 1 => col
        """
        for position in range(5):
            if all(
                entry[2]["marked"]
                for entry in self.board.values()
                if entry[index] == position
            ):
                return position
        return None

    def print_row(self, row_num):
        result = " ".join(
            [
                f"{number}{str(entry[2]['marked'])[0]}"
                for number, entry in self.board.items()
                if entry[0] == row_num
            ]
        )
        print(result)

    def bingo(self):
        result = self.check_rows() is not None or self.check_cols() is not None
        if result:
            self.isDone = True
        return result

    def move(self, number):
        self.mark_number(number)
        return not self.isDone and self.bingo()

    def print(self):
        for row in range(5):
            self.print_row(row)


def build_boards(source):
    boards = []
    rows = []
    for record in source:
        if record == "":
            boards.append(Board(len(boards) + 1, rows))
            rows = []
            continue
        rows.append(record)

    if len(rows):
        # Append the last board, given that the source might not have
        # a final "" separator
        boards.append(Board(len(boards) + 1, rows))

    return boards


bingo_numbers = source.pop(0).split(",")
source.pop(0)  # consume ''
boards = build_boards(source)

print("PART 1")


def move(number, game_boards):
    for board in game_boards:
        board.mark_number(number)

        if board.bingo():
            board.print()
            print(f"{board.name} won with number {number}")
            print(int(number) * board.sum_of_unmarked())
            return True
    return False


for number in bingo_numbers:
    if move(number, boards):
        break

print()
print("PART 2")
score_board = [
    int(number) * board.sum_of_unmarked()
    for number in bingo_numbers
    for board in boards
    if board.move(number)
]

print(score_board[-1])
