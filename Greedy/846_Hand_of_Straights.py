from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        elif len(hand) % groupSize != 0:
            return False
        
        # sort array in non-descending order
        hand.sort()

        cardCount = {}
        for card in hand:
            cardCount[card] = cardCount.get(card,0) + 1
        
        for card in hand:
            if cardCount[card]:
                for i in range(card, card + groupSize):
                    # Check if number exists and if its count is > 0
                    if i not in cardCount or not cardCount[i]:
                        return False
                    cardCount[i] -= 1
        
        return True