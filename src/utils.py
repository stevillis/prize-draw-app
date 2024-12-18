import random
from typing import List


def select_n_groups(names: List[str], n_groups: int) -> List[List[str]]:
    """
    Shuffle the list of names and divide them into n groups.

    Args:
        names (list): List of names to be divided into groups.
        n_groups (int): Number of groups to divide the names into.

    Returns:
        list: A list of lists, where each sublist represents a group.
    """
    random.shuffle(names)
    groups = [[] for _ in range(n_groups)]
    for i, name in enumerate(names):
        groups[i % n_groups].append(name)
    return groups


def select_n_names(names: List[str], n: int) -> List[str]:
    """
    Randomly select n names from the list of names.

    Args:
        names (list): List of names to select from.
        n (int): Number of names to select.

    Returns:
        list: A list of n randomly selected names.
    """
    return random.sample(names, n)
