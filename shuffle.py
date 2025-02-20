class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    
    >>> odd_cards = [1, 2, 3, 4, 5]
    >>> mod_oh_even = Shuffle.modified_overhand(odd_cards, 2)
    >>> mod_oh_even
    [1, 2, 3, 4, 5]
    """     
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert isinstance(num, int) and num >= 0 and num <= len(cards)
        assert isinstance(cards, list)
        if num == 0:
            return cards
        if len(cards) == 0:
            return []
        if num > 1:
            start = int(len(cards)/2 - num/2)
            end = start + num -1
            cards = cards[start:end+1] + cards[:start] + \
                cards[end+1:]
            return Shuffle.modified_overhand(cards, num-1)
        elif num == 1:
            start = int(len(cards)/2 - num/2)
            cards = [cards[start]] + cards[:start] + \
                cards[start+1:]
        return cards
                  
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 
        times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        if len(cards) <= 1:
            return cards
        if len(cards)%2 == 0:
            return [cards[-1]] + Shuffle.mongean(cards[:-1])
        else:
            return Shuffle.mongean(cards[:-1]) + [cards[-1]]