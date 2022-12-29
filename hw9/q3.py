

"""
Author: Shlomo Glick
Since: 2022-12
I used Erel Segal-Halevi's code
In the following link: https://github.com/erelsgl-at-ariel/algorithms-5783/blob/main/08-participatory-budgeting/code/fractional.py
But I made it a more general case
"""

from typing import List
import cvxpy

def Nash_budget(total: float, subjects: List[str], preferences:List[List[str]]):
    """
    This function receives as input:
    Total amount of the budget, a list of issues, and a list of the citizens' preferences.
    The function prints a distribution according to the Nash budget

    >>> Nash_budget(total=500, subjects=['Security','Education','Transportation','Communications'],preferences=[['Security','Education'],['Security','Transportation'],['Security','Communications'],['Education','Transportation'],['Security']])
    BUDGET: Security=370.156, Education=64.922, Transportation=64.922, Communications=0.000
    Citizen 0 gives 85.078 to Security and 14.922 to Education 
    Citizen 1 gives 85.078 to Security and 14.922 to Transportation 
    Citizen 2 gives 100.000 to Security 
    Citizen 3 gives 50.000 to Education and 50.000 to Transportation 
    Citizen 4 gives 100.000 to Security 
    """

    m = len(subjects)
    n = len(preferences)
    
    if min(m,n) < 1:
        raise ValueError('number of subjects and number of citizens must be greater than 1')

    minPref = min(preferences, key=lambda pref: len(pref))
    if len(minPref) < 1:
        raise ValueError('Every citizen must choose at least one subject')


    allocations = cvxpy.Variable(m)
    donations = [total/n] * n

    utilities = []
    for i in range(n):
        utilities.append(0)
        for j in preferences[i]:
            index = subjects.index(j)
            utilities[i]+=allocations[index]

    sum_of_logs = cvxpy.sum([cvxpy.log(u) for u in utilities])
    positivity_constraints = [v >= 0 for v in allocations]
    sum_constraint = [cvxpy.sum(allocations)==sum(donations)]

    problem = cvxpy.Problem(
        cvxpy.Maximize(sum_of_logs),
        constraints = positivity_constraints+sum_constraint)
    problem.solve()

    print('BUDGET:', end=' ')
    for j in range(m-1):
        print(f"{subjects[j]}=%.3f" % allocations[j].value, end=', ')
    print(f"{subjects[m-1]}=%.3f" % allocations[m-1].value)


    d = []
    for i in range(n):
        d.append({})
        for j in range(m):
            subjectJ = subjects[j]
            dij = allocations[j].value * donations[i] * (subjectJ in preferences[i]) /utilities[i].value
            if dij > 0.0001:
                d[i][subjectJ] = dij

    for i in range(n):
        print(f'Citizen {i} gives', end=' ')
        first = True
        for k,v in d[i].items():
            if first:
                first = False
            else:
                print('and',end=' ')
            print(f'%.3f to {k}' %v, end=' ')
        print()




def main():
    import doctest
    print(doctest.testmod())

if __name__ == "__main__":
    main()