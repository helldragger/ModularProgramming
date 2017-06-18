def clean_tree(tree):
    """
    Cleans the repeated nodes from an unclean tree and returns a clean one

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


def parse_tree(nodes, parent, visited=()):
    """
    returns a whole tree from a list of nodes and theirs children

    :param nodes: the entire list of nodes
    :param parent: the parent node
    :param visited: the already visited nodes
    :return: the unclean tree (include repeated imports of same files)
    """

    visited += (parent,)
    children = nodes[parent]
    child_tree = [parent]  # Dependencies queue here

    for child in children:
        if child in visited:
            raise Exception('Circular dependency: ' + str(parent) + ", " + str(child))
        else:
            child_tree.append(parse_tree(nodes, child, visited))

    return child_tree


def tree_dependencies(nodes, root):
    """
    Returns a dependencies tree from a list of each nodes children and the root

    :param nodes: the list of each nodes dependencies
    :param root: the root of the tree
    :return: the clean dependency tree of the whole tree in a callable order
    """
    return clean_tree(parse_tree(nodes, root))
