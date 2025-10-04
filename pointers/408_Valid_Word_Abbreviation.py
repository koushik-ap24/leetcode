class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ## Approach: Two pointers, one for word and one for abbr
        ## TC: O(n), SC: O(1)
        # Where n is max(len(word), len(abbr))
        wordLen = len(word)
        abbrLen = len(abbr)
        wordPtr = abbrPtr = 0
        subLen = ""

        while wordPtr < wordLen and abbrPtr < abbrLen:
            # Case 1, abbrPtr is a character
            if not abbr[abbrPtr].isdigit():
                if abbr[abbrPtr] != word[wordPtr]:
                    return False
                else:
                    wordPtr += 1
                    abbrPtr += 1
            
            # Case 2, abbrPtr is a digit
            else:
                # Leading 0 condition
                if abbr[abbrPtr] == '0' and not subLen:
                    return False
                
                # Get all adjacent digits
                while abbrPtr < abbrLen and abbr[abbrPtr].isdigit():
                    subLen += abbr[abbrPtr]
                    abbrPtr += 1
                
                wordPtr += int(subLen)
                subLen = ""
        
        return (wordPtr == wordLen) and (abbrPtr == abbrLen)

