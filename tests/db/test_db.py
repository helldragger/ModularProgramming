import src.db.manager as db


def test_start():
    assert db.start_database() is None


def test_stop():
    db.start_database()
    assert db.stop_database() is None


def test_query():
    db.start_database()
    with open("simple_db_example.py", 'r') as test_file:
        assert db.ask_database("SORT SIMPLE PYTHON") == "".join(test_file.readlines())
