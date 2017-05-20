"""
The script-query-to-database-query layer
"""
import src.db.database as db


def start_database():
    db.start_database()


def stop_database():
    db.stop_database()


def ask_database(script_query):
    algo_type, algo_spec, algo_lang = script_query
    return db.get_algorithm(algo_type, algo_spec, algo_lang)
