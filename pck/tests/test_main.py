from softeng.example import print_world

def test_main():
    test = print_world(4)
    assert(test == "hello world")


# Test Function
def test_marker_validation():
    game_board = Board()

    # Valid markers
    assert game_board.place_marker(1, 'X') == True, "Test failed for valid marker 'X'"
    assert game_board.place_marker(2, 'O') == True, "Test failed for valid marker 'O'"

    # Invalid markers
    assert game_board.place_marker(3, 'A') == False, "Test failed for invalid marker 'A'"
    assert game_board.place_marker(4, '1') == False, "Test failed for invalid marker '1'"
    assert game_board.place_marker(5, '') == False, "Test failed for empty marker"

    print("All marker validation tests passed!")


# Run the test
test_marker_validation()
