import networkx as nx
import math


def log2_edge(edge:tuple):
    w = edge[2]['weight']
    return  (edge[0], edge[1], math.log2(w))

def log2_edges(G:nx.DiGraph):
    """
    for all edges e in G: e.weight = log2(e.weight)
    """
    log2G = G.copy()
    log2G.add_weighted_edges_from(map( lambda e: log2_edge(e), log2G.edges(data=True)))
    return log2G

def crate_DIGraph(edges:list):
    """
    Create directed graph for tests
    """
    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    return G

def find_cycle_with_multiplication_less_than_one(G:nx.DiGraph):
    """
    Returns a cycle with a total weight less than 1, if it exists.
    Uses reduction to find a negative circle (bellman ford algorithm) using the log2G function
    because that for xi positive 0 <= i
    x1*x2*x3 ... <= 1  <-> log2(x1*x2*x3 ...) <= log2(1) <-> log2(x1)+log2(x2)+log2(x3)+... <= 0
    
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(1,2,4),(2,5,6)]))
    'not exist'
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(2,6,0.4),(6,5,2),(5,2,1),(2,1,19),(1,3,19),(3,2, 199)]))
    [5, 2, 6, 5]
    
    0.4 * 2 * 1.25 == 1
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(2, 6, 0.4),(6, 5, 2),(5, 2, 1.3)]))
    'not exist'
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(2, 6, 0.4),(6, 5, 2),(5, 2, 1.25)]))
    'not exist'
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(2,6,0.4),(6,5,2),(5,2,1.249)]))
    [5, 2, 6, 5]

    0.1 * 10 * 1 == 1
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(2,6,0.1),(6,5,10),(5,2,1)]))
    'not exist'
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(2,6,0.1),(6,5,10),(5,2,0.99)]))
    [5, 2, 6, 5]
    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([(2,6,0.1),(6,2,0.1)]))
    [2, 6, 2]

    >>> find_cycle_with_multiplication_less_than_one(crate_DIGraph([]))
    'not exist'
    """
    log2G = log2_edges(G)
    for c in nx.strongly_connected_components(G):
        try:
            return nx.find_negative_cycle(log2G, list(c)[0])
        except nx.NetworkXError:
            continue
    return "not exist"


def main():
    import doctest
    print(doctest.testmod())

if __name__ == "__main__":
    main()