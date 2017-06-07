"""
Algorithm dependencies resolver
"""

import src.db.errors as err
import src.db.filesystem as fs


def get_dependencies_tree(root_path, visited=(), files_cache={}):
    """
    returns a list of dependencies from a root file
    :param root_path: the root file path
    :param visited: the already visited files to check if there is any circular dependencies
    :param files_cache: a cache to store already visited files data
    :return: the unclean dependencies list (include repeated imports of same files)
    """
    print("Building dependecies tree. node visited:", str(visited))

    # Putting the file in cache in case of multiple imports
    if root_path not in files_cache.keys():
        files_cache[root_path] = fs.get_algorithm(root_path)
        print(root_path, "cached")

    visited += (root_path,)
    current_node = files_cache[root_path]
    next_nodes = current_node.requirements
    child_tree = []  # Dependencies queue here

    for node_path in next_nodes:
        childrens_path = get_dependencies_tree(node_path, visited, files_cache)
        print(node_path, "dependencies:", str(childrens_path))
        for child_path in childrens_path:
            if child_path in visited:
                raise err.CircularDependenciesException(node_path, child_path)
            else:
                child_tree.append(child_path)
    child_tree.insert(0, root_path)
    return child_tree


def clean_dependencies_tree(tree):
    """
    Cleans the repeated imports from an unclean tree and returns a clean one
    :param tree: the list of import from the root to the last dependencies found
    :return: a clean dependencies tree
    """
    i = 0
    removed = 0
    length = len(tree)

    while i < length - removed:
        # for each call in the tree
        node = tree[i]
        # the call (i.e. ABCDB becomes node = A | second loop => BCDB
        repetitions = [i]
        # position i of the call is remembered
        j = i + 1
        # position j of the next call after the current call
        while j < length - removed:
            # for each other calls
            if node == tree[j]:
                # if our call is repeated
                repetitions.append(j)
                # we save it's next call
            j += 1
        if len(repetitions) > 1:
            # if there is more than one call of the same import
            del repetitions[-1]
            # we keep the last call of the dependencies
            for j in repetitions[::-1]:
                # for each other call
                del tree[j]
                # we suppress it from the tree
        removed += len(repetitions)
        # we updates the tree actual size for the next verification
        i += 1
    return tree


def resolve_dependencies(root_path):
    """
    Returns the list of dependencies of the specified algorithm file
    :param root_path: the algorithm file
    :return: a queue of files to merge
    """
    unclean_tree = get_dependencies_tree(root_path)
    clean_tree = clean_dependencies_tree(unclean_tree)
    return clean_tree


def merge_sources(call_tree):
    """
    Merges the different dependencies into a single source code in the order of the call tree
    :param call_tree: the dependencies calls in correct order (root -> dependencies -> sub-dependencies...)
    :return: the merged source code
    """
    merged_source_code = ""
    call_tree = call_tree[::-1]
    for i in range(len(call_tree)):
        call = fs.get_algorithm(call_tree[i])
        merged_source_code = "\n\n".join([merged_source_code, call.source_code])
    return merged_source_code


def resolve_source_code(root_path):
    """
    Resolves the algorithm dependencies and merges the sources into a complete algorithm
    :param root_path: the root file path
    :return: the source_code
    """
    call_tree = resolve_dependencies(root_path)
    source_code = merge_sources(call_tree)
    return source_code


def get_algorithm(algo_type, algo_spec, algo_lang):
    """
    Alias function for ease of use, used to resolve an algorithm source code from a network query
    :param algo_type: the type of the algorithm (directory)
    :param algo_spec: the specific version (file name)
    :param algo_lang: the language used (file extension)
    :return: the source code
    """
    root_path = fs.get_file_path(algo_type, algo_spec, algo_lang)
    return resolve_source_code(root_path)
