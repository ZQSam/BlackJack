class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    True

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)
    num_rank_dict = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 
    'J':10, 'Q':10, 'K':10, 'A':11}
    suit_rank = {'spades':1, 'hearts':2, 'diamonds':3, 'clubs':4}
    
    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert isinstance(rank, int) or isinstance(rank, str)
        assert isinstance(suit, str)
        assert isinstance(visible, bool)
        self.rank = rank
        self.suit = suit
        self.visible = visible
        

    def __lt__(self, other_card):
        num_rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suit_rank = ['spades', 'hearts', 'diamonds', 'clubs']
        self_rank = num_rank.index(self.rank)
        other_rank = num_rank.index(other_card.rank)
        self_suit = suit_rank.index(self.suit)
        other_suit = suit_rank.index(other_card.suit)
        if self_rank == other_rank:
            return self_suit < other_suit
        return self_rank < other_rank


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        symbol_suit = ''
        if self.suit == 'hearts':
            symbol_suit = '♥'
        elif self.suit == 'spades':
            symbol_suit = '♠'
        elif self.suit == 'clubs':
            symbol_suit = '♣'
        else:
            symbol_suit = '♦'

        if not self.visible:
            return "____\n|?  |\n| ? |\n|__?|"
        return "____\n|" + self.get_rank() + \
            "  |\n| " + symbol_suit + \
            " |\n|__" + self.get_rank() + "|"

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        
        if not self.visible:        
            return '({0}, {0})'.format('?')
        return '({}, {})'.format(self.rank, self.suit)

    def get_rank(self):
        if isinstance(self.rank, int):
            return str(self.rank)
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
    