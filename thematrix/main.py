from itertools import combinations  # returns all possible
# from functools import reduce

# Formatted using autopep8 with aggressive level 1

# Input: quantity of bags N, number of turns T
# Output: minimum # of friends needed to search N bags in T turns
# Strategy: instead of computing the # of friends from the given input
# we use the known constraints to approach this as an optimization problem
# Constraints: N <= 10**6 ; T <= 10

# There are two important observations to make from which the solution stems:

# First, a given amount of friends can test ∑ n!/k!(n-k)! for k in [0,n]
# bags in the last turn. We will call this formula E(n)
# Concretely, a group of friends can test more bags by creating entities
# with subsets of the group, growing the amount of testable bags exponentially

# Second, we can maximize the amount of bags tested in early turns by knowing
# The number of turns ahead of time. We can give each entity/subset pills from
# multiple bags, as long as the total amount of bags tested is testable by
# E(total entities - entities)

# Code: I used two ways to solve this problem
# The recursive solution makes the most logical sense and was derived by
# induction, while the iterative solution was derived by recognizing a pattern
# I used dynamic programming to optimize recursion with cache


# Both are available below


class IntoTheMatrix(object):
    # Instanciate the game with desired parameters
    def __init__(self, f_max=21, N_max=10**6, turns_max=10):
        self.cache = self.populate_cache(f_max, N_max, turns_max)

    # Cache solutions at instanciation to optimize query performance
    def populate_cache(self, f_max, N_max, turns_max):
        cache = []
        ntot = range(f_max)
        current = 0
        for i in range(1, turns_max + 1):
            turn = []
            current = 0
            for n in ntot:
                if current < N_max:
                    current = self.compute_recursive(n, i)
                    turn.append(current)
            cache.append(turn)
        return cache

    # Recursive solution uses logic described above to compute
    # the total tot amount of testable bags givenf friends and t turns

    def compute_recursive(self, f, t):
        if t == 0:
            return 1
        t -= 1
        tot = 0
        for i in range(f + 1):
                # Multiply total number of combinations (subsets/entities)
                # by number of bags that can be handled in the next turn by
                # remaining players
            tot += len(list(combinations(range(f), i))) * \
                self.compute_recursive(f - i, t)
        return tot

    # Binary search algorithm to extract the number of friends from cache
    def find_combi(self, x, turns, low=0):
        arr = self.cache[turns - 1]
        high = len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low

    # Pattern shows that at a given turn, n friends can test
    # turn+1 times as many bags as (n-1) friends could test
    # Initialize --> 1 player can test (turn+1) bag
    def compute_iterative(self, N, turns):
        i = 0
        f = 1
        while f < N:
            i += 1
            f *= (turns + 1)
        return i

    # One line of code to calculate combinations, did not end up using, for clarity
    # def compute_combi(self, n):
    #     return reduce(lambda x,y : x + y,
    #     [len(list(combinations(range(n),i))) for i in list(range(1,n+1))])

    # main method:
    def take_pills(self, turns, N):
        if N == 1:
            return 0

        # toggle commenting between the latter two lines of code to test
        # the performance of recursion vs iteration
        return self.find_combi(N, turns)
        # return self.compute_iterative(N, turns)


# Basic tests
# Instanciate class and generate cache:
game = IntoTheMatrix()
print(game.cache)

# The following lines should ideally be ran on their own to evaluate performance
# Since instanciation is the only computationally heavy process with recursion
# Make sure that "game" instance of IntoTheMatrix is in the environment
print(game.take_pills(2, 10))
print(game.take_pills(2, 1000))
print(game.take_pills(10, 2))
print(game.take_pills(4, 50))
