"""
The script-query-to-database-query layer
"""
import src.db.database as db


def start_database():
    """
    Starts the database updater and put it in RAM
    :return: nothing
    """
    db.start_database()
    return


def stop_database():
    """
    Stops the database updater and kills the database memory
    :return:
    """
    db.stop_database()


def ask_database(script_query):
    """
    Returns the result of the query passed to the database
    :param script_query: the query to pass to the database
    :return: the result of the query
    """
    algo_type, algo_spec, algo_lang = script_query
    return db.get_algorithm(algo_type, algo_spec, algo_lang)
