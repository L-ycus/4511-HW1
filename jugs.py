"""
GIVEN, fully solved -- this is the same water jugs puzzle from lecture
(Week 1's solution reveal, Week 2's opening), just written generically enough
to also handle other capacities or more than 2 jugs, not only the specific
(3, 4) example from class. Nothing to fill in here. Use it to test the search
functions you write in search_engine.py: if your bfs is correct, running it
on jugs_sample.config should reproduce the 6-step solution from class.

Config file format (see jugs_sample.config):
    jugs
    (3, 4)      <- capacities of each jug (any number of jugs is fine)
    (0, 0)      <- initial state
    (0, 2)      <- goal state
"""
import ast

from problem import Problem


class JugsProblem(Problem):

    @staticmethod
    def from_config(lines):
        capacities = ast.literal_eval(lines[1])
        init_state = ast.literal_eval(lines[2])
        goal_state = ast.literal_eval(lines[3])
        return JugsProblem(capacities, init_state, goal_state)

    def __init__(self, capacities, init_state, goal_state):
        self.capacities = capacities
        self.init = init_state
        self.goal = goal_state

    def initial_state(self):
        return self.init

    def is_goal(self, state):
        return state == self.goal

    def successors(self, state):
        """The successor function -- same idea as in lecture, but written to
        work for any number of jugs of any capacities (not just the 2-jug,
        (3, 4) example from class): yield (action, next_state, cost) for
        every move that actually CHANGES something. There's no point
        filling a jug that's already full, dumping one that's already
        empty, or "pouring" when that would move 0 water (source empty,
        destination full, or both) -- those would just generate a
        next_state identical to state, wasted work for the search to
        redo/reject later. Every move costs 1.

        Actions are (verb, jug index) or (verb, from index, to index) --
        generic, so this doesn't care how many jugs there are or what an
        individual jug happens to be called.
        """
        n = len(state)
        for i in range(n):
            if state[i] < self.capacities[i]:
                s = list(state)
                s[i] = self.capacities[i]
                yield ("fill", i), tuple(s), 1

            if state[i] > 0:
                s = list(state)
                s[i] = 0
                yield ("dump", i), tuple(s), 1

            for j in range(n):
                if i == j:
                    continue
                amount = min(state[i], self.capacities[j] - state[j])
                if amount > 0:
                    s = list(state)
                    s[i] -= amount
                    s[j] += amount
                    yield ("pour", i, j), tuple(s), 1

    # heuristic: not needed in Phase 1 (no informed search yet), and jugs
    # doesn't have a particularly interesting one anyway -- that's saved for
    # tiles and cities in Phase 2.
