class Board:
    def __init__(self):
        # Initialize the board with nine dots
        self.board = ['.'] * 9

    def display(self):
        # Display the board in a 3x3 grid format
        for row in range(3):
            print(" ".join(self.board[row * 3:(row + 1) * 3]))
        print()  # Add an empty line for better readability

    def place_marker(self, position, marker):
        # Place 'X' or 'O' on the board at the specified position
        # `position` should be a number between 1 and 9
        if marker not in ['X', 'O']:
            print("Invalid marker! Use 'X' or 'O'.")
            return
        if position < 1 or position > 9:
            print("Invalid position! Choose a number between 1 and 9.")
            return
        if self.board[position - 1] != '.':
            print("Position already occupied! Choose another spot.")
            return
        self.board[position - 1] = marker
