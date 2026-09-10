"""
GIVEN -- run this (`python3 explore.py`) once your search_engine.py
functions are working, to try them on jugs and cities.

This won't do anything useful until you've filled in search_engine.py (all
four functions currently raise NotImplementedError) AND cities.py (also
currently NotImplementedError). jugs.py is already complete, so you can test
against it first.
"""
from jugs import JugsProblem
from cities import CitiesProblem
from search_engine import ALGORITHMS


def show(problem, algorithm_name):
    search_function = ALGORITHMS[algorithm_name]
    result = search_function(problem, None)   # no heuristic in Phase 1
    print(algorithm_name + ":")
    if result.solution is None:
        print("  no solution found")
    else:
        print("  solution:", result.solution)
        print("  cost:", result.cost)
    print("  nodes created:", result.nodes_created)
    print("  max frontier size:", result.max_frontier)
    print()


def load(config_path, problem_class):
    with open(config_path) as f:
        lines = [line.strip() for line in f if line.strip() != ""]
    return problem_class.from_config(lines)


if __name__ == "__main__":
    print("=== jugs (already given/solved -- test your search functions against this) ===")
    jugs = load("jugs_sample.config", JugsProblem)
    for algorithm_name in ["bfs", "dfs", "iddfs", "unicost"]:
        show(jugs, algorithm_name)

    print("=== cities (fill in cities.py first) ===")
    cities = load("cities_sample.config", CitiesProblem)
    for algorithm_name in ["bfs", "unicost"]:
        show(cities, algorithm_name)
