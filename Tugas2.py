import collections

Piece = collections.namedtuple('pieces', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 19)] + list('king','Queen','Rook','Knight','Bishop')
    color = 'white black'.split()

    def __init__(self):
        self._pieces = [Piece(rank, color) for color in self.colors
                                         for rank in self.ranks]

    def __len__(self):
        return len(self._pieces)

    def __getitem__(self, position):
        return self._pieces[position]