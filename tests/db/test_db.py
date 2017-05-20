import src.db.manager as db

root_path = "tests/db/simple_db_example.py"
dir_path = "simple_db_example.py"


def test_query():
    with open(root_path, 'r') as test_file:
        assert db.ask_database("SORT SIMPLE PYTHON".split(' ')) == "".join(test_file.readlines())
