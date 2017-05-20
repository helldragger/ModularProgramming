import src.db.manager as db


def test_query():
    with open('tests/db/simple_db_example.py', 'r') as test_file:
        assert db.ask_database("SORT SIMPLE PYTHON".split(' ')) == "".join(test_file.readlines())
