from jar import Jar


def test_init():
    galleta = Jar(10)
    assert galleta.capacity == 10
    assert galleta.size == 0
    galleta1 = Jar()
    assert galleta1.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    galleta = Jar()
    galleta.deposit(3)
    assert galleta.size == 3
    galleta.deposit(3)
    assert galleta.size == 6
    galleta.deposit(4)
    assert galleta.size == 10


def test_withdraw():
    galleta = Jar()
    galleta.deposit(10)
    galleta.withdraw(3)
    assert galleta.size == 7
    galleta.withdraw(2)
    assert galleta.size == 5
    galleta.withdraw(3)
    assert galleta.size == 2
