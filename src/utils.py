import random


def select_n_groups(names, n_groups):
    random.shuffle(names)
    groups = [[] for _ in range(n_groups)]
    for i, name in enumerate(names):
        groups[i % n_groups].append(name)
    return groups


def select_n_names(names, n=2):
    return random.sample(names, n)
