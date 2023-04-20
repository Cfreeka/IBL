from jar import Jar


def test_init():
    # Test initialization with default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test initialization with non-default capacity
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # Test initialization with negative capacity
    try:
        Jar(-5)
    except ValueError:
        assert True
    else:
        assert False


def test_str():
    # Test empty jar
    jar = Jar()
    assert str(jar) == ""

    # Test jar with cookies
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    # Test depositing positive number of cookies
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    # Test depositing negative number of cookies
    try:
        jar.deposit(-3)
    except ValueError:
        assert jar.size == 5
    else:
        assert False

    # Test depositing more cookies than capacity
    try:
        jar.deposit(20)
    except ValueError:
        assert jar.size == 5
    else:
        assert False


def test_withdraw():
    # Test withdrawing positive number of cookies
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    assert jar.size == 7

    # Test withdrawing negative number of cookies
    try:
        jar.withdraw(-3)
    except ValueError:
        assert jar.size == 7
    else:
        assert False

    # Test withdrawing more cookies than in jar
    try:
        jar.withdraw(10)
    except ValueError:
        assert jar.size == 7
    else:
        assert False


def test_size():
    # Test empty jar
    jar = Jar()
    assert jar.size == 0

    # Test non-empty jar
    jar.deposit(5)
    assert jar.size == 5
