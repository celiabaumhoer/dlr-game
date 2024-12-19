from softeng.example import print_world

def test_main():
    test = print_world(4)
    assert(test == "hello world")
