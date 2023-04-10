from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("1990-11-25") == ("1990", "11", "25")
    assert check_birthday("1990-july-25") == None
    assert check_birthday("1990-1-5") == None


if __name__ == "__main__":
    main()
