from wordle import check_word, create_word


def main():
    test_create_word()
    test_check_word()


def test_check_word():
    status = [0, 0, 0, 0, 0]
    assert check_word("melee", status, "eerie") == 5
    assert status == [0, 2, 0, 1, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("speed", status, "erase") == 3
    assert status == [1, 0, 1, 1, 0]
    status = [0, 0, 0, 0, 0]
    assert check_word("eerie", status, "erase") == 5
    assert status == [2, 0, 1, 0, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("melee", status, "eerie") == 5
    assert status == [0, 2, 0, 1, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("weary", status, "weary") == 10
    assert status == [2, 2, 2, 2, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("vague", status, "pills") == 0
    assert status == [0, 0, 0, 0, 0]
    status = [0, 0, 0, 0, 0]
    assert check_word("tears", status, "order") == 2
    assert status == [0, 1, 0, 1, 0]
    status = [0, 0, 0, 0, 0]
    assert check_word("civic", status, "which") == 2
    assert status == [1, 1, 0, 0, 0]


def test_create_word():
    assert create_word("melee") == {
        'e': [1, 3, 4],
        'l': [2],
        'm': [0]
    }

    assert create_word("eerie") == {
        'e': [0, 1, 4],
        'r': [2],
        'i': [3]
    }

    assert create_word("which") == {
        'w': [0],
        'h': [1, 4],
        'i': [2],
        'c': [3]
    }

    assert create_word("civic") == {
        'c': [0, 4],
        'i': [1, 3],
        'v': [2],
    }


if __name__ == "__main__":
    main()
