from typing import List
import re


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Store exact matches
        # Store lowercase
        # Store vowel-removed word
        # All with precidence

        exactMatch = set(wordlist)
        capitalisation = {}
        vowelRemoved = {}
        pattern = r"[aeiou]"

        # Process wordlist first
        for i in range(len(wordlist)):
            word = wordlist[i]
            lowercase = word.lower()
            deVowel = re.sub(pattern, "*", lowercase)
            if word.lower() not in capitalisation:
                capitalisation[lowercase] = word
            if deVowel not in vowelRemoved:
                vowelRemoved[deVowel] = word
        
        # Process queries
        res = []
        for query in queries:
            # Precendence rules
            if query in exactMatch:
                res.append(query)
                continue
            
            normalised = query.lower()
            if normalised in capitalisation:
                res.append(capitalisation[normalised])
                continue
            
            nonVowelQuery = re.sub(pattern, "*", normalised)
            if nonVowelQuery in vowelRemoved:
                res.append(vowelRemoved[nonVowelQuery])
                continue
            
            res.append("")
        
        return res
            
