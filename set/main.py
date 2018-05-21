

# How many cards are in a Set deck?
# There are four different characteristics with three possible values each
# n = 3^4 = 81

# Formatted using autopep8 with aggressive level 1

class Matching(object):
    # Store all possible characteristics at initialization in correct order
    def __init__(self):
        self.qualities = [
            ("CIRCLE", "SQUIGGLE", "DIAMOND"),
            ("RED", "BLUE", "GREEN"),
            ("SOLID", "STRIPED", "EMPTY"),
            ("ONE", "TWO", "THREE")
        ]

    
    def find_quality(self, index, firstq, secondq):
        # 
        return [qual for qual in self.qualities[index]
         if qual != firstq and qual != secondq][0]

    def find_match(self, first, second):
        # This case wouldn't happen in a real game because a deck
        #  is made of unique cards:
        if first == second:
            return "Fen is so"
        #  Initialize the matching card
        match = ['', '', '', '']
        # If input qualities aren't ordered, use this instead
        # [(x, y) for x in range(len(first)) for y in range(len(second))
        #  if first[x] == second[y]]

        # Iterate through first and second, if both are equal, record
        # quality at index, else record 0
        quals = [first[i] if first[i] == second[i]
                 else 0 for i in range(len(first))]
        #  if no quality is the same (all 0), return "1337"
        if not any(quals):
            return "1337"
        for i in range(len(quals)):
            if quals[i]:
                match[i] = quals[i]
            else:
                match[i] = self.find_quality(i, first[i], second[i])
        return match

# Basic tests
game = Matching()
print(
    game.find_match(
        ("DIAMOND",
         "RED",
         "EMPTY",
         "TWO"),
        ("CIRCLE",
         "RED",
         "SOLID",
         "TWO")))
