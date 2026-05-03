from app.main import sestej, odstej, zmnozi


def test_sestej():
    assert sestej(2, 3) == 5


def test_odstej():
    assert odstej(5, 2) == 3


def test_zmnozi():
    assert zmnozi(4, 3) == 12
