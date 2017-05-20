"""
The script-query-to-database-query layer
"""
import src.db.database as db


def ask_database(script_query):
    algo_type, algo_spec, algo_lang = script_query
    return db.get_algorithm(algo_type, algo_spec, algo_lang)
