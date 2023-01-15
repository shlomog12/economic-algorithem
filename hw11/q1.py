
from typing import List

#   q1.a
def find_trading_cycle(preferences: List[List[int]]):
    """
    >>> find_trading_cycle([[3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0]])
    [3, 3]
    >>> find_trading_cycle([[2, 0, 3, 1], [0, 1, 2, 3], [1, 0, 2, 3], [0, 3, 2, 1]])
    [0, 2, 1, 0]
    >>> p1 = [[5, 1, 2, 3, 0, 4], [0, 1, 4, 3, 5, 2], [3, 5, 1, 2, 0, 4], [3, 0, 5, 4, 1, 2], [2, 1, 4, 3, 5, 0], [1, 0, 2, 3, 5, 4]]
    >>> find_trading_cycle(p1)
    [0, 5, 1, 0]
    """
    res = []
    current = 0
    while (current not in res):
        res.append(current)
        current = preferences[current][0]
    index_first_in_cycle = res.index(current)
    res.append(current)
    return res[index_first_in_cycle:]

#   q1.b
def trading_cycles_algo(preferences: List[List[int]]):
    """
    >>> trading_cycles([[3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0]])
    {3: 3, 2: 2, 1: 1, 0: 0}
    >>> trading_cycles([[2, 0, 3, 1], [0, 1, 2, 3], [1, 0, 2, 3], [0, 3, 2, 1]])
    {0: 2, 2: 1, 1: 0, 3: 3}
    """
    selected = set()
    res = {}
    n = len(preferences)
    while(len(selected) < n):
        cur_cycle = find_trading_cycle(preferences)
        for i in range(len(cur_cycle)-1):
            player_i =  cur_cycle[i]
            selected.add(player_i)
            res[player_i] = cur_cycle[i+1]
        preferences  = update_preferences(preferences, cur_cycle[:-1])
    return res

def update_preferences(preferences:List[List[int]], deleted:set)->List[List[int]]:
    """
    >>> update_preferences([[3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 0]],[2,3])
    [[1, 0], [1, 0], [1, 0], [1, 0]]
    >>> update_preferences([[2, 0, 3, 1], [1, 0, 2, 3], [1, 0, 2, 3], [0, 3, 2, 1]],[2,3])
    [[0, 1], [1, 0], [1, 0], [0, 1]]
    >>> update_preferences([[2, 0, 3, 1], [1, 0, 2, 3], [1, 0, 2, 3], [0, 3, 2, 1]],[0,2])
    [[3, 1], [1, 3], [1, 3], [3, 1]]
    >>> update_preferences([[2, 0, 1], [1, 0, 2], [1, 0, 2]],[0])
    [[2, 1], [1, 2], [1, 2]]
    """
    for p in preferences:
        for i in deleted:
            p.remove(i)
    return preferences



def main():
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

if __name__ == "__main__":
    main()