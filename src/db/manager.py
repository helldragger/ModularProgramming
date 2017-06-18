"""
The script-query-to-database-query layer
"""

import src.db.errors as err
import src.db.resolver as db


def ask_database(script_query):
    """
    Returns the result of the query passed to the database
    :param script_query: the query to pass to the database
    :return: the result of the query
    """
    algo_type, algo_spec, algo_lang = script_query
    try:
        return db.get_algorithm(algo_type.lower(), algo_spec.lower(), algo_lang.lower())
    except err.DataBaseException as error:
        return error.reason
    except Exception as error:
        return str(error)
