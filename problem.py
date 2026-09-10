"""
The Problem interface. This is the ONLY thing search_engine.py knows about --
it never looks at what a state "is," only that these methods exist and behave
as documented below.

Every puzzle you write (Jugs, Cities, ...) is a class that inherits from
Problem and fills in these methods. Nothing here is puzzle-specific, and
nothing puzzle-specific belongs in search_engine.py.

This is a plain base class, not anything fancier. If a method below isn't
overridden by a puzzle class, calling it raises NotImplementedError -- that's
just a normal Python exception, not a special language feature.
"""


class Problem:

    def initial_state(self):
        """Return the starting state. A state can be any value that works as
        a dictionary key (a number, a string, a tuple of numbers, ...) --
        just not something mutable like a list."""
        raise NotImplementedError

    def is_goal(self, state):
        """Return True if this state is a goal state, False otherwise."""
        raise NotImplementedError

    def successors(self, state):
        """Yield (action, next_state, cost) for every legal move from this
        state -- this IS the successor function, same idea as in lecture.
        `action` can be anything you want (a string like "fill jug 0", a
        tuple, ...) -- the search engine never looks inside it, it just
        hands it back to you later as part of a solution path. `cost` is
        the real cost of taking that one action (just always yield 1 if
        every action in your puzzle costs the same)."""
        raise NotImplementedError

    def heuristic(self, state, name="zero"):
        """Estimate of remaining cost from state to a goal. Only used by
        greedy/astar/idastar -- bfs/dfs/iddfs/unicost never call this.

        `name` lets you support more than one heuristic and choose between
        them from the command line (puzzlesolver.py's optional 3rd argument).
        The default "zero" heuristic below is always available for free: it
        never overestimates (0 is never more than the true remaining cost),
        so greedy/astar/idastar are always runnable even before you've
        designed a real heuristic -- with h=0, astar behaves exactly like
        unicost.
        """
        if name == "zero":
            return 0
        raise ValueError("unknown heuristic name: " + name)
